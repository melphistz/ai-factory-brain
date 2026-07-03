---
name: shotlist-builder-skill
description: "Installed skill shotlist-builder — stateful 4-phase screenplay→shotlist generator, outputs HTML with CHINESE Seedance 2.0 prompts. Companion to seedance-2-pro-director. Has claude.ai-env deps that need adapting for Claude Code."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

Installed at `~/.claude/skills/shotlist-builder/` (from `~/Downloads/shotlist-builder.skill`; 9 files: SKILL.md + templates/HTML_TEMPLATE.md + 7 reference/*.md). The multi-scene companion referenced by [[seedance-2-pro-director-skill]]: director = single shot (English), shotlist-builder = whole screenplay → shotlist. Cinematic-film lane, NOT UGC. Also overlaps our own [[video-prompt-builder-framework]] — decide which to use per job.

## Portability — PATCHED for Claude Code (2026-07-01)
SKILL.md was edited so it runs locally. Added an "Environment (Claude Code)" section + inline fixes:
- `present_files` → Write file + report absolute path
- `visualize:show_widget` → write top-down schema as `.svg` file + describe in text
- `/mnt/user-data/outputs/` → `~/Desktop/Ads/FF_factory/shotlists/`
- uploaded images = local file paths, not chat attachments
Still emits **Chinese** Seedance prompts (提示词) + English UI, default **21:9, 15s/prompt** — for FF UGC switch to 9:16; Chinese prompts are fine for Seedance.

## What it does — 4-phase stateful loop (don't collapse phases)
1. **Read script** — scenes, INT/EXT, characters (first appearances), locations, props, beats, mood.
2. **Asset request** — scannable list (Characters/Locations/Props/Style-refs) → tell user to generate images + name files (`roko.png`) + say which scenes. STOP, wait for uploads.
3. **Scope + spatial blocking** — confirm scenes, map filenames→assets (never silent auto-assign), for any 2+ char or key-prop scene draw top-down schema, get approval before prompting.
4. **Generate HTML shotlist** — shot rows → group into 15s prompts → write Chinese prompt per pattern → multi-shot cuts as `【镜头N】` (机位/背景/动作/微表演细节) → assemble HTML template.

## Hard rules worth stealing (apply to our own prompts too)
- **Handles renumber per prompt**: `@image1` in scene 21 ≠ scene 14; each block declares its own handles (identity-drift guard).
- **Lighting ALWAYS practicals-only** — no fill/reflector/softbox/LED/neon; camera on shadow side (contre-jour). Non-negotiable house style.
- **Camera tracks emotion**: nervous handheld = anger/tension; smooth breathing handheld = calm; static + slow push = shock/revelation.
- **No generic emotion** — decompose every direction into muscles/breath/eyes/skin + numbered beats ①②③④⑤. "surprised" has ≥4 variants; ask which.
- **Top-down schema before prompting** any 2+ char scene.
- **⚠️ warnings in prompt** for likely failure modes; ⚠️⚠️⚠️ for critical (handle contamination, identity drift, light spill, prop misplace, focus drift).
- Style block: Lubezki × Deakins, contre-jour, 60:30:10, practicals-only (reference/STYLE_BLOCK.md, variants by scene type).

## Reference files (deep libraries)
STYLE_BLOCK (default Chinese style + variants) · PROMPT_PATTERNS (handles, spatial, 【镜头N】 syntax, dialogue, failure warnings) · CAMERA_EMOTION (move→emotion, lens, duration) · MICRO_BEATS (perf beats per emotion) · SPATIAL_BLOCKING (top-down schema rules) · PROMPT_DENSITY (group rows→15s) · PLAN_TYPES (shot-plan taxonomy).
