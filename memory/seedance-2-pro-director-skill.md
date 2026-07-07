---
name: seedance-2-pro-director-skill
description: Installed skill seedance-2-pro-director — elite single-shot Seedance 2.0 prompt director (formula + character-anchor + frame-coordinate + QA system). Cross-lane (commercial + UGC).
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

**07-07: Fable audit ยกระดับ (11 findings)** — เติมของ verified: กฎทองมุมกล้อง, under-direct ฉบับแก้ (ไม่ใช่หน้านิ่งตลอด/deadpan ที่ punchline), input-mode decision tree + extension>regen, hyperzoom, hand fix, emotional-arc micro-beats, host facts (หน้าจริงไม่บล็อก), working budget ≤1,800 — โดยคงระบบเดิม (anchor/coords/6-part output) ครบ

Installed at `~/.claude/skills/seedance-2-pro-director/SKILL.md` (from Higgsfield Cannes-film tutorial `6aJ2BneDB5M`, downloaded to `~/Downloads/seedance-2-pro-director.skill`). THIS skill IS the "system prompt compiling the 28 tips" the Cannes video promises — nothing else to pull from that video's Google Drive for the prompt system. Auto-invokes when user asks for a SINGLE-shot Seedance prompt ("write a Seedance prompt", "lock character in left third", "two-character blocking"). Companion `shotlist-builder` handles multi-scene shotlists (NOT yet installed). Sits alongside our own [[video-prompt-builder-framework]] skill (whole-ad planner) — director = single shot, video-prompt-builder = full ad; watch for trigger overlap. Deepens [[seedance-knowledge]]. Cross-lane: works for both cinematic-commercial [[higgsfield-3step-ai-ad-workflow]] and UGC [[ai-ugc-ad-factory-workflow]].

## 3-skill lane division (set 2026-07-01 to stop trigger collision)
- **video-prompt-builder** — brief → whole ad video as EFFECTS + energy-arc breakdown (timeline/inventory/density/3-act). Description rewritten to drop "shot list / Seedance prompt / mentions Seedance" catch-alls + hand off explicitly.
- **seedance-2-pro-director** (this) — ONE precise character-blocked shot.
- **shotlist-builder** — uploaded SCREENPLAY → multi-scene HTML shotlist.
Each description now names the other two for hand-off. To force one, name it explicitly ("use shotlist-builder" / call the skill by name).

## Core formula
`Subject + Motion + Environment + Aesthetics + Camera + Audio`
Cinema-expanded: `Output settings + Mode/refs + Spatial map + Character anchors + State locks + Motion plan + Camera plan + Environment + Aesthetics + Lighting + Audio + Continuity + Final frame`

## The 7 questions every prompt must answer
who's in frame / where exactly (coords) / pose+state / what moves / what's locked / how camera moves / what final frame must show.

## Key systems (all aimed at killing drift + identity break)
- **Frame coordinates**: thirds + x/y percent (x=30% = left third; feet near y=88%) + frame-occupancy %. Anchors, not math guarantees.
- **Character Anchor Block** (per character, 10 fields): identity / screen-position / depth / frame-occupancy / body-orientation / pose / state / gaze-line / contact-points / lock.
- **State locks**: emotion, posture, costume, hair, wet/dry, object-in-hand, expression, gaze, body tension.
- **Grounding/contact points** stop floating: "boots planted on same ground marks", "shadow stays attached to feet".
- **Motion hierarchy — 4 separate layers**: subject / internal (breath, hair, fabric) / camera / environmental.
- **Positive > negative**: rewrite prohibitions as positive locks (not "no face change" → "keeps same face, hair, costume, proportions, silhouette throughout").
- **Spatial locks (2+ chars)**: never swap sides, never cross center vertical axis, keep negative space, fixed eyelines/screen-direction.
- **Reference discipline**: Image1=identity, Image2=costume, Image3=environment, Image4=composition; Video1=motion-only, Video2=camera-only; on conflict, state priority explicitly.
- **Mode select**: T2V (idea only) / I2V (animate a still) / R2V (combine multi-refs) / V2V (transfer motion/camera/VFX from clip).

## Mandatory 6-part output
1 director's interpretation → 2 spatial blocking map → 3 reference plan → 4 final English prompt → 5 positive constraints → 6 QA checklist (12 items).

## Shot complexity limits
4–8s = one action · 8–12s = action+reveal · 12–15s = 2–3 beats · fight/chase/transformation = split into multiple prompts. 9:16 for TikTok/Reels, 16:9 cinema.

## Language rules
Simple present, concrete visual nouns, one instruction/sentence, standard film vocab. Kill empty words (epic/beautiful/cinematic-masterpiece) → replace with specifics (35mm anamorphic, warm practical key from screen-left, slow 10% dolly-in preserving blocking). On-screen text: keep short, spell exact, set timing/position/font/color.
