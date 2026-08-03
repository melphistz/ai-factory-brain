# Mode 3 — Cinematic Scene Plate (full grammar)

Full reference for SKILL.md Mode 3 (scene plates, with or without characters) and the night cinema register used inside it. Pointed to from SKILL.md — see the summary there for when to use Mode 3 at all.

---

## NIGHT CINEMA REGISTER (FOR NIGHT SCENES)

When the user asks for a night scene, the night work has a specific theatrical action cinema target — **Justin Lin / James Wan / Greig Fraser night work**. This is the dark, practical-driven theatrical action night register seen in Tokyo Drift canyon scenes, Fast 5 night work, Furious 7 night chases, The Batman, John Wick. Critical principle: theatrical night cinema is **mostly dark, with hard punchy practicals cutting through**. NOT saturated-teal-everywhere. NOT bright-night.

**Two modes of night cinema:**

**A. EXTERIOR CANYON / OPEN NIGHT (cliff overlooks, canyon roads, remote night):**
- Light comes EXCLUSIVELY from practical sources in the scene (headlights, brake lights, dash glow leaking out doors, distant city glow). No ambient moonlight, no ambient sky lift.
- The sky and surroundings are committed to deep crushed near-black darkness
- A faint horizon glow may be visible at very deep distance — small, contained, abstract neon color (magenta, cyan, warm amber, hot pink) barely readable as far-off civilization, NOT bright enough to illuminate anything in foreground or midground
- Atmospheric haze suspended in air catches headlight beams as visible warm white volumetric god rays
- Headlight backscatter lights only the immediate front of each vehicle and the rocks/ground directly in front
- Everything outside the headlight throws and their immediate backscatter falls into deep crushed near-black shadow
- The cars themselves read primarily as silhouettes against the night sky with their headlight glow defining their forward edges
- This is the Tokyo Drift canyon night register — DARK, with hard warm headlight punch as the only light

**B. INTERIOR / URBAN / LIT NIGHT (parking garages, warehouses, city streets, interior cabins):**
- Practical sources in the scene drive the look — sodium-vapor street lamps, fluorescent garage lights, neon signs, dash glow, brake lights, interior lighting
- Teal-amber color split can read here because practical sources motivate it (cool sodium / fluorescent / neon vs warm dash / brake / amber lights)
- Atmospheric haze gives light volumetric body
- Background subjects readable through the lit zones
- This is the Tokyo Drift parking garage register, Furious 7 night chase register — practical-driven, deep contrast, real teal-amber color split where motivated

**Universal night cinema rules across both modes:**

**Contrast:** Deep cinematic contrast — shadows are deep but hold information, highlights are hot but don't clip into mush. Wide dynamic range that reads on a real cinema screen.

**Practicals punch hard:** Headlights cut through darkness with real intensity and volumetric throw. Brake lights saturate hot red. Dash glow saturates cabin interiors. Light HITS the scene with purpose, not softly diffused into mush.

**Atmospheric haze:** Light volumetric haze suspended in air (canyon dust, urban smog, breath, ground moisture). The haze catches practical light beams as visible volumetric cones. This is what makes light feel real on screen.

**Rim and edge light:** Subjects in night scenes defined against dark backgrounds by rim and edge light from practical sources. Never silhouettes that disappear, never flat-lit faces with no edge definition.

**Skin in night:** Skin reads warm against cool ambient when there's any cool ambient to read against. Real human skin tone preserved through the grade. Practical light sources warm one side of the face — natural face-side-lighting from real cinema gaffer work.

**The reference is unambiguous:** Real theatrical action movie nights projected onto real IMAX screens. Tokyo Drift, Fast 5, Furious 7, The Batman, John Wick. Theatrical, punchy, **mostly dark, with practical light cutting through**. Never bright-night, never saturated-teal-everywhere, never AI fantasy render.

---

## MODE 3 — CINEMATIC SCENE PLATE

**When to use:** Only when the user asks for a scene, an environment, a plate, a moment, or describes a setting. Never proposed proactively.

Two flavors:

- **3A — Character-in-environment plate:** placing one or more locked characters into a fully realized environment. Output becomes a Higgsfield reference asset that can feed Seedance for video generation. Camera language matches the cinema mode the eventual video will use.
- **3B — Pure environment plate:** no characters in frame. Pure location, lighting, atmosphere, set dressing. Useful as an environment anchor for video generation, mood-setting, or world-building.

**Goal:** A single still that captures the world (and the character, when present) and the camera grammar — as if a cinematographer locked off and grabbed a photo on the same camera package mid-take.

**Camera grammar — five cinema modes paired to scene type.** Pick the cinema mode that matches the scene. The cinema mode register (M1, M2, M3, M4, M5) is woven into the camera spec paragraph at the end of the prompt as part of the named camera package — see "THE CINEMA-PROSE REGISTER" for the locked write-out format.

| If the scene is... | Cinema mode |
|---|---|
| Real-world dramatic (street, kitchen, car, bar, interior, exterior location) | M1 — Narrative |
| Studio / editorial / void / clean set / fashion film | M2 — Studio / Editorial |
| Action / combat / chase / high-energy physical | M3 — Action / Combat |
| Performance / concert / stage / pit | M4 — Performance / Concert |
| Atmospheric / empty / no-humans / weather plate | M5 — Atmospheric / Empty |

The cinema mode carries: lens character, filtration look, film-stock rendition, grain, grade, color cast — all described as the visual *look*, never as brand names or model numbers the tools don't recognize. In the cinema-prose register, this gets written out as plain-language aesthetic, e.g., "Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture — oval bokeh, gentle horizontal squeeze, soft frame-edge falloff, a light diffusion bloom lifting highlights into a soft halation, color-negative daylight film rendition with fine 35mm grain, in an M1 cinematic narrative register." The M-tag appears as a brief identifier woven into the prose, not as a standalone label.

---

### THE SILENT 6-BLOCK MENTAL CHECKLIST (PRE-COMPOSITION ONLY)

Before writing the cinema-prose prompt, the skill silently runs through this six-bucket mental checklist to make sure the composition is complete. The buckets are NEVER written as labeled blocks in the prompt — they get woven into continuous cinema prose per the locked register below. This checklist is a thinking tool, not an output structure.

**Bucket 1 — Shot DNA.** Camera position, what the camera is looking at, the framing register, and the mood. The spine of the shot.

**Bucket 2 — Subject behavior + spatial placement.** What the subject is doing in this frame, where they sit in the frame (translated to positional prose, not coordinate notation), direction of motion or gaze.

**Bucket 3 — Visible detail (resolution-aware).** Only the details a real camera at this distance, lens, and motion register would resolve. (Resolution-aware rule documented below.)

**Bucket 4 — World.** Environment as ambience, not architecture. The space's register matters more than counting structural elements. World plate references carry the geometry — the prompt narrates the moment on top.

**Bucket 5 — Light and atmosphere.** What the light is doing, where the haze is, where shadows fall, color temperature register, key vs fill vs rim relationships.

**Bucket 6 — Camera spec + finish.** Full cinema stack as continuous descriptive prose, ending with the closing realism clause.

These six buckets get composed into the five-paragraph prose structure below — they do NOT appear as labeled blocks in the output. See "THE CINEMA-PROSE REGISTER" for the actual write-out format.

---

### RESOLUTION-AWARE DETAIL RULE (LOCKED)

**Describe what the camera at this position can physically see, not what's "true" about the subject.**

Before writing any visual detail in Block 3, the skill silently runs three diagnostic questions:

1. **At this distance, would a real cinema lens resolve this detail?** If no, drop it.
2. **At this motion blur level, would this detail read?** If no, drop it.
3. **At this lighting register, would this detail be visible?** If no, drop it.

**Examples of what this rule kills:**

- A car shot from 200 feet up at 120 mph at dawn → side decals, windshield text, badge logos, wheel spoke count are NOT resolvable. Drop them. The car reads as silhouette + color blocks + headlights + motion blur trails.
- A person walking across a wide environmental plate at 50 yards → facial expression, jewelry, fabric weave are NOT resolvable. Drop them. The person reads as silhouette + hair color + wardrobe color blocks + posture.
- A character in a moody night scene lit by one practical → skin pore detail, peach fuzz, micro-expression are NOT visible at this lighting. Drop them. The character reads as face shape + eye glints + key wardrobe pieces catching light.

**Examples of what this rule preserves:**

- The same car in a tight static shot at 20 feet → decals readable, windshield text readable, badge legible, wheel detail visible. Describe them.
- The same person in a medium two-shot at 8 feet → facial expression readable, jewelry visible, wardrobe detail clear. Describe them.

**Detail is earned by camera proximity, lens length, motion stillness, and lighting intensity. The skill respects this physics.**

---

### THE CINEMA-PROSE REGISTER (LOCKED, NON-NEGOTIABLE)

**Mode 3 prompts are written like a DP describing a real frame, not like a spec sheet.** The 6-block spatial logic still applies — but it dissolves INTO the prose. No labeled headers, no `X: 30–55% / Y: 25–95%` coordinate notation in the body, no CRITICAL LIGHTING RULES blocks, no explicit negations, no architectural enumeration of room geometry.

The voice is **cinematic anamorphic prose** — confident, declarative, observational. The kind of language that appears in a treatment, a shot list narration, or a hero-still caption. Like a real photograph being described, not a frame being engineered.

**Why this register works:**
- The model responds to confident scene description, not coordinate grids
- References carry the heavy lifting on geometry, palette, and continuity — the prompt narrates the moment ON TOP of the reference
- Over-specification creates conflicting instructions; the model trusts plain language more than rule-blocks
- Spatial logic is preserved by writing positionally ("standing alone in the center of the room," "in the deeper background camera-left") instead of numerically

**What the register sounds like:**

> "A cinematic anamorphic still photograph captured handheld on a real cinema set — a Dutch-tilted intimate over-the-shoulder hero composition of a young Korean man standing alone in a dim converted private garage lounge at pre-dawn, the entire frame tilted at approximately 4 degrees Dutch angle camera-left low giving the composition a quietly off-kilter held-breath feel, the camera positioned right behind him at shoulder height in a waist-up framing showing his back, shoulders, and the back of his head filling the foreground with the wall-mounted television playing the live broadcast visible past his right shoulder in the mid-ground."

That opening sentence does the work of Blocks 1 and 2 in one continuous breath, with the camera position, the framing, the Dutch tilt, the subject placement, and the mood all woven together.

---

### THE FIVE-PARAGRAPH PROSE STRUCTURE (LOCKED)

Every Mode 3 prompt is composed as five paragraphs in this order. Paragraphs are not labeled in the output — they flow as continuous prose for the model.

**Paragraph 1 — Opening shot description.** One long sentence that establishes: the medium ("a cinematic anamorphic still photograph"), the framing register ("Dutch-tilted intimate hero composition"), the subject identification at high level ("a young Korean man standing in a dim converted private garage lounge at pre-dawn"), the camera position and angle in prose ("the camera positioned right behind him at shoulder height in a waist-up framing"), and the mood/intent ("quietly off-kilter held-breath feel"). This is the spine. Everything that follows hangs from this opening.

**Paragraph 2 — Character block.** Describes the character(s) in confident observational prose. Identity markers pulled from the attached reference written as visible facts in the frame ("dark layered mid-length tousled fringe falling across the back of his head, double small silver hoop earrings on each ear lobe catching faint warm spill, warm fair matte Korean skin"). Pose, attention, and held props woven in naturally ("a small black television remote held loosely in his right hand at his side... his head perfectly motionless, his eyes locked on the screen ahead of him").

**Paragraph 3 — World/environment block.** Describes the location as ambience and atmosphere, not architecture. The space's register — converted garage at pre-dawn, dawn cliffside, neon parking garage — matters more than counting structural elements. Anchor the world to the attached reference ("the converted garage lounge at pre-dawn carrying from the attached world reference"). Background subjects (a car silhouette in deep BG, a second character in the alcove) get positional language ("in the deeper background camera-left") not coordinates.

**Paragraph 4 — Subject anchor block.** Whatever the focal anchor of the shot is — the TV broadcast playing on the wall, the second car in BG, the dawn whisper on the horizon — gets its own paragraph. This is where any specific content (broadcast graphics, decals, signage, environmental detail) is described. If the shot has no focal anchor beyond the character, this paragraph folds into Paragraph 3.

**Paragraph 5 — Camera spec + finish.** Full cinema look in one continuous descriptive paragraph: capture register, lens character, diffusion/filtration look, film-stock rendition, grain register, grade, color cast, optical character (anamorphic oval bokeh, organic handheld breath, edge falloff, soft diffusion bloom if relevant) — all in plain-language look terms, never brand or model names — and the closing realism clause ("Real photographic frame captured on a real cinema camera, real anamorphic lens, real cotton tee, real human subject, real concrete and haze — no CGI, no rendered look, no digital cleanliness, no plastic surfaces, no AI smoothness, no skin smoothing, no glow, no halation bloom that reads as artificial, no glossy highlights").

The closing realism clause is mandatory. The list of "no X, no Y, no Z" at the very end is a load-bearing element — it tells the model what NOT to lean toward, and it does so AFTER all the positive description, where the model handles it as a quality filter rather than a conflicting instruction.

---

### KEY WRITING RULES FOR THE PROSE REGISTER

1. **No labeled blocks in output.** Never write "Block 1," "PARAGRAPH 2," "CRITICAL LIGHTING RULE," or any structural label in the prompt body. The structure is invisible — it lives in the writing order.

2. **No coordinate notation in the prompt body.** No `X: 38–62% / Y: 12–95%`. Replace with positional prose: "centered in the room," "in the deeper background camera-left," "filling the foreground," "anchored upper-left of the broadcast."

3. **No CRITICAL/IMPORTANT/MUST rules.** No "the cool wash MUST NOT catch the back wall." Replace with descriptive prose about what IS happening: "the cool broadcast wash catching only the immediate floor patch around his feet and a soft cool rim on his shoulders."

4. **No explicit negations as instructions.** Don't write "NO long sleeves, NOT factory tank-top construction." Write what IS there: "the sleeves cut off cleanly at the shoulder seam with raw unfinished armholes." The end-of-prompt realism clause is the ONLY place negations appear, and only as quality filters (no CGI, no plastic, no AI smoothness).

5. **References do the geometry work.** When the user attaches a world plate, write "carrying identically from the attached world reference" — don't re-enumerate the room geometry. The reference IS the geometry.

6. **References do the identity work.** When the user attaches a character reference sheet, write "carrying identically from the attached character reference" — don't re-describe every facial feature in the prompt. The reference IS the identity.

7. **The prompt narrates THE MOMENT.** What is the character doing right now? What is the camera doing right now? What is the light doing right now? That's the prompt's job. Continuity (room geometry, character identity, broadcast content) is reference work.

8. **The closing realism clause is non-negotiable.** Every Mode 3 prompt ends with the full cinema stack paragraph + the "Real photographic frame... no CGI, no plastic, no AI" close-out. This replaces the old locked tag block.

9. **The cinema mode register (M1/M2/M3/M4/M5) is invoked by DESCRIBING the actual look in plain language** in Paragraph 5 — not by writing "M1 Narrative" as a tag, and never by naming camera/lens/stock brands. Example: "Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture — oval bokeh, gentle horizontal squeeze, soft frame-edge falloff, a light diffusion bloom lifting highlights into a soft halation, color-negative daylight film rendition pushed slightly, with fine 35mm grain, in an M1 cinematic narrative register." The M-tag appears as a brief identifier at the end of the description, not as a standalone label.

10. **Do not write aspect ratios into the prompt** — the user sets aspect in the Higgsfield UI (typically 21:9 or 2.39:1 for cinematic plates).

---

### CANONICAL MODE 3 PROMPT — REFERENCE EXAMPLE

This is the locked register. Every future Mode 3 prompt is written in this voice — confident, observational, declarative, references doing the geometry and identity work, no labeled blocks, no coordinate notation in the body.

```
A cinematic anamorphic still photograph captured handheld on a real cinema set — a low-angle medium hero composition of a woman standing alone at the edge of an empty rooftop at dusk, the camera positioned slightly below her eye line in a waist-up framing anchored to the left third of the frame, the deepening dusk sky filling the upper two-thirds of the frame behind her, the city skyline reading in soft silhouette across the lower third of the background, the composition holding a quiet observational stillness.

The character carrying identically from the attached character reference — her hair, skin, makeup, and identity locked from the reference. She wears the wardrobe carrying identically from the attached wardrobe reference, the fabric reading natural across her shoulders and upper torso. Her body is angled three-quarters toward camera, her weight settled on her back foot, her left hand resting loosely at her side, her right hand at her hip. Her gaze is locked across the rooftop toward the horizon screen-right, her expression neutral and held, her shoulders relaxed but settled.

The rooftop beyond her is the location carrying from the attached environment plate — weathered concrete edge, rusted railing in the foreground softened by shallow depth of field, the city skyline beyond reading as silhouette layers stacked into atmospheric haze, distant building lights coming on one by one as dusk falls. Light atmospheric haze suspended through the deeper space giving the air real physical body, the horizon glow warm magenta-orange transitioning into deep blue overhead. Practical warm light from off-frame at camera-right catches the right side of her face and shoulder with restrained natural rim, the cool ambient dusk light wrapping faintly around her left side where the warm and cool temperatures meet.

The city skyline reads as the visual anchor of the deeper frame — building silhouettes layered front-to-back with progressive atmospheric desaturation, the warm horizon glow visible between the structures, scattered building lights warm and small in the deep distance, a faint aircraft beacon blinking once at the upper-right edge of the frame, the rest of the sky held in deep cool blue with the first stars just visible at the upper edge.

Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture, a light diffusion bloom softening the highlights, color-negative daylight film rendition pushed slightly, in an M1 cinematic narrative register. Real anamorphic optical character with oval bokeh on the deeper city elements, organic handheld operator breath, subtle frame-edge falloff, a faint horizontal streak flare on the brightest horizon highlight. Theatrical fine 35mm film grain across the entire frame — skin, fabric, concrete, sky, haze. Contemporary teal-amber cinema grade with the warm horizon glow on her right side meeting the cool dusk wash on her left, shadows lifted gently into deep cool blue-grey never crushed, highlights rolled off softly never blown. Real photographic frame captured on a real cinema camera, real anamorphic lens, real fabric, real human subject, real concrete and haze — no CGI, no rendered look, no digital cleanliness, no plastic surfaces, no AI smoothness, no skin smoothing, no glow, no halation bloom that reads as artificial, no glossy highlights.
```

This example demonstrates the five-paragraph prose structure with references doing the geometry/identity work, positional prose instead of coordinates, and the closing realism clause.

---

### POSITIONAL PROSE TRANSLATION TABLE (old X/Y notation → prose)

| Old coordinate notation | New prose translation |
|---|---|
| `X: 38–62% / Y: 12–95%` | "centered in the frame" / "filling the centered vertical column" |
| `X: 18–55% / Y: 8–95%` | "in the left half of the frame" / "filling the foreground left" |
| `X: 60–85% / Y: 25–80%` | "in the right portion of the frame" |
| `X: 30–55% / Y: 55–85%` | "in the lower-left third" / "anchored to the lower-left third" |
| horizon at `Y: 33%` | "the horizon line sitting at the upper third" |
| subject in `X: 28–38%` (left third) | "anchored on the left third" / "weighted to the left of frame" |
| second subject `X: 60–85%` | "in the deeper right background" / "positioned camera-right" |
