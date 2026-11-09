# Production Status

Updated: 2026-11-10

## Current state

- [x] Public repository and project scaffold.
- [x] Architecture and production workflow documented.
- [x] Two-presenter Manim smoke-test scene added.
- [x] First multi-beat pilot animation scene added at `src/stixplainer/scenes/pilot.py`.
- [x] Pilot narration draft and source ledger added at repository root (`script.md`, `sources.md`).
- [x] Pilot visual build plan added.
- [x] GitHub Actions workflow updated to attempt both the smoke test and pilot scene at 24 fps.
- [ ] Confirm GitHub Actions completes successfully.
- [ ] Inspect actual MP4 render for visual and timing errors.
- [ ] Record and sync British English male narration.
- [ ] Add licensed music and sound effects.
- [ ] Create and time subtitles against final narration.
- [ ] Render final 1920×1080, 24 fps master.
- [ ] Complete final quality-control review and publish deliverables.

## Render verification

The pilot scene and workflow are committed. The workflow is configured to render at low quality (Manim's 480p preset) as an inexpensive technical check, not as the final 1080p master. A successful run and an inspected MP4 are still required before calling the render verified.

## Editorial verification

The script is an initial research-backed draft. The source ledger cites U.S. EPA material for general heat-island mechanisms. It intentionally avoids applying U.S. temperature ranges to Chennai or presenting invented local measurements. Local claims would need India- or city-specific evidence before publication.

## Important distinction

Committed source code and a configured workflow are not proof of a successful render. Mark a milestone complete only after inspecting the actual workflow result or output file.
