"""Mux animation and narration; keep subtitles as a separate deliverable."""
from pathlib import Path
import json
import subprocess

VIDEO = Path("media/videos/pilot/1080p24/UrbanHeatIslandPilot.mp4")
AUDIO = Path("artifacts/narration.wav")
OUT = Path("artifacts/final_video.mp4")


def duration(path):
    raw = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", str(path)
    ], text=True)
    return float(json.loads(raw)["format"]["duration"])


def main():
    for path in (VIDEO, AUDIO):
        if not path.exists():
            raise FileNotFoundError(path)
    vd, ad = duration(VIDEO), duration(AUDIO)
    # Never stretch a static final frame for a long time; use a small tail pad only.
    if abs(vd-ad) > 2.5:
        raise RuntimeError(f"Animation/audio mismatch: video={vd:.2f}s audio={ad:.2f}s")
    pad = max(0.0, ad-vd+0.15)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-i", str(VIDEO), "-i", str(AUDIO),
        "-vf", f"tpad=stop_mode=clone:stop_duration={pad:.3f}",
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "libx264",
        "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
        "-r", "24", "-c:a", "aac", "-b:a", "192k", "-shortest",
        "-movflags", "+faststart", str(OUT)
    ]
    subprocess.run(cmd, check=True)
    print(f"Created {OUT}: video={vd:.2f}s narration={ad:.2f}s final={duration(OUT):.2f}s")


if __name__ == "__main__":
    main()
