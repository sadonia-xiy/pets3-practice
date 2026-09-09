from pathlib import Path
import json,re,hashlib,difflib,itertools
ROOT=Path(__file__).resolve().parents[1]
seen=set();errors=[];report=[];materials=[]
global_prompts={}
for path in sorted((ROOT/'content').glob('paper??.json')):
 p=json.loads(path.read_text(encoding='utf-8-sig'));ns=[];row={'id':p['id'],'counts':[]}
 for s in p['sections']:
  ns.extend(q['n'] for q in s['questions'])
  text=s.get('transcript',s.get('text',''));n=len(re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*",text))
  row['counts'].append([s['kind'],n])
  if text:
   materials.append((path.name,s['title'],s['kind'],text))
   h=hashlib.sha256(text.encode()).hexdigest()
   if h in seen:errors.append(f'{path.name}: duplicate passage')
   seen.add(h)
  limits={'listenA':(175,230),'listenB':(175,230),'readA':(315,385),'readB':(315,385),'readC':(200,250)}
  if s['kind'] in limits:
   low,high=limits[s['kind']]
   if not low<=n<=high:errors.append(f'{path.name} {s["title"]}: {n} words outside {low}-{high}')
  expected={'listenA':4,'listenB':5,'readA':5,'readB':5,'readC':10,'writing':1}[s['kind']]
  if len(s['questions'])!=expected:errors.append(f'{path.name} question count')
  for q in s['questions']:
   if not q['explanation']:errors.append(f'{path.name} Q{q["n"]} no explanation')
   options=q.get('options')
   if options and (q['answer'] not in 'ABCDEFGHIJKLMNO'[:len(options)] or len(options) not in [4,7,15]):errors.append(f'{path.name} Q{q["n"]} invalid options/key')
  if s['kind']=='writing' and not 110<=len(s['model'].split())<=140:errors.append(f'{path.name} model length')
 prompts=[q['prompt'].strip().lower() for s in p['sections'] for q in s['questions'] if not (46<=q['n']<=55)]
 dup_prompts=[x for x,n in __import__('collections').Counter(prompts).items() if n>1]
 if dup_prompts:errors.append(f'{path.name} repeated prompts: {dup_prompts}')
 for prompt in prompts:
  global_prompts.setdefault(prompt,[]).append(path.name)
 if sorted(ns)!=list(range(1,57)):errors.append(f'{path.name} numbering')
 if [s['kind'] for s in p['sections']]!=['listenA']*5+['listenB']+['readA']*3+['readB','readC','writing']:errors.append(f'{path.name} section sequence')
 report.append(row)
for a,b in itertools.combinations(materials,2):
 if a[2]==b[2] and difflib.SequenceMatcher(None,a[3],b[3]).ratio()>.72:
  errors.append(f'highly similar materials: {a[0]} {a[1]} / {b[0]} {b[1]}')
print(json.dumps({'papers':len(report),'errors':errors,'lengths':report},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
