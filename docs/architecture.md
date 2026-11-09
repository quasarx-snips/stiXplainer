# stiXplainer Production Architecture

**Status:** Baseline roles and visual direction documented; end-to-end execution still requires validation.

## Pipeline
1. Research — primary/reputable sources, dates and claim evidence.
2. Fact-check — verify each factual statement and qualify uncertainty.
3. Script — accessible British-English narration; visual notes separate.
4. Story architecture — scene beats, actions, diagrams, transitions and assets.
5. Visual direction — apply the style bible to composition, colour and pacing.
6. Character/asset design — original reusable cast, poses and illustrations.
7. Animation — scene motion and explanatory visuals.
8. Audio/post — narration, rights-cleared sound, synchronized subtitles and assembly.
9. QC — inspect actual media, evidence, timing, picture and sound.

## Specialist layer
Eight worker profiles live in `.github/agents/`: Research Producer, Fact Checker, Scriptwriter, Story Architect, Visual Director, Character Designer, Animation Engineer, and Audio, Editor & QC Producer. The Studio Director coordinates them. See [agent-team.md](agent-team.md).

These are configuration profiles for compatible agent hosts, not live processes. GitHub Actions does not execute them. Real delegation requires a host with custom-agent/subagent support; otherwise use the roles sequentially.

## Visual direction
The owner-supplied silent reference informs the original hand-drawn 2D stickman style in [visual-style-bible.md](visual-style-bible.md). The owner can change it. Do not copy exact frames, characters, branding or assets.

## Toolchain
Python, Manim Community, SVG/Pillow, FFmpeg, Kokoro and optional Whisper are candidates. Verify free-tier feasibility, licences and runtime. No paid fallback is allowed.

## Pilot acceptance
60–90 seconds; expressive original stickman; multiple illustrated environments; moving objects/diagrams; purposeful scene transitions; optional British male narration if free voice quality is adequate; licensed sound only; synchronized subtitles; 1920×1080, 24 fps, 16:9; actual file inspected and QC report completed.

## Deliverables
`final_video.mp4`, `narration.wav`, `subtitles.srt`, `script.md`, `sources.md`, `thumbnail.png`, `qc-report.md`.

Never equate source code or workflow configuration with a finished video. Never commit secrets, private material, reference footage or unlicensed assets. Public release requires owner approval.
