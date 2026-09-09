"""Prepare single-route static export for GitHub project Pages."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'dist/client'
assert (root/'index.html').is_file(), 'Missing static entry page'
for p in root.rglob('*'):
 if p.is_file() and p.suffix in ['.html','.js','.json','.rsc','.txt','.css']:
  text=p.read_text(encoding='utf-8')
  text=text.replace('/_next/','/pets3-practice/_next/')
  p.write_text(text,encoding='utf-8')
(root/'.nojekyll').touch()
print('Prepared GitHub Pages asset paths')
