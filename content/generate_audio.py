import sys,asyncio,json,subprocess,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'tmp/audio-tools'))
import edge_tts
def valid(path,min_seconds=1):
 try:
  r=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(path)],capture_output=True,text=True,encoding='utf-8',errors='ignore',check=True)
  return float(r.stdout.strip())>=min_seconds
 except Exception:return False
async def run():
 out=ROOT/'public/audio';out.mkdir(exist_ok=True)
 cache=ROOT.parent/'tmp/speech';cache.mkdir(exist_ok=True)
 for path in sorted((ROOT/'content').glob('paper*.json')):
  p=json.loads(path.read_text(encoding='utf-8-sig'))
  for idx,s in enumerate(p['sections']):
   if 'transcript' not in s:continue
   target=out/f'{p["id"]:02}-{idx+1}.mp3'
   digest=hashlib.sha256(s['transcript'].encode()).hexdigest()
   marker=target.with_suffix('.sha256')
   if target.exists() and marker.exists() and marker.read_text()==digest and valid(target,30):continue
   lines=s['transcript'].split('\n');parts=[]
   for j,line in enumerate(lines):
    voice='en-GB-RyanNeural' if line.startswith('M:') else 'en-GB-SoniaNeural'
    text=line[2:].strip() if line[:2] in ('M:','W:') else line
    if not text.strip():continue
    f=cache/f'{hashlib.sha256((voice+text).encode()).hexdigest()}.mp3'
    if not valid(f,0.05):
     f.unlink(missing_ok=True)
     for attempt in range(3):
      try:
       await edge_tts.Communicate(text,voice,rate='-5%').save(str(f))
       if not valid(f,0.05):raise RuntimeError(f'invalid generated audio for: {text!r}')
       break
      except Exception:
       if attempt==2:raise
       await asyncio.sleep(2)
    parts.append(f)
   cat=cache/'concat.txt';cat.write_text('\n'.join("file '"+str(f).replace('\\','/')+"'" for f in parts),encoding='utf-8')
   subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(cat),'-ar','24000','-ac','1','-b:a','64k',str(target)],check=True)
   if not valid(target,30):raise RuntimeError(f'invalid output {target}')
   marker.write_text(digest)
   print('READY',target.name,flush=True)
  target=out/f'{p["id"]:02}-exam.mp3'
  full_digest=hashlib.sha256(''.join(s.get('transcript','') for s in p['sections']).encode()).hexdigest()
  full_marker=target.with_suffix('.sha256')
  if target.exists() and full_marker.exists() and full_marker.read_text()==full_digest and valid(target,600):continue
  full=[]
  async def say(text,key):
   f=cache/f'direction-{key}.mp3'
   if not f.exists():await edge_tts.Communicate(text,'en-GB-SoniaNeural',rate='-5%').save(str(f))
   full.append(f)
  def silence(n):
   f=cache/f'silence-{n}.mp3'
   if not f.exists():subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t',str(n),'-b:a','64k',str(f)],check=True)
   full.append(f)
  await say('Section one. Listening. Part A. You will hear five dialogues or monologues. For questions one to twenty, choose the best answer. You will hear each recording only once.','intro')
  for k in range(5):
   lo=k*4+1;hi=lo+3
   await say(f'Questions {lo} to {hi}. You now have twenty seconds to read the questions.',f'pre-{k}')
   silence(20);full.append(out/f'{p["id"]:02}-{k+1}.mp3')
   await say(f'You now have forty seconds to check your answers to questions {lo} to {hi}.',f'post-{k}');silence(40)
  await say('Part B. For questions twenty one to twenty five, fill out the outline. Use one word or number for each blank. You will hear the recording twice. You now have twenty five seconds to read the outline.','b-intro');silence(25)
  full.append(out/f'{p["id"]:02}-6.mp3')
  await say('You now have thirty seconds to check your answers.','b-check1');silence(30)
  await say('Now you will hear the recording a second time.','b-repeat');full.append(out/f'{p["id"]:02}-6.mp3')
  await say('You now have twenty seconds to check your answers.','b-check2');silence(20)
  await say('You now have two minutes to transfer your answers to the answer sheet.','transfer');silence(120)
  await say('That is the end of the listening section.','end')
  cat=cache/'full-concat.txt';cat.write_text('\n'.join("file '"+str(f).replace('\\','/')+"'" for f in full),encoding='utf-8')
  subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(cat),'-ar','24000','-ac','1','-b:a','64k',str(target)],check=True)
  if not valid(target,600):raise RuntimeError(f'invalid full audio {target}')
  full_marker.write_text(full_digest)
  print('READY',target.name,flush=True)
asyncio.run(run())
