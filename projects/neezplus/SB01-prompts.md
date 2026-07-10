---
project: "Neezplus"
type: ad
doc: SB01-prompts
phase: B
clip: SB01
formula: "Grain Free Tuna & Salmon (dry kibble)"
ratio: "9:16"
duration: "30s"
image_model: "GPT Image 2 (primary) · Nano Banana Pro (alt)"
video_model: "Veo 3 / Google Flow"
bg_color: "solid light sky-blue studio backdrop"
created: "2026-07-10"
---

# SB01 — Grain Free Tuna & Salmon · Presenter Talking-Head Prompt Kit (Phase B)

Pipeline: GPT Image 2 first-frame → Veo 3 / Google Flow animate + Thai lip-sync.
6 scenes. Presenter frames = scenes 1 / 3 / 5 / 6. Scenes 2 / 4 = B-ROLL real/AI cat inserts
(no presenter frame — see §B-ROLL). All presenter frames = solid **light sky-blue** studio backdrop,
9:16, upper-left negative space kept clear for the post-added Thai text highlight (คนบังได้).
Chest logo = blank white box in the gen, real `logo-nees-on-black.jpg` composited in post (kit §4).

---

## 1 · CONTINUITY LEDGER (rebuilt from the REAL generated sheet pixels)

**Identity ref files (attach every frame):**
- `@Image1` = full-body master sheet → `/Volumes/WONYOUNG/Neezplus/ChatGPT Image Jul 10, 2026, 03_00_58 PM.png` (identity + wardrobe)
- `@Image2` = face sheet → `/Volumes/WONYOUNG/Neezplus/ChatGPT Image Jul 10, 2026, 02_56_47 PM.png` (face lock)
- `@Image3` = Tuna & Salmon 1kg **food** bag mockup → `/Volumes/WONYOUNG/Neezplus/package/Grain Free - Adult Tuna&Salmon/pic/TU1kg-1.png` (front, straight-on; alt angles TU1kg-2/-3, back TU1kg-4). Sky-blue+cyan front, brown "NEEZ+" box top-left, big cyan "TUNA & SALMON" panel, fisherman illustration. Attach on scenes 3 / 5 / 6 only — NOT scene 1 (no bag yet). ✅ CONFIRMED food bag (not the litter `*_10L` files).

**IDENTITY BLOCK — VERBATIM (paste unchanged into every image + video prompt):**
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

**WARDROBE LEDGER — VERBATIM (as generated):**
```
WARDROBE: black oversized crew-neck cotton t-shirt — ribbed crew collar, dropped shoulder seams,
relaxed boxy fit, short sleeves ending mid-bicep, plain matte-black fabric; at the left chest a
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder;
paired with plain relaxed black trousers.
```

**SCENE / LIGHT LEDGER (SB01):** solid, evenly-lit **light sky-blue** seamless studio backdrop,
smooth, slightly darker toward the edges. One soft frontal key + gentle fill, natural soft shadow
under the jaw. No visible floor line, no reflective surface (plain seamless studio). Upper-left
quadrant kept as empty negative space for the on-screen text highlight.

**DRIFT NOTES vs Phase A (logged once — ledger follows reality, block kept verbatim because the
sheet is the attached anchor in every frame):**
- Stubble reads *lighter / near clean-shaven* in the generated sheet than "light sparse stubble"
  implies — still within wording, kept verbatim.
- The "two small moles low on the left cheek" are *not clearly visible* in the generated sheet
  (faint at most). Kept in the block as a harmless safety-lock; the sheet governs the actual face.
- Hair reads as a fuller, softly textured short fringe (mild bowl-crop) rather than heavily
  tousled — "short with a soft slightly tousled fringe over the forehead" still holds.
- Chest placeholder box sits roughly centre-left of the chest in the sheet (post-comp target) —
  position is governed by the attached sheet; do not re-describe per frame.

---

## 2 · GEN ORDER (manual — each step = a FRESH GPT Image 2 chat, then a fresh Veo job)

Attach ONLY the refs each step names. Accumulated chat context causes identity drift.

| # | Step | Tool | Attach | Save as |
|---|------|------|--------|---------|
| 1 | Scene 1 first-frame (HOOK, no bag) | GPT Image 2 | `@Image1` full-body sheet · `@Image2` face sheet | `sb_SB01_01_hook.png` |
| 2 | Scene 1 animate + lip-sync | Veo 3 / Flow | upload `sb_SB01_01_hook.png` | `sb_SB01_01_hook.mp4` |
| 3 | Scene 3 first-frame (recommend, holds bag) | GPT Image 2 | `@Image1` · `@Image2` · `@Image3` bag mockup | `sb_SB01_03_recommend.png` |
| 4 | Scene 3 animate + lip-sync | Veo 3 / Flow | upload `sb_SB01_03_recommend.png` | `sb_SB01_03_recommend.mp4` |
| 5 | Scene 5 first-frame (spec 33%/16%, holds bag) | GPT Image 2 | `@Image1` · `@Image2` · `@Image3` bag mockup | `sb_SB01_05_spec.png` |
| 6 | Scene 5 animate + lip-sync | Veo 3 / Flow | upload `sb_SB01_05_spec.png` | `sb_SB01_05_spec.mp4` |
| 7 | Scene 6 first-frame (warm close, holds bag) | GPT Image 2 | `@Image1` · `@Image2` · `@Image3` bag mockup | `sb_SB01_06_close.png` |
| 8 | Scene 6 animate + lip-sync | Veo 3 / Flow | upload `sb_SB01_06_close.png` | `sb_SB01_06_close.mp4` |
| 9 | Scene 6 product pack-shot (optional close-up tail) | GPT Image 2 | `@Image3` bag mockup only | `sb_SB01_06b_packshot.png` |
| — | Logo post-comp on every presenter frame | editor | `logo-nees-on-black.jpg` onto blank chest box | (overwrite finals) |

> After each first-frame gen, composite the real logo into the blank white chest box (kit §4)
> BEFORE uploading to Veo, so the logo is locked and identical across the clip.

---

## B-ROLL INSERT SCENES (no presenter frame — cutaways, VO continues over them)

These are separate insert clips (real or AI cat footage, kept tonally matched to the AI presenter).
Voiceover from the neighbouring presenter take continues over them — no lip-sync, no face on screen.

- **Scene 2 — cat-problem insert (~1s, 3 quick cuts).** Footage needed: (a) a thin cat with visible
  rib line, (b) dull/rough matte coat close-up, (c) eye with heavy tear-stain / eye-gunk near the
  inner corner. Text tag overlay: `ขี้ตาเยอะ`. Carries the tail of Scene 1's VO.
- **Scene 4 — benefit-problem insert (~2s).** Footage needed: (a) cat scratching/grooming itself,
  (b) shed fur caught on a brush, (c) tear-stain streak under the eye. Text tag overlay:
  `ลดคัน ขนร่วง`. Carries the tail of Scene 3's VO (the benefits list — see Scene 3 VO split below).

---

## 3 · STORYBOARD FRAME PROMPTS + VEO VIDEO PROMPTS

Reminder on first-frame discipline: each image is second 0 of its shot — render the TRUE STARTING
pose (mouth just parting to begin the line, gesture not yet at its peak), spatial not temporal,
expression = literal muscle state. Leave the upper-left clear for the post text highlight.

---

### SCENE 1 — HOOK close-up (speak-first, concerned, NO bag)

**► 1A · GPT Image 2 first-frame** — attach `@Image1` full-body sheet + `@Image2` face sheet.
Save as `sb_SB01_01_hook.png`.

```
NEEZ_PRESENTER, tight medium close-up from mid-chest up, 9:16 vertical. Match @Image1 and @Image2
exactly — the same person and the same black NEEZ+ t-shirt. He faces the camera as a credible,
concerned company representative speaking directly to a cat owner.

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
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder.

Pose: standing, upper body squared to camera, no product in frame, one hand loosely raised near
lower chest in a soft open gesture (fingers relaxed, not pointing). Expression: gently concerned
and caring — inner brows drawn faintly together and slightly raised, a soft crease between the
brows, eyes attentive behind the glasses, lips just barely parted as if about to begin the first
word. Head level, gaze straight into the lens.

Background: a clean, evenly-lit SOLID light sky-blue studio backdrop, smooth and seamless, slightly
darker toward the edges; empty negative space in the upper-left for a later on-screen text
highlight. One soft frontal key light plus gentle fill, natural soft shadow under the jaw.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image.
```

**► 1B · Veo 3 / Google Flow video** — upload `sb_SB01_01_hook.png` (logo already composited).
Speech ~5–6s of an 8s clip. Company-rep tone.

Spoken line (full hook — editor may cut to Scene 2 B-roll over the tail):
`น้องแมวผอม ขนไม่สวย ขี้ตาเยอะ ปรับลุคให้สวยสมราคาง่ายนิดเดียวครับ`

```
Use the uploaded reference image as the single source of truth.
[CHARACTER_LOCK]
Maintain 100% consistency of: facial structure, face proportions, eye shape, eyebrow shape, nose
shape, lips shape, skin texture, hairstyle, hair color, glasses, age appearance, ethnicity.
Do not redesign, beautify, stylize, or alter identity. The character must remain visually identical
to the reference image throughout the entire video.
[BODY_LOCK]
Preserve: body shape, body proportions, posture, shoulder width, arm proportions, hand
characteristics. No body morphing. No character replacement. No identity drift.
[OUTFIT_LOCK]
Preserve exactly: the black oversized crew-neck t-shirt, the white chest logo patch, colors,
fabric. Do not change wardrobe. No outfit replacement. No color changes.
[ENVIRONMENT_LOCK]
Preserve the solid light sky-blue seamless studio backdrop from the reference image and the empty
upper-left negative space. Do not add objects, text, furniture, or background elements.
[ATMOSPHERE_LOCK]
Maintain identical soft frontal key lighting, gentle fill, soft under-jaw shadow, sky-blue color
grading and mood. Preserve the visual feeling of the reference image.
[IDENTITY_PERSISTENCE]
Maintain the exact same person throughout. No identity drift, no face morphing, no age changes, no
hairstyle changes. The final frame must match the first frame.
[FRAME_CONSISTENCY]
Maintain frame-to-frame consistency. No sudden changes in face, clothing, hairstyle, body
proportions, glasses, environment.
[TEMPORAL_LOCK]
Maintain temporal consistency throughout. The character remains unchanged from beginning to end.
No visual drift, no character regeneration.
[CAMERA_LOCK]
Camera: realistic, cinematic, natural perspective, stable framing, minimal motion. No fisheye, no
distortion, no sudden zooms.
[ACTION]
The character speaks directly to the camera as a caring company representative. Stable upright
posture, minimal movement, a small caring nod, gentle concerned eyebrows, maintains eye contact.
The soft open hand gesture near the chest settles naturally. Natural body language.
[SPEECH]
The character speaks naturally in Thai. "น้องแมวผอม ขนไม่สวย ขี้ตาเยอะ ปรับลุคให้สวยสมราคาง่ายนิดเดียวครับ"
Speaking pace: medium, natural Thai conversational rhythm. Clear pronunciation.
Voice tone: warm, confident, credible, reassuring — a trustworthy brand representative. Avoid:
sleepy tone, monotone voice, robotic delivery, over-excited hard-sell.
Perfect Thai lip sync. Natural mouth movement, natural facial expressions, natural blinking.
Finish speaking within the first 5-6 seconds.
[QUALITY]
Ultra realistic. Photorealistic. Natural skin texture with visible pores. Professional
cinematography. Stable identity, facial consistency, outfit consistency, environment consistency.
8-second video.
```

---

### SCENE 3 — recommend (holds the Tuna & Salmon bag, explaining)

**► 3A · GPT Image 2 first-frame** — attach `@Image1` full-body sheet + `@Image2` face sheet +
`@Image3` Tuna & Salmon 1kg bag mockup. Save as `sb_SB01_03_recommend.png`.

```
NEEZ_PRESENTER, medium shot from mid-chest up, 9:16 vertical. Match @Image1 and @Image2 exactly —
the same person and the same black NEEZ+ t-shirt. He holds the product bag shown in @Image3 — the
Neezplus Grain Free Tuna & Salmon 1kg bag, sky-blue front with the "NEEZ+" mark top-left, a large
"TUNA & SALMON" panel and a fisherman illustration — reproduce that bag artwork faithfully. He
faces the camera as a friendly, credible company representative speaking directly to a cat owner.

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
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder.

Pose: standing, upper body squared to camera, both hands holding the Tuna & Salmon bag at
lower-chest height, angled so its sky-blue front face reads clearly to camera, held toward the
lower-right of frame so the presenter's face and the upper-left stay clear. Expression: warm and
explaining — relaxed brows, soft eyes behind the glasses, faint friendly smile, lips parted mid-word
as if introducing the product. Head level, gaze into the lens.

Background: a clean, evenly-lit SOLID light sky-blue studio backdrop, smooth and seamless, slightly
darker toward the edges; empty negative space in the upper-left for a later on-screen text
highlight. One soft frontal key light plus gentle fill, natural soft shadow under the jaw.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image except the product bag's
own printed artwork.
```

**► 3B · Veo 3 / Google Flow video** — upload `sb_SB01_03_recommend.png`.

**VO SPLIT (this scene's script line is long — presenter lip-syncs the on-screen intro, the
benefits tail becomes VO over Scene 4 B-roll):**
- **Presenter lip-sync (Scene 3, ~4–5s):** `แค่ลองเปลี่ยนอาหารเป็น นีซพลัส สูตรเกรนฟรี ทูน่าแซลมอน`
- **VO over Scene 4 B-roll (no lip-sync, voiceover only):** `ก็ช่วยลดอาการแพ้สัตว์ปีก แพ้ธัญพืช ลดคัน ขนร่วง ลดคราบน้ำตาได้ครับ`

```
Use the uploaded reference image as the single source of truth.
[CHARACTER_LOCK]
Maintain 100% consistency of: facial structure, face proportions, eye shape, eyebrow shape, nose
shape, lips shape, skin texture, hairstyle, hair color, glasses, age appearance, ethnicity.
Do not redesign, beautify, stylize, or alter identity. Visually identical to the reference image
throughout the entire video.
[BODY_LOCK]
Preserve: body shape, proportions, posture, shoulder width, arm proportions, hand characteristics.
No body morphing, no character replacement, no identity drift.
[OUTFIT_LOCK]
Preserve exactly: the black oversized crew-neck t-shirt, the white chest logo patch, colors,
fabric. No wardrobe change.
[PROP_LOCK]
Preserve exactly the Neezplus Grain Free Tuna & Salmon bag held in both hands — its sky-blue front,
"NEEZ+" mark, "TUNA & SALMON" panel and fisherman illustration. Keep the bag artwork stable and
legible, front face toward camera. Do not warp, redesign, or relabel the bag. Hands stay natural
with five fingers, no extra fingers.
[ENVIRONMENT_LOCK]
Preserve the solid light sky-blue seamless studio backdrop and the empty upper-left negative space.
Do not add objects or text.
[ATMOSPHERE_LOCK]
Maintain identical soft frontal key lighting, gentle fill, sky-blue color grading and mood.
[IDENTITY_PERSISTENCE]
Same person throughout. No identity drift, no face morphing, no age or hairstyle changes. The final
frame must match the first frame.
[FRAME_CONSISTENCY]
No sudden changes in face, clothing, hairstyle, body proportions, glasses, the bag, or environment.
[TEMPORAL_LOCK]
Temporal consistency throughout. Character and bag unchanged from beginning to end.
[CAMERA_LOCK]
Camera: realistic, cinematic, natural perspective, stable framing, minimal motion. No fisheye, no
distortion, no sudden zooms.
[ACTION]
The character speaks directly to the camera as a friendly company representative and gently lifts
and steadies the Tuna & Salmon bag toward camera to present it. Stable posture, minimal movement,
maintains eye contact, warm explaining expression. The bag stays in frame, front face to camera.
[SPEECH]
The character speaks naturally in Thai. "แค่ลองเปลี่ยนอาหารเป็น นีซพลัส สูตรเกรนฟรี ทูน่าแซลมอน"
Speaking pace: medium, natural Thai conversational rhythm. Clear pronunciation.
Voice tone: warm, confident, credible, reassuring brand representative. Avoid sleepy, monotone,
robotic, or hard-sell delivery.
Perfect Thai lip sync. Natural mouth movement, natural facial expressions, natural blinking.
Finish speaking within the first 5-6 seconds.
[QUALITY]
Ultra realistic. Photorealistic. Natural skin texture with visible pores. Professional
cinematography. Stable identity, facial, outfit, prop and environment consistency. 8-second video.
```

---

### SCENE 5 — spec emphasis (protein 33% / fat 16%, holds bag)

**► 5A · GPT Image 2 first-frame** — attach `@Image1` full-body sheet + `@Image2` face sheet +
`@Image3` Tuna & Salmon 1kg bag mockup. Save as `sb_SB01_05_spec.png`.

```
NEEZ_PRESENTER, medium shot from mid-chest up, 9:16 vertical. Match @Image1 and @Image2 exactly —
the same person and the same black NEEZ+ t-shirt. He holds the product bag shown in @Image3 — the
Neezplus Grain Free Tuna & Salmon 1kg bag, sky-blue front with the "NEEZ+" mark top-left, a large
"TUNA & SALMON" panel and a fisherman illustration — reproduce that bag artwork faithfully. He
faces the camera as a confident, credible company representative emphasising a key fact to a cat
owner.

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
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder.

Pose: standing, upper body squared to camera, one hand cradling the Tuna & Salmon bag at
lower-chest height with its sky-blue front toward camera (held toward the lower-right of frame),
the other hand just beginning a soft open-palm presenting gesture beside the bag (fingers relaxed,
gesture not yet at full extension). Expression: confident and emphatic but warm — eyebrows slightly
raised, engaged focused eyes behind the glasses, lips parted mid-word as if stating a number. Head
level, gaze into the lens.

Background: a clean, evenly-lit SOLID light sky-blue studio backdrop, smooth and seamless, slightly
darker toward the edges; empty negative space in the upper-left for a later on-screen text
highlight. One soft frontal key light plus gentle fill, natural soft shadow under the jaw.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image except the product bag's
own printed artwork.
```

**► 5B · Veo 3 / Google Flow video** — upload `sb_SB01_05_spec.png`.

Spoken line (primary, deliver briskly to land inside ~6s):
`ด้วยโปรตีน 33% ไขมัน 16% ถ้าอยากให้น้องแมวสุขภาพดีทั้งภายในภายนอก ไม่ต้องลองผิดลองถูกเลยครับ`

Fallback split (if the full line overruns 6s in Veo): lip-sync
`ด้วยโปรตีน 33% ไขมัน 16% ถ้าอยากให้น้องแมวสุขภาพดีทั้งภายในภายนอก` on the presenter, and run
`ไม่ต้องลองผิดลองถูกเลยครับ` as VO into the Scene 6 head.

```
Use the uploaded reference image as the single source of truth.
[CHARACTER_LOCK]
Maintain 100% consistency of: facial structure, face proportions, eye shape, eyebrow shape, nose
shape, lips shape, skin texture, hairstyle, hair color, glasses, age appearance, ethnicity.
Do not redesign, beautify, or alter identity. Visually identical to the reference image throughout.
[BODY_LOCK]
Preserve body shape, proportions, posture, shoulder width, arm proportions, hand characteristics.
No morphing, no character replacement, no identity drift.
[OUTFIT_LOCK]
Preserve exactly the black oversized crew-neck t-shirt, white chest logo patch, colors, fabric.
[PROP_LOCK]
Preserve exactly the Neezplus Grain Free Tuna & Salmon bag — sky-blue front, "NEEZ+" mark,
"TUNA & SALMON" panel, fisherman illustration. Keep bag artwork stable and legible, front to
camera. Do not warp or relabel. Hands natural, five fingers, no extra fingers.
[ENVIRONMENT_LOCK]
Preserve the solid light sky-blue seamless backdrop and empty upper-left negative space. No added
objects or text.
[ATMOSPHERE_LOCK]
Maintain identical soft frontal key lighting, gentle fill, sky-blue color grading and mood.
[IDENTITY_PERSISTENCE]
Same person throughout. No drift, no morphing, no age or hairstyle change. Final frame matches first.
[FRAME_CONSISTENCY]
No sudden changes in face, clothing, hairstyle, proportions, glasses, bag, or environment.
[TEMPORAL_LOCK]
Temporal consistency throughout. Character and bag unchanged start to end.
[CAMERA_LOCK]
Camera: realistic, cinematic, natural perspective, stable framing, minimal motion. No fisheye, no
distortion, no sudden zooms.
[ACTION]
The character speaks directly to the camera as a confident company representative, giving a small
emphatic nod and completing the soft open-palm presenting gesture beside the bag while stating the
numbers. Bag stays in frame, front to camera. Stable posture, maintains eye contact.
[SPEECH]
The character speaks naturally in Thai. "ด้วยโปรตีน 33% ไขมัน 16% ถ้าอยากให้น้องแมวสุขภาพดีทั้งภายในภายนอก ไม่ต้องลองผิดลองถูกเลยครับ"
Speaking pace: medium-fast but clear, natural Thai conversational rhythm. Precise pronunciation of
the numbers "สามสิบสามเปอร์เซ็นต์" and "สิบหกเปอร์เซ็นต์".
Voice tone: confident, credible, warm brand representative. Avoid sleepy, monotone, robotic, or
hard-sell delivery.
Perfect Thai lip sync. Natural mouth movement, natural facial expressions, natural blinking.
Finish speaking within the first 5-6 seconds.
[QUALITY]
Ultra realistic. Photorealistic. Natural skin texture with visible pores. Professional
cinematography. Stable identity, facial, outfit, prop and environment consistency. 8-second video.
```

---

### SCENE 6 — warm close (holds bag) + product close-up

**► 6A · GPT Image 2 first-frame (presenter warm close)** — attach `@Image1` full-body sheet +
`@Image2` face sheet + `@Image3` Tuna & Salmon 1kg bag mockup. Save as `sb_SB01_06_close.png`.

```
NEEZ_PRESENTER, medium shot from mid-chest up, 9:16 vertical. Match @Image1 and @Image2 exactly —
the same person and the same black NEEZ+ t-shirt. He holds the product bag shown in @Image3 — the
Neezplus Grain Free Tuna & Salmon 1kg bag, sky-blue front with the "NEEZ+" mark top-left, a large
"TUNA & SALMON" panel and a fisherman illustration — reproduce that bag artwork faithfully. He
faces the camera as a warm, reassuring company representative giving a friendly closing
recommendation to a cat owner.

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
single small plain WHITE rounded-corner rectangle (blank, no text inside) as a logo placeholder.

Pose: standing, upper body squared to camera, both hands holding the Tuna & Salmon bag at
mid-chest height, presented gently forward with its sky-blue front toward camera. Expression: warm
friendly closing smile, eyes slightly narrowed with genuine warmth behind the glasses, lips just
parting to begin the closing line. Head level, gaze into the lens.

Background: a clean, evenly-lit SOLID light sky-blue studio backdrop, smooth and seamless, slightly
darker toward the edges; empty negative space in the upper-left for a later on-screen text
highlight. One soft frontal key light plus gentle fill, natural soft shadow under the jaw.

Photographed on a full-frame camera, natural skin texture with visible pores and slight natural
facial asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss, true-to-life adult
man. no text, no captions, no logos, no watermarks anywhere in the image except the product bag's
own printed artwork.
```

**► 6B · Veo 3 / Google Flow video** — upload `sb_SB01_06_close.png`.

⚠️ **COMPLIANCE (กฎกระทรวงเกษตรฯ 2560):** original storyboard line flagged for a "ที่สุด" /
"ขายดีที่สุด" restricted absolute-claim risk. Below is a compliant delivery — no "ที่สุด", no
absolute/guarantee, keeps the "ขายดี / รีวิวเพียบ" flavour as a soft popularity statement.

- **Compliant Veo line (use this):**
  `แนะนำลองเริ่มที่ตัวนี้เลยครับ สูตรนี้ขายดี รีวิวในโซเชียลก็เพียบเลยครับ`
- **More-conservative alt (if legal wants extra safety, drops even "ขายดี"):**
  `แนะนำลองเริ่มที่ตัวนี้เลยครับ เป็นสูตรที่ได้รับความนิยม รีวิวในโซเชียลก็มีให้อ่านเยอะเลยครับ`
- **NOTE:** final script text (and the `[รีวิวเพียบ]` on-screen tag) must be **client-approved
  before lip-sync render** — reworking Thai wording after render breaks the lip sync.

```
Use the uploaded reference image as the single source of truth.
[CHARACTER_LOCK]
Maintain 100% consistency of: facial structure, face proportions, eye shape, eyebrow shape, nose
shape, lips shape, skin texture, hairstyle, hair color, glasses, age appearance, ethnicity.
Do not redesign, beautify, or alter identity. Visually identical to the reference image throughout.
[BODY_LOCK]
Preserve body shape, proportions, posture, shoulder width, arm proportions, hand characteristics.
No morphing, no character replacement, no identity drift.
[OUTFIT_LOCK]
Preserve exactly the black oversized crew-neck t-shirt, white chest logo patch, colors, fabric.
[PROP_LOCK]
Preserve exactly the Neezplus Grain Free Tuna & Salmon bag held in both hands — sky-blue front,
"NEEZ+" mark, "TUNA & SALMON" panel, fisherman illustration. Keep bag artwork stable and legible,
front to camera. Do not warp or relabel. Hands natural, five fingers, no extra fingers.
[ENVIRONMENT_LOCK]
Preserve the solid light sky-blue seamless backdrop and empty upper-left negative space. No added
objects or text.
[ATMOSPHERE_LOCK]
Maintain identical soft frontal key lighting, gentle fill, sky-blue color grading and warm mood.
[IDENTITY_PERSISTENCE]
Same person throughout. No drift, no morphing, no age or hairstyle change. Final frame matches first.
[FRAME_CONSISTENCY]
No sudden changes in face, clothing, hairstyle, proportions, glasses, bag, or environment.
[TEMPORAL_LOCK]
Temporal consistency throughout. Character and bag unchanged start to end.
[CAMERA_LOCK]
Camera: realistic, cinematic, natural perspective, stable framing, minimal motion. No fisheye, no
distortion, no sudden zooms.
[ACTION]
The character speaks directly to the camera as a warm company representative, gently presenting the
bag a touch closer to camera with a friendly closing smile and a small warm nod. Bag stays in
frame, front to camera. Stable posture, maintains eye contact.
[SPEECH]
The character speaks naturally in Thai. "แนะนำลองเริ่มที่ตัวนี้เลยครับ สูตรนี้ขายดี รีวิวในโซเชียลก็เพียบเลยครับ"
Speaking pace: medium, natural Thai conversational rhythm. Clear pronunciation.
Voice tone: warm, friendly, reassuring brand representative — a genuine caring close. Avoid sleepy,
monotone, robotic, or hard-sell delivery.
Perfect Thai lip sync. Natural mouth movement, natural facial expressions, natural blinking.
Finish speaking within the first 5-6 seconds.
[QUALITY]
Ultra realistic. Photorealistic. Natural skin texture with visible pores. Professional
cinematography. Stable identity, facial, outfit, prop and environment consistency. 8-second video.
```

**► 6C · (OPTIONAL) product close-up pack-shot** — the "product close-up" tail of Scene 6. Separate
non-presenter frame; attach `@Image3` bag mockup only. Save as `sb_SB01_06b_packshot.png`. Animate
in Veo as a slow push-in / slow rotate (storyboard-prompter writes that video prompt).

```
Product pack-shot, 9:16 vertical. The Neezplus Grain Free Tuna & Salmon 1kg cat-food bag from
@Image3 — sky-blue front with the "NEEZ+" mark top-left, a large "TUNA & SALMON" panel and a
fisherman illustration — reproduce the bag artwork faithfully and keep all printed text crisp and
legible. The bag stands upright, front face square to camera, slightly hero-lit from the upper
left, on a clean solid light sky-blue seamless studio backdrop with a soft contact shadow beneath
it and empty negative space in the upper-left for a later on-screen text highlight.

Photographed on a full-frame camera, soft studio product lighting, subtle realistic sheen on the
foil bag, natural soft shadow, no beauty-filter gloss. no text, no captions, no logos, no
watermarks anywhere in the image except the product bag's own printed artwork.
```

---

## 4 · SELF-QA

- Every frame cites real existing files (`@Image1`/`@Image2` real sheet paths; `@Image3` bag = Mirko-attached). ✔
- Identity block + wardrobe ledger wording IDENTICAL and VERBATIM across all four presenter frames + all Veo prompts. ✔
- First-frame discipline: true starting pose (lips just parting; gestures pre-peak), spatial not temporal, expression = literal muscle state (brows/eyes/lips). ✔
- No temporal/motion words inside the IMAGE prompts (motion lives only in Veo `[ACTION]`/`[SPEECH]`). ✔
- No-text tail on every image prompt (bag-artwork exception stated where the bag is held). ✔
- BG = solid light sky-blue on every SB01 presenter frame; upper-left negative space reserved for text highlight (คนบังได้). ✔
- Module distinction: Scene 1 = tight concerned CU (no bag) vs Scenes 3/5/6 = medium, bag-in-hand, distinct beats (recommend / spec / warm close). ✔
- Chest logo kept as blank white box for post-comp; product bag reproduced from @Image3. ✔
- Veo prompts follow the lock-tag master template + Thai VO pacing (finish 5–6s) + company-rep tone (warm/credible, not hard-sell). ✔
- Long lines split so lip-sync fits the 8s/5–6s window; benefit tail = VO over B-roll. ✔
- Scene 6 superlative-claim risk handled: compliant rewrite + conservative alt + client-approval note. ✔
- B-roll cutaways (Scenes 2/4) listed with required footage; no presenter frame built for them. ✔
- Content limits: fully-clothed male presenter, product ad, non-sexual — no policy risk. ✔

---

## ⚠ ASK (Mirko / client)

1. **Sky-blue BG confirm** — derived from the real bag; confirm the client is happy with a solid
   light sky-blue backdrop for the whole SB01 clip (kit §7 ASK #1 was still open).
2. **Scene 6 final script** — pick the compliant line vs the conservative alt, and get client
   sign-off on the `[รีวิวเพียบ]` on-screen tag before any lip-sync render (regulation proof).
3. **Scene 5 pacing** — confirm delivering the full protein/fat line in ~6s is acceptable, or use
   the provided split (tail as VO into Scene 6).
4. **Standing vs seated** — SB01 built STANDING throughout (matches "holds bag, talks"); confirm
   standing is the house default for the talking clips.
5. **Bag mockup file** — confirm which file in `/Volumes/WONYOUNG/Neezplus/` is the final Tuna &
   Salmon 1kg FOOD bag to attach as `@Image3` (the `*_10L mockup` files on hand are the litter
   line, not this kibble bag).
