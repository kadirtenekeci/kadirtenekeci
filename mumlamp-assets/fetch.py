# Downloads Canva images listed in urls.tsv, saves JPG <=1600px, ~<=400 KB.
import io, os, re, sys, urllib.request, urllib.error
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))

def variants(url, w, h):
    full = re.sub(r"height:\d+", f"height:{h}", url)
    full = re.sub(r"width:\d+", f"width:{w}", full)
    full = full.replace("quality:75", "quality:95")
    yield full
    yield re.sub(r"&x-canva-quality=thumbnail", "", full)
    yield re.sub(r"/image-resize/format:JPG/height:\d+/quality:\d+/(uri:[^/]+)/watermark:F/width:\d+", r"/image-resize/format:JPG/height:%d/quality:95/\1/watermark:F/width:%d" % (h, w), url)

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def save(im, dst):
    im = im.convert("RGB")
    im.thumbnail((1600, 1600), Image.LANCZOS)
    for q in range(90, 50, -3):
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(dst) <= 400_000:
            break
    return im.size, os.path.getsize(dst)

failed = 0
for line in open(os.path.join(BASE, "urls.tsv")):
    name, w, h, url = line.rstrip("\n").split("\t")
    w, h = int(w), int(h)
    got = None
    for v in variants(url, w, h):
        try:
            data = get(v)
            im = Image.open(io.BytesIO(data))
            print(f"  {name}: {im.size} from variant")
            if max(im.size) >= 800:
                got = im
                break
        except urllib.error.HTTPError as e:
            print(f"  {name}: HTTP {e.code}")
        except Exception as e:
            print(f"  {name}: {e!r}")
    if got is None:
        print(f"FAIL {name}")
        failed += 1
        continue
    dst = os.path.join(BASE, name + ".jpg")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    size, nbytes = save(got, dst)
    print(f"OK {name}.jpg {size} {nbytes} bytes")

print(f"failed: {failed}")
sys.exit(1 if failed else 0)
