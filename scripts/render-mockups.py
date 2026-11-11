"""Render device mockups on black: 2400x1800 JPEGs (900x675 CSS, supersampled at 4x).

usage: python3 render.py jobs.json
jobs.json: [{"src": "public/media/x.webp", "out": "public/media/mockups/x.jpg",
             "device": "laptop"|"phone", "layout": "flat-r"|"flat-l"|"slant"|"iso"}]
"""
import asyncio, json, sys, io, pathlib
from PIL import Image
from playwright.async_api import async_playwright

ROOT = pathlib.Path('/home/claude/portfolio')
W, H = 900, 675
OUT = 2.6667  # 4x supersample, saved at 2400x1800


CSS = """
*{margin:0;box-sizing:border-box}
html,body{width:900px;height:675px;background:#000;overflow:hidden}
.stage{position:absolute;inset:0;perspective:2400px;overflow:hidden}
.dev{position:absolute;transform-style:preserve-3d}
.dev img{display:block;width:100%;height:auto}
/* display (web) */
.laptop{width:var(--w);padding:12px;border-radius:22px;background:#0c0c0d;
  box-shadow:0 0 0 1.5px #3a3b3e, inset 0 0 0 1px #1d1e20}
.laptop .scr{border-radius:10px;overflow:hidden;background:#111}
/* phone */
.phone{width:var(--w);padding:calc(var(--w)*.032);border-radius:calc(var(--w)*.16);background:#050505;
  box-shadow:0 0 0 2.5px #4a4b4f, 0 0 0 4px #1b1c1e}
.phone .scr{border-radius:calc(var(--w)*.13);overflow:hidden;position:relative;background:#111}
.phone .island{position:absolute;top:calc(var(--w)*.035);left:50%;width:calc(var(--w)*.3);height:calc(var(--w)*.085);
  transform:translateX(-50%);background:#000;border-radius:99px;z-index:2}
/* slab thickness for angled layouts */
.thick::before{content:"";position:absolute;inset:0;border-radius:inherit;background:#232427;transform:translateZ(-14px)}
.thick::after{content:"";position:absolute;inset:0;border-radius:inherit;background:#17181a;transform:translateZ(-7px)}
"""

def layout(device, name):
    """Return (css width var, inline style) placing the device so it bleeds off the
    bottom and one side, leaving air above and on the other side."""
    if device == 'laptop':
        return {
            'flat-r': ('920px', 'left:96px;top:84px'),
            'flat-l': ('920px', 'right:96px;top:84px'),
            'slant':  ('960px', 'left:70px;top:70px;transform-origin:0 0;transform:rotateY(-24deg) rotateX(7deg)'),
            'iso':    ('900px', 'left:560px;top:400px;transform:translate(-50%,-50%) rotateX(50deg) rotateZ(-34deg)'),
        }[name]
    return {
        'flat-r': ('360px', 'left:430px;top:70px'),
        'flat-l': ('360px', 'left:110px;top:70px'),
        'slant':  ('380px', 'left:330px;top:64px;transform-origin:50% 0;transform:rotateY(-28deg) rotateX(6deg) rotateZ(2deg)'),
        'iso':    ('380px', 'left:540px;top:470px;transform:translate(-50%,-50%) rotateX(48deg) rotateZ(-30deg)'),
    }[name]

def html(src, device, name):
    w, style = layout(device, name)
    thick = ' thick' if name in ('slant', 'iso') else ''
    island = '<i class="island"></i>' if device == 'phone' else ''
    return f"""<!doctype html><html><head><style>{CSS}</style></head><body><div class="stage">
<div class="dev {device}{thick}" style="--w:{w};{style}"><div class="scr">{island}<img src="{src}"></div></div>
</div></body></html>"""

import numpy as np

QUAD_JS = """() => {
  const el = document.querySelector('.dev'), cs = getComputedStyle(el);
  const [ox, oy] = cs.transformOrigin.split(' ').map(parseFloat);
  const t = cs.transform === 'none' ? new DOMMatrix() : new DOMMatrix(cs.transform);
  const m = new DOMMatrix().translate(el.offsetLeft + ox, el.offsetTop + oy).multiply(t).translate(-ox, -oy);
  const d = 2400, cx = 450, cy = 337.5;
  const P = new DOMMatrix().translate(cx, cy); const pm = new DOMMatrix(); pm.m34 = -1 / d;
  const full = P.multiply(pm).translate(-cx, -cy).multiply(m);
  const w = el.offsetWidth, h = el.offsetHeight;
  return {w, h, quad: [[0,0],[w,0],[w,h],[0,h]].map(([x,y]) => { const q = new DOMPoint(x,y,0,1).matrixTransform(full); return [q.x/q.w, q.y/q.w]; })};
}"""

def coeffs(dst, src):
    """PIL PERSPECTIVE coefficients mapping output (dst quad) back to input (src rect)."""
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u*x, -u*y], [0, 0, 0, x, y, 1, -v*x, -v*y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

S = 4  # supersample

async def main(jobs):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=S)
        for j in jobs:
            src = (ROOT / j['src']).resolve().as_uri()
            pathlib.Path('/tmp/mock.html').write_text(html(src, j['device'], j['layout']))
            await pg.goto('file:///tmp/mock.html', wait_until='load'); await pg.wait_for_timeout(150)
            geo = await pg.evaluate(QUAD_JS)
            # flat device, transparent, at S x
            await pg.evaluate("""() => { const el = document.querySelector('.dev'); el.classList.remove('thick');
              el.style.transform = 'none'; el.style.left = '20px'; el.style.top = '20px'; el.style.right = 'auto';
              document.documentElement.style.background = document.body.style.background = 'transparent'; }""")
            pg_h = max(H, int(geo['h']) + 40)
            await pg.set_viewport_size({'width': max(W, int(geo['w']) + 40), 'height': pg_h})
            png = await pg.screenshot(type='png', omit_background=True,
                                      clip={'x': 18, 'y': 18, 'width': geo['w'] + 4, 'height': geo['h'] + 4})
            await pg.set_viewport_size({'width': W, 'height': H})
            dev = Image.open(io.BytesIO(png)).convert('RGBA')
            sw, sh = dev.size; k = sw / (geo['w'] + 4); o = 2 * k
            src_rect = [(o, o), (o + geo['w'] * k, o), (o + geo['w'] * k, o + geo['h'] * k), (o, o + geo['h'] * k)]
            dst = [(x * S, y * S) for x, y in geo['quad']]
            canvas = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 255))
            if j['layout'] in ('slant', 'iso'):
                # slab edge: silhouette offset down/right, darker grey
                edge = dev.copy(); edge.putdata([(40, 41, 44, a) for *_, a in edge.getdata()])
                for off in (10, 20):
                    sh_dst = [(x + off * 0.35, y + off) for x, y in dst]
                    canvas.alpha_composite(edge.transform(canvas.size, Image.PERSPECTIVE, coeffs(sh_dst, src_rect), Image.BICUBIC))
            canvas.alpha_composite(dev.transform(canvas.size, Image.PERSPECTIVE, coeffs(dst, src_rect), Image.BICUBIC))
            im = canvas.convert('RGB').resize((2400, 1800), Image.LANCZOS)
            out = ROOT / j['out']; out.parent.mkdir(parents=True, exist_ok=True)
            im.save(out, 'JPEG', quality=86, optimize=True, progressive=True, subsampling=0)
            print(j['out'], out.stat().st_size // 1024, 'KB')
        await b.close()

asyncio.run(main(json.load(open(sys.argv[1]))))
