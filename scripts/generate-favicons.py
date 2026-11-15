"""Render the blog's simple SVG mark to browser icons (requires Pillow)."""
from pathlib import Path
import re
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / 'static'
SHAPES = [
    ('#795139', 'M 33 22 C 31 15 33 9 39 4 L 43 7 C 38 11 37 16 38 22 Z'),
    ('#F4A623', 'M 36 16 C 48 14 57 23 55 36 C 53 51 36 61 21 56 C 9 52 7 44 15 34 C 22 26 22 18 31 17 C 33 16 35 16 36 16 Z'),
    ('#FFD36A', 'M 31 21 C 24 24 25 30 19 37 C 15 42 14 46 19 49 C 17 43 24 40 27 33 C 29 28 28 25 31 21 Z'),
    ('#287A48', 'M 37 14 C 38 3 50 1 59 5 C 56 15 46 20 37 14 Z'),
    # A small robot face and antennas bring the "Driod" back into the mango.
    ('#245D40', 'M 22 29 L 16 21 L 19 19 L 25 27 Z'),
    ('#245D40', 'M 42 27 L 48 19 L 51 21 L 45 30 Z'),
    ('#245D40', 'M 19 40 C 19 30 25 25 34 25 C 43 25 49 31 49 40 L 49 43 L 19 43 Z'),
    ('#FFF6E5', 'M 29 35 C 29 38 25 38 25 35 C 25 32 29 32 29 35 Z'),
    ('#FFF6E5', 'M 43 35 C 43 38 39 38 39 35 C 39 32 43 32 43 35 Z'),
]

def points(path):
    tokens = re.findall(r'[MLCZ]|-?\d+(?:\.\d+)?', path)
    out = []
    i = 0
    while i < len(tokens):
        cmd = tokens[i]
        i += 1
        if cmd in ('M', 'L'):
            pt = (float(tokens[i]), float(tokens[i + 1]))
            i += 2
            out.append(pt)
        elif cmd == 'C':
            start = out[-1]
            a, b, end = [(float(tokens[i + k]), float(tokens[i + k + 1])) for k in (0, 2, 4)]
            i += 6
            for step in range(1, 65):
                t = step / 64
                out.append(tuple((1-t)**3*start[d] + 3*(1-t)**2*t*a[d] + 3*(1-t)*t*t*b[d] + t**3*end[d] for d in (0, 1)))
        elif cmd != 'Z':
            raise ValueError(cmd)
    return out

svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">\n'
svg += '  <title>MangoDriod</title>\n'
svg += ''.join(f'  <path fill="{color}" d="{path}"/>\n' for color, path in SHAPES)
(STATIC / 'favicon.svg').write_text(svg + '</svg>\n')
mask = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="black">\n'
mask += ''.join(f'  <path d="{path}"/>\n' for color, path in SHAPES if color not in ('#FFD36A', '#FFF6E5'))
(STATIC / 'safari-pinned-tab.svg').write_text(mask + '</svg>\n')
master = Image.new('RGBA', (1024, 1024))
draw = ImageDraw.Draw(master)
for color, path in SHAPES:
    draw.polygon([(x*16, y*16) for x, y in points(path)], fill=color)
for size in (16, 32):
    master.resize((size, size), Image.Resampling.LANCZOS).save(STATIC / f'favicon-{size}x{size}.png')
master.save(STATIC / 'favicon.ico', sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
# Apple touch icons use an opaque background; iOS supplies the rounded mask.
apple = Image.new('RGBA', master.size, '#FFF6E5')
apple.alpha_composite(master)
apple.convert('RGB').resize((180,180), Image.Resampling.LANCZOS).save(STATIC / 'apple-touch-icon.png')
