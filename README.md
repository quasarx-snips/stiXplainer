# stiXplainer

**An AI-assisted, hand-drawn stickman documentary studio.**

A zero-budget workflow for turning researched documentary ideas into story-led 2D explainer films. The visual target is based on the owner's supplied audio-removed reference: expressive stick-figure acting, illustrated environments, objects, diagrams and changing scene scales. See [the visual style bible](docs/visual-style-bible.md).

## Default production settings

| Setting | Default |
|---|---|
| Pilot | 60–90 seconds |
| Full documentary | 10–15 minutes |
| Export | 1920×1080, 24 fps, 16:9 |
| Visuals | Original hand-drawn 2D stickmen + illustrated worlds + explanatory diagrams |
| Narration | Warm British English male storyteller |
| Captions | Separate synchronized SRT |
| Budget | ₹0; no paid credits, trials, subscriptions or paid fallbacks |

Edit [config/production_profile.toml](config/production_profile.toml) and [docs/default-production-profile.md](docs/default-production-profile.md) to change the defaults.

## Eight specialist agents

- Research Producer
- Fact Checker
- Scriptwriter
- Story Architect
- Visual Director
- Character Designer
- Animation Engineer
- Audio, Editor & QC Producer

The **stiXplainer Studio Director** is the default coordinator. Role profiles are in `.github/agents/`; shared instructions are in [AGENTS.md](AGENTS.md), and the hand-off sequence is in [docs/agent-team.md](docs/agent-team.md).

**Important runtime note:** these are reusable custom-agent profiles, not eight processes already running. Actual subagent delegation needs a compatible GitHub Copilot / VS Code agent host with custom-agent and subagent support. GitHub Actions does not execute the profiles. If the active host lacks subagent support, use the same roles sequentially and don't claim they ran autonomously.

## Production toolchain

Python, Manim Community, SVG/Pillow, FFmpeg and Kokoro are current free/open-source candidates, subject to actual runtime and quality validation. No paid fallback is allowed.

## Project principles

- Evidence-backed claims and traceable sources.
- Character action and illustration carry the story; no static narrated slideshow.
- Original character/art assets; reference is inspiration, not material to copy.
- Human approval for material creative changes, rights-sensitive assets, spending and public release.
- A render is complete only after the real file is inspected.

## Status

The repository has an earlier pilot script and animation pipeline. The new reference style bible and agent profiles are now committed. The existing pilot scene still needs restyling to match the new reference, and the custom-agent runtime must be validated in a compatible host before claiming that eight subagents are actually executing.

See [docs/production-status.md](docs/production-status.md).

## Licence

No licence has been selected. Do not assume reuse rights for repository contents or third-party assets.
