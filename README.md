# stiXplainer

**An AI-assisted animated documentary production studio.**

stiXplainer is an open-source project exploring an end-to-end workflow for turning researched documentary ideas into visually engaging animated films. The goal is to combine human editorial judgement with reproducible, open-source production tools.

> **Project status:** Early development — foundational repository and workflow scaffold. A working video-rendering pipeline and sample film are not yet complete.

## Vision

Create a beginner-friendly production workflow that can support:
- Research, source tracking and fact-checking.
- Documentary scripting and visual story planning.
- Hybrid animation: stick-figure characters, hand-drawn-style illustrations and selected photographic inserts.
- Narration, sound design, subtitles and synchronized editing.
- Reproducible 1080p, 24 fps, 16:9 video exports.

## Production target

| Setting | Target |
| --- | --- |
| Film length | 10–15 minutes |
| Resolution | 1920 × 1080 |
| Frame rate | 24 fps |
| Aspect ratio | 16:9 |
| Visual language | Stick figures + rough illustrations + occasional photographs |
| Narration direction | British English, male storyteller |
| Intended cadence | Approximately one film per week |
| Cost constraint | ₹0: free and open-source tools only; no paid credits or paid fallbacks |

These are project goals, not claims that the pipeline already achieves them.

## Planned toolchain

The implementation will evaluate and integrate free/open-source components such as:
- **Python** for orchestration and production logic.
- **Manim Community** for programmatic animation.
- **FFmpeg** for video and audio assembly.
- **Pillow** and SVG assets for image and character workflows.
- **Kokoro** for local text-to-speech experiments, subject to voice and runtime validation.
- **Whisper** for optional subtitle generation.

Tool choices will be validated against the zero-budget requirement before adoption. No paid-service fallback is permitted.

## Repository map

```text
.
├── .github/workflows/   # Automated checks
├── docs/                # Architecture and production notes
├── src/stixplainer/     # Application package
├── tests/               # Automated tests
├── .gitignore
├── pyproject.toml
└── README.md
```

## Development approach

1. Establish a reproducible, free development and rendering environment.
2. Build a 60–90 second proof-of-concept before attempting a full episode.
3. Validate character motion, illustration animation, photo inserts, narration, sound effects and subtitle timing.
4. Measure render time and resource usage on genuinely free compute.
5. Expand toward the 10–15 minute production target only after the pilot is repeatable.

## Quality principles

- **Evidence first:** factual claims must be traceable to sources.
- **Story over slideshow:** motion and visual explanation should carry the narrative.
- **Human editorial control:** AI assists; a human approves research, scripts and final cuts.
- **Reproducibility:** record dependencies, settings and production steps.
- **Cost transparency:** document free-tier limits and never silently switch to a paid service.

## Contributing

See [docs/architecture.md](docs/architecture.md) for the initial system boundaries and planned pipeline. Contributions, issue reports and practical tests on free compute are welcome.

## Licence

A project licence will be selected before the first public release. Until then, do not assume that the repository grants reuse rights to its contents or third-party assets.
