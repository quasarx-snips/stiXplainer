"""Generate British English narration with the open Kokoro voice model."""
from pathlib import Path
import numpy as np
import soundfile as sf
from kokoro import KPipeline

TEXT = """The sun has gone down. So why does this street still feel like an oven?

Because a city is covered in materials that soak up sunlight. Roads, roofs and walls absorb energy through the day, then release some of that stored heat after sunset.

And where have the trees gone?

Vegetation cools its surroundings with shade and by moving water from soil and leaves into the air. Replace much of that greenery with hard, dry surfaces, and you lose some of that cooling.

So every street is equally hot?

Not at all. A shaded park, a tree-lined street and a wide paved car park can feel very different. Building layout and airflow matter too.

Vehicles, buildings and air-conditioning systems can add waste heat as well. The result is an urban heat island: built-up places can be warmer than nearby less-developed areas.

Can we make cities cooler?

We can help. More shade and vegetation, greener roofs, and more reflective roofs and pavements can all reduce heat in the right conditions. The best choice depends on the place.

So the heat isn't just in the weather. It's also in what we've built."""

def main():
    out = Path("artifacts/narration.wav")
    out.parent.mkdir(parents=True, exist_ok=True)
    pipeline = KPipeline(lang_code="b")
    chunks = []
    for _, _, audio in pipeline(TEXT, voice="bm_george", speed=0.96, split_pattern=r"\n+"):
        chunks.append(np.asarray(audio, dtype=np.float32))
        chunks.append(np.zeros(int(0.28 * 24000), dtype=np.float32))
    if not chunks:
        raise RuntimeError("Kokoro returned no audio chunks")
    sf.write(out, np.concatenate(chunks), 24000, subtype="PCM_16")
    print(f"Wrote {out} ({sf.info(out).duration:.1f}s)")

if __name__ == "__main__":
    main()
