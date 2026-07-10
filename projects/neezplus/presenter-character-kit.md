---
project: "Neezplus"
type: ad
doc: presenter-character-kit
phase: A
target_model: "GPT Image 2 (primary) · Nano Banana Pro (alt)"
created: "2026-07-10"
---

# Neezplus — Presenter Identity-Lock Character Kit (Phase A)

Single recurring male presenter for ALL 12 talking-head clips (ก้อน A). Locked from two client
reference images. Identity + wardrobe must hold hard across every scene, so this kit builds a
named reference sheet FIRST, then every clip is a fresh drop-in against that sheet.

**Locked sources (do NOT invent a different look):**
- Face ref (Ref A): `/Volumes/WONYOUNG/Neezplus/ChatGPT Image Jul 6, 2026, 05_49_12 PM.png`
- Wardrobe ref (Ref B): `/Volumes/WONYOUNG/Neezplus/Screenshot 2569-07-08 at 09.25.41.png`
- Clean logo file (for post-comp): `/Volumes/WONYOUNG/Neezplus/logo-nees-on-black.jpg`

**Target model:** GPT Image 2 — recurring character, lowest identity drift (~6% in benchmark,
named-reference-sheet method). Alt = Nano Banana Pro (holds identity across refs, good if GPT
garbles the sheet; use the SAME sheet + SAME prompt text). One-change-at-a-time, fresh
conversation per gen, sheet-as-identity-anchor throughout.

---

## 0 · IDENTITY BLOCK (VERBATIM — copy character-for-character into every prompt)

> Paste this block unchanged into the Face Sheet, the Full-Body Sheet, the expression sheet,
> and every per-scene drop-in. Do not paraphrase, trim, reorder, or synonym-swap it.

```
NEEZ_PRESENTER — a real 28-year-old Korean man, roman-name reference NEEZ_PRESENTER; long oval
face with a soft defined jaw and moderate cheekbones; warm brown eyes with a subtle low double
eyelid, slightly hooded and gentle; natural medium-thick straight eyebrows; straight
moderate-bridge nose; round thin black metal-frame glasses with full-round lenses; thick
matte-black hair, short, with a soft slightly tousled fringe falling over the forehead; light
sparse stubble over the upper lip, chin and jaw; warm neutral-undertone skin with natural pores
and two small moles low on the left cheek near the jaw; calm, friendly, academic/nerdy demeanor
with a soft closed-mouth smile.
```

## 0b · WARDROBE LEDGER (VERBATIM — the locked outfit)

> SCENE/CLIP version (real logo, if you go the text-lock route OR post-comp target):
```
WARDROBE: black oversized crew-neck cotton t-shirt — ribbed crew collar, dropped shoulder seams,
relaxed boxy fit, short sleeves ending mid-bicep, plain matte-black fabric with no other print;
at the left chest a small white rounded-corner rectangular logo box containing the "NEEZ+"
wordmark, with a smaller "neezplus." wordmark directly beneath the box; paired with plain relaxed
black trousers.
```

> SHEET version (logo replaced by a blank anchor box — see §4 logo handling):
```
WARDROBE: black oversized crew-neck cotton t-shirt — ribbed crew collar, dropped shoulder seams,
relaxed boxy fit, short sleeves ending mid-bicep, plain matte-black fabric; at the left chest a
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder;
paired with plain relaxed black trousers.
```

## 0c · REALISM SUFFIX (VERBATIM tail on every image prompt)

```
Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image.
```
> BANNED words (do not use): hyperrealistic, ultra-detailed, 8K, masterpiece.
> Sheet exception: the sheet keeps its printed NAME label — its negative tail is stated inline.

---

## 1 · ASSET MAP

| id | type | file to save | feeds |
|---|---|---|---|
| `NEEZ_PRESENTER_facesheet` | sheet (face) | `NEEZ_PRESENTER_facesheet.png` | face-lock ref for full-body sheet + face-lock 2nd ref in every clip |
| `NEEZ_PRESENTER_fullbody` | sheet (full-body + wardrobe) | `NEEZ_PRESENTER_fullbody.png` | MASTER identity+wardrobe ref for all 12 talking clips |
| `NEEZ_PRESENTER_expr` | sheet (expression, OPTIONAL) | `NEEZ_PRESENTER_expr.png` | acting-beat reference for hook/warm-close expressions across clips |
| (per-clip drop-in) | scene frame | `clip_<formula>_<nn>.png` | first-frame of each talking-head video shot |

Ref A already IS the client-approved hero look (no separate portrait-approval gen needed — the
face is locked). Ref A + Ref B feed the Face Sheet directly.

---

## 2 · GEN ORDER (manual — Mirko gens by hand; each step = a FRESH conversation)

Attach ONLY the refs each step names. Accumulated chat context causes identity drift.

1. **Face Sheet** — new GPT Image 2 chat. Attach **Ref A** (`ChatGPT Image Jul 6, 2026,
   05_49_12 PM.png`) + **Ref B** (`Screenshot 2569-07-08 at 09.25.41.png`). Paste prompt §3.1.
   Save output as **`NEEZ_PRESENTER_facesheet.png`**. If a panel breaks, regen using this sheet
   itself as the reference.
2. **Full-Body Sheet** — new chat. Attach **`NEEZ_PRESENTER_facesheet.png`** (identity) +
   **Ref B** (wardrobe/tee shape). Paste prompt §3.2. Save as **`NEEZ_PRESENTER_fullbody.png`**.
3. **(Optional) Expression Sheet** — new chat. Attach **`NEEZ_PRESENTER_facesheet.png`** only.
   Paste prompt §3.3. Save as **`NEEZ_PRESENTER_expr.png`**. Do this only once acting beats per
   clip are final (hook faces vary by clip).
4. **Per-clip drop-ins** (×12, one per clip) — new chat EACH clip. Attach
   **`NEEZ_PRESENTER_fullbody.png`** as `@Image1` (identity + wardrobe master) +
   **`NEEZ_PRESENTER_facesheet.png`** as `@Image2` (face lock). Paste template §5, fill the
   `{FORMULA_COLOR}` / `{PRODUCT_BAG}` / `{POSE}` slots. Save as `clip_<formula>_<nn>.png`.
5. **Logo post-comp** — after each clip frame, composite `logo-nees-on-black.jpg` (white NEEZ+
   box + neezplus.) onto the blank white chest box in an editor (see §4). Do NOT rely on the
   model to render the fine wordmark legibly.

---

## 3 · CHARACTER PROMPTS

### 3.1 · FACE SHEET  (attach Ref A + Ref B)

```
Create a character reference sheet for a single person named NEEZ_PRESENTER. Match the two
attached reference images exactly — the same person: use the first image for the exact face and
the second image for the black t-shirt. This is one identity asset, neutral studio lighting, flat
plain light-grey seamless background, even soft frontal light, no scene, no story, no props.

Print the label "NEEZ_PRESENTER" in clean latin letters at the top of the sheet.

Show a 1x2 layout of 2 head-and-shoulders panels of the SAME single person, identical face, hair,
glasses and outfit across both views, only the camera angle changes:
- Left panel: straight front view, looking at camera, neutral relaxed expression, soft closed-mouth smile.
- Right panel: clean 90-degree left-side profile.

NEEZ_PRESENTER — a real 28-year-old Korean man, roman-name reference NEEZ_PRESENTER; long oval
face with a soft defined jaw and moderate cheekbones; warm brown eyes with a subtle low double
eyelid, slightly hooded and gentle; natural medium-thick straight eyebrows; straight
moderate-bridge nose; round thin black metal-frame glasses with full-round lenses; thick
matte-black hair, short, with a soft slightly tousled fringe falling over the forehead; light
sparse stubble over the upper lip, chin and jaw; warm neutral-undertone skin with natural pores
and two small moles low on the left cheek near the jaw; calm, friendly, academic/nerdy demeanor
with a soft closed-mouth smile.

He wears a black oversized crew-neck cotton t-shirt with a ribbed crew collar and dropped shoulder
seams; at the left chest a single small plain WHITE rounded-corner rectangle (blank, no text
inside) as a logo placeholder.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text except the "NEEZ_PRESENTER" name label at the top; no other captions, logos or
watermarks anywhere in the image.
```

### 3.2 · FULL-BODY SHEET  (attach NEEZ_PRESENTER_facesheet.png + Ref B)

```
Create a full-body character reference sheet for NEEZ_PRESENTER. Match the attached face sheet
exactly — the same person, same face, hair, glasses and stubble; use the second image only for
the black t-shirt shape. One identity asset, neutral studio lighting, flat plain light-grey
seamless background, even soft light, no scene, no props.

Print the label "NEEZ_PRESENTER" in clean latin letters at the top of the sheet.

Show a 1x2 layout of 2 full-body panels of the SAME single person, standing straight, arms
relaxed at the sides, identical face, hair, glasses and outfit across both views, only the camera
angle changes:
- Left panel: straight front full-body view.
- Right panel: clean 90-degree left-side full-body profile.

NEEZ_PRESENTER — a real 28-year-old Korean man, roman-name reference NEEZ_PRESENTER; long oval
face with a soft defined jaw and moderate cheekbones; warm brown eyes with a subtle low double
eyelid, slightly hooded and gentle; natural medium-thick straight eyebrows; straight
moderate-bridge nose; round thin black metal-frame glasses with full-round lenses; thick
matte-black hair, short, with a soft slightly tousled fringe falling over the forehead; light
sparse stubble over the upper lip, chin and jaw; warm neutral-undertone skin with natural pores
and two small moles low on the left cheek near the jaw; calm, friendly, academic/nerdy demeanor
with a soft closed-mouth smile.

WARDROBE: black oversized crew-neck cotton t-shirt — ribbed crew collar, dropped shoulder seams,
relaxed boxy fit, short sleeves ending mid-bicep, plain matte-black fabric; at the left chest a
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder;
paired with plain relaxed black trousers and plain dark shoes.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text except the "NEEZ_PRESENTER" name label at the top; no other captions, logos or
watermarks anywhere in the image.
```

### 3.3 · EXPRESSION SHEET  (OPTIONAL — attach NEEZ_PRESENTER_facesheet.png only)

> Expressions chosen from what the talking script actually plays: hook (concern/curiosity),
> body (explaining, reassuring), warm close. Generate only after clip acting beats are final.

```
Create an expression reference sheet for NEEZ_PRESENTER. Match the attached face sheet exactly —
the same single person, identical framing, face, hair, glasses and outfit in every panel; ONLY
the expression changes. Neutral studio lighting, flat plain light-grey background, no props.

Print the label "NEEZ_PRESENTER" in clean latin letters at the top of the sheet.

Show a 2x3 grid of 6 head-and-shoulders close-ups, all the same distance and angle (front,
looking at camera), varying only the expression:
1. neutral soft closed-mouth smile
2. slightly concerned, brows drawn faintly together, lips pressed (hook / stating a problem)
3. curious, one brow lifted, head level, attentive
4. warm open explaining look, lips parted mid-word, relaxed brows
5. reassuring gentle nod expression, soft eyes, easy smile
6. warm friendly closing smile, eyes slightly narrowed with genuine warmth

NEEZ_PRESENTER — a real 28-year-old Korean man, roman-name reference NEEZ_PRESENTER; long oval
face with a soft defined jaw and moderate cheekbones; warm brown eyes with a subtle low double
eyelid, slightly hooded and gentle; natural medium-thick straight eyebrows; straight
moderate-bridge nose; round thin black metal-frame glasses with full-round lenses; thick
matte-black hair, short, with a soft slightly tousled fringe falling over the forehead; light
sparse stubble over the upper lip, chin and jaw; warm neutral-undertone skin with natural pores
and two small moles low on the left cheek near the jaw.

He wears the black oversized crew-neck t-shirt with the blank white rounded-rectangle placeholder
at the left chest.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text except the "NEEZ_PRESENTER" name label at the top; no other captions, logos or
watermarks anywhere in the image.
```

---

## 4 · LOGO HANDLING (the fine print AI garbles)

The chest mark is two lines of fine type — white "NEEZ+" box + "neezplus." wordmark. GPT Image 2
and Nano Banana both mangle type this small (garbled letters, dropped ®, wrong wordmark = QA
fail). Two routes:

**► RECOMMENDED — blank-box anchor + post-comp (used in all prompts above).**
- Sheets and clip frames render the tee with a single **blank white rounded rectangle** at the
  left chest as a position anchor. It reads as a logo patch, frames correctly, and never garbles.
- In post (Photoshop/Photopea/Canva/Affinity), paste the clean `logo-nees-on-black.jpg` artwork
  into that white box on every final frame. Trivial mask — the box is already the right shape,
  colour and position. Perfect, legally-correct logo every time.
- Trade-off: one extra 20-second post step per frame. Reward: 100% correct branding, zero regens.

**► ALT — careful in-model text-lock (only if you refuse post-comp).**
Replace the chest line in any prompt with:
```
at the left chest a small white rounded-corner rectangular box containing the wordmark "NEEZ+" in
bold black letters, and directly below the box the word "neezplus." in white lowercase letters —
render this small logo crisp and legible.
```
- Trade-off: even when it lands, expect frequent garble (missing +, wrong "neezplus" spelling,
  smeared ®) → many rerolls, and it drifts differently on every clip = inconsistent branding
  across the 12 clips. Not recommended for a 12-clip set that must match.

**Verdict:** use the blank-box + post-comp route for the whole campaign — it is the only way to
keep the logo identical across all 12 clips.

---

## 5 · PER-SCENE DROP-IN TEMPLATE (talking clips — 9:16)

> New chat per clip. Attach `@Image1 = NEEZ_PRESENTER_fullbody.png` (identity + wardrobe master)
> and `@Image2 = NEEZ_PRESENTER_facesheet.png` (face lock). Fill slots. This is the FIRST FRAME
> of the video shot, so render a natural holdable starting pose (not the peak gesture). Spatial,
> not temporal — no motion words.

**Slots:**
- `{FORMULA_COLOR}` = solid BG colour that echoes the product formula (e.g. purple for Chicken
  Senior 7+, green for chicken wet, orange for fish wet, TBD for Tuna & Salmon kibble).
- `{PRODUCT_BAG}` = which Neezplus bag/box he holds (leave blank / "no product yet" for
  speak-first hook frames).
- `{POSE}` = `standing` or `seated` (see two ready variants below).

```
NEEZ_PRESENTER, medium shot from mid-chest up, 9:16 vertical. Match @Image1 and @Image2 exactly —
the same person and the same black NEEZ+ t-shirt. He faces the camera as a friendly, credible
company representative speaking directly to a cat owner.

NEEZ_PRESENTER — a real 28-year-old Korean man, roman-name reference NEEZ_PRESENTER; long oval
face with a soft defined jaw and moderate cheekbones; warm brown eyes with a subtle low double
eyelid, slightly hooded and gentle; natural medium-thick straight eyebrows; straight
moderate-bridge nose; round thin black metal-frame glasses with full-round lenses; thick
matte-black hair, short, with a soft slightly tousled fringe falling over the forehead; light
sparse stubble over the upper lip, chin and jaw; warm neutral-undertone skin with natural pores
and two small moles low on the left cheek near the jaw.

WARDROBE: black oversized crew-neck cotton t-shirt — ribbed crew collar, dropped shoulder seams,
relaxed boxy fit, short sleeves ending mid-bicep, plain matte-black fabric; at the left chest a
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder.

Pose: {POSE}, upper body squared to camera, relaxed shoulders, {PRODUCT_BAG} held in both hands
at lower-chest height, angled so its front face reads to camera. Expression: attentive and warm,
lips parted mid-word as if explaining, soft eyes behind the glasses, faint friendly smile.

Background: a clean, evenly-lit SOLID {FORMULA_COLOR} studio backdrop, smooth and seamless,
slightly darker toward the edges; empty negative space on the upper-left for a later on-screen
text highlight. One soft frontal key light plus gentle fill, natural soft shadow under the jaw.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image.
```

**Ready POSE variants:**
- `{POSE}` STANDING drop-in: `standing`, and set `{PRODUCT_BAG}` to the bag (or `no product yet,
  both hands relaxed, one hand loosely gesturing at chest height` for a speak-first hook frame).
- `{POSE}` SEATED drop-in: `seated behind a clean {FORMULA_COLOR}-matched surface, forearms
  resting near the table edge`, product bag standing on the surface beside him or held.

> Reminder: leave the upper-left negative space clear — the brief wants a text highlight behind
> the presenter (คนบังได้). Insert shots (cats / ingredients) are separate frames, not this one.

---

## 6 · STORYBOARD PLAN (preview — Phase B builds these, one per talking clip)

12 talking-head clips, each a 30s clip. Per clip, the Phase-B first-frame follows the brief's
4-beat script (hook 3s → problem origin → recommend formula → warm close). BG colour = that
formula's colour. Frame list (module tags per clip = HOOK / BODY / CTA within the single shot):

1. `clip_tunasalmon_01` (kibble, HOOK) — presenter speak-first, concerned look, no bag yet, BG {TBD-confirm}.
2. `clip_chickensenior_01` (kibble 7+, BODY) — holds purple Chicken Senior bag, explaining, BG purple.
3–8. remaining 6 food clips (เม็ด+เปียกคละ) — one per formula, holding that bag, BG = formula colour.
9. `clip_litter_green_01` — holds green litter bag, BG green.
10. `clip_litter_<c2>_01` — litter colour 2.
11. `clip_litter_<c3>_01` — litter colour 3.
12. `clip_litter_<c4>_01` — litter colour 4.

(Exact formula→colour map and which clips are seated vs standing get locked in Phase B once the
full script + confirmed formula colours arrive. Insert shots — fat cat / shedding / salmon oil —
are separate non-presenter frames handled outside this presenter kit.)

---

## 7 · SELF-QA

- Gen order is generatable top-to-bottom (Ref A+B → face sheet → full-body → drop-ins). ✔
- Identity block appears VERBATIM in face sheet, full-body sheet, expression sheet, drop-in. ✔
- Wardrobe wording identical (sheet = blank-box version everywhere; scene ledger reserved for
  the real-logo/post-comp target). ✔
- Realism rules applied; banned words (hyperrealistic/ultra-detailed/8K/masterpiece) absent. ✔
- No-text tail on every prompt; sheet name-label exception stated inline. ✔
- Content limits: fully-clothed male presenter, non-sexual — no policy risk. ✔
- Sheets use explicit grid geometry + "same single person… identical across all views". ✔
- Logo garble handled explicitly (blank-box anchor + post-comp primary, text-lock alt). ✔

---

## ⚠ ASK (Mirko / client)

1. **Tuna & Salmon kibble BG colour** (SB01, first clip) still TBD — need the confirmed
   `{FORMULA_COLOR}` before that drop-in can render.
2. **Confirm `logo-nees-on-black.jpg` is the exact chest artwork** (white NEEZ+ box + "neezplus."
   wordmark) to composite — it matches Ref A/B visually; just need the yes for post-comp.
3. **Standing vs seated** default for the talking clips — kit ships both variants; say which is
   the house default (or per-clip).
4. **Expression sheet:** generate now with the 6 generic beats above, or wait for final per-clip
   scripts so the beats match exactly? (Recommend: wait — hook faces differ per formula.)
5. **Full formula→colour map** for all 12 clips (only purple/green/orange confirmed so far).
