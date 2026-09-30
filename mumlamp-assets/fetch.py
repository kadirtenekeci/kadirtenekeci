# Downloads JPGs listed in urls.tsv (name<TAB>url) and saves them <=1600px, ~<=400 KB.
import io, os, sys, urllib.request
from PIL import Image
BASE = os.path.dirname(os.path.abspath(__file__))
failed = 0
for line in open(os.path.join(BASE, "urls.tsv")):
    name, url = line.rstrip("\n").split("\t")
    try:
        im = Image.open(io.BytesIO(urllib.request.urlopen(url, timeout=60).read())).convert("RGB")
    except Exception as e:
        print("FAIL", name, e); failed += 1; continue
    im.thumbnail((1600, 1600), Image.LANCZOS)
    dst = os.path.join(BASE, name + ".jpg"); os.makedirs(os.path.dirname(dst), exist_ok=True)
    for q in range(90, 50, -3):
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(dst) <= 400_000: break
    print("OK", name, im.size, os.path.getsize(dst))
sys.exit(1 if failed else 0)
