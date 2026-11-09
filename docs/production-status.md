# Production Status

Updated: 2026-11-10

## Reference and agent setup
- [x] Inspected the owner's uploaded audio-removed reference (approximately 21:19; supplied proxy 256×144, 30 fps).
- [x] Added the visual style bible and editable default profile.
- [x] Added eight specialist custom-agent profiles and the Studio Director coordinator.
- [x] Added shared instructions and documented hand-offs.
- [ ] Restyle the existing pilot scene and inspect a fresh proof render.
- [ ] Validate a compatible host can load profiles and delegate subagents.
- [ ] Validate full pilot build and inspect actual MP4, narration and subtitle sync.
- [ ] Add licensed sound only if suitable.
- [ ] Produce full delivery package and QC report.

## Existing pilot
The repository already contains an earlier urban-heat pilot script, source ledger, Manim scene, Kokoro narration generator, provisional SRT and FFmpeg assembly script. These predate the new visual reference and have not yet been restyled to match it. No current MP4 is marked complete here without download and inspection.

## Agent-runtime limitation
The nine profiles are repository configuration: eight workers plus one coordinator. They are not running processes; GitHub Actions does not execute them. Real delegation requires a compatible Copilot/VS Code agent host with subagent support and its own model/runtime access. No paid API or runtime is configured.

## Project rule
stiXplainer is a stickman explainer/documentary channel. Prioritise expressive recurring characters, gestures, illustrated environments, diagrams, timelines and visual metaphors over static slides. Do not call a milestone complete until the actual file is inspected.
