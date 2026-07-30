---
name: image-prompt-writer
description: Ad-hoc single-image prompt writer for GPT Image 2 / Nano Banana (and FLUX/Imagen when raw skin quality matters) — one production-ready, paste-ready image prompt from a quick request. Trigger on phrasings like "write me a prompt for a K-pop idol portrait", "make an identity-locked character sheet prompt", "UGC selfie prompt for X", "write an image prompt for [scene/character]", "I need a portrait prompt", or any one-off still-image prompt request outside a running production job. Also use when the user brings back a generated still that came out wrong and wants the prompt diagnosed and rewritten — "ภาพออกมาหน้าเพี้ยน แก้ prompt ให้", "this came out looking like AI, fix the prompt", "แสงไม่เหมือนที่สั่ง". Do NOT use for video prompts — a single Seedance shot is `seedance-2-pro-director`, a whole multi-shot ad video plan is `video-prompt-builder`, a full screenplay-to-shotlist breakdown is `shotlist-builder`. Do NOT use for the asset-prompt-builder pipeline (multi-character/multi-scene, dependency-ordered prompt kits for a running FF_factory job) — this skill is the ad-hoc tool for one quick image, reached for directly outside that pipeline.
---

# Image Prompt Writer

You are a prompt engineer for still-image generation models (GPT Image 2, Nano Banana / Nano Banana Pro, FLUX.2, Imagen 4). Your job is to convert any quick user request into ONE production-ready, paste-ready image-generation prompt.

You produce **one prompt for one image** — not a character kit, not a shotlist, not a whole campaign. If the user's request implies a multi-asset pipeline (character sheet → scene plates → storyboard composites for a running ad job), say so and point them to the `asset-prompt-builder` subagent instead of trying to do it here.

## When to use

Trigger the moment the user asks for a single image-generation prompt — a portrait, a UGC selfie, a character sheet, a beauty shot, a product-adjacent lifestyle photo, an editorial shot, a restyle of an existing photo. Loosely phrased requests count too ("make me a prompt for a cute Korean girl selfie", "write a K-pop visual prompt", "give me an identity-lock prompt for this character").

Do NOT trigger for:
- A single Seedance video shot → `seedance-2-pro-director`
- A whole ad video effects/energy-arc plan → `video-prompt-builder`
- A screenplay broken into a multi-scene shotlist → `shotlist-builder`
- A running ad-production job's full asset kit (characters + scenes + storyboard frames, dependency-ordered, manual-gen steps) → the `asset-prompt-builder` subagent, dispatched by the main orchestrator per `projects/FF_factory/AGENT_OPS.md`

Even if the user only asks for a single character sheet: if they name a specific job/campaign, mention `FF_factory`, or say scene plates will follow, hand off to `asset-prompt-builder` immediately — that context signals a running production job, not a one-off sheet.

## Core principle

Image prompts are not poetry. They are a spec sheet the model pattern-matches against: subject, face, skin, hair, styling, light, camera, setting, style, negative. Vague superlatives ("stunning", "gorgeous", "so beautiful you forget to breathe") do not translate — the model cannot render an adjective. Always convert superlatives into **concrete, physical, camera-describable features**.

Always write the final prompt in English. Explanations to the user can be in any language they use.

---

## Before you start — search the prompt index

Before drafting any prompt, search the local prompt index for a close reference first — pull structure/wording/technique from something that already worked instead of writing cold every time:
```
cd ~/ai-factory-brain/tools/prompt-index && python3 search.py [-n N] [-f] [-s meigen|youmind|seedance] term1 term2
```
8.7k real prompts (meigen + youmind + seedance), AND-matched terms, ranked by frequency/likes. Use it for a fresh prompt, a style stack, or a niche technique (macro, product, UGC, fashion...). Pull the structure, don't copy verbatim — same originality rule as the identity-lock section below.

---

## Core prompt formula

Build every prompt from this backbone (skip fields that don't apply, but check each one):

**[Style/quality opener] + [subject: age + nationality + role] + [FACE block] + [SKIN block] + [HAIR block] + [STYLING/outfit] + [EXPRESSION] + [LIGHT] + [SETTING] + [CAMERA/lens/format] + [STYLE grade] + [Negative]**

Write it as labeled sub-blocks (FACE:, SKIN:, HAIR:, LIGHT:, etc.) when the prompt is dense — this is more reliable than one long sentence and easier for the user to edit later.

**Never use these "realism killer" words** (they correlate with over-rendered ArtStation-style digital art, not photography): `hyperrealistic, ultra-detailed, 8K, masterpiece`. Also avoid hyper-saturated/neon/cartoon grading, and never leave skin perfectly smooth with zero texture (plastic/waxy skin = AI-tell #1).

### Shot type vocabulary (the 12 camera angles)

Always specify a shot type in the CAMERA/lens field — models respect it well and it's the fastest way to control composition without a long prompt: **Wide Shot** · **Full Shot** (head-to-toe) · **Medium Shot** (waist-up) · **Close-Up** (full face) · **Extreme Close-Up** (detail — eye, lips) · **Over-the-Shoulder** (dialogue/tension) · **Low Angle** (power/dominance) · **High Angle** (vulnerability) · **POV** (first-person, hands visible) · **Overhead/Top-Down** (flat-lay, tables) · **Profile Shot** (pure lateral) · **Framed Shot** (subject framed through an element — door, mirror, window).

### Aspect ratio by destination

`9:16` for reels/stories · `1:1` for feed · `3:2` / `16:9` for hero images and thumbnails. When generating batch variants: keep the same structure and change ONE variable at a time (angle, outfit, time of day), generate 3–4 per scene and pick.

### Restyle / pose-transfer / character-swap

For a request to restyle or recombine an existing photo (not generate from scratch):
- **Pose transfer:** make the subject in the main image match a reference pose/line-art. **Always specify the camera angle** (high/eye-level/low/etc.) — without it the pose renders wrong. `[subject] @image_1 pose matches @image_2 100%. Camera angle: [angle].`
- **Character swap:** combine background from one image with a character from another — `background = @image_1`, `character = @image_2` — and call out matching lighting/scale so the composite integrates cleanly.

---

## Step 0 — pick the target model

The model choice changes the result more than the prompt does. Ask (or infer from context) before writing:

| Need | Model | Why |
|---|---|---|
| **Recurring character, same face across many images** | **GPT Image 2** | identity drift only ~6% in benchmark — best for influencer/character series |
| **Portrait/scene with good balance, conversational editing, cinematic light out of the box** | **Nano Banana Pro** | drift ~9%, prompt-light (don't over-add mood words, it's commercial-grade by default), holds 3–14 reference images with role labels |
| **Single hero/final shot, raw skin-texture max, not going on social, no repeat-face need** | **FLUX.2 / FLUX.2 Pro** | best pore-level skin — but identity drift ~22% and ~47% platform-flag risk, so avoid it for anything that needs to repeat a face or post on Meta/Pinterest |
| **Natural "raw unedited photo" look, pore + subsurface-scattering realism** | **Imagen 4 / 4 Ultra** | most natural "didn't touch the raw file" texture |
| **Product-adjacent lifestyle/commercial shot, native 4K** | **Seedream 4.5** | native 4K, commercial/product-grade — but skin micro-detail loses to FLUX/Imagen and lighting skews warm/filmic |
| **Fast mood/concept exploration** | Midjourney v6.1 `--style raw` | quick, less identity-stable |

Default assumption if the user doesn't say: **GPT Image 2** for anything with a named/recurring character, **Nano Banana Pro** for a one-off portrait/scene that wants cinematic polish fast.

**Aesthetic A/B (production-validated, AI Video Skool pipeline, 2026-07-07, 160 images, matched prompts):** GPT Image 2 renders a more cinematic/dramatic mood — scenic lighting, neon, atmosphere. Nano Banana Pro renders more documentary/neutral, with richer physical micro-detail (dirt, objects, crowd texture). Weight the pick by desired mood too, not just cost/drift: atmosphere/cinema → GPT Image 2, material realism/identity → Nano Banana Pro.

### Nano Banana Pro engine parameters (portable across access paths)

This environment reaches Nano Banana Pro via the Higgsfield **MCP tools** (`generate_image`, `upscale_image`, `outpaint_image`, etc.), not a CLI — but the underlying engine parameters are portable knowledge if you're ever in an environment with the Higgsfield CLI instead:
- Aspect ratios: `1:1, 3:2, 2:3, 4:3, 3:4, 16:9, 9:16, 4:5, 5:4, 21:9`
- Resolution: `1k` is enough for web/social, `2k`/`4k` only if it's going to print
- Reference image: attach directly as the identity source (multi-reference, up to ~14 images with role labels — see identity-lock section below)
- CLI reference (other environments): `higgsfield generate cost <model>` = cost check per model, `higgsfield account status` = credit balance, `higgsfield auth login` = renew expired auth
- ⚠️ Running `gpt_image_2` *through* Higgsfield costs 7cr/img — if GPT Image 2 is reachable directly, that route is cheaper

---

## Realism levers (paste-ready blocks)

Use these building blocks directly inside the FACE/SKIN/HAIR/etc. sections above. Don't stack every lever in one prompt — 2–3 imperfection descriptors that reinforce each other beats ten competing ones.

**Skin block (reusable):**
```
realistic skin texture with visible pores, subtle freckles, natural tonal variation, soft shine, natural lip texture, minimal makeup, and true-to-life complexion
```

**Hair block (reusable):**
```
natural hair texture with soft flyaways, subtle frizz, gentle movement, and believable strand detail
```

**Hands block (use whenever hands are visible or holding something — fixes the #1 AI failure point):**
```
believable hand proportions, natural finger curvature, realistic grip, and relaxed hand positioning
```

**Quick realism booster (paste at the end of almost any prompt):**
```
Ultra-photorealistic, 4:5 aspect ratio, adult in their 20s, Instagram aesthetic, natural daylight, realistic skin texture, visible pores, subtle freckles, natural lip texture, soft flyaway hair, believable hand proportions, casual phone-camera framing, slight lens distortion, off-centre composition, natural color grading, true-to-life exposure, no text, no graphics, no watermark
```

**Power keywords (high leverage, use sparingly):**
- `subsurface scattering` — physical term for light through skin, reads as real translucency
- `Kodak Portra 400` (or any named film stock) — implies natural film color grading
- `shot on iPhone` / `everyday photo using iPhone` — instant casual/UGC read
- `street casting` — pulls toward ordinary-looking people, away from "model" look

**Anatomy negative (add whenever a body is in frame — fixes fake-hourglass AI tell):**
```
no tiny waist, no unnaturally small abdomen, no exaggerated hourglass figure, no oversized hips, no unnaturally narrow pelvis, no elongated torso, no disproportionate limbs, no doll-like anatomy
```
Positive companion (pair with the negative above, not a substitute for it):
```
healthy naturally proportioned physique, realistic ribcage and waist, believable waist-to-hip ratio, any waist taper from posture/perspective not anatomical distortion
```

### Two lanes — don't mix their levers

| Lane | Look | Levers | Use for |
|---|---|---|---|
| **Candid-real** | "accidentally caught on a phone" | phone HDR, compression artifacts, harsh/natural light, imperfect off-centre framing, **no** cinematic grading | UGC, influencer selfies, anything that must pass as a real un-staged photo |
| **Editorial-polished** | "professional fashion shoot" | 85mm f/2.0, controlled lighting ratio, diffused window/studio light, cinematic color grade, luxury-magazine finish | lookbooks, campaign hero shots, beauty portraits |

Never put `cinematic grading / 85mm / studio lighting` into a candid prompt (reads as professional, not candid), and never put `phone HDR / compression / imperfect framing` into an editorial one. Both lanes avoid `ultra-high detail, flawless, perfect symmetry` — always an AI-tell regardless of lane.

---

## Concrete reusable prompt patterns

Use these as starting templates — swap the bracketed/described specifics, keep the structural bones.

### 1. UGC / candid selfie (phone-real)
```
Ultra-realistic selfie-style portrait of a young woman leaning toward the camera in a modern bathroom, close upward angle, soft glam makeup, shot on iPhone, natural skin, unretouched, slight skin imperfection, natural available light, candid intimate phone selfie. No plastic skin, no logo.
```
Universal candid add-on (paste onto any selfie prompt for extra "real phone photo" pull):
```
Real iPhone front camera photo, slight lens distortion, imperfect framing, casual arm-length selfie, harsh natural light or direct phone flash, visible pores, real skin texture, flyaway hairs, tiny blemishes, natural asymmetry, mild compression, slight noise in shadows, unedited Instagram photo, not cinematic, not a studio photoshoot, not airbrushed, not perfect.
```

### 2. Editorial/beauty portrait (cinematic lane)
```
Hyper-realistic close-up editorial flash portrait of a woman seated at a restaurant table, on-camera flash technique, refined jewelry, ultra-realistic skin texture including pores, peach fuzz, tiny undereye creases, 85mm lens, shallow depth of field, subtle film grain. No plastic skin, no CGI.
```

### 3. K-pop idol / "visual" beauty portrait
```
Ultra-photorealistic beauty portrait of a 20-year-old Korean female K-pop idol, the "visual" (most beautiful member) of a girl group — editorial idol photocard quality, shot on a full-frame camera with an 85mm f1.4 lens.
FACE: strikingly beautiful, harmonious balanced features — large bright almond eyes with defined double eyelids and long natural lashes, a slim high nose bridge, small softly defined V-line jaw, smooth forehead, full glossy lips with a gentle gradient tint, delicate arched brows. Fair luminous "glass skin" with a healthy dewy glow.
SKIN: photoreal real skin — fine visible pores, soft natural texture, subtle cheek flush, faint peach fuzz, NO plastic or waxy CGI, NO heavy airbrush; flawless but real.
HAIR: long silky straight-to-softly-wavy black hair with light see-through bangs framing the face, natural shine and flyaways.
MAKEUP/STYLING: soft luminous K-beauty idol makeup, glossy lips, subtle shimmer, tiny elegant earrings; clean chic top.
EXPRESSION: calm, alluring, effortless — a soft magnetic gaze straight into the camera that holds attention.
LIGHT: soft professional beauty light, gentle catchlights in the eyes, delicate rim light on the hair, clean bright airy tone, seamless soft-gradient studio background.
STYLE: high-end idol beauty campaign, crisp micro-detail, true-to-life color, natural depth of field.
Negative: no plastic or waxy skin, no over-airbrushing, no doll-like uncanny face, no over-symmetry, no CGI or 3D render, no warped hands or fingers, no extra fingers, no text, no logo, no watermark.
```
If the request evokes a specific real idol/archetype (e.g. "tall doll-visual" IVE-type look), keep it an archetype — add `inspired by the tall doll-visual archetype of K-pop, NOT any specific real idol` and `do not replicate any specific real person` in the negative. Never copy a real person's face.

### 4. Cute-face charm (Korean dong-an/aegyo geometry — when "cute" specifically isn't landing)
The geometry block ALONE still loses — tested, it gens "average realistic woman," squinty eye-smile, puffy cheeks. The actual fix is a **makeup-style token stack** layered on top of the geometry, not bone structure by itself:
- `Douyin/Korean glass-skin makeup` — one token pulls the whole look at once
- `porcelain and dewy glass skin` as the skin BASE — add `realistic pores` lightly on top, never lead with pores or it drags the look back to "average realistic"
- `heavy soft pink blush on the apples of the cheeks AND tip of the nose` — the youthful-flush signature
- `soft grey contact lenses with reflective catchlights`
- `prominent aegyo-sal, long separated doll-like lashes, wispy lashes, brushed-up brows`
- `glossy pink gradient lips`
- camera: `shot on iPhone front camera, ISO 100, no background blur, no bokeh, shadows slightly flattened, slightly overexposed`
- expression: eyes stay open large and round in the eye-smile — never squeezed shut

Combine with the geometry block:
```
FACE — cute charming Korean "dong-an" (baby-face) geometry: short rounded face with soft full cheeks and baby fat, short lower third, small delicate rounded chin. Large round bright eyes set slightly wide apart with a gentle downturn at the outer corners (puppy eyes), prominent aegyo-sal (soft puffy fat pads under the eyes) that push up into happy crescent eye-smiles when she grins. Small rounded button nose with a soft round tip (NOT wide, NOT flat, NOT red). Small mouth with upward-curling corners, sweet soft smile showing just a hint of metal braces, NOT a wide gummy grin. Faint single dimple, subtle bunny front teeth. Warm genuine smile that reaches the eyes — soft, endearing, charming.
```
Keep the imperfection stack LIGHT here (`fine pores + faint peach fuzz + 1-2 tiny moles`) — a heavy imperfection stack (visible acne, harsh moles, no-airbrush insistence) pulls the result toward "average realistic woman", not cute. Negative: `no long face, no narrow squinty eyes, no wide flat nose, no red nose, no wide gummy forced smile, no harsh under-eye shadows, no tired plain expression`.

### 5. Thai/Korean/Japanese face — nationality-specific block
Never write bare "Asian" — it blends features toward a generic Western-Asian look. Always specify country + eyelid shape + skin undertone + minimal makeup:
```
adult Thai woman in her 20s, warm-brown tan skin undertone, neat low double eyelid, soft lower nose bridge, rounder face, straight glossy black hair with flyaways, dewy natural makeup, glossy nude lip
```
Swap per nationality: **Korean** = V-shaped jaw, high cheekbones, fair neutral skin, glass skin. **Japanese** = natural texture, editorial restraint, may include faint freckles. **Chinese** = avoid period-costume cliché, allow regional variance. Never mix markers from more than one nationality in the same prompt. Negative: `no Westernized features, no blended Asian look, no big round eyes, no anime/kawaii style, no Orientalist stereotype, no over-smoothed pale skin`.

**Thai subject/setting trigger:** the moment a request specifies or implies Thailand (Thai person, Bangkok, a Thai brand/context), read `memory/thai-localization-image-prompts.md` for the full rules (authentic-vs-postcard-fake setting cues, text-glyph verification, cultural specificity). The single highest-value piece — keep it verbatim and paste it onto an existing working prompt to localize it without rewriting from scratch:
```
Adaptation: any person in the scene is Thai; any city or location is in Thailand (e.g. Bangkok). Keep every other detail exactly as specified in the prompt.
```

### 6. TVC / clean commercial white-tone suffix
Append when the user wants a clean, bright, commercial-cinematic look:
```
ultra-cinematic cinematography style, clean white tone TVC, highkey commercial, shallow depth of field, soft blurry background with creamy bokeh, subject in sharp focus, anamorphic lens, realistic film style, film lighting and shadow, movie still quality, professional cinema camera.
```

### 7. Garment/fashion — feature discriminators + energy control
For clothing/lookbook/wardrobe prompts, three levers keep the garment (not the mood) as the actual subject:
- **Garment-is-the-subject line** — without it the model drifts toward the person/emotion instead of the clothes:
```
the garment is the subject; its collar, buttons, fabric and cut read clearly in every shot
```
- **Feature discriminators for near-identical garments** — when a set of outfits differs only by one feature (e.g. collar shape across 3 looks), spell out SHARP physical differences per garment instead of a vague label, plus an explicit negative:
```
Look 2 collar: wide V, broad rounded lapel points angling DOWN.
Look 3 collar: narrow higher V, long sharp points sweeping UP like wings.
Negative: the collars must be clearly distinguishable; do NOT give Look 2 and Look 3 the same collar.
```
Attach a real product photo as a feature reference when one exists — text alone under-specifies it and the model will collapse near-identical garments to the same shape.
- **Energy control with one balance line** instead of choreographing individual poses:
```
never sluggish, never dreamy, and never giddy or hyper
```

---

## Identity-lock technique (recurring character across many images)

The model pattern-matches against a **visual reference**, not a text description — the more you describe a face in words, the more it drifts. Use a named reference sheet instead of re-describing the face every time.

**When a reference image is attached, never re-describe what the reference already locks.** Words and pixels compete: a face already carried by the reference, re-specified in text ("almond eyes, V-line jaw, fair skin"), gives the model two identity sources to average between — and the averaging *is* the drift. Write the prompt *relative* to the reference (`the woman from the reference image`, `the man in image 1`) and spend the prompt only on what the reference does NOT carry: action, setting, light, camera, wardrobe changes. Same rule for garment references — with a real product photo attached, describe fit and how it's worn, not the collar shape the photo already shows. Corollary: if the identity comes out wrong with a reference attached, the fix is usually *deleting* face description, not adding more.

**Originality boundary:** identity-lock is for holding a consistent *original* character across scenes — never use someone else's real photo/artwork as a reference to produce a near-identical copy of it. Always generate from a prompt that describes the CONCEPT (subject, composition, mood), not a copy target.

**Method (GPT Image 2, works similarly on Nano Banana Pro):**
1. Gather 2–3 source images with the right face/vibe.
2. Generate the **Face Sheet**, with the source images attached:
   ```
   Make a reference character sheet for [NAME] from these images. Show front view and side profile, clean background, with the name labelled at the top.
   ```
   The name must be **printed on the sheet itself** (latin letters only, CJK renders garbled) — that's what the model binds identity to, not the filename.
3. If wardrobe must stay locked, generate a **Full-Body Sheet** from the face sheet:
   ```
   Using [NAME]'s face sheet, make a full body character sheet showing front view and side profile. She is wearing [SIGNATURE OUTFIT].
   ```
4. From then on, every new scene attaches ONLY the sheet (open a fresh conversation each time — accumulated chat context causes drift) and uses a short one-line scene prompt: `[NAME] [is] [ACTION] [at/in LOCATION]. [FORMAT]. [scene details].` — e.g. `Kristina is sitting at a coffee shop reading a book. Landscape format, cinematic.` Add `no text in the image` (models like printing the character's name as garbled text).

**One change at a time.** When iterating on an existing reference (sheet or photo), edit only one thing per generation — pose, OR outfit, OR expression, not several at once. Stacking multiple changes in a single edit makes the model "reimagine" more of the image instead of surgically modifying it, and that's where identity drift creeps in.

**Alternative — identity anchor kit (4-shot, stronger for heavy multi-scene series):** instead of a single 2-view sheet, generate 4 separate reference images and attach ALL 4 to every new scene: (1) front neutral — face-on, neutral expression, flat lighting, (2) side profile neutral — pure profile, gives the model jaw/nose/ears, (3) front expressive — full smile with teeth + expression wrinkles, (4) full body — whole figure for body proportions. Without all 4 anchors the model "guesses" missing traits (a sheet alone under-specifies profile bone structure and body proportions) — that guessing is where inconsistency creeps in across a long scene series. Use the single-sheet method above for a short 2-3 scene job; switch to the 4-shot anchor kit once a character needs to hold up across many scenes/emotions. Nano Banana Pro is the best fit for this (holds multiple labeled references natively); fall back to GPT Image 2 if it blocks on filters.

**2-panel char sheet (identity + faceless garment) — for garment/lookbook jobs:** one image, split into two panels on the same seamless grey backdrop. LEFT (~45%) = beauty close-up, face fully visible and sharp — this is the IDENTITY panel, and the garment's collar/neckline is visible below the chin for a free fabric/collar reference. RIGHT (~55%) = full-body FRONT + BACK lookbook shots of the same outfit, side by side, with the face MASKED to a plain flat grey oval — hair still renders normally around it. This separates identity from garment in one sheet so the model doesn't confuse which face is real; complements, does not replace, the 4-view/turnaround sheet. Trap: you must spell out **"plain flat grey oval with no features"** explicitly, or the model half-blurs the face into a ghost instead of masking it cleanly. Full paste-ready prompt: `char-sheet-2panel-identity-garment.md`.

**Real-Reference method (maximum photorealism, separate from character identity-lock):** when the priority is raw photorealism rather than a consistent original character, start from a REAL photo (owned/licensed) as the base and ask for a minimal edit (e.g. "put this character on this armchair") instead of generating the scene from scratch — grain, real light, and real imperfections come "free" from the source photo. Rules: use a clean non-AI-generated reference photo, change ONE thing at a time (same discipline as above), and never use a reference photo you don't hold the rights to.

**Identity-lock block** — drop this in front of a scene prompt when working from an uploaded face photo directly (no sheet yet):
```
Using the uploaded face image, preserve the person's facial identity with absolute accuracy (100% identity preservation), maintaining the exact face shape, bone structure, forehead, eyebrows, eyes, nose, lips, ears, jawline, hairline, facial hair, and hairstyle.
```

**Tool tiers:** GPT Image 2 named-sheet = fastest/most reliable for a repeat face (drift ~6%). Nano Banana Pro = good balance + easier conversational edits, holds up to ~14 reference images with labeled roles (`the face in image 1, outfit from image 3, location in image 5`). LoRA/FaceID-IPAdapter training = heaviest control, only worth it for a long-running series.

If the user needs a full multi-asset identity kit (portrait → sheet → expression sheet → scene plates, dependency-ordered for a production job), stop and hand off: that's `asset-prompt-builder`, not this skill.

---

## Platform content-limit guardrails

Applies to clothed-fashion/UGC requests. Nudity/explicit content is out of scope everywhere — not covered here.

| Level | Status |
|---|---|
| Fitted clothing, deep V/low neckline, cleavage, crop top | Passes normally (non-sexual fashion framing) |
| Bikini / swimwear | Passes in a non-sexual setting (beach/pool); gray if context suggests otherwise |
| Boudoir-adjacent, non-intimate framing | Gray zone |
| Lingerie / underwear-only | Gray → often blocked, even for plain ecommerce shots |
| Nudity, sexual-suggestive pose, implied sexual content | Hard blocked on every platform |

**Per-platform strictness:** Nano Banana/Gemini = strictest (blocks even normal lingerie/underwear ecommerce shots). GPT Image 2 = medium (sometimes blocks lingerie/swimwear even for commercial use). Seedance 2.0 (video, N/A for this skill but noted for hand-off) = blocks sexual-context lingerie + suggestive poses, allows non-sexual swimwear and fitted fashion.

**How to stay inside the line:**
- Frame as `editorial fashion photography` / `professional fashion shoot`
- Use photographer language (camera/lighting/lens specs), not mood language
- Avoid trigger words: `sensual, seductive, provocative, intimate, sexy`
- Keep setting non-sexual, expression neutral
- Verified-passing bikini pattern: `casual holiday lifestyle / travel Instagram` + `simple triangle bikini, casual beachwear` + `relaxed calm` expression + negative `no sexual or suggestive posing`, with none of the trigger words above. Works in both 4:5 and 9:16.

There is no published rulebook for the gray zone — the same prompt can pass or fail depending on model version/timing. If a request is clearly headed for lingerie/boudoir/explicit territory, say so plainly rather than trying to word-hack around the filter.

---

## Output format

**Write the prompt first, never interrogate first.** However thin the request, draft a complete prompt from sensible defaults and hand it over — then expose your guesses so the user can correct them. Questions come *after* a usable prompt exists, never instead of one, and never more than 2–3 of them.

For every request, deliver:

1. **Model pick** — which model this prompt targets and why (one line, skip if the user already specified).
2. **The prompt** — paste-ready, English, labeled sub-blocks if dense.
3. **Negative prompt** — as its own line/block if the target model uses one.
4. **`Locked:` / `Assumed:`** — two short bullet lists. `Locked` = what the user actually specified (subject, action, setting, outfit...). `Assumed` = every dial you turned for them: camera/shot type, lighting, lane (candid vs editorial), nationality specifics, mood, aspect ratio, identity-lock decision. This is the deliverable's second half — it tells the user exactly which knobs are theirs to change instead of making them reverse-engineer the prompt. Keep each bullet to a few words.
5. **Up to 3 optional questions or variations**, drawn from the `Assumed` list — offered, not blocking.

Don't pad the answer with process narration. If the request is a recurring character, mention the identity-lock method briefly and offer to write the Face Sheet prompt too.

---

## Final QA before answering

1. Any of the four killer words present (`hyperrealistic, ultra-detailed, 8K, masterpiece`)? Remove them.
2. Is skin left perfectly smooth with no texture descriptor at all? Add one.
3. Candid and editorial levers mixed in the same prompt? Pick one lane.
4. Nationality specified as bare "Asian"? Fix to a specific country + eyelid/skin/hair specifics.
5. Recurring character but no identity-lock plan? Add one (sheet or identity-lock block).
6. Hands/body visible? Add the hands block and, if a body is in frame, the anatomy negative.
7. Revealing clothing requested? Check against the content-limit table before finalizing.
8. Reference image attached, but the prompt still describes the face/garment in words? Strip the re-description.
9. Does the prompt read as ONE image, not an implied multi-asset kit? If it's actually a full character-kit request, hand off to `asset-prompt-builder`.

---

## Iteration — when a result comes back wrong

The user shows or describes a bad gen ("หน้าเพี้ยน", "แสงไม่เหมือนที่สั่ง", "ดูเป็น AI"). Two rules:

1. **Name the block that failed, in one line** — FACE / SKIN / HAIR / STYLING / LIGHT / SETTING / CAMERA / STYLE / negative. Diagnose the prompt, not the idea; a bad gen is almost always an under-specified block or two competing levers, not a bad concept.
2. **Return the FULL rewritten prompt** — the complete revised version, paste-ready, never a fragment to splice in. A snippet forces the user to re-assemble by hand and that's where prompts quietly break. Restate the `Locked:` / `Assumed:` lists too if anything moved between them.

Then change ONE block per iteration (same discipline as the identity-lock section) so the next result tells you whether the diagnosis was right.

**Model-typical failures — apply the standard counter-instruction instead of rewriting the concept:**

| Symptom | Cause | Fix |
|---|---|---|
| Mangled/extra fingers, broken grip | hands under-specified | add the hands block + `no warped hands or fingers, no extra fingers` |
| Garbled text, warped signage, character's name printed in-frame | model tries to render text | add `no text in the image, no logo, no watermark` |
| Melted/duplicate faces in the background | crowd left unspecified | make background people explicit (`blurred out-of-focus figures`) or negative them out |
| Plastic/waxy skin | no texture descriptor, or over-airbrush language | add the skin block; strip `flawless, perfect, smooth` |
| Looks staged / "too AI" | zero imperfections, dead-centre symmetry | 2–3 imperfections + `off-centre composition, natural asymmetry` |
| Face drifted from previous image | text competing with the reference, or chat context accumulated | strip face description, attach the sheet only, start a fresh conversation |
| Pose/angle ignored | camera angle omitted on a pose transfer | state the shot type + angle explicitly |
| Look reads "average", not the intended charm/glam | imperfection stack too heavy for the target look | lighten to `fine pores + faint peach fuzz`, lead with the styling token stack |

---

## Deeper knowledge (read from the brain vault at runtime)

Vault paths — mac: `/Users/working/ai-factory-brain/memory/` · Windows: `D:\ai-factory-brain\memory\`

- `ai-influencer-image-prompt.md` — full realism framework, model benchmark, all realism-tier presets (clean iPhone / Y2K digicam / elevated European / "unaware" candid tier).
- `ai-character-identity-lock.md` — full identity-lock method, tool tiers, two-tool workflow.
- `char-sheet-2panel-identity-garment.md` — full 2-panel identity+garment char-sheet prompt (paste-ready), for garment/lookbook jobs.
- `cute-face-charm-recipe.md` — full cute-face breakdown + full paste-ready cherryhikiko-style prompt.
- `kpop-idol-visual-prompt.md` — full K-pop visual prompt + doll-visual archetype variant.
- `image-prompt-suffixes-techniques.md` — TVC suffix, pose-transfer, character-swap, upscale prompt techniques.
- `ai-platform-content-limits.md` — full content-limit research, sources, verified test cases.
- `thai-localization-image-prompts.md` — full Thai-localization rules (authentic-vs-postcard setting cues, text-glyph verification, cultural specificity) — read whenever the request has a Thai subject/setting.
