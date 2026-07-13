# VALENSHIELD vid04 — "Dokkaew Workday Styling" · Prompt Kit (Phase B)

Format: 20s · 9:16 · NO VO · upbeat fashion music + SFX only (tap click + soft whoosh) · ends hard-cut to Valenshield logo.
REF template: UNIQLO "Workday Styling" (`/Volumes/WONYOUNG/Dokkeaw/ref/04.mp4`) — female nurse clone, lavender uniform, no Uniqlo branding.
Mechanic: per look = TAP floating item in air → outfit changes instantly → delighted "WOW" reaction → confident pose. Change = HARD CUT in CapCut (Look N tap → cut → Look N+1 wow). Each Seedance clip = ONE outfit start-to-finish (morph-safe, no in-clip change, no flash/sparkle/dissolve). Floating items + text/logo = AE/CapCut only; model taps EMPTY AIR.

---

## 1) CONTINUITY LEDGER

### Identity block (VERBATIM in every still)
> a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss

### Lavender-shade lock
> soft light lavender / pale periwinkle, matte finish — cool but NOT blue, NOT lilac-grey, NOT purple. Same exact shade every frame. Buttons = silver faceted domed metal.

### ⚠️ COLLAR DISCRIMINATION (critical — L2 vs L3 kept generating identical)
> The three collars MUST look unmistakably different at a glance:
> - **Look 1 = round, CLOSED, no V** (Peter-Pan, flat circular leaves, piped edge)
> - **Look 2 = wide V, broad rounded lapel points angling DOWN** (classic notched revere)
> - **Look 3 = higher narrow V, long sharp points sweeping UP like wings** (bird-wing, topstitched)
> Add to every prompt: `the three collars must be clearly distinguishable; do NOT give Look 2 and Look 3 the same collar`
> Best ref = real product collar photo (3 mannequins) — attach alongside the char sheet when generating.

### Wardrobe (from pixels)
- **Look 1** (`ChatGPT Image Jul 10, 2026, 04_56_04 PM.png`): a rounded PETER-PAN collar (two soft circular collar leaves lying flat on the chest, closed high at the neck, NO lapel and NO V-opening, fine piping along the curved edge); SHORT sleeve turned-up cuff; **5** silver buttons; princess seams; 2 hip patch pockets; lavender knee-length pencil SKIRT; white ballet flats w/ toe-bow.
- **Look 2** (`ChatGPT Image Jul 10, 2026, 12_03_35 PM.png`): classic notched tailored lapel (wide V, broad rounded points angling DOWN) (worn open); LONG sleeve buttoned cuff; **4** silver buttons; straight-leg lavender TROUSERS w/ pressed crease; chunky white low-top sneakers.
- **Look 3** (`ChatGPT Image Jul 10, 2026, 05_28_40 PM.png`): a SHARP POINTED "BIRD-WING" LAPEL (narrower higher V, LONG NARROW SHARP points sweeping UPWARD and outward like wings — never downward, high crisp notch, topstitched edges); SHORT sleeve turned-up cuff; **4** silver buttons; straight-leg lavender TROUSERS w/ pressed crease; chunky white low-top sneakers.

### Scene lock
Identical bright mid-century styling room every look; same camera, eye-level, static; same full-length framing + body scale in both stills; soft window light screen-left; pale glossy floor faint reflection.

### Tap-point lock (AE)
Fixed point in EMPTY AIR at upper-chest-to-chin height, screen-RIGHT of centre, ~one forearm in front of torso. Right hand raised, index finger pressing; left hand relaxed. Same screen coordinate in all 3 tap stills.

### Drifts vs board
- Look 3 = TROUSERS (board said skirt) · product = LAVENDER (board said white) · only Look 1 = skirt+flats · only Look 2 = long sleeve · Look 1 = 5 buttons, Looks 2&3 = 4.

---

## 2) GEN ORDER + @REF (each row = fresh context)

| # | Output | Tool | @Image1 (identity+wardrobe) | @Image2 (framing/scene) |
|---|---|---|---|---|
| 1 | `scene01_room.png` | GPT Image 2 / Nano Banana | — | — |
| 2 | `wow_look1.png` | GPT Image 2 | Look-1 sheet | `scene01_room.png` |
| 3 | `tap_look1.png` | GPT Image 2 | Look-1 sheet | `wow_look1.png` |
| 4 | `wow_look2.png` | GPT Image 2 | Look-2 sheet | `scene01_room.png` |
| 5 | `tap_look2.png` | GPT Image 2 | Look-2 sheet | `wow_look2.png` |
| 6 | `wow_look3.png` | GPT Image 2 | Look-3 sheet | `scene01_room.png` |
| 7 | `tap_look3.png` | GPT Image 2 | Look-3 sheet | `wow_look3.png` |
| 8 | Seedance Look 1 | Seedance 2.0 i2v | first=`wow_look1.png` · last=`tap_look1.png` | |
| 9 | Seedance Look 2 | Seedance 2.0 i2v | first=`wow_look2.png` · last=`tap_look2.png` | |
| 10 | Seedance Look 3 | Seedance 2.0 i2v | first=`wow_look3.png` · last=`tap_look3.png` | |

Montage + hard-cut swaps + music/SFX + logo = CapCut. Floating items + supers = AE.

Sheet paths (folder `/Volumes/WONYOUNG/Dokkeaw/vid04/`):
- Look 1 = `ChatGPT Image Jul 10, 2026, 04_56_04 PM.png`
- Look 2 = `ChatGPT Image Jul 10, 2026, 12_03_35 PM.png`
- Look 3 = `ChatGPT Image Jul 10, 2026, 05_28_40 PM.png`

---

## 3) SCENE PLATE — `scene01_room.png`

```
Photorealistic interior photograph of a bright, airy mid-century-modern styling room, completely empty with NO people. Warm cream and off-white walls, generous open center floor left clear for a person to stand full-length. Props arranged toward the edges: a sculptural curved wavy-arc accent floor lamp screen-left, one small colourful accent stool (soft coral), a low rectangular glass coffee table, a light-wood open shelf holding a few tasteful objects (a ceramic vase, a couple of books, a small sculpture), and a leafy potted plant in a corner. Subtle soft-lavender accents in the styling (a cushion, a vase). Soft diffused daylight entering from a large window at screen-left, gentle falloff to screen-right. Pale glossy light-wood floor with a faint soft reflection. Vertical 9:16, eye-level camera, wide clean composition, calm upmarket editorial fashion mood, natural realistic lighting and materials.
No brand marks, no signage, no screens. no text, no captions, no logos, no watermarks anywhere in the image.
```

---

## 4) STILLS

### LOOK 1 — `wow_look1.png` (FIRST) · @Image1=Look-1 sheet · @Image2=`scene01_room.png`
```
Match the two attached references exactly. @Image1 = the SAME person and the SAME uniform — copy her face and outfit exactly. @Image2 = the exact room she stands in — copy it exactly, same layout and light.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-1 uniform: soft light lavender matte fabric; a rounded PETER-PAN collar (two soft circular collar leaves lying flat on the chest, closed high at the neck, NO lapel and NO V-opening, fine piping along the curved edge); short sleeves with a turned-up cuff; single-breasted front with 5 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching lavender knee-length pencil skirt; white ballet flats with a small toe-bow. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): standing full-length in the centre of the room, just arrived in a new outfit, delighted and pleasantly surprised — eyes widened, bright open genuine smile, chin dipped slightly as she glances down at her own outfit while her eyes flick up toward camera, both hands lifted a little away from her sides, her left hand lightly touching the Peter-Pan collar. Weight even, feet together.
Framing: full-length, eye-level, static camera, subject centred, whole room and floor visible. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
No floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

### LOOK 1 — `tap_look1.png` (LAST) · @Image1=Look-1 sheet · @Image2=`wow_look1.png`
```
Match the two attached references exactly. @Image1 = the SAME person and SAME uniform — copy face and outfit exactly. @Image2 = keep the EXACT same room, camera position, full-length framing, body scale and lighting as this image — only the arms and expression change.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-1 uniform: soft light lavender matte fabric; a rounded PETER-PAN collar (two soft circular collar leaves lying flat on the chest, closed high at the neck, NO lapel and NO V-opening, fine piping along the curved edge); short sleeves with a turned-up cuff; single-breasted front with 5 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching lavender knee-length pencil skirt; white ballet flats with a small toe-bow. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): settled into a confident, poised fashion stance facing camera, calm pleased half-smile. Her RIGHT arm is raised so the hand is at upper-chest-to-chin height, screen-right of centre and about one forearm-length in front of her torso, index finger extended and pressing a single point in EMPTY AIR. Left hand relaxed at her side. Exactly two hands, five fingers each, natural undistorted fingers.
Framing: full-length, eye-level, static camera, subject centred, identical to the reference. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
She presses empty air only — no floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

### LOOK 2 — `wow_look2.png` (FIRST) · @Image1=Look-2 sheet · @Image2=`scene01_room.png`
```
Match the two attached references exactly. @Image1 = the SAME person and the SAME uniform — copy her face and outfit exactly. @Image2 = the exact room she stands in — copy it exactly, same layout and light.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-2 uniform: soft light lavender matte fabric; a CLASSIC NOTCHED TAILORED LAPEL — wide V opening, broad softly-rounded lapel points angling DOWNWARD and outward, clear notch between collar and lapel (calm blazer-style revere); long sleeves with buttoned cuffs; single-breasted front with 4 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching straight-leg lavender trousers with a pressed centre crease; chunky white low-top sneakers. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): standing full-length in the centre of the room, just arrived in a new outfit, delighted and pleasantly surprised — eyes widened, bright open genuine smile, chin dipped slightly as she glances down at her own outfit while her eyes flick up toward camera, both hands lifted a little away from her sides, her left hand lightly touching the open lapel. Weight even, feet together.
Framing: full-length, eye-level, static camera, subject centred, whole room and floor visible. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
No floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

### LOOK 2 — `tap_look2.png` (LAST) · @Image1=Look-2 sheet · @Image2=`wow_look2.png`
```
Match the two attached references exactly. @Image1 = the SAME person and SAME uniform — copy face and outfit exactly. @Image2 = keep the EXACT same room, camera position, full-length framing, body scale and lighting as this image — only the arms and expression change.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-2 uniform: soft light lavender matte fabric; a CLASSIC NOTCHED TAILORED LAPEL — wide V opening, broad softly-rounded lapel points angling DOWNWARD and outward, clear notch between collar and lapel (calm blazer-style revere); long sleeves with buttoned cuffs; single-breasted front with 4 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching straight-leg lavender trousers with a pressed centre crease; chunky white low-top sneakers. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): settled into a confident, poised fashion stance facing camera, calm pleased half-smile. Her RIGHT arm is raised so the hand is at upper-chest-to-chin height, screen-right of centre and about one forearm-length in front of her torso, index finger extended and pressing a single point in EMPTY AIR. Left hand relaxed at her side. Exactly two hands, five fingers each, natural undistorted fingers.
Framing: full-length, eye-level, static camera, subject centred, identical to the reference. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
She presses empty air only — no floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

### LOOK 3 — `wow_look3.png` (FIRST) · @Image1=Look-3 sheet · @Image2=`scene01_room.png`
```
Match the two attached references exactly. @Image1 = the SAME person and the SAME uniform — copy her face and outfit exactly. @Image2 = the exact room she stands in — copy it exactly, same layout and light.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-3 uniform: soft light lavender matte fabric; a SHARP POINTED "BIRD-WING" LAPEL — narrower higher V opening, LONG NARROW SHARP collar points sweeping UPWARD and outward like wings (never downward), high crisp notch, topstitched edges; short sleeves with a turned-up cuff; single-breasted front with 4 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching straight-leg lavender trousers with a pressed centre crease; chunky white low-top sneakers. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): standing full-length in the centre of the room, just arrived in a new outfit, delighted and pleasantly surprised — eyes widened, bright open genuine smile, chin dipped slightly as she glances down at her own outfit while her eyes flick up toward camera, both hands lifted a little away from her sides, her left hand lightly touching the pointed wing lapel. Weight even, feet together.
Framing: full-length, eye-level, static camera, subject centred, whole room and floor visible. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
No floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

### LOOK 3 — `tap_look3.png` (LAST) · @Image1=Look-3 sheet · @Image2=`wow_look3.png`
```
Match the two attached references exactly. @Image1 = the SAME person and SAME uniform — copy face and outfit exactly. @Image2 = keep the EXACT same room, camera position, full-length framing, body scale and lighting as this image — only the arms and expression change.
Subject: a late-20s Western woman, oval face with defined cheekbones and a straight nose, neat low natural double eyelids, dark well-defined straight eyebrows, a small defined cupid's-bow mouth, fair skin with a neutral undertone and real visible pore texture, chin-length dark near-black wavy bob parted slightly off-centre with a few flyaway strands, slim build; natural facial asymmetry, unretouched skin, no beauty-filter gloss.
Wearing Look-3 uniform: soft light lavender matte fabric; a SHARP POINTED "BIRD-WING" LAPEL — narrower higher V opening, LONG NARROW SHARP collar points sweeping UPWARD and outward like wings (never downward), high crisp notch, topstitched edges; short sleeves with a turned-up cuff; single-breasted front with 4 silver faceted domed buttons; princess seams; two lower hip patch pockets; matching straight-leg lavender trousers with a pressed centre crease; chunky white low-top sneakers. Lavender shade: soft light lavender / pale periwinkle, matte — cool but not blue, not lilac-grey, not purple.
Pose (frozen, holdable): settled into a confident, poised fashion stance facing camera, calm pleased half-smile. Her RIGHT arm is raised so the hand is at upper-chest-to-chin height, screen-right of centre and about one forearm-length in front of her torso, index finger extended and pressing a single point in EMPTY AIR. Left hand relaxed at her side. Exactly two hands, five fingers each, natural undistorted fingers.
Framing: full-length, eye-level, static camera, subject centred, identical to the reference. Soft window light from screen-left.
Photorealistic fashion advertising still, natural skin texture with visible pores and natural asymmetry, a few flyaway hairs, unretouched, no beauty-filter gloss. Vertical 9:16.
She presses empty air only — no floating objects, no cards, no hangers, no accessories, no UI, no sparkle. no text, no captions, no logos, no watermarks anywhere in the image.
```

---

## 5) SEEDANCE i2v (motion-only · first=wow · last=tap · ~3–4s · camera locked no zoom)

### LOOK 1 (first=`wow_look1.png` · last=`tap_look1.png`)
```
Animate this still with smooth, steady, minimal motion. She holds her delighted surprised reaction for a moment — bright smile, a small pleased breath — then eases down from the raised-hands reaction and settles into a confident, poised fashion stance. In one calm continuous move her right arm lifts so the hand reaches up to upper-chest-to-chin height, screen-right, and her index finger presses a single fixed point in empty air; she holds there on the final frame. Left hand relaxed at her side throughout. Gentle natural micro-movement in hair and posture only.
Keep her exact face, chin-length dark wavy bob, and the Look-1 lavender uniform (Peter-Pan collar, short turned-up cuffs, 5 silver buttons, knee-length pencil skirt, white ballet flats) identical throughout; lavender shade unchanged, fabric clean and undistorted.
Hands: the right hand performs the single air-tap with the index finger extended, pressing one fixed point; the left hand stays relaxed. Exactly two hands, five fingers each, no second or third hand, no extra or warped fingers, slow and steady. She presses EMPTY AIR — do not render any floating object, card, hanger, accessory, sparkle, flash, dissolve, or UI.
Camera: locked, static, eye-level, no zoom, no push-in, no shake.
Sound: upbeat fashion music bed, a soft cloth whoosh as she settles, a crisp tap click on the finger press. No voice, no dialogue.
Avoid: identity drift, warped face, melting or morphing fabric, in-clip outfit change, colour shift, extra or missing limbs/fingers, floating objects, jitter, smearing.
```

### LOOK 2 (first=`wow_look2.png` · last=`tap_look2.png`)
```
Animate this still with smooth, steady, minimal motion. She holds her delighted surprised reaction for a moment — bright smile, a small pleased breath — then eases down from the raised-hands reaction and settles into a confident, poised fashion stance. In one calm continuous move her right arm lifts so the hand reaches up to upper-chest-to-chin height, screen-right, and her index finger presses a single fixed point in empty air; she holds there on the final frame. Left hand relaxed at her side throughout. Gentle natural micro-movement in hair and posture only.
Keep her exact face, chin-length dark wavy bob, and the Look-2 lavender uniform (classic notched tailored lapel (wide V, broad rounded points angling DOWN), long sleeves, 4 silver buttons, straight-leg lavender trousers with a pressed crease, chunky white low-top sneakers) identical throughout; lavender shade unchanged, fabric clean and undistorted.
Hands: the right hand performs the single air-tap with the index finger extended, pressing one fixed point; the left hand stays relaxed. Exactly two hands, five fingers each, no second or third hand, no extra or warped fingers, slow and steady. She presses EMPTY AIR — do not render any floating object, card, hanger, accessory, sparkle, flash, dissolve, or UI.
Camera: locked, static, eye-level, no zoom, no push-in, no shake.
Sound: upbeat fashion music bed, a soft cloth whoosh as she settles, a crisp tap click on the finger press. No voice, no dialogue.
Avoid: identity drift, warped face, melting or morphing fabric, in-clip outfit change, colour shift, extra or missing limbs/fingers, floating objects, jitter, smearing.
```

### LOOK 3 (first=`wow_look3.png` · last=`tap_look3.png`)
```
Animate this still with smooth, steady, minimal motion. She holds her delighted surprised reaction for a moment — bright smile, a small pleased breath — then eases down from the raised-hands reaction and settles into a confident, poised fashion stance. In one calm continuous move her right arm lifts so the hand reaches up to upper-chest-to-chin height, screen-right, and her index finger presses a single fixed point in empty air; she holds there on the final frame. Left hand relaxed at her side throughout. Gentle natural micro-movement in hair and posture only.
Keep her exact face, chin-length dark wavy bob, and the Look-3 lavender uniform (sharp pointed "bird-wing" lapel with long narrow points sweeping UP like wings, short turned-up cuffs, 4 silver buttons, straight-leg lavender trousers with a pressed crease, chunky white low-top sneakers) identical throughout; lavender shade unchanged, fabric clean and undistorted.
Hands: the right hand performs the single air-tap with the index finger extended, pressing one fixed point; the left hand stays relaxed. Exactly two hands, five fingers each, no second or third hand, no extra or warped fingers, slow and steady. She presses EMPTY AIR — do not render any floating object, card, hanger, accessory, sparkle, flash, dissolve, or UI.
Camera: locked, static, eye-level, no zoom, no push-in, no shake.
Sound: upbeat fashion music bed, a soft cloth whoosh as she settles, a crisp tap click on the finger press. No voice, no dialogue.
Avoid: identity drift, warped face, melting or morphing fabric, in-clip outfit change, colour shift, extra or missing limbs/fingers, floating objects, jitter, smearing.
```

---

## 6) QA HOOKS (freeze-frame every gen)
1. **Hands (#1):** right hand taps only, index extended, one fixed point; left relaxed; exactly 2 hands/5 fingers; no 2nd/3rd hand, no warp.
2. **Bottoms/feet:** L1 skirt flat + ballet flats w/ toe-bow; L2&L3 trousers pressed crease + chunky sneakers. No shoe swap/melt.
3. **Face drift:** tap frame vs wow frame — no feature/age shift, bob + brows consistent.
4. **Lavender lock:** 3 clips side by side = one shade, no blue/grey/purple drift.
5. **No in-clip zoom / no in-clip outfit change** (change only at CapCut cut).
6. **Empty-air:** no floating object/card/sparkle/flash rendered by Seedance.
7. **Collar/buttons per look:** L1 Peter-Pan+5 · L2 notched-open+long+4 · L3 pointed-wing+short+4. Reject drift.

---

## EDIT (CapCut/AE — not Seedance)
- AE: floating items (garment/accessory/UI) tapped into being on the fixed tap-plane · product supers if wanted
- CapCut: intro card "Dokkaew Workday Styling" · hard-cut swaps (tap→cut→wow) · fast montage 16-20s · music + SFX (tap click, whoosh) · hard-cut end logo (ดอกแก้ว + ผ้าวาเลนชีลด์ + "ชิลทุกที่ที่มีเรา")
- NO VO anywhere.

---

# ⭐ MARCO FREESTYLE — posing clips (13 ก.ค., แทน per-clip แบบสั่งละเอียด)

หลัก = [[seedance-marco-freestyle-method]] — **set the RULES not the SHOTS**. สั่ง shot-by-shot ละเอียด = "the AI tell" (ช้า แข็ง). ปล่อยให้ Seedance เลือกมุม/ท่าเอง → ธรรมชาติ + ได้มุมแปลกที่เราไม่เขียนเอง.
- ใช้กับ **ช่วงใส่ชุดแล้วโพส (ลุค 1-3)** เท่านั้น — 10 วิ/ลุค, Seedance แตกหลายช็อต/หลายมุมเองใน gen เดียว → ตัดเลือกใน CapCut
- ❌ **ห้ามใช้กับ** ช่วงเปิดตู้ / ปัด / กดจิ้ม — AE ต้อง track จุดจิ้ม ต้องล็อกมือ+เฟรม (ใช้ i2v first+last แบบเดิม)
- **ไม่ over-specify** (ไม่ต้องบอกว่าหน้าคนอยู่ช่องไหน ฯลฯ) — โมเดลฉลาดพอ

## CHAR SHEET ใหม่ (erase-face — sheet = garment ref, ไม่แย่ง identity)
| ไฟล์ | ปก | ล่าง | ลุค |
|---|---|---|---|
| `Bua.jpg` | ปกบัว (กลม ปิดคอ ไม่มี V) | กระโปรง | Look 1 |
| `Pointy.jpg` | ปกเทเลอแหลม (V กว้าง ปลายชี้ลง) | กางเกง, **แขนยาว** | Look 2 |
| `Nok.jpg` | ปกปีกนก (V แคบ ปลายแหลมเชิดขึ้น) | กางเกง, แขนสั้น | Look 3 |

## PROMPT (2 ref: char sheet + ห้อง) — สลับ Image 1 ต่อลุค ไม่ต้องแก้อย่างอื่น
```
FORMAT
10-second video, 9:16 vertical.

REFERENCE ROLES
Image 1 = the woman and the uniform she wears; full identity from this image, and she wears exactly this piece throughout — collar, cut and colorway from this image.
Image 2 = the room; every shot takes place here.

CAMERA
Handheld on an iPhone 15 Pro, imperfections are present. The camera moves with her, quick and kinetic.

AMBIENCE
A bright styling room in late-morning light. Upbeat, playful, full of life.
AMBIENCE SOUNDS
Environment sound only, no music — quick footsteps, fabric swishing, a small delighted laugh.

SHOTS
Several shots showing the uniform on the woman, both close details and full looks. She is having fun with it — giddy with joy about what she just put on, bouncing, twirling, playing up to the camera, barely still for a second. Snappy pacing, quick bursts of movement. Nothing slow, nothing dreamy.
Rare camera angles.
```
> **v2 (13 ก.ค.) — JOY/ENERGY fix:** v1 ออกมา **อืด** (AMBIENCE "calm, airy" + SHOTS passive "poses freely" → โมเดลเนิบ). แก้โดย **ใส่พลังเป็น "กฎ" ไม่ใช่ choreograph ท่า**: AMBIENCE → upbeat/playful · CAMERA → moves with her, quick and kinetic · SHOTS → giddy with joy/bouncing/twirling + `Snappy pacing` + **`Nothing slow, nothing dreamy.`** (ตัด AI-tell ตรงๆ ตามที่ Marco เตือน) · ห้ามใช้ "fast" (= jitter) → ใช้ snappy/quick bursts/kinetic
> ทางเลือก CAMERA ถ้าอยากคลีนแบบ commercial: `Clean commercial camera, mostly locked and observational; you choose the framing.`

## SCENE PLATE — ห้องโทนขาว (แทนห้อง cream เดิม) — gen ใบเดียว ไม่ต้องแนบ ref
```
Photorealistic interior photograph of a bright, clean, WHITE-toned modern styling room, completely empty with NO people. Crisp white walls, white sheer curtains drifting over a large window at screen-LEFT with soft diffused daylight pouring in, and a pale near-white washed-oak floor with a faint soft reflection. Generous open centre floor left clear for a person to stand full-length.
Minimal light furniture arranged toward the edges: a sculptural curved wavy-arc floor lamp in matte white, a small soft stool in a muted pale lavender, a low glass coffee table, a light open shelf holding a few white and pale-lavender ceramic vases and stacked books, a large soft-pastel abstract artwork on the wall in white and lavender tones, and a leafy potted plant in a corner.
Palette: white on white, with subtle soft-lavender accents only — no warm wood tones, no coral, no strong colour. Airy, luminous, high-key, calm upmarket editorial fashion mood.
Vertical 9:16, eye-level camera, wide clean composition, natural realistic lighting and materials — real matte paint, real fabric, real ceramic, no CGI look, no plastic sheen.
No brand marks, no signage, no screens. no text, no captions, no logos, no watermarks anywhere in the image.
```

---

## 🎚️ MARCO PROMPT — TONE LADDER (เก็บทุกเวอร์ชัน อย่าลบ)

ปรับ "พลัง" ของ Marco prompt = แตะแค่ **AMBIENCE + CAMERA + SHOTS** (ไม่แตะ REFERENCE ROLES / FORMAT)

| ver | tone ที่สั่ง | ผลจริง |
|---|---|---|
| **v1** | `Calm, airy, lived-in` + `poses freely` | ❌ **อืด** เนิบ ไม่มีพลัง |
| **v2** | `upbeat, playful, full of life` + `giddy with joy, bouncing, twirling` + `Snappy pacing` | ❌ **ร่าเริงเกิน** ดูเป็นคลิปเด็ก ไม่ใช่ ads |
| **v3** ✅ | `light, warm, effortless` + `easy confidence` + `never sluggish, never dreamy, never giddy or hyper` + **"garment is the subject"** | ✅ **ฟีล ads ขายชุด** พอดี |

> บทเรียน: prompt โฆษณาเสื้อผ้า **ต้องมีบรรทัดบอกว่า "ชุดคือพระเอก"** — v1/v2 ลืม ทำให้โมเดลโฟกัสที่ตัวคน/อารมณ์แทนที่จะเป็นชุด
> คุมพลังด้วย **balance line เดียว** (`never sluggish, never dreamy, and never giddy or hyper`) แทนการสั่งท่า — ยังอยู่ในหลัก Marco (set the rules, not the shots)

### ⭐ v3 — ADS TONE (ใช้ตัวนี้)
```
FORMAT
10-second video, 9:16 vertical.

REFERENCE ROLES
Image 1 = the woman and the uniform she wears; full identity from this image, and she wears exactly this piece throughout — collar, cut and colorway from this image.
Image 2 = the room; every shot takes place here.

CAMERA
Handheld on an iPhone 15 Pro, imperfections are present. The camera stays with her and moves naturally.

AMBIENCE
A bright styling room in late-morning light. Light, warm, effortless.
AMBIENCE SOUNDS
Environment sound only, no music — soft footsteps, fabric moving.

SHOTS
This is a fashion advert for the uniform — the garment is the subject; its collar, buttons, fabric and cut read clearly in every shot.
Several shots showing the uniform on the woman, both close details and full looks. She wears it with easy confidence — light on her feet, moving between poses, a natural smile, comfortable and pleased with the fit.
Keep it alive and effortless: never sluggish, never dreamy, and never giddy or hyper.
Rare camera angles.
```

### v1 — CALM (เก็บไว้อ้างอิง, ออกมาอืด)
```
CAMERA
Handheld on an iPhone 15 Pro, imperfections are present.

AMBIENCE
A bright quiet styling room in late-morning light, soft daylight through sheer curtains. Calm, airy, lived-in.
AMBIENCE SOUNDS
Environment sound only, no music.

SHOTS
Several shots showing the uniform on the woman, both close details and full looks. She poses freely, alive and pleased with what she is wearing.
Rare camera angles.
```
> (v2 = บล็อก MARCO FREESTYLE ด้านบน — energy สูง ร่าเริงเกินสำหรับ ads)
