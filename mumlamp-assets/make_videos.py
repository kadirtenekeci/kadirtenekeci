# Builds short 16:9 MP4 loops from scene JPGs: slow camera push/pan + lantern flicker.
import subprocess, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS, SEC = 1920, 1080, 30, 8
N = FPS * SEC
# name, source, zoom end, focus x, focus y (0..1 of frame)
CLIPS = [
    ("ay-isiginda-gol", "hero/kamp-gecesi-hero.jpg", 1.18, 0.78, 0.72),
    ("cadirdan-yildizli-gece", "scenes/03-cadirdan-yildizli-gece.jpg", 1.15, 0.30, 0.65),
    ("ates-basi-gitar", "scenes/15-ates-basi-gitar.jpg", 1.16, 0.25, 0.45),
    ("kuzey-isiklari", "scenes/19-kuzey-isiklari.jpg", 1.14, 0.35, 0.55),
]
for name, src, zend, fx, fy in CLIPS:
    z = f"1+({zend}-1)*on/{N}"
    vf = (
        f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
        f"zoompan=z='{z}':x='(iw-iw/zoom)*{fx}':y='(ih-ih/zoom)*{fy}':d={N}:s={W}x{H}:fps={FPS},"
        "eq=eval=frame:brightness='0.018*sin(2*PI*t*1.1)+0.012*sin(2*PI*t*3.3)+0.006*sin(2*PI*t*7.9)':saturation=1.05,"
        "vignette=PI/5,fade=t=in:st=0:d=0.6,fade=t=out:st=7.4:d=0.6,format=yuv420p"
    )
    out = f"videos/{name}.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", "-loop", "1", "-i", src, "-vf", vf,
                    "-t", str(SEC), "-r", str(FPS), "-c:v", "libx264", "-preset", "slow",
                    "-crf", "22", "-movflags", "+faststart", out], check=True)
    print("OK", out)
