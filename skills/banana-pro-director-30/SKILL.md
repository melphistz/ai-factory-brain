---
name: banana-pro-director-3.0
description: "Higgsfield image prompt director for Banana Pro, Soul Cinema, and GPT-2 — primarily scene plates and stills; character modes kept as reference grammar (character work routes to character-builder). Modes: (0) face lock for new characters — Banana Pro (default), GPT-2 (higher fidelity, more credits), or Soul Cinema two-pass, on mid-gray seamless with a black camisole/tank baseline; (1) single-image character outfit — Banana Pro or Soul Cinema two-step; (2) character sheets — 3-panel is the default (headless front, full rear, tight chest-up face lock), 6-panel on explicit request only; (3) cinematic scene plates with or without characters; (4) GPT-2 detail face/chest-up; (5) outfit replacement — swap a face onto an outfit using two refs. Reads references for hair, makeup, wardrobe, jewelry, identity. Outputs photorealistic prompts with one clean cinema stack — pores, subsurface scattering, strand hair, fabric weave, atmospheric perspective, anamorphic character, theatrical grain. Use for scene and environment plates, detail shots, outfit replacement onto a worn-in-photo reference, or any photorealistic Higgsfield still. Do NOT use for building or locking a NEW character, character additions, or character sheets — that is character-builder. Do NOT use for flat-lay outfit swaps onto a character — use the wichcraft recipe in memory. Do NOT use for one-off GPT Image 2 stills outside the Higgsfield pipeline — that is image-prompt-writer."
---

# Banana Pro Director 3.0 — Image Asset Builder

The locked image prompt grammar for great Higgsfield image assets. Six modes, in strict order:

0. **Face lock (new characters only)** — for any character being developed from scratch. Tool fork: **Banana Pro single-pass** (default, balanced), **GPT-2 single-pass** (highest fidelity, higher credits, chest-up only), or **Soul Cinema two-pass** (cheap iteration — Soul Cinema face plate then Banana Pro 3:4 lock). All paths use mid-gray seamless (the locked default backdrop — white only on explicit request), soft soft lighting from camera-left or camera-right, and a locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men). No outfit styling, no environment, no in-depth prompting at this stage. Identity only.
1. **Single-image character outfit** — mid-gray seamless studio (locked default — white only on explicit request), full styling readable, locked as the base reference for that character/outfit. Two paths: **Banana Pro** (full custom styling written from prompt — best for simpler outfits) or **Soul Cinema** (outfit built on a bland slim model first, then composited onto the locked character — best for custom fits where wardrobe should be designed separately from casting). User picks based on outfit complexity.
2. **Character sheet** — built ONLY after a single-image base exists. **The 3-panel sheet (Mode 2A) is the default and primary format**: full body front with the head cleanly removed, full body rear with the head attached, and a tight chest-up face lock. The **6-panel sheet (Mode 2B) is legacy** — available on explicit request only, and never proposed proactively, because splitting the frame six ways starves the face panels of resolution.
3. **Scene plates** — character(s) in a fully realized cinematic environment, OR pure environment plates with no characters. Always available, but never proposed proactively — only built when the user asks.

Plus two optional capabilities:

4. **GPT-2 detail mode** — Higgsfield's higher-fidelity image model, used only for detail face shots and chest-up portraits when the user explicitly asks for that level of close-up. Never suggested otherwise.
5. **Outfit replacement** — two-reference swap that puts the character from one image into the outfit and pose from another image. Single locked prompt, character/IP-agnostic. Used only when the user explicitly asks to swap a face onto an outfit reference, or any equivalent phrasing.

Photoreal is the universal default. Every prompt this skill produces describes a real human (or real environment) in a real frame, never plastic, never rendered, never CGI.

---

## HOUSE OVERRIDES (ai-factory-brain) — these beat any rule below

- **@img role tags are ALLOWED and preferred** on our GPT Image 2 / Nano Banana stack (@img1 = identity, @img2 = wardrobe). The "no @image tags" rule below applies to the Higgsfield UI only.
- **Aspect ratio in the prompt body is ALLOWED** (e.g. "vertical 9:16 framing") — our drama/ad output is 9:16.
- **Adult age + nationality register is REQUIRED** for our casting accuracy: e.g. "Thai woman in her late twenties, natural Thai facial features, medium skin tone" (see `memory/thai-localization-image-prompts.md`). Only minor-coded words (teen, young girl/boy, schoolgirl etc.) stay banned.
- **Tool name mapping:** "Banana Pro" → Nano Banana Pro. Higgsfield "GPT-2" is NOT OpenAI GPT Image 2 — treat GPT-2 guidance as Higgsfield-product-specific. Skip any credit-upsell dialogue ("want to run this on GPT-2?") — our factory is prompt-first/manual-gen.
- **The no-teeth-smile default applies to reference plates (Modes 0/1/2) only**, not to UGC/ad output stills.

---

## THE WORKFLOW — STRICT ORDER

The skill enforces this order. Don't skip steps. Don't combine steps.

### Step 0 — Is the character already built?

Before anything else, ask the user: **does the character already exist, or are we developing them?**

**If the character exists:** ask the user to drop the reference image(s). Then study and lock — face, bone structure, skin tone, hair color and texture, identity markers, body proportions. Mirror back the locked spec in plain language so the user can confirm or correct before any prompt is built. Wait for confirmation, then proceed to Mode 1 (outfit work) or whichever mode the user asked for.

**If the character is new:** development happens in two stages — first a text spec, then a face-lock build via Mode 0. Do NOT jump straight to outfit prompts. The face has to be locked as a visual reference before any outfit work can happen.

Stage 1 — text spec: let the user describe the character in their own words. Listen. Then mirror back a locked spec in plain language covering:

- Approximate apparent age register (described by build, not number)
- Face: bone structure, eye shape and color, brow shape, nose, lip shape, skin tone and finish
- Hair: color (every nuance), length, texture, style
- Body: build, proportions, posture, distinguishing markers
- Default makeup register (if any)
- Default expression and energy
- Any key identity markers — piercings, scars, beauty marks, tattoos, signature jewelry

Wait for confirmation or correction. Iterate on the text spec freely until the user says it's locked. Then move to Stage 2.

Stage 2 — Mode 0 face lock build (see Mode 0 section below). Tool fork between Banana Pro single-pass (default), GPT-2 single-pass (higher fidelity, higher credits), or Soul Cinema two-pass (iteration path). Produces the canonical character reference image used as the identity anchor for every future outfit/scene/sheet prompt. Always run this before any outfit work for a new character. No exceptions.

### Mode 0 — Face lock (new characters only)

See the Mode 0 section below. Tool fork: Banana Pro single-pass (default), GPT-2 single-pass (highest fidelity, higher credits, chest-up only), or Soul Cinema two-pass (cheap iteration — Soul Cinema face plate then Banana Pro 3:4 lock). All paths use mid-gray seamless (the locked default backdrop — white only on explicit request), soft soft lighting, and a locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men). Produces the canonical reference image. Run once per new character.

### Mode 1 — Single-image character outfit (the base outfit reference)

Once the character is locked (either confirmed from existing reference upload, or built via Mode 0), the FIRST image generated for any new outfit is a single-image character outfit on a mid-gray seamless studio backdrop (the locked default — white only on explicit request). No character sheet — 3-panel or 6-panel — ever gets built before a base outfit reference exists.

Ask the user to describe the outfit they want — every garment, every accessory, every styling choice. If they upload a wardrobe reference image, study it visual-only. Mirror back the wardrobe spec for confirmation.

**Then — before writing the prompt — ask which tool to build the base in:**

> Want to build this in Banana Pro (Nano Banana) or Soul Cinema?
> — **Banana Pro:** writes styling from scratch via prompt, single locked output. Best when the outfit is relatively simple and full prompt control gets us there cleanly in one shot.
> — **Soul Cinema (two-step flow):** Step 1 builds the outfit on a bland slim fit model on mid-gray seamless. Step 2 takes that outfit reference + the locked character reference and composites them. Best for custom/complex fits where wardrobe should be designed separately from casting.

Wait for the user to pick. Different tools use different prompt structures — see Mode 1A (Banana Pro) and Mode 1B (Soul Cinema, two-step) below.

Then run the standard pre-prompt check, wait for the green light, then deliver the prompt in a single fenced code block.

### Mode 2 — Character sheet

Only after a single-image base reference has been generated (and the user is happy with it) can a character sheet be built.

**Default to the 3-panel (Mode 2A).** When the user asks for "a character sheet" without naming a format, build the 3-panel: full body front with the head cleanly removed (ghost-mannequin hollow for structured necklines, clean neck cut for dresses and open necklines), full body rear with the head attached, and a tight chest-up face lock. Do not ask which format, do not offer the 6-panel.

**6-panel (Mode 2B) is legacy and explicit-request only.** If the user names it, flag once that six cells starve the face panels of resolution, then proceed on their go-ahead.

Same pre-prompt confirmation rule: bulleted summary, get the nod, then deliver the prompt in a code block.

### Mode 3 — Scene plates (with or without characters)

Always available. Never proposed proactively. Only built when the user asks for a scene, an environment, a plate, a moment, or describes a setting.

Same pre-prompt confirmation rule applies.

### Mode 4 — GPT-2 detail mode (optional, gated)

Only used for chest-up portraits or detail face shots, and only when the user explicitly asks for that level of close-up. Even when the user asks, ask first: "want to run this on Higgsfield GPT-2 for the higher-fidelity face read? heads-up, GPT-2 uses more Higgsfield credits than Banana Pro." Mention the credit cost once per conversation, then drop it for the rest of the session. Wait for confirmation, then deliver the prompt.

GPT-2 prompt structure differs slightly — see the GPT-2 section below.

---

## THE PRE-PROMPT CONFIRMATION RULE (UNIVERSAL)

Every prompt — single image, character sheet, scene plate, GPT-2 — gets a short "here's what I'm about to prompt, sound good?" check before the full prompt is written. This is not optional. Long prompts are expensive in attention and copy-paste effort, and the user shouldn't have to wait on a wall of text only to discover it missed the mark.

**Exception — minor iteration on a just-delivered prompt.** When the user requests a small adjustment to a prompt that was already approved and delivered in this same conversation thread (composition tweak, framing shift, pose change, lighting nudge, swap one wardrobe element, repositioning subjects, etc.), skip the pre-prompt check and deliver the revised full prompt directly in a fenced code block. The character is locked, the wardrobe is locked, the world is locked — only the variable being tweaked is changing, and the user has already seen the spec. Re-confirming on tiny deltas creates friction.

What still triggers a full pre-prompt check even mid-thread:
- New character entering the frame
- New wardrobe (not a tweak — a full outfit swap)
- New mode (going from single-image to a character sheet, or from base to scene plate)
- New environment / scene type
- The user explicitly asking for a check ("walk me through it first")

Default to delivering when in doubt on a clear minor delta. Default to checking when the change touches anything load-bearing.

**Format: clean bullet points only.** No quote blocks, no em-dash prose lines, no narrative wrapper. One short opening line ("Pre-prompt check:" or similar), then bullets. **References listed first, always** — this confirms back to the user that every reference image they uploaded is being read and accounted for in the composition. If a reference is uploaded but missing from the list, the prompt is being composed wrong and the user catches it before the full prompt ships.

The pre-prompt check is short, plain-language, and lists in this order:
- **References attached** (one bullet, always first — list every uploaded reference image by short visual descriptor)
- **Character** (one bullet — hair, skin, identity markers, expression)
- **Outfit / styling** (one bullet — wardrobe head-to-toe, jewelry, body markers)
- **Backdrop or environment** (one bullet)
- **Framing** (one bullet, only if non-default)

Close with a single short question line ("Sound good?" / "Lock it?" / "Run it?").

Format example:

Pre-prompt check:
- **References attached:** locked character reference sheet, outfit wardrobe reference plate
- **Character:** platinum-blonde ponytail, warm fair skin, sharp almond eyes, neutral expression
- **Outfit:** ivory zip-V corset, ivory parachute pants, cream platforms, clear acrylic accessories
- **Backdrop:** mid-gray seamless studio (locked default)
- **Framing:** full body

Sound good?

If no references are attached, the first bullet reads: **References attached:** none — pure text composition.

Wait for the green light. Then drop the full prompt in a single fenced code block.

---

## CORE PHILOSOPHY

No plastic. No CGI sheen. No 3D-render look. No commercial gloss. No AI-generic skin or hair.

Every image this skill produces should read as a photograph — taken on a real camera, by a real person, of a real subject. The character should look lived-in: real pore texture, peach fuzz, hair with flyaways and individual strands catching light, fabric with weight and weave and wear, jewelry with surface detail, eyes with reflection and depth.

**The flattering-realism ceiling (LOCKED — applies to every face, every mode).** Full skin realism is always on — visible pore texture, peach fuzz at the jaw and hairline, subsurface scattering, hair flyaways, the matte finish that carries the anti-plastic look. But realism never means *unflattering*. Faces are never rendered with harsh, severe, or distracting imperfections: no acne, no blemishes, no prominent spots, no scarring, no enlarged or cratered pores, no rough or bumpy texture, no aggressive skin detail that reads as ugly or clinical. The texture is fine, soft, even, and natural — the lived-in realism of good cinema skin under a flattering key, not the brutal macro-detail of a dermatology photo. Matte (never plastic) is the anti-plastic lever; *fine and even* (never harsh) is the flattering lever. Both are always on together. When the two ever seem to pull against each other, resolve toward fine-even-flattering — a face should always look good.

Photorealism is not a tier you opt into — it's the universal default, baked into every prompt. The skill never produces a "stylized," "illustration," "anime," "painterly," "comic," or "rendered" prompt unless the user specifically requests a stylization override (rare, and then noted explicitly).

---

## UNIVERSAL RENDER RULES — FIGHTING THE AI AESTHETIC

These rules are baked into every Banana Pro, Soul Cinema, and GPT-2 prompt this skill produces. They're how the skill fights the AI render aesthetic — digital sharpness, dewy faces, plastic skin, glossy beauty register, AI-render flatness — and forces a real photographic register.

**1. Real human skin.**
- Real natural pore texture visible at close range — soft, fine, and even, never as blemishes or acne or marks, never enlarged/cratered/rough, never harsh clinical macro-detail
- Real peach fuzz catching light along the jawline, hairline, temples, and upper lip — fine, photographic, never plastic
- Real subsurface scattering present, warm and real — semi-translucent biology, not opaque plastic
- Skin tone held at the character's natural register — preserved through the grade, never washed out, never cool-shifted ghostly
- No retouching, no skin smoothing, no digital cleanup, no porcelain plastic look, no waxy AI render, no beauty bloom
- **Flattering ceiling:** the realism is always flattering — fine, soft, even texture under the key, never severe or unflattering imperfection. A face should look good and real at the same time; matte carries the anti-plastic, fine-and-even carries the flattering. Resolve any tension toward flattering.
- Doll-coded characters (when explicitly requested): smooth matte register without visible pores or peach fuzz but still real and natural, never plastic, never AI-render, never waxen

**2. Real hair physics — strand-by-strand, context-aware.**
- All hair rendered strand by strand with realistic flyaways, baby hairs at the hairline, separation between strands, light transmission through hair ends — never block-of-hair animation
- Hair responds to the actual environment of the scene: still interior = settled hair, moving vehicle = wild hair in active motion, wind = drift, action = kinetic lift and fall, wet = damp matte clumping never glossy oil-slick
- Hair register defaults matte — fine diffuse fiber with soft natural shape, never glossy shine, never reflective sheen unless the user specifies a high-gloss styling

**3. Real lens character.**
- Wide-latitude digital cinema capture as the default register — broad dynamic range, gentle filmic highlight roll-off, never a flat video look
- For character canonicals and seamless studio stills (gray or white): a clean fast normal prime around a 50mm full-frame field of view at a wide aperture — natural round bokeh, even sharpness, gentle background separation, no anamorphic stretch on portraits unless requested
- For scene plates with characters or environments: vintage 2x anamorphic optical character — oval bokeh, a gentle horizontal squeeze on out-of-focus highlights, soft frame-edge falloff, mild organic optical imperfection toward the edges, plus a light diffusion bloom that lifts highlights into a soft halation and takes the hard digital edge off
- Real anamorphic-style horizontal streak flares on point light sources when called for, never on portraits

**4. Real light physics.**
- **Atmospheric depth is default-on across every mode, scaled to fit the shot.** Visible haze and air density between planes — distant elements rendered softer, desaturated, lower contrast than foreground, never a flat backdrop. This is the primary lever against the flat, over-contrasted, plastic look: real air between camera, subject, and background is what makes a frame read as photographed depth rather than a pasted-on plane. Scale the density to the scene (thin for a clean interior, light for most exteriors, heavy for moody/night/destroyed environments) and apply it wherever the shot has planes to separate. The one place it reduces toward zero is a deliberately flat white-seamless still — and even there the mid-gray plate option carries the same low-contrast intent.
- Shadow falloff with physically accurate wrap on real anatomy — soft transitions, never hard edges, real human anatomy under real cinema light
- Subsurface scattering at ear edges, nostrils, eye sockets with warm undertone bleed
- Highlights rolled off gently in a filmic curve, never clipping to pure white — light blooms softly into haze rather than punching as hard white discs
- Lifted blacks that stay open and never crush to pure black, highlights that roll off and never clip — wide dynamic range, full detail held in both shadows and highlights

**5. Real grain.**
- Color-negative motion-picture film look — daylight-balanced for day registers, tungsten-balanced and pushed for night work, the organic color rendition of real film stock baked in
- Fine theatrical 35mm film grain across the entire frame including skin, fabric, atmosphere, backdrop — never the silent clinical fine-grain register of editorial photography
- The grain is what ties everything to real cinema photographic capture

**These five rules are the lock. Every prompt this skill produces invokes them through the merged cinema stack documented below.**

## NIGHT CINEMA REGISTER (FOR NIGHT SCENES)

When the user asks for a night scene, the target is theatrical action night cinema — **Justin Lin / James Wan / Greig Fraser night work** (Tokyo Drift, Fast 5, Furious 7, The Batman, John Wick). Theatrical night cinema is **mostly dark, with hard punchy practicals cutting through** — NOT saturated-teal-everywhere, NOT bright-night. Two registers: **exterior canyon/open night** (light exclusively from practicals, everything else crushed near-black) and **interior/urban/lit night** (practical-driven teal-amber split where motivated).

Full grammar: `references/mode-3-scene-plates.md` — both night registers in full, plus the universal night cinema rules (contrast, practicals, atmospheric haze, rim/edge light, skin-in-night).

---

## 18% GRAY SEAMLESS + FLAT GRADE (LOCKED DEFAULT FOR ALL CHARACTER WORK)

**18% neutral gray seamless with a completely flat, shadowless grade is the locked default** for all character work — face locks, character references, outfit plates, 3-panel and 6-panel sheets, and prop references. **Pure white seamless is now the explicit-request exception**, used only when the user specifically asks for a clean white card (e.g. a finished standalone still meant to be posted or handed off as a polished deliverable). When in doubt, default to gray.

**Why gray as the standing default.** Pure white (and pure black) seamless creates maximum subject-to-background contrast. Video models amplify small mistakes most at high-contrast edges — that's where halo, edge "breathing," and contour instability get baked in during motion. A neutral mid-gray ground lowers the subject-to-background contrast, which means cleaner edge extraction and far less inherited contrast and plastic when the still is read as a reference frame. The same principle that makes a hazy scene plate read as real depth — lower contrast between planes — applies here: gray is the flat-plate version of the fix. Because virtually all character plates eventually seed downstream video work, gray is the correct standing default; white is reserved for the occasional finished standalone still.

**The background stays neutral; the character does not.** The gray ground is an **even neutral mid-gray** — do NOT warm-shift it toward warm-gray. The neutral ground is the locked look. But the gray must never be allowed to cool or neutralize the subject: skin renders at its **true natural skin tone**, and body and wardrobe render at their **true natural color values**, exactly as they'd read under neutral daylight — never cooled, never washed-out, never color-shifted by the background. The relight-from-scratch language and the explicit "warmth preserved and natural, never pale or washed-out or cool-shifted" clause in the lighting close below are what hold this. Keep the background neutral and the subject true.

**The white exception:** only when the user explicitly asks for white. In that case, swap the gray backdrop line for "Pure white seamless studio background, no gradient, no seam line, perfectly even" — but **keep the flat shadowless grade**. Flatness survives the backdrop swap; it is not a property of the gray, it is the locked look for all character work.

**Lighting close for a gray plate (LOCKED FLAT GRADE — use this, NOT the full cinema stack):**

Close with the LOCKED FLAT GRADE — full canonical paragraph in `references/flat-grade-close.md`; paste it verbatim into the delivered prompt.

**Why flat, and why the lean close instead of the full cinema stack.** These plates are references, not finished frames. Any shadow baked into a reference — a cheek triangle, a nose shadow, a contact shadow under the feet, a falloff on the backdrop — gets inherited and amplified by every downstream generation that reads the plate, and it fights whatever lighting the actual scene wants. So the character plate carries **zero lighting information**: no key direction, no shadow side, no cast shadow, no backdrop falloff. The gray stays one flat value, the subject is described entirely by bone structure, hair, and fabric folds, and the scene plate or video prompt does all the lighting later. The full texture-and-grade stack would push contrast back up, which is exactly what this grade is killing; the lean flat close does the matte/specular/true-color work without re-introducing any of it.

**The three things that must appear in every flat close, always:**
1. **Flat backdrop** — one uniform 18% gray value corner to corner, no seam, no gradient, no hotspot, no vignette, no falloff.
2. **Shadowless illumination** — huge frontal source at camera position, matched equal fill left/right/above/below, no key-and-fill ratio, no shadow side, no rim, no hair light, no kicker, no specular hotspot.
3. **Zero cast shadow** — nothing thrown onto the background, no contact shadow, no drop shadow, no ambient occlusion under the feet or the hem.

If any one of the three is missing, the plate will come back with modelling in it.

**3-panel sheets:** the flat default applies the same way, and the flatness must be stated as applying **uniformly across all three panels** — same flat gray value, same shadowless light, no cast shadow in any panel. Close with the flat grade above instead of the full cinema stack. Only swap to white if the user explicitly asks, and keep the flatness when you do.

**6-panel sheets:** same — flat gray value and shadowless light stated as applying uniformly across all six panels, no cast shadow in any panel. Close with the flat grade above instead of the full cinema stack. Keep everything else (panel layout, identity lock) identical. Only swap to white if the user explicitly asks, and keep the flatness when you do.

---

When the user attaches reference images (character canonical sheets, wardrobe references, environment plates, car interior plates), those references carry the visual identity load. The prompt does NOT need to re-describe what the references already show. Heavy visual description on top of strong references creates double-weight prompts that dilute the photographic direction Banana Pro / Soul Cinema / GPT-2 actually need from the text.

**The new structure for every prompt this skill produces:**

**1. Identify subjects by short, distinguishing visual descriptors only.**
- "the woman with platinum-blonde hair in the white unitard" — not a paragraph describing her face structure, skin texture, hair waves, lash length, lip shape, brow arch, body type, posture, makeup
- "the cream pearl coupe interior" — not a paragraph describing every dash gauge, knob, charm, harness, switch
- One distinguishing visual handle per subject is enough — the reference image carries the rest

**2. Put the load on what the prompt UNIQUELY needs to communicate:**
- Composition and framing (where the subject is in the frame, what's in foreground/background, what the camera angle is)
- Pose, expression, what bodies and hands are doing
- Light direction and quality (where the light is coming from, how it falls on the subject)
- Wardrobe or styling SPECIFIC TO THIS PLATE that's not in the existing references
- The cinema stack at the end

**3. Drop the redundant identity descriptions entirely UNLESS the reference is ambiguous.**
- If the user attached the character canonical, the prompt does not need to re-describe face structure, body proportions, skin tone, eye shape. Mention them only when something specific to this plate requires it
- Trust the references to carry identity. The prompt's job is to tell Banana Pro what to DO with the identity in this specific shot

**4. When in doubt, lean shorter.**
- A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time
- Banana Pro reads the front of the prompt most heavily; loading the front with composition + pose + light gets better results than burying those decisions under visual description
- The references show the model what things LOOK like. The prompt tells the model how to FRAME them.

**Lean prompt rule of thumb:** if a sentence in the prompt re-describes something that's already visible in an attached reference, cut it unless it's load-bearing for the composition or action.

---

## THE CINEMA STACK (LOCKED — APPENDS TO MOST PROMPTS)

Every prompt this skill outputs ends with a version of this single merged cinema stack. It's the texture + light physics + lens character + grain foundation that fights every AI render tell at once. One block, one job — close the prompt with a real photographic register.

```
Real human skin captured on a real cinema camera — refined and real, peach fuzz catching light along the jawline and hairline, real natural pore texture soft fine and even, subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed reading as semi-translucent biology never opaque plastic. No retouching, no skin smoothing, no porcelain plastic look, no waxy AI render, no blemishes, no acne, no marks, no enlarged or rough pores, no harsh clinical texture — fine flattering even skin that always looks good, no dewy wet finish, no glass-skin, no highlighter glow. Hair rendered strand by strand with realistic flyaways and baby hairs at the hairline, hair physics responding to the actual environment of the scene — wind makes it fly, stillness lets it settle. Fabric with real weave detail, real weight, real drape. Captured with a wide-latitude cinema look, lens character matched to the shot — a clean fast normal prime around a 50mm full-frame field of view at a wide aperture for portraits and character canonicals giving natural round bokeh and even sharpness, OR a vintage 2x anamorphic character for scene plates giving oval bokeh, a gentle horizontal squeeze on out-of-focus highlights, soft frame-edge falloff, organic optical imperfection toward the edges, a light diffusion bloom lifting highlights into a soft halation, and subtle horizontal streak flares on point light sources. Shallow depth of field with strong foreground-to-background separation. True atmospheric perspective with visible haze and air density between planes — distant elements rendered softer, desaturated, and lower contrast than foreground, real volumetric atmosphere never a flat backdrop. Key light wrapping around subjects with physically accurate shadow falloff into the neck, jawline, ear shadow, nostril shadow, lip shadow, collarbone shadow — soft transitions never hard edges, real human anatomy under real cinema light. Highlights rolled off gently in a filmic curve, never clipping to pure white, light blooms softly into haze rather than punching as hard white discs. Lifted blacks that stay open and never crush to pure black, highlights that roll off and never clip — wide dynamic range with full detail held in both shadows and highlights. Color-negative motion-picture film look baked in — daylight-balanced rendition for day registers, tungsten-balanced and pushed for night work, fine theatrical 35mm film grain across the entire frame including skin, fabric, atmosphere, and backdrop. No HDR overprocessing, no digital oversharpening, no plastic skin rendering, no uniformly-lit flat-plane staging — photographed not generated, captured on a real camera by a real cinematographer on a real set.
```

**Modal application:**
- **Mode 0 (face lock), Mode 1 (single-image character outfit), Mode 2 (character sheet), Mode 4 (GPT-2 detail), Mode 5 (outfit replacement) — i.e. all studio character work:** these close with the **LOCKED FLAT GRADE**, not the full cinema stack. The full stack's key-wrap, anatomical shadow-falloff, and atmospheric-perspective language actively fights the flat plate — never append it to a character plate or sheet. It is documented here for Mode 3 and for the explicit white-card standalone-still exception only.
- **Mode 3A (character-in-scene plate) and Mode 3B (pure environment plate):** Mode 3 uses the cinema-prose register, which folds the cinema stack language INTO the closing camera-spec paragraph rather than appending it as a separate block. See Mode 3 documentation for the prose register and its closing realism clause.
- **Mode 1B Step 1 (bland model outfit reference, Soul Cinema two-step):** use the lighter outfit-reference close documented in the Mode 1B section — NOT the full cinema stack. The outfit reference image just needs to read clean and matte so the outfit is the only subject.

**The single most powerful phrases in this stack:**
- **"atmospheric perspective with visible haze and air density between planes"** — forces multi-plane depth instead of single-plane staging. Biggest fix for the "video game" look.
- **"shadow falloff into the neck, jawline, ear shadow, nostril shadow"** — fights the AI uniform-lit face. Forces real anatomical shadow geometry.
- **"subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed"** — fights plastic skin at the biological level. Forces the model to render skin as semi-translucent biology instead of opaque material.
- **"highlights rolled off gently in a filmic curve, never clipping to pure white"** — fights the blown-bright AI highlight that makes everything look digital. Forces the cinema highlight roll-off.
- **"photographed not generated, captured on a real camera by a real cinematographer on a real set"** — surprisingly strong negative signal against AI uniformity at the language level.

**For pure environment plates with no humans:** drop the human-skin and hair lines, drop the subsurface scattering line, drop the shadow-falloff-on-anatomy line. Keep the lens character, atmospheric perspective, light physics, log curve, grain, and closing realism clause.

---

## READING REFERENCE IMAGES

When the user uploads reference images, extract everything visible in the frame by **visual description only** — never use names, never invent details that aren't in the image.

**For each character in the reference, capture:**

- **Hair:** color (every nuance — platinum, jet black with cool undertone, rose-pink, burgundy, ash brown, dirty blonde, etc.), length, style, texture (straight, wavy, curly, coily), parting, any styling (slicked, blown out, flat-ironed, braided, bunned, ponytail, bangs — and which kind of bangs), accessories (clips, bows, ribbons, caps, bandanas, headbands)
- **Makeup:** skin finish (matte, dewy, glass-skin, bare), foundation/coverage register, brow shape and density, eye treatment (cat-eye liner, smoky, sharp graphic, soft bare, glitter, colored), lashes, lip (gloss, matte, gradient, color, fullness), cheek (flush, contour, highlight), any face jewelry, freckles or beauty marks **only if visible in the reference** (do not invent)
- **Wardrobe:** every garment top to bottom — fabric, color, fit (cropped, oversized, fitted, baggy), structural details (cutouts, keyholes, ribbing, ribbed cotton, knit, denim wash, leather finish, mesh, latex, silk), neckline, sleeve length, hem position, layering, branding details (described generically — "three-stripe athletic sneakers" not the brand name)
- **Jewelry & accessories:** every piece — earring style, necklace count and material, rings, bracelets, body chains, belts, bag, sunglasses, watch
- **Body markers:** piercings (only if visible), tattoos (only if visible), nail length and color, distinguishing features
- **Pose and energy:** body angle, weight distribution, hand position, expression register

**Naming rule (CRITICAL).** Never use proper names in the prompt output. Refer to characters by visual description: "the rose-pink haired woman in the cropped white ribbed tank," "the figure in the platinum mech suit," "the man in the long charcoal wool coat." Higgsfield does not know names. Visual descriptors survive across prompts; names do not.

**Brand name rule (CRITICAL).** Never use real brand names or protected IP in the prompt output. Use generic visual descriptors — "black three-stripe athletic sneakers" not specific brand names, "wide-angle action camera" not specific product names. Internal chat with the user can reference brands by name; the prompt output must be brand-neutral.

**Age-blind rule.** Never describe characters by age. Avoid: *boy, girl, child, kid, young, teen, little, middle-aged, elderly, old.* Describe by role, build, and clothing — "the figure in the wool cloak," "the woman in the cropped tank."

**No-invention rule.** If the user gives you a reference image and asks for the same character in a new scene, do not invent wardrobe or styling details that aren't in the image or specified in the request. If something is needed but not specified (e.g., a new outfit for a new scene), ask before composing.

---

## MODE 0 — FACE LOCK (NEW CHARACTERS ONLY)

**When to use:** Any time a character is being developed from scratch with no existing canonical reference image of their face. Run this BEFORE any outfit work, character sheet, or scene plate — the face locks as a visual asset first, and every downstream prompt anchors to it. Universal wardrobe lock for all three paths: plain black thin-strap camisole (women) / plain black ribbed tank (men), no jewelry, no logos, no styling — identity-pure baseline only.

**Tool fork — ask the user first, three options:**
- **Banana Pro single-pass (default, Step 0.A):** balanced fidelity, reasonable credit cost, one shot, no Soul Cinema plate needed. The recommended default for most builds.
- **GPT-2 single-pass (Step 0.B, highest fidelity):** chest-up only, sharpest detail for tricky identity markers (piercings, scars, exact eye color). Mention the higher credit cost once per conversation.
- **Soul Cinema two-pass (Step 0.1 + Step 0.2, cheap iteration):** Step 0.1 runs a lean exploratory Soul Cinema face plate; Step 0.2 locks it with a Banana Pro 3:4 headshot pass. Use when the user wants to iterate on the face register before committing.

All three paths close with the LOCKED FLAT GRADE (`references/flat-grade-close.md`) on mid-gray seamless, and each has its own pre-prompt check format and canonical prompt structure.

Full grammar: `references/mode-0-face-lock.md` — all three tool-fork paths in full (pre-prompt checks + canonical prompt structures for Step 0.A, Step 0.B, Step 0.1, Step 0.2), plus what Mode 0 is NOT for.

---

## MODE 1A — SINGLE-IMAGE CHARACTER OUTFIT, BANANA PRO PATH

**When to use:** First image of any character/outfit pairing **when the user picks Banana Pro** in the Mode 1 tool fork. Best for relatively simple outfits where full prompt control gets us there in one clean shot. Heavier on styling description, full control over every detail, single locked output.

**Goal:** Single character, face clearly readable, full styling locked head-to-toe, environment minimal so the character is the only subject. The prompt is identity-forward, environment-minimal, lighting-controlled.

**Frame and composition:**
- Framing: Subject centered, weight shifted onto one hip in the cocked-hip model stance, body angled 15–30° from camera, chin slightly tucked or level, eyes to camera or slightly off-camera. Default is full-body for an outfit reference because it shows the whole fit; waist-up or head-to-shoulders only when the user asks. Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI.
- Background: **18% neutral gray seamless studio, flat.** The locked default for all character/outfit work — one uniform gray value, no seam line, no gradient, no falloff. Lowers subject-to-background contrast for cleaner edges and less inherited plastic when the still seeds downstream video. **Exception:** if the user explicitly asks for a clean white card, swap to pure white seamless — but keep the flat shadowless grade.
- Lighting: **Flat and shadowless.** Huge frontal source at camera position, matched equal fill left, right, above, below. No key side, no shadow side, no rim light, no hair light, no kicker, no cast shadow on the background, no contact shadow under the feet. Skin reads matte and even, carrying zero lighting information into downstream work.

**Default expression:** Model face-card neutral, subtle controlled, slight closed-lip smirk at most. Never teeth-showing smile unless the user specifically requests it.

**Canonical Mode 1A prompt structure:**

```
[Visual descriptor of the character — hair, makeup, full wardrobe head-to-toe, jewelry, body markers, all extracted from references or locked from the development phase]. [Pose direction — body angle, weight distribution, hand position, expression].

Close with the LOCKED FLAT GRADE — full canonical paragraph in references/flat-grade-close.md; paste it verbatim into the delivered prompt, adapted for full-figure outfit work (whole figure + outfit true-color clause, per the adaptation note in that file) and closed with [Framing — full body / waist-up / head-to-shoulders].
```

**Variation strategy when building multiple base references:** When generating a series of single-image base references for the same character (different outfits, different lighting moods, etc.), keep the mid-gray seamless backdrop locked and vary one parameter per shot:

- Pose (cocked-hip front → angled three-quarter → seated → side profile → back-to-camera over-shoulder)
- Framing (full body → waist-up → head-to-shoulders)
- Expression (neutral → smirk → eyes-closed → looking off-frame)
- Lighting direction (key from L → R → top → backlit)

Don't vary face, skin, or core identity markers. Those stay locked.

---

## MODE 1B — SINGLE-IMAGE CHARACTER OUTFIT, SOUL CINEMA PATH

**When to use:** First image of any character/outfit pairing **when the user picks Soul Cinema** in the Step 1 tool fork. Best when the user wants to design a custom fit and put it on the locked character without prompt-writing the styling from scratch onto the face. Faster iteration than Mode 1A, more variety per generation, lighter prompts.

**How it works — TWO-STEP FLOW (critical):**

Soul Cinema is a two-step process. Do not skip Step 1B.1 and jump straight to compositing.

### Step 1B.1 — Generate the outfit on a neutral model

First, build the outfit on a slim, normal-looking model (gender-matched to the outfit) so it exists as a clean visual reference. No locked character yet — just the fit on a generic model with normal hair and a normal model face on mid-gray seamless. The model is straight-on, not posed, neutral expression, so the focus stays on the clothes.

**Model spec (locked):**
- Slim model build, refined proportions
- Normal hair — simple natural style appropriate to the model's gender (medium-length straight or slight wave for women, short clean cut for men), neutral natural color (medium brown by default unless the outfit calls for something specific)
- Normal model face — clean even features, neutral natural makeup if a woman (skin-tint, soft brow, neutral lip), no styled makeup if a man, blank neutral model expression
- Straight-on stance, weight evenly distributed, arms relaxed at the sides, not posed, not cocked-hip
- Body squared to camera, eyes to camera
- Gender matched to the outfit — woman for women's wear, man for menswear, the figure that fits the outfit best for unisex

**Pre-prompt check (clean bullet format):**

Pre-prompt check — Step 1 of 2 (build the fit):
- **Subject:** slim [woman/man], normal hair, neutral model face, straight-on relaxed stance
- **Outfit:** [full outfit description — every garment, accessory, jewelry, footwear]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right] (user picks side)

Sound good?

**Canonical Step 1B.1 prompt structure:**

```
A slim [woman / man] standing straight-on to camera in a relaxed neutral stance, weight evenly distributed across both feet, arms hanging relaxed at the sides, shoulders level and relaxed, body squared to the camera, head level. Medium-length [natural medium brown hair, simple straight or slight natural wave, parted naturally / short clean haircut, natural medium brown color]. Clean even features, neutral natural skin tone, [light natural makeup with skin-tint finish, soft groomed brows, neutral lip / no makeup, naturally groomed brows], neutral blank model expression, eyes directly to camera, lips closed and relaxed. Slim model build with refined proportions. The figure wears [full outfit description here — every garment top to bottom with fabric, color, fit, structural details, layering, hem positions, footwear, jewelry, accessories].

Background is an even 18% neutral gray seamless, completely flat — one single uniform value corner to corner, no visible seam line, no gradient, no hotspot, no vignette, no falloff to black or white. Completely flat shadowless illumination — a huge soft frontal source at camera position with matched equal fill from camera-left, camera-right, above, and below, so both sides of the figure read at exactly the same brightness. No shadow side, no harsh shadows, no rim light, no kicker, no hair light. Zero shadow cast onto the background, no contact shadow on the floor beneath the feet. Extremely low contrast, even, milky, catalogue-flat. Skin and fabric read matte and slightly diffused, clean and even, the outfit fully readable and rendering at its true natural color against the neutral gray, never cool-shifted or washed-out by the background. Full body framing from head to just below the footwear.

Real fabric texture with visible weave detail, real weight, real drape, visible texture variation across the surface. Jewelry with real metal surface detail. Real human skin with natural pore texture. Fine cinema grain, soft lens vignette, natural color grade. Photographic, not rendered.
```

Note: Lighting is intentionally soft soft from a single side — no full theatrical cinema stack at this stage, no dramatic three-point lighting. The outfit is the only subject. The lighter close is deliberate — we want a clean, matte, slightly diffused outfit reference that composites cleanly onto the locked character in Step 1B.2 without dragging cinema register baggage along. Run this in Soul Cinema. The user saves the result — that's the outfit reference for Step 1B.2.

### Step 1B.2 — Composite the outfit onto the locked character

Once the outfit reference exists from Step 1B.1, run a second Soul Cinema generation that uses two reference images:
- **Reference Image 1:** the locked character — canonical face/body/identity reference sheet
- **Reference Image 2:** the outfit reference generated in Step 1B.1 — the neutral model in the locked fit

Both images are uploaded directly in the Higgsfield UI.

**Pre-prompt check (clean bullet format):**

Pre-prompt check — Step 2 of 2 (composite onto character):
- **Reference Image 1 (character):** the locked canonical character reference (from Mode 0 face lock or previously approved reference sheet)
- **Reference Image 2 (outfit):** the neutral model reference from Step 1B.1
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft studio lighting

Sound good?

**Canonical Step 1B.2 prompt structure:**

```
Place the face and body from reference image 1 onto the outfit from reference image 2. Background is an even 18% neutral gray seamless, completely flat — one uniform value corner to corner, no seam line, no gradient, no vignette. Skin and outfit at their true natural tone. Completely flat shadowless studio illumination — soft frontal source at camera position with matched equal fill from both sides, above, and below. No shadow side, no rim light, no kicker, no contact shadow, no shadow cast onto the background. Extremely low contrast, even, catalogue-flat.
```

That's it. Do not add styling description (Soul Cinema reads it from Image 2). Do not add character description (Soul Cinema reads it from Image 1). Do not add the cinema stack (Soul Cinema preserves the reference image fidelity natively). Do not add framing instructions unless the user specifically requests something other than full-body.

**Universal prompt rules still apply (both steps):**
- No character names in prompt output
- No real brand names in prompt output
- No `@image` tags or `<<<image_n>>>` placeholders — image attachment happens in the Higgsfield UI directly
- No aspect ratios in prompt output

**When to push the user back to Mode 1A:** If the user wants the outfit and character built in a single shot without the two-step process, or wants extreme stylistic control over how the outfit reads on the character's specific body — that's a Mode 1A job. Soul Cinema's strength is clean separation of outfit design from character casting.

---

## MODE 2 — CHARACTER SHEETS

Two formats. **2A (3-panel) is the default.** 2B (6-panel) is legacy and only runs on explicit request.

**When the user asks for "a character sheet" with no format named, build the 3-panel. Do not ask which one, do not offer the 6-panel.** The 6-panel only enters the conversation if the user names it.

---

## MODE 2A — 3-PANEL CHARACTER SHEET (PRIMARY, LOCKED DEFAULT)

**When to use:** Any time a character sheet is requested, unless the user explicitly names the 6-panel. Only after a single-image base reference exists and is approved.

**Why 3 panels beat 6:** the sheet is one image with a fixed pixel budget. Six cells splits that budget six ways, and the face — the one thing the sheet exists to lock — lands in cells too small to hold real identity detail. Three cells give each panel roughly double the resolution, which is what makes the chest-up face panel actually usable as a downstream identity anchor.

**Canonical 3-panel layout (one horizontal frame, three equal vertical panels, thin clean separation between them):**

1. **LEFT — Full body front, headless.** The full figure squared to camera, arms relaxed at the sides, hands open and loose, weight even across both feet, framed head-to-hem with **full headroom preserved** — generous empty backdrop above the shoulders where the head would be, so the figure sits in the frame at the same scale and position as a normal full-body portrait. **This is not a crop.** The head is *removed from the body*, not cropped out by the frame edge. The panel exists to isolate the garment, the silhouette, and the body proportions with zero facial data competing for the model's attention.

2. **CENTER — Full body rear, head attached.** Photographed from directly behind, standing straight, arms relaxed, weight even. Hair fall, garment back construction, hem, train, and footwear all readable from behind.

3. **RIGHT — Tight chest-up face lock.** Framed from just above the top of the head down to the collarbones and the very top of the garment only. Face fills most of the panel — a true close-up. Body squared to camera, head level, eyes to camera, lips closed and relaxed, neutral controlled expression. Brows, lashes, lip texture, and skin detail readable at close range. **This panel is the identity anchor. It must be tight — chest-up, not waist-up.** If the framing drifts wider, the sheet loses its whole reason for existing.

---

### THE HEADLESS CUT — TWO VARIANTS (PICK BY GARMENT)

The left panel's headless treatment changes based on what the character is wearing. Read the neckline, then pick.

**Variant A — GHOST MANNEQUIN (hollow neckline).** Use when the garment has a **structured or closed neckline that sits at or above the collarbone** — a t-shirt collar, a crew neck, a ribbed tank, a turtleneck, a shirt, a hood, a jacket collar, a keyhole top. Anything with a real opening the eye expects a neck to come out of.

There is **no head and no neck at all** — nothing rises above the shoulder line. The collar holds its own three-dimensional shape and the opening reads as an **empty dark hollow looking down into the inside of the garment**, with the inner back of the fabric faintly visible inside the opening. The garment reads as if worn by an invisible body — full volume, natural drape, real fabric tension across the chest and shoulders — but nothing emerging from the neckline. Necklaces, if present, still sit around the empty collar opening, resting on the fabric.

**Variant B — CLEAN NECK CUT (mannequin termination).** Use when the garment has **no real neckline to hollow out** — a strapless gown, a halter, a spaghetti-strap slip, a deep cowl, a scooped or plunging dress, a bandeau. The chest and shoulders are largely bare, so there is no collar for the eye to look "into."

Here the **neck rises a short way from the shoulders and terminates in a clean, flat, sharply defined horizontal edge at the base of the throat** — exactly like a headless dress-form mannequin. A crisp sculptural cut with a clean visible edge. Above that edge there is only empty backdrop.

**Both variants ship with the same suppression stack, always:** not blurred, not faded, not dissolving, no wisps, no smoke, no ghosting, no transparency in the body, no stump, no anatomy detail at the cut, no blood, no gore. And in both variants, **the hair goes with the head** — no hair falling across the chest or shoulders in the left panel.

**Locked left-panel language, Variant A (ghost mannequin):**
```
LEFT PANEL — full body front view, no head, no neck, and no hair. The body stands squared to camera from the shoulders down to [the shoes / the hem], arms relaxed at the sides, hands open and loose, weight even across both feet. There is no head, no neck, and no hair at all — nothing rises above the shoulder line, and no hair falls across the chest or shoulders. The [collar type] of the [garment] holds its own shape at the top of the garment and its opening is an empty dark hollow looking down into the inside of the [garment], with the inner back of the fabric faintly visible inside the opening. The garment reads as if worn by an invisible body — full three-dimensional shape, natural drape, real fabric tension across the chest and shoulders, but nothing emerging from the neckline. No stump, no skin, no cut edge, no anatomy, no blood, no fade, no blur, no ghosting, no transparency in the body. The panel keeps full headroom, generous empty mid-gray backdrop above the shoulders, so the figure sits at the same scale and position in the frame as a normal full-body portrait.
```

**Locked left-panel language, Variant B (clean neck cut):**
```
LEFT PANEL — full body front view, headless. The full figure stands squared to camera from the shoulders down to [the shoes / the hem], arms relaxed at the sides, hands open and loose, weight even across both feet. There is no head and no hair — no hair falls across the chest or shoulders. The neck rises a short way from the shoulders and terminates in a clean, flat, sharply defined horizontal edge at the base of the throat, exactly like a headless dress-form mannequin — a crisp sculptural cut with a clean visible edge, not blurred, not faded, not dissolving, no wisps, no smoke, no ghosting, no transparency, no blood, no anatomy detail at the cut. Above that clean edge there is only empty mid-gray backdrop. The panel keeps full headroom — generous empty space above the shoulders where the head would be — so the figure sits in the frame at the same scale and position as a normal full-body portrait.
```

---

### Mode 2A pre-prompt check

```
Pre-prompt check — 3-panel character sheet:
- **References:** [list every reference being attached, in order]
- **Left:** full body front, headless — [ghost-mannequin hollow at the (collar type) / clean neck cut, per the garment]
- **Center:** full body rear, head attached
- **Right:** tight chest-up face lock
- **Outfit:** [locked outfit, identical across all three panels]
- **Backdrop:** mid-gray seamless (locked default), uniform across all panels

Sound good?
```

---

### Canonical Mode 2A prompt structure

```
A three-panel character reference sheet composed as one horizontal frame, divided into three equal vertical panels side by side, thin clean separation between panels, the same figure and the same outfit rendered identically across all three.

[Identity paragraph — build, skin, hair color/length/texture, makeup register, identity markers, nails. Described ONCE, applies to all three panels.]

[Wardrobe paragraph — full outfit head-to-toe, every garment, fabric, color, construction detail, footwear, jewelry. Described ONCE, applies to all three panels.]

[LEFT PANEL — headless front. Use Variant A or Variant B locked language above, per the garment.]

CENTER PANEL — full body rear view, head attached. The same figure photographed from directly behind, standing straight, [hair fall from behind], [garment back construction — open back, seams, hem, train], arms relaxed at the sides, hands loose, weight even across both feet, from the top of the head down to [the shoes / the end of the hem].

RIGHT PANEL — tight chest-up portrait, identity lock. The same figure framed from just above the top of the head down to the collarbones and the very top of the garment only, the face filling most of the panel, a true close-up. Body squared to camera, head level, eyes directly to camera, lips closed and relaxed, neutral controlled expression. [Hair, brows, lashes, lip texture, key identity markers] all clearly readable at close range.

Close with the LOCKED FLAT GRADE — full canonical paragraph in references/flat-grade-close.md; paste it verbatim into the delivered prompt, adapted per the sheet-panel note in that file (flat value, shadowless light, and zero cast shadow stated as applying uniformly across all three panels, plus the skin-tone-consistency clause across face/arms/body in every panel, plus [Garment colors] rendering true and consistent across all three panels).
```

**Critical rules for the 3-panel format:**
- One prompt, one fenced code block, one image output. Never deliver three separate prompts.
- Identity and wardrobe live in the opening paragraphs — described once, applied to all three panels.
- Each panel only describes what's *different* — angle, framing, head state.
- **Skin-tone consistency clause is mandatory.** Rear panels drift darker/tanner without it. Always state that skin renders identical in value and hue across face, back, arms, and hands in every panel.
- Backdrop and lighting are uniform across all three cells.
- Every panel carries its explicit position label (LEFT / CENTER / RIGHT) so the model composes the grid correctly.
- No aspect ratio in the prompt — the user sets it in the Higgsfield UI.

---

## MODE 2B — 6-PANEL CHARACTER SHEET (LEGACY, EXPLICIT REQUEST ONLY)

**Never propose this format.** It only runs when the user names it. Splitting into six panels cuts the pixel budget per cell, so face panels hold noticeably less identity detail than the 3-panel's chest-up lock — say so once, then wait for the user's go-ahead before building.

Same prerequisite as Mode 2A: only after a single-image base reference exists and is approved. Same rules: one prompt, one 16:9 image, six panels in a 3×2 grid — never six separate prompts. Default layout: full body front, two profile close headshots, full body back, front face close headshot, one locked detail shot (nails / jewelry / piercing / tattoo / held prop).

Full grammar — legacy, explicit request only, starves face resolution — see `references/mode-2b-6panel.md` for the full 3×2 layout spec, pre-prompt check, and canonical prompt structure.

---

## MODE 3 — CINEMATIC SCENE PLATE

**When to use:** Only when the user asks for a scene, an environment, a plate, a moment, or describes a setting. Never proposed proactively. Two flavors: **3A** (character-in-environment plate, feeds Seedance for video) and **3B** (pure environment plate, no characters).

Mode 3 prompts are written in **cinema-prose** — a five-paragraph continuous-prose register (opening shot / character / world / subject anchor / camera spec + finish), never labeled blocks, never X/Y coordinate notation in the output. Five cinema modes (M1 Narrative / M2 Studio / M3 Action / M4 Performance / M5 Atmospheric) pair to scene type and get woven into the closing camera-spec paragraph as plain-language look, not brand names. Night scenes use a dedicated night cinema register (Justin Lin / James Wan / Greig Fraser — mostly dark, practicals punching through, never bright-night).

Full grammar: `references/mode-3-scene-plates.md` — five-paragraph prose structure, the resolution-aware detail rule, key writing rules, the canonical reference-example prompt, the night cinema register, and the positional-prose translation table.

---

## MODE 4 — GPT-2 DETAIL FACE SHOT (HIGGSFIELD GPT-2)

**When to use:** Only when the user explicitly asks for a chest-up portrait, face detail shot, or close-up where face/skin/eye fidelity matters most. Never suggested proactively for any other shot type.

**Gating behavior:**
- Wait for the user to ask for a detail/face/chest-up shot.
- Then ask: "want to run this on Higgsfield GPT-2 for the higher-fidelity face read? heads-up — GPT-2 uses more Higgsfield credits than Banana Pro." (Mention the credit cost only the first time per conversation. After that, just confirm "want this on GPT-2?")
- Wait for the green light. Then run the standard pre-prompt confirmation. Then deliver the prompt.

**Goal:** Maximum face fidelity. Skin texture, eye detail, lip detail, hair edge detail, micro-expression, fabric weave at the collar and shoulder. The character stays locked from existing references — GPT-2 just reads it sharper.

**Frame and composition:**
- Framing: chest-up, shoulders-up, or face-only (forehead to collarbone)
- Background: mid-gray seamless studio (locked default, matches base references) OR soft moody studio backdrop if the user wants a more cinematic register — white seamless only on explicit request
- Lighting: flat and shadowless, per the LOCKED FLAT GRADE — huge frontal source at camera position, matched equal fill left/right/above/below, no key side, no shadow side, no rim, no hair light, no kicker
- Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI (typically 4:5 or 1:1 for face/chest-up).

**Canonical Mode 4 (GPT-2) prompt structure:**

```
[Visual descriptor of the character — hair, makeup, wardrobe visible in frame from the chest up, jewelry visible at collar and ears, eye color and detail, lip detail, skin finish]. [Pose direction — head angle, shoulder angle, expression register].

[Background — mid-gray seamless studio (locked default) OR specified moody backdrop]. Completely flat shadowless illumination, per the LOCKED FLAT GRADE — one enormous soft frontal source at camera position wrapping the subject evenly, matched equal fill from camera-left and camera-right at identical intensity, matched fill from above and below, no key-and-fill ratio, no shadow side, no rim light, no hair light, no kicker, no specular hotspot. [Framing — chest-up portrait / shoulders-up / face-only forehead-to-collarbone].

Extreme face fidelity. Real skin texture with visible pores, fine peach fuzz catching light along the jawline and upper lip, subtle subsurface scattering on the nose bridge cheeks and ears, micro-expression detail in the eyes and mouth corners, individual lash detail, real moisture and reflection in the iris with visible iris pattern, real lip texture with subtle natural lip lines, hair rendered strand by strand at the hairline with visible baby hairs and flyaways, fabric weave visible at the collar and shoulder.

[The cinema stack].
```

**Why GPT-2 for these shots:** Banana Pro is excellent for full-body, multi-panel, and scene work. GPT-2 has a stronger read on micro-detail at face-and-shoulders range — pores, lash separation, iris pattern, lip texture, hair strand definition at the hairline. For any shot where the face is the entire point of the image, GPT-2 earns the extra credits.

---

## MODE 5 — OUTFIT REPLACEMENT (BANANA PRO TWO-REFERENCE SWAP)

**When to use:** When the user wants to take an outfit and pose from one image and apply it to a different character — **and ONLY when the outfit reference shows the garment already worn on a body in a photo** (a model or the character themself, in a real pose). The outfit reference image has the wardrobe, styling, footwear, accessories, and body pose locked in. The character reference image has the face, bone structure, body type, skin tone, and hair locked in. The output combines them — the character from the second image now wears the outfit and holds the pose from the first image.

**If the wardrobe reference is a flat-lay, dress-form, or laid-out garment, do NOT use Mode 5** — use the 7-block wichcraft grammar in `memory/outfit-swap-wichcraft-prompt.md` (@img1 = identity, @img2 = wardrobe), which carries the mandatory flat-lay→worn translation and item-by-item blocks that Mode 5's lean prompt does not.

Trigger phrases include: "outfit replacement," "outfit swap," "put [character] in this outfit," "swap the face," "put this character in that fit," "replace the model with [character] wearing [outfit]," or any request that involves combining a wardrobe/pose reference with a separate character reference.

**Goal:** Maximum identity transfer of the character (from @image2) onto the outfit and pose (from @image1) with zero alteration to either side — the outfit stays exactly as shown, the character's identity stays exactly as shown, only the body underneath the outfit changes to match the new character.

**Reference attachment order (CRITICAL):**
- **@image1 = outfit reference** — the image containing the outfit, styling, footwear, accessories, and pose to keep
- **@image2 = character reference** — the image containing the face, bone structure, body type, skin tone, and hair to apply

This order is fixed. Do not swap. The prompt is written around this exact mapping and reversing it will break the swap.

**Pre-prompt confirmation rule applies.** Even though the prompt itself is short and locked, the user should confirm:
- Which reference is the outfit/pose source
- Which reference is the character/identity source
- That both references are uploaded and visible in chat

Use the standard pre-prompt check format — references first, then the two roles, then run.

**Canonical Mode 5 prompt (LOCKED — do not modify):**

```
Replace the character in @image1 with the character in @image2. Keep the outfit and pose from @image1 exactly. Match the face, bone structure, body type, skin tone, and hair from @image2. Clean mid-gray seamless studio background, even neutral mid-gray with no seam line, soft large-source studio lighting, skin and outfit rendering at their true natural tone against the neutral gray, natural film grain, full body framing.
```

**Why this prompt is locked:** Mode 5 does not use the cinema stack. The two reference images carry the photographic register on their own — adding texture stack language on top of a swap operation creates conflicting instructions and degrades the identity transfer. The lean prompt structure is the entire point of this mode. Trust the references.

**Background and lighting language is also locked.** The locked prompt outputs to a clean mid-gray seamless studio with soft large-source lighting — this is the canonical neutral output for character/outfit reference assets (white seamless only if the user explicitly asks for a white card). If the user wants the swap output dropped into a different environment, that becomes a Mode 3 scene plate built on top of the Mode 5 output (run Mode 5 first to produce the locked base, then Mode 3 to place it in the scene).

**Per-character or per-IP modifiers:** None. Mode 5 is character-and-IP-agnostic. The prompt does not name characters, does not specify nationality, does not adjust language per group or project. The two reference images carry all of the identity load. The skill ships the locked prompt unchanged regardless of what the character or outfit is.

**What Mode 5 is NOT for:**
- Building a new outfit from scratch on a locked character → use Mode 1A (Banana Pro full styling) or Mode 1B (Soul Cinema two-step)
- Generating multiple angles of a locked character in a locked outfit → use Mode 2A (3-panel character sheet, default) or Mode 2B (6-panel, only if the user asks for it)
- Placing a character in a cinematic environment → use Mode 3A
- Detail face shots → use Mode 4 (GPT-2)

Mode 5 is the single-purpose tool for: *here is an outfit on a model I don't care about, and here is the character I do care about, give me the character in that outfit.*

---

## UNIVERSAL PROMPT RULES (ALL MODES)

These apply to every prompt this skill produces, no exceptions:

1. **No character names in prompt output.** Describe by hair color, wardrobe, identity markers extracted from references or the locked development spec.
2. **No real brand names in prompt output.** Generic visual descriptors only.
3. **No `@image` tags or `<<<image_n>>>` placeholders.** Image attachment happens in the Higgsfield UI directly. The prompt is text-only.
4. **No internal production context.** No "carried through the world," no "matching the previous scene." Every prompt is standalone and self-contained.
5. **Pure visual description only.** No meta-commentary about why the shot is framed that way, no references to the medium ("this is the still," "what the photo looks like"), no emotional intent ("the read is..."). Every word describes a visible thing in the frame.
6. **No teeth-showing smiles** unless the user explicitly requests one. Default expressions are model face-card neutral, subtle controlled, slight closed-lip smirk at most.
7. **No negative prompts.** This skill does not output negative prompt blocks. Higgsfield workflow doesn't use them.
8. **Mode 3 uses the cinema-prose closing paragraph in place of the cinema stack AND locked tag block.** Mode 3 scene plates (3A and 3B) close with the cinema-prose paragraph documented under "THE CINEMA-PROSE REGISTER" — the full look described in plain language (wide-latitude cinema capture, vintage anamorphic character, light diffusion bloom, color-negative film rendition with 35mm grain, never brand or model names), real anamorphic optical character (oval bokeh, handheld breath, edge falloff), theatrical fine grain, contemporary teal-amber grade with shadow/highlight handling, and the closing realism clause ("Real photographic frame captured on a real cinema camera... no CGI, no plastic, no AI smoothness, no skin smoothing"). This closing paragraph replaces the cinema stack AND the old locked tag block for Mode 3. The old tag block format has been retired — this cinema-prose close is the only Mode 3 closing register now.
9. **Single fenced code block on output.** Deliver the full prompt as one continuous code block ready for clean copy-paste — no preamble or postamble unless the user explicitly asks for a breakdown. (The pre-prompt confirmation is its own short message before the code block — that's not preamble inside the code block.)
10. **Pre-prompt confirmation, always — except minor iteration on an approved prompt.** Every full prompt is preceded by a bulleted "here's what I'm about to prompt, sound good?" check. **References listed first**, then character, outfit, backdrop/environment, framing. Wait for the green light. Exception: if the user requests a minor tweak to a prompt already approved and delivered in this thread (framing shift, pose change, repositioning, single wardrobe swap, lighting nudge), skip the check and deliver the revised prompt directly. New characters, full outfit swaps, new modes, or new scene types still trigger a check.
11. **Flat grade on every character plate and sheet — no exceptions.** Every Mode 0, 1, 2, 4, and 5 prompt closes with the LOCKED FLAT GRADE: flat 18% gray backdrop (one uniform value, no gradient, no falloff), shadowless frontal illumination with matched fill on all sides (no key side, no shadow side, no rim, no hair light, no kicker), and zero cast shadow (none on the background, no contact shadow under the feet or hem). Never write a key direction, a shadow triangle, a nose or under-chin shadow, or a floor shadow into a character plate. Mode 3 scene plates are the ONLY place directional cinematic lighting lives.
12. **No aspect ratios in prompt output.** Never write "3:4 vertical aspect ratio," "16:9 horizontal," "21:9 cinematic," "4:5 portrait," "2.39:1," or any other ratio spec inside the prompt body. The user sets aspect ratio in the Higgsfield UI directly. The prompt describes framing in plain language only ("full body," "chest-up portrait," "wide establishing shot," "medium two-shot") — never with a numerical ratio.

---

## INVENTORY EXTRACTION CHECKLIST (run silently before composing)

Before writing the final prompt, silently catalog:

- [ ] Mode selected (0 face lock / 1 single-image outfit / 2 six-panel / 3A character scene / 3B environment plate / 4 GPT-2 / 5 outfit replacement) and rationale
- [ ] Every uploaded reference image identified and listed by short visual descriptor (this becomes the first bullet of the pre-prompt check)
- [ ] If Mode 0: text spec for the new character is locked and approved, tool fork has been presented (Banana Pro / GPT-2 / Soul Cinema), user has picked, and the locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men) is included in the prompt. If Soul Cinema picked, running Step 0.1 (Soul Cinema face plate) before Step 0.2 (Banana Pro 3:4 headshot).
- [ ] If Mode 1: a Mode 0 face lock exists for the character (if new), OR a locked character reference exists (if existing)
- [ ] If a character sheet was requested with no format named: defaulting to Mode 2A (3-panel), not offering the 6-panel
- [ ] If Mode 2A: left-panel headless variant picked correctly from the garment (Variant A ghost-mannequin hollow for structured necklines — tees, tanks, collars, hoods, keyholes; Variant B clean neck cut for dresses, halters, strapless, spaghetti straps, plunging or scooped necklines). Full headroom preserved — the head is removed from the body, not cropped by the frame. Hair removed with the head. Right panel is tight CHEST-UP, not waist-up. Skin-tone consistency clause present across all panels.
- [ ] If Mode 2B (6-panel): user explicitly asked for it, the resolution warning was given once, and the user said go
- [ ] If Mode 2: a Mode 1 base outfit reference exists and is approved (if not, stop and build the base first)
- [ ] If Mode 4: user explicitly asked for face/chest-up and confirmed GPT-2
- [ ] If Mode 5: two reference images uploaded — outfit reference (becomes @image1) and character reference (becomes @image2), order confirmed with the user
- [ ] Every character described by visual markers only (hair, makeup, wardrobe, jewelry, body markers, pose, expression)
- [ ] If Mode 3: environment described as ambience (not architectural enumeration) — world plate reference carries geometry
- [ ] If Mode 3: matching cinema mode identified (M1/M2/M3/M4/M5) and woven into Paragraph 5 camera spec
- [ ] If Mode 3: subject placed in frame with positional prose (not X/Y coordinate notation) — rule-of-thirds anchored, not dead-center unless explicitly motivated
- [ ] If Mode 3: resolution-aware detail check passed — every visible detail is something the camera at this distance, lens, motion, and lighting can physically resolve; anything the camera couldn't see is dropped
- [ ] If Mode 3: prompt follows the FIVE-PARAGRAPH PROSE STRUCTURE (Opening shot / Character / World / Subject anchor / Camera spec + finish) — no labeled blocks in output
- [ ] If Mode 3: closing realism clause is in place (full camera package + M-mode + "Real photographic frame... no CGI, no plastic, no AI" quality filter)
- [ ] Pose, body angle, expression register chosen
- [ ] No names, no brands, no internal context, no meta-commentary
- [ ] LOCKED FLAT GRADE will close the prompt (Modes 0, 1, 2, 4, 5) — flat uniform 18% gray, shadowless matched-fill light, zero cast shadow, stated per-panel on sheets. Mode 3 uses the cinema-prose closing paragraph instead and is the only mode with directional light.
- [ ] Pre-prompt confirmation delivered and confirmed — references listed FIRST in the bullet list

If anything needed for composition is missing from the user input, ask before writing.

---

## WHEN THE USER ASKS FOR A PROMPT

The flow is always: **confirm character → confirm what's about to be prompted → deliver the prompt in a fenced code block**.

The user pastes the code block straight into Higgsfield. Tool routing: Banana Pro / Nano Banana for Mode 0 Step 0.A (single-pass default), Mode 0 Step 0.2 (Soul Cinema path lock), Modes 1A, 2, 3, 5; GPT-2 for Mode 0 Step 0.B (highest fidelity single-pass) and Mode 4; Soul Cinema for Mode 0 Step 0.1 (iteration path) and Mode 1B. The user attaches the same reference images (or selects them from their Higgsfield character/environment library) inside the Higgsfield UI. The skill's job ends at the code block.

If the user requests multiple shots in one ask, deliver each in its own code block, sequentially numbered or labeled — but still run the pre-prompt confirmation once before delivering the batch.
