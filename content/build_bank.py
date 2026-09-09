from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
def q(n,prompt,options,answer,explanation):return dict(n=n,prompt=prompt,options=options,answer=answer,explanation=explanation)
def load():
 papers=[]
 for path in sorted((ROOT/'content').glob('paper*.json')):papers.append(json.loads(path.read_text(encoding='utf-8')))
 out=ROOT/'public/papers';out.mkdir(parents=True,exist_ok=True)
 (out/'index.json').write_text(json.dumps(papers,ensure_ascii=False),encoding='utf-8')
 print(f'{len(papers)} papers, {sum(len(s["questions"]) for p in papers for s in p["sections"])} questions')
if __name__=='__main__':load()
