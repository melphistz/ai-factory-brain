---
name: video-prompt-builder
description: Turn a creative brief into a complete short-form AD VIDEO planned as an effects + energy-arc breakdown for Seedance 2.0 — a shot-by-shot effects timeline, master effects inventory, effects-density map, and three-act energy arc. Use when the user gives a brief or concept for a WHOLE promo / brand film / product video / social ad and wants the full multi-shot video planned with pacing, transitions, and effects. Trigger on "plan a video", "video concept", "brand film", "ad concept", "effects breakdown", "energy arc", "make me an ad video from this brief". Do NOT use for writing one precise character-blocked single shot — use seedance-2-pro-director. Do NOT use for turning an uploaded screenplay into a multi-scene production shotlist — use shotlist-builder.
---

# Video Prompt Builder for Seedance 2.0

Build a whole-ad, shot-by-shot effects plan from a creative brief. Every output follows a structured effects breakdown format covering camera work, effects, transitions, pacing, and energy arc.

## Scope — planning layer, NOT a paste-ready Seedance prompt

- This skill plans the WHOLE video: energy arc + effects map + shot list. Most stacked effects in this format (whip pan, mirror/symmetry, stroboscopic clone, bloom flash, frame rotation) are EDIT-layer effects (CapCut/post) — not things Seedance 2.0 generates inside one clip.
- Do NOT feed this output to Seedance directly — it breaks the per-clip rule "1 prompt = 1 simple clip". Per-clip prompts are written separately after this plan is locked.
- Text plan only: never call any image/video generation tool or MCP from this skill (factory rule: no credits burned from Claude; all generation is manual).

## Hand-off after the plan

- ONE precise character-blocked shot → `seedance-2-pro-director` skill (single-shot lane). Uploaded screenplay → multi-scene shotlist → `shotlist-builder`.
- Factory pipeline (`projects/FF_factory/AGENT_OPS.md`): this plan feeds the brief/concept stage. Per-shot video prompts are written by the **storyboard-prompter** agent (step 4, from real storyboard frames); the effects map feeds edit/timeline cues (**timeline-builder**, step 5 fx markers) — not the Seedance prompt itself.
- For an individual shot where freestyle liveliness matters more than exact control (mood/fashion/product feel), the per-clip prompt can use the Marco "rules, not shots" pattern instead of full blocking — see `memory/seedance-marco-freestyle-method.md`. This is a per-clip prompting choice made at the hand-off stage, not part of this plan's four sections.
- Vault sources, readable at runtime on both OS (mac `/Users/working/ai-factory-brain/` · Windows `D:/ai-factory-brain/`): `memory/video-prompt-builder-framework.md` (this framework + scope rule) · `memory/seedance-knowledge.md` (per-clip prompt craft, "1 prompt = 1 clip", resolution/no-seed notes) · `memory/seedance-marco-freestyle-method.md` (rules-not-shots alternative).

## How this skill works

1. The user provides a **creative brief** — this can be as simple as "a runner in a stadium for a Nike-style ad" or as detailed as a full storyboard description. They may also provide a reference video, mood, brand context, or specific effects they want.
2. Read the reference file at `references/effects-breakdown-reference.txt` to internalise the structure and level of detail expected.
3. Generate a complete video prompt in plain text, structured into the four mandatory sections below.

## Input expectations

The user's brief can include any combination of:
- Subject/talent description (who or what is on screen)
- Setting/environment
- Mood, tone, energy level
- Brand or product context
- Specific effects or camera moves they want
- Duration target
- Reference to existing ads, films, or visual styles
- Colour palette or grade preferences

If the brief is too vague to build a full prompt (e.g. "make something cool"), ask one focused clarifying question before proceeding. Don't over-interrogate — work with what you're given and make creative decisions where the user hasn't specified.

## Output structure

ALWAYS output ALL FOUR sections in this exact order. Never skip a section.

### Section 1: SHOT-BY-SHOT EFFECTS TIMELINE

This is the core of the prompt. Each shot gets its own block structured like this:

```
SHOT [N] ([timestamp]) — [Shot Name / Description]
• EFFECT: [Primary effect name] + [secondary effects if stacked]
• [Detailed description of what's happening visually]
• [Camera behaviour — angle, movement, lens if relevant]
• [Speed/timing information]
• [How this shot connects to the next — transition type]
```

Guidelines for writing shots:
- Each shot should be 1-4 seconds unless the brief calls for longer holds
- Name effects precisely: "speed ramp (deceleration)" not just "speed ramp"; "digital zoom (scale-in)" not just "zoom"
- Describe stacked effects explicitly — if 3 things happen at once, list all 3
- Include transition logic: how does this shot EXIT and how does the next shot ENTER?
- Describe the visual result, not the editing software technique. For example, say "the frame scales inward rapidly" rather than "apply a keyframed scale effect in After Effects" — the plan must read as director's notes that translate later into per-clip prompts and edit cues
- Note the most impactful or signature shot with a callout like "This is the SIGNATURE VISUAL EFFECT"
- Be specific about speed percentages when using slow-motion (e.g. "approximately 20-25% speed")
- Describe motion blur, light behaviour, and atmospheric effects where relevant

### Section 2: MASTER EFFECTS INVENTORY

A numbered list of every distinct effect used across the full prompt, with:
- Effect name
- How many times it's used (e.g. "used 3x")
- Which shots it appears in
- A one-line description of its role in the edit

This section helps the user (and the generator) see the full palette of techniques at a glance. Group similar effects together. Typical categories include: speed manipulation, camera movement, digital effects, transitions, compositing, optical effects.

### Section 3: EFFECTS DENSITY MAP

Break the timeline into segments (roughly 3-6 second chunks) and rate each as:
- **HIGH DENSITY** — 4+ effects stacked or rapid-fire
- **MEDIUM DENSITY** — 2-3 effects
- **LOW DENSITY** — 1 effect or clean/simple footage

Format:
```
[timestamp range] = [DENSITY LEVEL] ([brief list of effects] — [count] effects in [duration])
```

### Section 4: ENERGY ARC

Describe the overall energy structure of the video as a narrative arc. The reference uses a three-act model:
- **Act 1**: Opening energy — how the video grabs attention
- **Act 2**: Middle section — how it develops and what the signature moments are
- **Act 3**: Resolution — how the energy resolves and lands

Adapt the number of acts to suit the video's length and structure. A 5-second clip might only need two beats; a 30-second brand film might need four.

## Creative principles

These principles should guide every prompt you write:

1. **Contrast drives impact.** Alternate high-density and low-density moments. A slow-motion shot after a speed ramp hits harder than two speed ramps back-to-back.
2. **Signature moments matter.** Every video should have at least one "hero" effect — something visually distinctive that makes it memorable. Call it out explicitly.
3. **Transitions are shots.** Don't treat transitions as throwaway connectors. A whip pan, a bloom flash, a motion blur smear — these are creative moments, not just cuts.
4. **Specificity over vagueness.** "The frame rotates clockwise by approximately 15-20°" is better than "the camera tilts." "Approximately 20-25% speed" is better than "slow motion."
5. **Energy must resolve.** No matter how intense the opening, the video needs to land. The final moments should feel intentional, not like the effects budget ran out.

## Tone and style

- Write in a direct, technical tone — like a director's shot notes, not a marketing brief
- Use bullet points within each shot block for clarity
- Be concise but complete — every detail should earn its place
- No hype language, no "stunning" or "breathtaking" — describe what happens and let the visuals speak

## Duration calibration

Adjust the number of shots and effects density to match the target duration:
- **5-10 seconds**: 4-7 shots, lean and punchy, 1 signature effect
- **10-20 seconds**: 8-14 shots, room for contrast and build, 1-2 signature effects
- **20-30 seconds**: 12-20 shots, full three-act arc, 2-3 signature effects
- **30+ seconds**: Scale accordingly, but maintain density contrast — don't fill every second with effects

If the user doesn't specify a duration, default to 15-20 seconds (a sweet spot for AI video generation).

## Example workflow

**User says:** "I want a dramatic brand film for a trail running shoe. Mountain setting, golden hour, single runner. Make it feel epic but not over-the-top. About 15 seconds."

**You do:**
1. Read `references/effects-breakdown-reference.txt` to calibrate detail level
2. Generate the full four-section output: shot-by-shot timeline (8-12 shots), master effects inventory, density map, and energy arc
3. Present in plain text in chat
4. Close with the hand-off: per-clip Seedance prompts are written separately, one simple prompt per clip (see "Hand-off after the plan" above)
