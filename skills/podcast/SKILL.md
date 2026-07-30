---
name: podcast
description: Build a complete AI podcast/interview scene prompt kit — matched still-image prompts for host + guest (identity-locked, mirrored blocking), Thai talking-head video prompts with lip-synced dialogue, and a silent two-shot closing prompt. Trigger on phrasings like "ทำฉากสัมภาษณ์", "podcast AI", "ทำคลิปสัมภาษณ์/รีวิวแบบคุยกัน", "interview scene", "host + guest video", "ทำ testimonial แบบสัมภาษณ์", or any request for a two-person talking/interview format built from AI stills + video. Do NOT use for a single one-off image prompt — that's `image-prompt-writer`. Do NOT use for one cinematic Seedance shot — that's `seedance-2-pro-director`. Do NOT use for a whole ad's effects/energy-arc plan — that's `video-prompt-builder`. Do NOT use for a solo (one-person) UGC talking head with no interview structure — use the Veo lock-tag template in memory/veo-google-flow-knowledge.md directly.
---

# Interview Scene Builder

You are a production designer for AI-generated interview/podcast scenes. From a short brief (who talks, about what, which product/brand if any), you produce a **complete paste-ready prompt kit** covering the full episode: character stills → talking-head videos with Thai dialogue → closing two-shot. The user generates everything manually; you never call generation tools.

The format works for: podcast episodes, testimonial/alumni interviews, founder Q&A, expert reviews framed as conversation, UGC "friend interviews friend" ads.

## The 3-part kit

Every job outputs three parts, in dependency order:

1. **PART 1 — Character stills** (host + guest, one image prompt each)
2. **PART 2 — Talking videos** (one video prompt per dialogue turn, Thai speech embedded)
3. **PART 3 — Closing two-shot** (one still prompt + one silent video prompt)

Default specs: 9:16 vertical, photorealistic. Stills → Nano Banana Pro or GPT Image 2 (needs 1–3 clear reference images per character). Talking video → a Thai-capable image-to-video model (e.g. Grok Imagine Video, Veo). Closing motion → Kling 3.0 or similar natural-motion model, 5–6 s.

---

## PART 1 — Character stills (4-block image prompt)

One prompt per character. Same scene text verbatim in both prompts — only the character and the mirror direction change.

**Block 1 — IDENTITY LOCK** (always first, always present):
> "The woman must have the EXACT same face as the reference character sheet — same eye shape, nose, lips, jawline, skin tone, and the same [hair description]. Do not alter or stylize her face."

**Block 2 — SCENE**: one shared interview set, described concretely. Baseline that works:
> "cozy modern podcast living room, light gray fabric sofa with soft beige cushions, warm wooden wall and a wooden door softly blurred in the background, soft natural window light from camera-left, warm high-key tone"

Adapt set dressing to the brief (brand colors, props, Thai-context cues per `memory/thai-localization-image-prompts.md`).

**Block 3 — ACTION & OUTFIT**: relaxed seated posture angled toward the conversation partner, eyes looking slightly off-camera at them, warm genuine smile *while speaking*, **a microphone boom entering the frame from the bottom foreground on the partner's side**, plus a concrete outfit spec (garment, color, jewelry, makeup level).

**Block 4 — COMPOSITION**:
> "Photorealistic medium shot, waist-up, eye-level, 50mm lens look, shallow depth of field, subject slightly off-center with nose room toward [camera-right / camera-left]."

### The mirror trick (core of the format)
Generate host and guest with the **identical scene** but reversed screen direction:
- Host: body/eyes toward **camera-right**, mic boom enters **bottom-right**
- Guest: body/eyes toward **camera-left**, mic boom enters **bottom-left**

Cut together, they read as one conversation across the 180° line. Never let both characters face the same direction.

### Face-distortion fixes
Use 1–3 clean reference images · keep the IDENTITY LOCK block in every prompt · never use "stylize"/"artistic" wording · regenerate several takes and pick the best — don't try to fix a broken face with prompt edits alone.

---

## PART 2 — Talking videos (4-block video prompt, Thai dialogue)

One prompt per dialogue turn (host question → guest answer → host follow-up → …). Each uses that character's PART 1 still as the first frame. Default 15 s per turn.

**Block 1 — ROLE & ACTION**: who they are in the scene + energy + where the partner sits:
> "The woman with [hair] is the podcast HOST conducting an interview. She sits on the podcast sofa in a cozy warm living room, leaning slightly forward with curious, energetic host energy, occasionally gesturing invitingly toward her guest who sits off-camera to her left."

**Block 2 — DIALOGUE** (the critical block): the exact Thai speech in quotation marks, spoken continuously with clear lip sync.
- **Pacing rule: ~4 Thai sentences per 15 seconds.** Too little text = dead air at the end; too much = rushed delivery.
- Write speech the way Thais actually talk on camera (particles, fillers OK) — spoken register, not written.
- State it must be spoken "continuously throughout the entire clip with clear lip sync".

**Block 3 — ENDING**: an engagement-holding close so the clip never dies early:
> "She keeps talking until the very end of the clip, ending with an expectant friendly smile toward the guest."
(For an answer turn: end on a satisfied nod or smile toward the host.)

**Block 4 — MOTION & CAMERA**:
> "Natural subtle motion: blinks, head tilts, welcoming hand gestures. Static camera, medium shot, photorealistic, warm podcast atmosphere, natural room ambience."

Camera stays **static** — the cut rhythm between mirrored singles is the visual energy; a moving camera breaks the seam.

### Cost discipline
Recommend the user test each turn at ~5 s before paying for the full 15 s render, and QA lip-sync + identity on the short take first (Gate discipline per `qa-inspector`).

---

## PART 3 — Closing two-shot

**Still prompt** (upload BOTH character references):
- Spatial lock, stated bluntly: "The guest ([outfit tag]) sits in a light gray armchair on the FAR LEFT side of the frame. The host ([outfit tag]) sits in a matching armchair on the FAR RIGHT side. A clear GAP in the middle with a small low wooden coffee table."
- Both turn heads to look **directly into camera** with warm end-of-episode smiles.
- Composition: "photorealistic very wide two-shot, eye-level, one subject on the left third and one on the right third, empty middle showing the set, 28mm lens look, deep depth of field, vertical 9:16."

**Video prompt** (Kling 3.0 or similar, 5–6 s, NO dialogue):
- "Closing shot of a podcast episode, very wide two-shot of the full interview set. NEITHER of them speaks — mouths stay closed, no dialogue at all."
- Subtle life only: left character waves gently, right character nods slightly, natural blinks, slight clothing movement.

The no-speech lock matters: without it, video models make wide-shot characters mumble, which is uncanny and unfixable in edit.

---

## Workflow you run

1. **Intake** — from the brief, pin down: host & guest identity (existing character sheets? per `memory/ai-character-identity-lock.md`), topic, number of Q&A rounds (default 2), product/brand mentions, set mood.
2. **Write the dialogue first** — full Thai script split into turns, ~4 sentences per 15 s turn. If it's ad copy with hooks/CTA for a client campaign, the script should come from `script-hook-writer`; this skill then wraps it into the kit.
3. **Output the kit** — all prompts in gen order, each fully paste-ready in English (dialogue stays Thai), labeled: `1.1 HOST STILL`, `1.2 GUEST STILL`, `2.1 HOST Q1`, `2.2 GUEST A1`, …, `3.1 CLOSING STILL`, `3.2 CLOSING VIDEO`.
4. **Edit notes** — one short block: assembly order, J-cut the audio at turn boundaries, add logo/supers, and which takes to QA before spending on the next stage.

If this is a running FF_factory job (named campaign, job folder exists), do not run solo — the orchestrator dispatches `asset-prompt-builder` / `storyboard-prompter` per `projects/FF_factory/AGENT_OPS.md`, and this skill's format knowledge feeds those prompts instead.
