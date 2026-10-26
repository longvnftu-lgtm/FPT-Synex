"""Đóng gói deck thành một file HTML duy nhất (ảnh, logo, chữ đã sửa nhúng sẵn)."""
import base64, json, re, pathlib
here = pathlib.Path(__file__).parent
h = (here / 'index.html').read_text(encoding='utf-8')
b64 = lambda p, mt: f'data:{mt};base64,' + base64.b64encode(p.read_bytes()).decode()
for f in ['base.png', 'base-mark.png', 'synnex.png', 'cover-hero.jpg']:
    h = h.replace(f'src="logos/{f}"', 'src="' + b64(here / 'logos' / f, 'image/png' if f.endswith('png') else 'image/jpeg') + '"')
shots = re.findall(r"\['(\d\d_[^']+)','", h)
img = {s: b64(here / 'screens' / f'{s}.jpg', 'image/jpeg') for s in shots}
texts = json.loads((here / 'texts.json').read_text(encoding='utf-8') or '{}')
pre = ('<script type="application/json" id="texts">' + json.dumps(texts, ensure_ascii=False).replace('<', '\\u003c') + '</script>'
       '<script>window.IMG=' + json.dumps(img) + ';window.__SRC=document.documentElement.outerHTML;</script>\n')
TAG = '\n<script id="main">\n'; assert h.count(TAG) == 1
h = h.replace(TAG, '\n' + pre + TAG.lstrip())
out = ('<!doctype html>\n<html lang="vi"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>\n' + h + '\n</body></html>\n')
dst = here / 'Synnex_FPT_Agentic_Sales_OS.html'
dst.write_text(out, encoding='utf-8')
print(dst.name, round(len(out.encode()) / 1e6, 2), 'MB')
