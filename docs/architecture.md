# stiXplainer — Initial Architecture

**Status:** Design baseline; implementation is in progress.

## Product boundary

stiXplainer aims to coordinate a documentary workflow from a sourced brief to an edited video package. It is not intended to automate editorial responsibility: source reliability, factual claims, script approval and final export remain reviewable human decisions.

## Pipeline stages

1. **Research** — gather primary and reputable sources; record URLs, publication dates and relevant claims.
2. **Fact-check** — map factual statements in the script to supporting sources and flag uncertainty.
3. **Script** — produce a narration draft with timing estimates and scene references.
4. **Story architecture** — divide the script into scenes, beats and visual explanations.
5. **Visual direction** — define visual language, composition, transitions and asset requirements.
6. **Asset creation** — create reusable character, illustration and photographic-insert assets, respecting licences.
7. **Animation** — render scene-level motion and transitions.
8. **Narration and sound** — generate or record narration; add music and effects with documented usage rights.
9. **Edit and subtitles** — synchronize picture, narration, sound and captions.
10. **Quality control** — inspect duration, resolution, frame rate, audio levels, subtitle timing and source completeness.

These are workflow responsibilities, not claims of independently running AI agents.

## Initial technical direction

| Concern | Candidate | Validation still required |
| --- | --- | --- |
| Orchestration | Python | Reproducible environment and CLI |
| Animation | Manim Community | Character and illustration scene prototype |
| Image assets | SVG + Pillow | Style consistency and asset licensing |
| Video assembly | FFmpeg | Audio/video synchronization and export checks |
| Narration | Kokoro | British male voice quality, runtime and licensing |
| Subtitles | Whisper or timed script captions | Accuracy and synchronization |
| Automation | GitHub Actions | Free runner feasibility and render duration |

Only free/open-source tools and genuinely free execution paths may be adopted. A paid plan, paid credits, trial or paid fallback is out of scope.

## Pilot acceptance criteria

The first proof-of-concept should be 60–90 seconds and demonstrate:
- At least two animated stick-figure characters.
- Visible facial expression or pose changes.
- Moving explanatory illustrations, not just static slides.
- One or two photographic inserts with documented rights.
- British English male storyteller narration, if the selected free voice can meet the quality bar.
- Background music and sound effects with clear usage rights.
- Narration and animation synchronization.
- Export at 1920×1080, 24 fps and 16:9.

The pilot must be rendered and inspected before the system is described as functional.

## Output package target

A completed production should be able to provide:
- `final_video.mp4`
- `narration.wav`
- `subtitles.srt`
- `script.md`
- `sources.md`
- `thumbnail.png`

This is a target deliverable contract, not an existing output set.

## Compute strategy

The first compute experiment will test a small CPU-only render in a free environment. Measure setup time, render time, memory use, output size and reliability. Do not assume a free-tier quota guarantees a successful 10–15 minute export. Record current provider limits and re-check them before relying on them.

## Security and publishing

- Never commit API keys, access tokens, credentials or private source material.
- Public repository contents are visible to everyone.
- Use only assets with compatible licences and retain attribution.
- Avoid uploading copyrighted footage, music or personal data without permission.
