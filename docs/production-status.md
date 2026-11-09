# Production Status

Updated: 2026-11-10

## Stickman explainer pilot

- [x] Two recurring stick-figure presenters and multi-beat city animation source committed.
- [x] Pilot narration draft and source ledger committed.
- [x] British male voice generation script added using Kokoro voice `bm_george` (British English).
- [x] Subtitle draft committed; timings are provisional and must be checked against the generated narration.
- [x] FFmpeg assembly script added to combine animation, narration and subtitles.
- [x] Automated workflow configured for 1080p/24fps animation, British voice generation and final MP4 assembly.
- [ ] Confirm latest workflow completes all three jobs.
- [ ] Download and inspect final MP4, duration, resolution, frame rate and audio sync.
- [ ] Correct subtitle timings against actual speech.
- [ ] Review the final video for visual quality and story pacing.
- [ ] Add appropriately licensed music and sound design.
- [ ] Decide whether the pilot needs photo inserts; the current visual direction is primarily stickman illustration.

## Quality and honesty notes

A previous smoke-test artifact was successfully produced: 854×480, 24 fps, about 12.1 seconds. It is a title-card test, not the documentary pilot. The actual pilot MP4 has not yet been verified.

The current workflow aims to create a 1920×1080, 24 fps MP4 with a British English male synthetic narration track and captions. This remains a target until the final artifact is downloaded and inspected. No music or third-party photos are included in the automated build yet; reuse rights must be checked before adding assets.

## Core project rule

stiXplainer is a stickman explainer/documentary channel. Prioritize clear recurring characters, expressive gestures, visual metaphors, diagrams, scene transitions and motion-led storytelling over static text slides. Do not call a milestone complete until the actual video has been inspected.
