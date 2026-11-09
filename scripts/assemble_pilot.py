"""Mux the rendered stickman explainer, narration and captions into an MP4."""
from pathlib import Path
import json
import subprocess

ROOT = Path(".")
VIDEO = ROOT / "media/videos/pilot/1080p24/UrbanHeatIslandPilot.mp4"
AUDIO = ROOT / "artifacts/narration.wav"
SUBS = ROOT / "subtitles.srt"
OUT = ROOT / "artifacts/final_video.mp4"


def duration(path: Path) -> float:
    raw = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", str(path)
    ], text=True)
    return float(json.loads(raw)["format"]["duration"])


def main():
    for path in (VIDEO, AUDIO, SUBS):
        if not path.exists():
            raise FileNotFoundError(path)
    video_duration = duration(VIDEO)
    audio_duration = duration(AUDIO)
    # Hold the final animation frame if narration runs longer than the scene.
    pad = max(0.0, audio_duration - video_duration + 0.5)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg", "-y", "-i", str(VIDEO), "-i", str(AUDIO),
        "-vf", f"tpad=stop_mode=clone:stop_duration={pad:.3f},subtitles={SUBS}",
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "libx264",
        "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
        "-r", "24", "-c:a", "aac", "-b:a", "192k", "-shortest",
        "-movflags", "+faststart", str(OUT)
    ]
    subprocess.run(command, check=True)
    print(f"Created {OUT}: video={video_duration:.1f}s narration={audio_duration:.1f}s")
    print(f"Final duration: {duration(OUT):.1f}s")


if __name__ == "__main__":
    main()
