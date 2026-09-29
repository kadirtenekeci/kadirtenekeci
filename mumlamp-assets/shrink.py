# usage: shrink.py SRC DST  -> JPG, max 1600px long edge, ~<=400 KB
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
im.thumbnail((1600, 1600), Image.LANCZOS)
for q in range(88, 50, -4):
    im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
    import os
    if os.path.getsize(dst) <= 400_000:
        break
print(dst, im.size, os.path.getsize(dst))
