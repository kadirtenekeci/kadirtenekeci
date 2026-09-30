# usage: shrink.py SRC DST  -> JPG, max 1600px long edge, <= 400 KB (exits 1 if impossible)
import os
import sys
from PIL import Image

MAX_EDGE, MAX_BYTES, MIN_QUALITY, MIN_EDGE = 1600, 400_000, 52, 400

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
while True:
    for q in range(88, MIN_QUALITY - 1, -4):
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(dst) <= MAX_BYTES:
            print(dst, im.size, os.path.getsize(dst))
            sys.exit(0)
    if max(im.size) <= MIN_EDGE:
        break
    im = im.resize((int(im.width * 0.9), int(im.height * 0.9)), Image.LANCZOS)
os.remove(dst)
sys.exit(f"{dst}: cannot fit under {MAX_BYTES} bytes")
