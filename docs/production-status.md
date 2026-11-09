# Production Status

Updated: 2026-11-10

## Current state

- [x] Public repository created.
- [x] Project overview and architecture documented.
- [x] Python package scaffold committed.
- [x] Automated Python-check workflow added.
- [x] First Manim scene smoke-test source added.
- [x] Smoke-test scene expanded to show two stick-figure presenters, a sun, city buildings, windows and animated heat waves.
- [x] Pilot topic and visual beat sheet drafted.
- [ ] Confirm CI test run passes.
- [ ] Confirm Manim renders a video on a free hosted runner.
- [ ] Build the full 60–90 second pilot scene.
- [ ] Add verified research and source ledger.
- [ ] Validate a British English male narration option on free compute.
- [ ] Add licensed music, sound effects and subtitles.
- [ ] Render and inspect 1920×1080 at 24 fps.
- [ ] Publish the pilot deliverables.

## Current render proof

The expanded scene source is committed in `src/stixplainer/scenes/smoke_test.py`. The GitHub Actions workflow is configured to render it at low quality and 24 fps, then upload an MP4 artifact. The workflow has not yet been observed completing, and no MP4 has been inspected; this is source-code progress, not a verified render.

## Important distinction

A committed scene or workflow is not proof of a successful render. Mark a milestone complete only after inspecting the actual workflow result or output file.
