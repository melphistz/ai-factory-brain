---
name: higgsfield-3step-ai-ad-workflow
description: "CINEMATIC-COMMERCIAL lane (NOT UGC) — Higgsfield's own Seedance 2.0 4K tutorial: 3-step asset→shotlist→scene + consistency tricks (layout map, erase-face, style prefix)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

**LANE: cinematic commercial, NOT UGC.** This is the polished broadcast-grade side (headphones ad, 8K IMAX 16:9, multi-location, choreography, packshot) — the Commercial half of FF factory's "10 ตัว Commercial + UGC". Do NOT mix its cine style prefix into UGC work (UGC = phone selfie, vertical 9:16, raw/imperfect). Only the cross-lane techniques below carry over to UGC.

Higgsfield AI official tutorial "3-Step Workflow To Make Ultra-Realistic AI Ads" (YouTube `3rDs6FhFoUQ`, 35:37, 2026-06-23). Same stack as FF factory: Higgsfield + Seedance 2.0 + GPT Image 2 + custom Claude skill script→shotlist. Reinforces [[ai-ugc-ad-factory-workflow]] and [[video-prompt-builder-framework]].

**Cross-lane (works for UGC too):** element `@naming`, erase-face identity-lock, multiple-outfit lock, per-scene cut-by-cut formula, spell-out-every-move choreography.
**Commercial-only (do NOT copy to UGC):** the 8K/IMAX/cine-lens style prefix, layout-map for multi-location scenes.

**Skill they distribute:** `higgsfield-seedance-shotlist-director.skill` (zip) at https://higgsfield.ai/s/cinema-studio-higgsfieldai-whzLmx — worth comparing to our own video-prompt-builder skill.

## 3-step workflow
1. **Build + test all assets first** (product sheet, hero character, locations, props) — lock everything before camera moves.
2. **Shotlist via Claude skill** — turns script into connected shotlist: reusable style prefix + named per-scene prompts (1a,1b,2a...). Edit prefix once = updates all scenes.
3. **Generate scenes one at a time**, iterate, edit keeper seconds from dozens of gens into final cut.

## Tools per stage
- GPT Image 2 → product sheets, edits, schematic/layout maps
- Soul Cinema + Cinematic Locations → photoreal stills (character, locations)
- Seedance 2.0 → the scenes (now 4K native — no upscale, no AI-slop look)

## Element naming system (key trick)
Attach assets with exact matching `@names` (`@hero`, `@headphones`, `@kitchen`...). Because prompt names match attached image names, every skill-written prompt auto-attaches the right refs on generate.

## Style prefix (reusable header on every scene prompt)
- "8K IMAX commercial, 16:9 widescreen. Photorealistic — no 3D render, no game engine."
- Natural light only + time-of-day direction
- Color "60:30:10 — dominant/secondary/accent"
- "Physical cine lens. 180° shutter motion blur"
- Skin: "Pore-level realism — vellus hair, asymmetric moles, capillary flush"
- Acting: "Hollywood — micro-pauses before reactions, precise eye-line, living eyes"
- Physics: "Gravity and inertia respected — mass has real weight"
- Audio: "Diegetic dialogue and environmental SFX only. No music. No subtitles."

## Consistency techniques (solve our 2 physical risks)
- **Layout map trick**: text can't pin a location; a schematic map can. Make GPT Image 2 top-down/schematic marking fixed object positions, reference in every cut → placement stays across shots.
- **Erase-face**: character sheet with 2 faces → prompt "Erase the face from the full-body shot on the right panel" so video model has single face to lock (stops identity drift). Relevant to Ploy identity-lock.
- **Multiple-outfit lock**: separate sheets per look (everyday / athletic / sweat-soaked) so costume change ≠ identity drift.

## Per-scene prompt formula
style header → character list w/ @refs → scene desc (location/light/time/layout ref) → cut-by-cut (framing: lens/FOV/angle/motion; action beat-by-beat; performance cues). Choreography = spell out each move, not "he dances". Product lock w/ directional cues ("headphones stay locked rock-solid on his ears"). Repeat continuity details across cuts. Music: `@music_track` audio ref, movement locked to rhythm; else all diegetic.

## 2nd tutorial — Football/robot soda ad (advanced techniques)
"How To Make Cinematic Football Ads With AI" (YouTube `ODNzk5x2tR4`, 46:05, 2026-06-15 / blog https://higgsfield.ai/blog/cinematic). Same 3-stage, action/sports genre, 7 scenes incl transformation + robot match + villain comeback. Separate skill zip: `higgsfield.ai/s/football-ad-workflow-higgsfieldai-gdGTwo`. Adds:
- **Beat-based narration + slow-mo ramping**: write action as discrete "beats", pair camera move to each; specify speed ramp as % per shot e.g. `100%→60%→70%→40%→100%`. Toggle per scene: "NO slow-motion — full speed throughout". (cross-lane usable)
- **Physics rewrite for weight** (override AI softness): ball = "SOLID FORGED-STEEL, 22cm, 7kg, behaves like a cannonball"; bodies = "practical suits with stunt actors, biomechanically committed". (cross-lane)
- **Transformation prompt**: armor "assembles from FLYING PIECES OF METAL — solid hard-surface plates"; anti-game negatives "no 3D render, no game engine, no game-cutscene aesthetic"; lock emotion "JOYFUL, exhilarated throughout — grinning". (commercial-only)
- **Location = STYLE REFERENCE ONLY, not a fixed keyframe** → lets Seedance extend/build environment while holding tone. Different from layout-map (which pins fixed positions). Pick per need: pin placement = map; free-extend = style-ref-only. (commercial-only)
- **Exact numeric cues**: handheld shake in cm (`6–10cm`, `10–16cm`), dutch angle degrees (`14°–20°`), multishot 3–5 shots/scene w/ timecodes (0:00–0:15), hard cuts no fades. (commercial-only)
- **Ref syntax**: uses both `@name` and inline `<<<image_1>>>` in prompt body.
- **Football style-header variant**: "8K large-format. Photorealistic — no 3D render/game engine/game-cutscene. naturalistic large-format, long flowing takes, available-light realism. Natural light only — contre-jour backlight, camera on shadow side. Physical cine lens 180° shutter. Aggressive operator shake 6–10cm, no stabilization. NO MUSIC. SFX ONLY — diegetic."
- Both tutorials show every failed generation + director's note + fix (learn why gens break).
