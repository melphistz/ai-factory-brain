---
name: ai-influencer-image-prompt
aliases:
  - seedance-ugc-image-prompt
description: "How to generate very realistic AI influencer / virtual-model images that don't look AI"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# AI Influencer Image — ทำภาพคนปลอมให้เหมือนจริงสุด

> วิธีสร้างภาพ AI influencer / virtual model ให้ดูเป็นรูปถ่ายจริง ไม่ใช่ AI.
> ใช้ภาพที่ได้เป็น **reference image** ป้อนเข้า Seedance → คุมหน้า/ลุค (ดู blur face trick ใน [[seedance-ugc-repository]]).
> คู่กับ [[seedance-knowledge]] (สูตรวิดีโอ). เก็บ มิ.ย. 2026

## โมเดลภาพที่จริงสุด 2026 (เลือกถูกตั้งแต่ต้น)
| Model | จุดเด่น |
|---|---|
| **FLUX.2 / FLUX.2 Pro** | skin texture, lighting physics, fine detail — hero shot/final asset. คุ้มราคา (~$0.035) |
| **Imagen 4 / 4 Ultra** | ลุค "รูปถ่ายดิบไม่ผ่านแต่ง" ธรรมชาติสุด, pore-level + subsurface scattering |
| **Nano Banana Pro** | realism + identity consistency + แก้ภาพ (ผ่าน Higgsfield/Gemini) — คนเหมือนจริงสุดสำหรับ human |
| **Seedream 4.5** | commercial/product, native 4K (แต่ skin micro-detail สู้ FLUX/Imagen ไม่ได้, lighting อุ่นเป็นหนัง) |
| Midjourney v6.1 `--style raw` | concept/mood เร็ว, ธรรมชาติกว่า default |

## 🎯 เลือกโมเดลตามงาน (PRACTICAL — สำคัญกว่า benchmark ผิวล้วน)
> ⚠️ แก้ความเข้าใจเดิม: FLUX ชนะ "ผิวสวยสุด" จริง **แต่ไม่ใช่ตัวเลือกที่ดีสำหรับ AI influencer** เพราะแพ้ 2 เรื่องที่สำคัญกว่า:
> identity consistency (หน้าเดิมหลายภาพ) + platform-flag risk (โดน Meta/Pinterest แปะ AI throttle)

**125-prompt benchmark (May 2026) — score ยิ่งต่ำยิ่งดี:**
| Model | plastic skin | identity drift | หมายเหตุ |
|---|---|---|---|
| **GPT Image 2** | 18% | **6%** ✅ | หน้าเดิมแม่นสุด → ตัวเลือกหลัก AI influencer series · เก่ง text/layout/character grid |
| **Nano Banana Pro** | 14% | 9% | balance ดีสุด + cinematic light + แต่งภาพง่าย + prompt น้อยก็ได้ลุค commercial |
| **FLUX 2 Pro** | **12%** ✅ | 22% ❌ | ผิวดีสุด แต่หน้า drift + **platform-flag risk 47%** (โดน throttle เกือบครึ่ง) → เลี่ยงสำหรับ social |
| Midjourney v8.1 | 31% | 38% | แพ้ทั้งคู่ |

**สรุปเลือก:**
- **หน้าเดิมหลายภาพ (influencer series)** → **GPT Image 2** (drift 6%) หรือ **Nano Banana Pro**
- **อยู่ใน ChatGPT สะดวก + text/layout** → GPT Image 2
- **portrait สวย + cinematic light + แต่งภาพ conversational** → Nano Banana Pro (Higgsfield/Gemini)
- **hero shot เดี่ยว เน้น pore สุด ไม่ลง social / ไม่ต้องหน้าเดิม** → FLUX 2 Pro (ระวัง flag)
- **ทำไมคนไม่ค่อยใช้ FLUX:** identity drift สูง + โดน platform flag + ไม่มี chat-edit ในตัว → creator เลย Nano Banana / GPT Image 2

**Nano Banana Pro — tips เฉพาะ:**
- default tonality เป็น commercial-grade อยู่แล้ว → **prompt น้อยก็พอ** อย่าใส่ mood word ("beautiful/cinematic") มันดันไปทาง AI generic
- identity: อัป **3–5 ref หลายมุม** (รับได้ถึง 14 ref) + **label role**: "the face in image 1, outfit from image 3, location in image 5"
- เก่ง `subsurface scattering, micro-roughness, specular highlights` — ใช้ภาษา physical เจาะจง

แนวใช้ (เดิม — สำหรับ raw skin quality): FLUX = hero/final, Midjourney = explore mood เร็ว — **แต่สำหรับ influencer ใช้ GPT Image 2 / Nano Banana Pro ตามตารางบน**

## ⚠️ คำที่ "ฆ่า" ความสมจริง (ห้ามใช้)
- ❌ `hyperrealistic, ultra-detailed, 8K, masterpiece` — tag พวกนี้ correlate กับ ArtStation render ใน training data ไม่ใช่รูปถ่าย → ดันเป็นลุค digital-art over-rendered
- ❌ hyper-saturated, neon, cartoon grading
- ❌ ผิวเนียนไม่มี texture = plastic/waxy skin (AI tell อันดับ 1)

## 8-Category Realism Framework (สูตรหลัก)
1. **Realism triggers:** `photorealistic, real-world photography, cinematic realism, lifelike details, natural imperfections, true-to-life textures, realistic skin`
2. **Camera/lens:** `DSLR photography, mirrorless, documentary-style, editorial portrait, street photography` + lens: `35mm` (natural สุด) / `50mm` (ใกล้ตามนุษย์) / `85mm` (หน้า/headshot) + `shallow depth of field, natural bokeh, shot on 85mm f/1.8`
3. **Lighting:** `natural light, soft window light, golden hour sunlight, overcast daylight, practical lighting, studio softbox, subtle rim light, realistic shadows`
4. **Texture/imperfection:** `visible pores, skin micro-details, fabric grain, slight imperfections, peach fuzz, tiny undereye creases, flyaway hairs, slight asymmetry`
5. **Color/tone:** `natural colour grading, muted tones, earthy palette, realistic contrast, soft highlights and deep shadows`
6. **Composition:** `rule of thirds, eye-level shot, candid moment, unstaged composition, over-the-shoulder angle`
7. **Film grain/quality:** `subtle film grain, cinematic grain, high dynamic range, sharp focus, clean but not overly polished, sensor noise in shadows`
8. **Negative:** `no cartoon, no CGI, no 3D render, no game engine, no plastic skin, no unrealistic lighting, no text, no logo, no watermark`

## 🔑 Power keywords (leverage สูงสุด)
- **`sub-surface scattering`** — ศัพท์เทคนิคแสงทะลุผิว → ได้ผิวโปร่งแสงแบบจริง
- **`Kodak Portra 400`** (หรือ film stock อื่น) — implies natural color grading + film-like
- **combo เด็ด:** `Kodak Portra 400, film grain, pore-level skin texture, subsurface scattering`
- **`shot on iPhone` / `everyday photo using iPhone`** — ดัน casual/real ทันที (สำหรับ UGC/selfie)
- **`street casting`** — ได้คนธรรมดา ไม่ใช่ลุคนางแบบ

## Skin realism — บทเรียนจาก deep-dive (Midjourney แต่ใช้ได้ทุกโมเดล)
**ได้ผลจริง:**
- `natural skin, unretouched, slight skin imperfection` — balance ดีไม่เวอร์
- `everyday photo using iPhone, street casting, natural skin` — portrait น่าเชื่อ
- `a bit overweight, baggy eyes, normal looking` — เพิ่มความ relatable/จริง
- `wrinkles` เดี่ยวๆ เพิ่ม character
- High-key lighting (ลดเงาเทียม) + plain white background

**ได้ผลน้อย/ไม่ค่อยติด:** `detailed skin` (texture เยอะเกิน), `visible skin pores` (ผลน้อยใน MJ — แต่ FLUX/Imagen ติด), `acne` (ไม่ค่อยติด)

**ระวัง:** `slight rosacea` / `natural discoloration` → เพิ่มความแก่เกินตั้งใจ
**หลักทอง:** ใช้ 2–3 descriptor ที่เสริมกัน ดีกว่าซ้อนเยอะ (restraint)

## Character/identity consistency (หน้าเดิมทุกภาพ — โจทย์ยากที่สุด)
> 1 หน้าจริงง่าย — หน้าเดิม 50 ภาพคือของจริง (สำคัญสุดสำหรับ AI influencer/brand)
- โมเดลทั่วไปไม่มี identity-preservation → หน้า drift ทุก gen
- **เครื่องมือเฉพาะ:** Nano Banana Pro, Morphed AI influencer studio, Melies, Ideogram Character, getimg.ai Elements — lock หน้าข้ามฉาก
- **Training-based (SOUL ID, Person Elements):** อัป **10+ ภาพ** (5–10 ครอบคลุมส่วนใหญ่) → train avatar → gen ได้ทุก pose/expression/lighting หน้าคงที่
- ยิ่งให้ reference เยอะ → face shape/skin tone/hair แม่นขึ้น

---

## ตัวอย่าง prompt เต็ม

**Formula example (สูตรรวมทุก category):**
```
Ultra-realistic cinematic photography of a female model, shot on a 35mm lens with
natural daylight lighting, realistic shadows, shallow depth of field, true-to-life
textures, visible skin imperfections, subtle film grain, natural colour grading.
No cartoon style, no plastic skin.
```

**Editorial flash close-up (skin texture เน้นสุด):**
```
Hyper-realistic close-up editorial flash portrait of a woman seated at a restaurant
table, on-camera flash technique, refined jewelry, ultra-realistic skin texture
including pores, peach fuzz, tiny undereye creases, 85mm lens, shallow depth of
field, subtle film grain. No plastic skin, no CGI.
```

**Phone selfie (UGC-ready, casual):**
```
Ultra-realistic selfie-style portrait of a young woman leaning toward the camera in
a modern bathroom, close upward angle, soft glam makeup, shot on iPhone, natural
skin, unretouched, slight skin imperfection, natural available light, candid intimate
phone selfie. No plastic skin, no logo.
```

**Golden hour editorial (lifestyle/แบรนด์):**
```
Hyper-realistic upper body portrait at golden hour in a tropical setting, warm rim
lighting, emerald foliage background, Kodak Portra 400, film grain, pore-level skin
texture, subsurface scattering, 85mm f/1.8, natural bokeh, luxury candid editorial.
No cartoon, no plastic skin.
```

**Street casting realism (คนธรรมดาน่าเชื่อ):**
```
Documentary-style street photograph of a 30-year-old woman, street casting, everyday
photo, natural skin, slight imperfection, baggy eyes, normal looking, 35mm lens,
overcast daylight, candid unstaged composition, subtle film grain. No plastic skin,
no retouching.
```

---

## Workflow: ภาพ → วิดีโอ Seedance
1. gen ภาพ AI influencer ด้วย FLUX/Imagen/Nano Banana Pro ตาม framework บน
2. lock หน้าด้วย identity tool หรือ train 10+ ภาพ (ถ้าต้องหลายภาพ)
3. เบลอหน้าก่อนอัปเข้า Seedance (blur face trick — [[seedance-ugc-repository]])
4. ใช้เป็น @Image1 reference ใน Seedance prompt → วิดีโอ UGC หน้าเดิม

## เช็กลิสต์ก่อน gen ภาพ
- [ ] เลือกโมเดลถูก (FLUX/Imagen สำหรับ human realism)?
- [ ] **ตัด** `8K, hyperrealistic, masterpiece` ออกหมด?
- [ ] มี camera + lens + film stock (35/50/85mm, Kodak Portra 400)?
- [ ] มี skin imperfection 2–3 ตัว (pores/peach fuzz/unretouched/slight asymmetry)?
- [ ] มี `subsurface scattering` ถ้าเน้น close-up?
- [ ] lighting ธรรมชาติ + negative prompt (no plastic skin/CGI)?
- [ ] identity plan ถ้าต้องหน้าเดิมหลายภาพ?

---

## ⭐⭐ "Real iPhone" realism formula (พิสูจน์แล้ว — เนียนสุด) — AI Video Bootcamp prompt pack
> ชุดนี้ให้ผลเนียนกว่า golden-hour-dreamy เยอะ. **แก้ที่ผมพลาดตอนแรก:** dreamy glow + film grain = cinematic เกิน → ของจริงคือ **harsh light + phone mechanics + compression + imperfection stack**

### Universal realism add-on (ต่อท้าย prompt ใดก็ได้ — reusable สูงสุด)
**เวอร์ชัน A:**
```
Make it look like an ordinary real iPhone photo uploaded to Instagram, imperfect framing, visible pores, flyaway hairs, natural facial asymmetry, slight motion blur, phone HDR, compression artifacts, uneven lighting, no beauty retouching, no professional studio setup, no cinematic colour grading.
```
**เวอร์ชัน B (selfie):**
```
Real iPhone front camera photo, slight lens distortion, imperfect framing, casual arm-length selfie, harsh natural light or direct phone flash, visible pores, real skin texture, flyaway hairs, tiny blemishes, natural asymmetry, mild compression, slight noise in shadows, unedited Instagram photo, not cinematic, not a studio photoshoot, not airbrushed, not perfect.
```

### Negative prompt (pattern ใช้ทุกอัน)
```
studio lighting, perfect skin, airbrushed face, plastic texture, over-smoothed, cinematic portrait, professional camera, perfect symmetry, waxy skin, CGI, doll-like face, fantasy lighting, over-retouched, text, watermark
```

### Levers ที่ทำให้เนียน (ต่างจาก cinematic)
1. **aspect 4:5** (Instagram) — ไม่ใช่ 9:16
2. **เรียกชื่อ phone mechanics:** `iPhone front camera, 24mm equivalent`, `arm's length`, `slightly high/low angle`, `wide-angle selfie distortion`, `phone HDR`, `compression artifacts`, `noise in shadows`, `arm partially visible in foreground`, `slightly tilted horizon`
3. ⭐ **harsh light ไม่ใช่ dreamy** — `harsh direct iPhone flash` หรือ `harsh midday sun` → strong contrast/shadow. **dreamy golden glow = AI tell** (ที่ผมพลาด)
4. **imperfection stack:** visible pores · flyaway hairs · **natural facial asymmetry** · under-eye texture/shadows · oily/shine forehead · freckles · tiny blemishes · redness around nose
5. **mundane real settings ดีกว่าสวยเวอร์:** convenience store fridge · airport/stairwell · ferry deck · car seat · gym · sidewalk — ที่ธรรมดา = เชื่อ
6. **`compressed social media photo` / `unedited Instagram photo`** — compression = realism signal
7. **expression candid:** winking, kissy pout, looking off-camera, "not posing too hard"

### โครง prompt (ตามแพตเทิร์น 20 prompt ในชุด)
`[Ultra-realistic + iPhone camera type + aspect] + [subject + พฤติกรรม candid] + [เสื้อผ้า/jewelry เจาะจง] + [skin imperfection stack] + [mundane background เจาะจง] + [harsh light description] + [phone mechanics + compression] + [negative]`

> source = AI Video Bootcamp prompt pack (Google Doc) — ผลลัพธ์จริงเนียนระดับแยกจากคนจริงไม่ออก

## 💎 Beautiful-but-real dial (✅ verified มิ.ย. 2026)
> ปัญหา: ดันสวย → ผิวเนียน glossy = AI tell. ดันจริง → unflattering. **dial นี้ได้ทั้งคู่** (พิสูจน์แล้ว Japanese indoor)
- คง **ความสวย:** warm ambient light + subtle makeup + glossy lips + หน้า idealized
- **ถ่วงกลับให้จริง:** `visible pores, fine skin texture, subtle T-zone shine on forehead and nose, faint under-eye texture, flyaway hairs, natural facial asymmetry, unretouched, soft HDR but NOT over-smoothed` + expression `candid, not posing too hard`
- **negative อัด:** `poreless airbrushed face, beauty filter, glamour glow, doll-like, flawless symmetry, waxy over-smoothed skin, overprocessed HDR`
- **dial:** เนียนไป → เพิ่ม `visible pores` / `older iPhone, mild sensor noise` · สวยไป → ลด imperfection

**Realism spectrum (เลือกตามงาน):**
`gritty-real (conv-store, unaware/unflattering) → real-pretty (beautiful+imperfection ⬆) → glossy-pretty (AI-beauty, สวยแต่เพ่งรู้) → editorial (polished pro)`
- งานต้อง undetectable → ซ้ายสุด · โฆษณาสวย → กลาง-ขวา

## 🥇 Next-level realism (tier บนสุด — "accidental/unaware" levers) ⭐⭐⭐
> รูปที่จริงที่สุดที่เจอ (Korean convenience-store candid). lever พวกนี้เหนือ "clean iPhone" ปกติ — ใช้เมื่อต้อง "แยกจากคนจริงไม่ออก 100%"

1. ⭐⭐ **unposed/unaware** — `accidental candid, completely unaware of the camera, not posing, spontaneous everyday moment` → ฆ่า AI tell "โพสกล้อง" ที่ใหญ่สุด
2. ⭐ **unflattering mundane action** — `wiping sweat from forehead, slightly impatient distracted expression, subtle facial shine from indoor warmth` → ยอมให้ดู "น่าเกลียดนิดๆ/เหนื่อย" = จริง (รูปอื่นพยายามสวย = AI tell)
3. **older phone** — `authentic smartphone image quality from an older iPhone` → sensor แย่ลง จริงขึ้น (ไม่ pristine)
4. **older-phone artifacts** — `mild sensor noise, compressed detail, slight motion blur on the moving hand, imperfect framing`
5. ⭐⭐ **random accidental element** — ของหลุดเฟรมแบบสุ่ม เช่น `a small guinea pig barely visible near the bottom corner, appearing accidentally included` → **ไม่มีใคร AI เจนของแปลกตั้งใจ** = สมองอ่านว่าจริงทันที
6. **ugly-real color cast** — `bright overhead fluorescent lighting, cool-toned shadows, faint yellow-green store color cast` (ไม่ใช่สีสวย)
7. setting มุนแดนจริง + คน distracted (checkout line, reading a label, squatting at shelf)

> tier นี้ = candid-real สุดทาง. ตรงข้าม editorial. ใช้กับงานที่ realism สำคัญกว่าสวย

## 🕹️ Style variant: Y2K / digicam ยุค 2000s (MySpace/Tumblr energy)
> core anti-AI เหมือน "clean iPhone" ด้านบน (pores, asymmetry, imperfect framing, harsh flash) แต่ lever เฉพาะยุค → ลุค 2000s digicam

**levers ที่ต่างจาก iPhone-modern:**
1. **กล้อง = compact digital camera / point-and-shoot ยุคเก่า** (ไม่ใช่ iPhone) → `older digital camera, compact point-and-shoot`
2. **direct on-camera flash เป็นหลัก** → `harsh flash, crushed black background, overexposed skin highlights, hard shadow falloff, harsh flash shadow edges`
3. **color/texture ยุค:** `warm colour cast, saturated Y2K colour, high contrast, mild grain, uneven exposure` → ระบุ `MySpace/Tumblr/Y2K digital camera photo`
4. **Y2K styling:** low-rise jeans, baby/angel-graphic tank, chain belt, wraparound/narrow rectangular sunglasses, leg warmers, charm bracelets, layered gold/silver, butterfly clips
5. **cluttered nostalgic settings** (background chaos = realism): laundromat · vintage record/CD store · gamer bedroom (toys/figures) · dark football pop-up · tiled cafe corner
6. **`leave clean space for bold white text overlay`** — สำหรับ carousel ad slide (แบบ "Comment Y2K for the prompts")

### Global negative (ครบกว่าตัวบน — ใช้แทนได้)
```
No plastic skin, no waxy face, no airbrushed model look, no perfect symmetry, no overly clean studio lighting, no CGI background, no fake hands, no extra fingers, no distorted jewellery, no unreadable AI text, no fake logos, no celebrity likeness, no fashion editorial polish, no beauty campaign lighting, no over-smoothed skin, no cartoonish proportions, no sterile room, no grid, no collage.
```
> เพิ่มจากตัวบน: **no fake hands / extra fingers / distorted jewellery / celebrity likeness / grid / collage** — กันจุดพังที่เจอบ่อย

## 🧱 Reusable building blocks + formula (modular — ใช้กับทุก preset) ⭐⭐⭐
> ดีสุดในชุด — paste บล็อกพวกนี้ลง prompt ไหนก็ได้

**Prompt formula:**
`[style] + [adult woman/man in their 20s] + [scene] + [outfit] + [prop] + [pose/framing] + [lighting] + [realism details] + [camera feel] + [no text]`

**Skin block (paste ได้ทุก prompt):**
```
realistic skin texture with visible pores, subtle freckles, natural tonal variation, soft shine, natural lip texture, minimal makeup, and true-to-life complexion
```
**Hair block:**
```
natural hair texture with soft flyaways, subtle frizz, gentle movement, and believable strand detail
```
**Hands block (⭐ แก้จุดพัง #1 — ใช้เมื่อถือของ: แก้ว/หนังสือ/โทรศัพท์/ช่อดอก):**
```
believable hand proportions, natural finger curvature, realistic grip, and relaxed hand positioning
```
**Quick realism booster (paste ท้าย prompt ไหนก็ได้):**
```
Ultra-photorealistic, 4:5 aspect ratio, adult in their 20s, Instagram aesthetic, natural daylight, realistic skin texture, visible pores, subtle freckles, natural lip texture, soft flyaway hair, believable hand proportions, casual phone-camera framing, slight lens distortion, off-centre composition, natural color grading, true-to-life exposure, no text, no graphics, no watermark
```

**levers ใหม่:**
- ⭐ **"adult woman/man in their 20s"** — ระบุ adult ชัด กันหน้าเด็กเกิน (safety + realism)
- **imperfection > beauty** = realism booster ที่ใหญ่สุด (ไม่ใช่ความสวย)
- **off-centre composition** — เฉพาะเจาะจง สู้ AI symmetry
- **text ทำใน edit** (Canva/Photoshop/CapCut) ไม่ generate — ใส่บางคำหลังตัว บางคำหน้าตัว (ยืนยันกฎเรา)

## 📐 Scaling 1 character → ซีรีส์ (สลับ 3 ตัวแปร)
อย่าซ้ำ coffee+white tank+arm-out ทุกรูป → **สลับ scene + prop + pose พร้อมกัน**
- **scene:** bookstore · flower market · rooftop · clothing store mirror · beach promenade · grocery aisle · balcony · car · hotel hallway · art gallery · airport lounge
- **prop:** book · bouquet · tote · sunglasses · sandals · fruit basket · pastry · smoothie · headphones
- **pose:** arm-length selfie · mirror selfie · turning toward camera · walking glancing back · leaning on railing · chin on hand · adjusting sunglasses · cross-legged
> = วิธีทำ identity pack ให้ออก 15–30 รูปไม่ซ้ำ (เชื่อม modular scaling ใน [[seedance-ugc-repository]])

## 🎥 POV lifestyle format (aspirational realism — high-convert)
นำด้วย `POV / first-person view / looking down / from my perspective` + **โชว์ hands/legs/body** = ขาย realism ทันที. ใส่ lifestyle context เจาะจง (woven basket, cozy slippers, candle) ไม่ใช่แค่ "doing laundry". ฉาก: gym mirror, nails appointment, laundry, laptop work, bath wind-down. palette neutral (beige/cream/wood) = ดู "expensive" + cohesive

## 🎨 3 realism presets (เลือกตามลุค — แกน anti-AI เดียวกัน)
| preset | light | camera | setting |
|---|---|---|---|
| **clean iPhone modern** | harsh sun/flash หรือ natural daylight | iPhone | candid selfie ทั่วไป |
| **Y2K digicam** | on-camera flash + crushed black | compact point-and-shoot | laundromat/record store/2000s clutter |
| **elevated European** | warm ambient/candlelight + bright daylight | iPhone | brasserie/Paris street/café/mirror |
แกนร่วม: imperfection stack + named camera mechanics + off-centre + mundane setting + anti-AI negative

## 🔧 Parameterized prompt template (batch variants เร็ว)
prompt แม่แบบใส่ช่องตัวแปร — สลับค่าได้ไม่ต้องเขียนใหม่ (format ของ tool ที่ fill default):
```
{argument name="hair color" default="dark brown"} ... {argument name="top color" default="black"} ... {argument name="skirt pattern" default="gray-brown plaid pleated skirt"}
```
- ใช้ทำ **variant หลายแบบเร็ว** (สลับผม/เสื้อ/ฉาก)
- ⚠️ **= สร้าง variant ต่างคน ไม่ใช่ identity lock** (หน้าจะต่าง) → หน้าเดิมต้อง reference sheet ([[ai-character-identity-lock]])

**Composition lever (เฉพาะ):** `camera held high above the face, arm extended toward the lower foreground, wide-angle selfie perspective with slight foreshortening of the arm` — มุม selfie ชูสูง แขนยื่น = candid จริง

## 🦴 Anatomy realism negative (universal — เติมได้ทุก lane ไม่ conflict)
> แก้จุดพัง AI ที่เรายังไม่มี: **เอวเล็ก/สะโพกบานเกินจริง (hourglass ปลอม)** — เริ่มเห็นในรูป bikini ที่เอียง model-polished
ใช้เมื่อมี body ในเฟรม (เสริมเข้า negative เดิม):
```
no tiny waist, no unnaturally small abdomen, no exaggerated hourglass figure, no oversized hips, no unnaturally narrow pelvis, no elongated torso, no disproportionate limbs, no doll-like anatomy
```
+ positive เสริม: `healthy naturally proportioned physique, realistic ribcage and waist, believable waist-to-hip ratio, any waist taper from posture/perspective not anatomical distortion`
> ใช้ได้ทั้ง candid และ editorial — เป็นเรื่อง anatomy ไม่ใช่ style จึงไม่ชนกับ lever อื่น

## 🎭 2 lanes อย่าปนกัน (สำคัญ — กัน conflict)
realism มี 2 ทิศ เลือกตาม**เป้าหมาย** อย่าผสม lever ข้ามกัน:
| lane | ลุค | levers | เหมาะ |
|---|---|---|---|
| **Candid-real** (default, undetectable สุด) | "แอบถ่าย IG จริง" | phone HDR, compression, harsh/natural light, imperfect/off-centre framing, **ไม่มี** cinematic grading | UGC, influencer selfie, ของที่ต้อง "แยกจากคนจริงไม่ออก" |
| **Editorial-polished** | "รูปถ่ายแฟชั่นโปร" | 85mm f/2.0, controlled lighting ratio (4:1), diffused window, cinematic color grading, luxury magazine | lookbook, campaign, hero shot สวยคุม |
**กฎกัน conflict:** อย่าเอา `cinematic grading / 85mm / studio lighting` ไปใส่ candid (มันจะดูโปรไม่ใช่แอบถ่าย) · อย่าเอา `phone HDR / compression / imperfect framing` ไปใส่ editorial · ⚠️ ทั้ง 2 lane เลี่ยง `ultra-high detail, flawless, perfect symmetry` เหมือนกัน (AI tell)
> 3 preset ด้านล่าง (clean iPhone / Y2K / elevated) = ทั้งหมดอยู่ใน lane **candid-real**. editorial = lane ที่ 4 แยกต่างหาก

## 🎞️ Cinematic-grade realism levers (editorial/commercial lane — net-new จาก Yapper "Hollywood look" doc)
> เสริมเฉพาะที่ไม่ทับของเดิม. lane = editorial-polished / cinematic (ไม่ใช่ candid iPhone). แก้ "gloss ปลอมของ AI" ด้วย grade+exposure ไม่ใช่ imperfection stack.
1. **opener กัน render:** `grounded live-action cinema frame, flat but cinematic` — ดันเป็น footage จริง ไม่ใช่ digital render
2. **exposure lever:** `underexposed but still readable` — คุมมู้ด/เงา แต่ยังเห็น detail (ต่างจากการดัน bright)
3. **anti-gloss combo:** `muddy colors, soft blacks, controlled contrast` — สู้ความคม/HDR เกินของ AI (คมกว่า "muted tones" เดิม)
4. **motivated lighting** (คม): แสงในเฟรมต้องมีที่มาในฉากจริง (street lamp / dashboard / window) ไม่ใช่แสงลอย
> source: Yapper AI "Master Cinematic AI Realism" (YT `P2890ik3lU8`) + free prompts Google Doc. ที่เหลือในเอกสาร (genre grade/texture/material/negative) ทับ 8-category framework ด้านบนแล้ว. 7 movie style-prompts (Bond/Matrix/Wick/Dunkirk/Dune/Batman/Mad Max) ซ้อน [[director-styles-knowledge]] → ไม่เก็บ.

## 🛏️ Worked example — editorial-real Japanese lifestyle portrait (dual motivated light)
> ตัวอย่างเต็มของ lane **editorial-polished** (ต่างจาก candid ส่วนใหญ่ในไฟล์). เคสจริง: ผู้หญิงญี่ปุ่นนั่งบนเตียงคืนก่อนนอน. โจทย์ = สวย mood แต่ไม่ให้ gloss AI. สูตรที่ใช้ = beautiful-but-real dial + Asian 6-field + named camera/film + anti-gloss grade.

**levers ที่ทำให้เคสนี้เนียน (reusable):**
- **dual motivated light**: cool blue window rim (ผม/ไหล่) + warm lamp fill (แก้ม/ไหปลาร้า/ผ้า) → blend น้ำเงิน-ส้ม = depth + realism ฟรี (แสงมีที่มาในฉากทั้งคู่)
- **beautiful-but-real dial**: คงสวย (blush/gloss lip/soft highlight) + ถ่วง `visible pores, peach fuzz, natural facial asymmetry, subtle T-zone shine, faint under-eye texture, unretouched, soft HDR NOT over-smoothed`
- **face-lock ญี่ปุ่น**: `neat low double eyelid, soft lower nose bridge, warm ivory undertone` + negative `no Westernized/blended features, no big round eyes, no anime`
- **camera จริง**: `85mm f/2.0 medium-telephoto, Kodak Portra 400, fine grain, low-medium contrast, soft blacks, flat but cinematic, no glossy AI sheen`
- **makeup "doll-like" OK แต่ face ห้าม doll-like**: แยกใน negative (`doll-like face, plastic skin` ห้าม / doll-like *makeup* เก็บ)
- **hands block**: five natural fingers + believable proportions + contact shadows where skin/cloth/bed meet (จุดพัง #1)
- aspect **4:5** editorial. safety: ระบุ adult late-20s + negative underage เสมอ
> เต็ม prompt เก็บใน chat นี้. ถ้าจะสลับเป็น candid-real → ตัด Portra/85mm/cinematic ออก ใส่ phone mechanics + compression แทน (ดู lane table ด้านบน).

## 🌏 หน้าเอเชีย/ไทย — สู้ปัญหา model "Westernize หน้า" (addendum)
> pack ฝรั่งทั้งหมดข้างบนใช้ได้ แค่ swap subject + ต้องระบุ feature เอเชียชัด ไม่งั้น model ดันเป็น blended Western-Asian + ผิวซีดเกลี้ยง

### 6-field framework (หน้าเอเชียเสถียร)
1. **เจาะจงประเทศ** — `Thai / Korean / Japanese / Chinese` **ห้ามใช้ "Asian" ลอยๆ** (มัน blend มั่ว)
2. ⭐ **โครงตา** — `soft monolid` / `neat double eyelid` / `slight epicanthic fold` (ไม่ระบุ = ดัน double-lid ฝรั่ง · **ห้าม "big eyes"** = ลบ anatomy เอเชีย)
3. **ผิว** — `fair skin with warm undertones` / `glass skin, subtle highlight on cheekbones` · **ไทย: `warm-brown/tan skin`**
4. **ผม** — เจาะจง `long straight black hair` / `ash-brown shoulder-length`
5. **แต่งหน้าน้อย** — `glossy nude lip, light pink balm only` (⚠️ **heavy makeup pulls the face Westward**)
6. **scene anchor วัฒนธรรม** — Seoul street / Tokyo café / 7-Eleven ไทย / ตลาดนัด / BTS / คาเฟ่กรุงเทพ

### Negatives เฉพาะ
```
no Westernized features, no blended Asian look, no big round eyes, no anime/kawaii style, no Orientalist stereotype, no over-smoothed pale skin
```
+ อย่าผสม cultural marker หลายชาติ (Chinese+Japanese+Korean หักล้างกัน)

### Per-nationality feature
| ชาติ | ลักษณะเด่น |
|---|---|
| **Thai** | warm-brown/tan skin, rounder face, sun-kissed |
| **Korean** | V-shaped jaw, high cheekbones, fair neutral skin, glass skin (K-beauty) |
| **Japanese** | natural texture, editorial restraint, documentary feel, อาจมี freckle เบา |
| **Chinese** | regional variance, เลี่ยง period-costume cliché |

### ตัวอย่าง
**Thai (clean iPhone + 7-Eleven):**
```
Ultra-photorealistic 4:5 candid iPhone selfie of an adult Thai woman in her 20s inside a 7-Eleven at night, warm-brown tan skin undertone, neat low double eyelid, soft lower nose bridge, rounder face, straight glossy black hair with flyaways, dewy natural makeup, glossy nude lip, straight brows, realistic skin texture, subtle T-zone shine, minimal freckles, natural facial asymmetry. Oversized graphic tee, holding bottled Thai milk tea. Harsh convenience-store fluorescent light, phone HDR, slight overexposure, arm partially visible, off-centre framing, compression artifacts, unedited Instagram photo. No Westernized features, no blended Asian look, no over-smoothing, no text, no watermark.
```
**Korean (K-beauty editorial):**
```
A 26-year-old Korean woman, sharp jawline with soft cheeks, glass skin with very subtle highlight on cheekbones, glossy nude lip, neat double eyelid, jet black sleek hair down, oversized cream blazer, neutral cool backdrop, single soft top light, 85mm f/2.8 K-beauty editorial, 4:5. No Westernized features, no big eyes.
```
**Japanese (lifestyle documentary):**
```
A 23-year-old Japanese woman, slight wave shoulder-length black hair, light freckles across the nose, soft monolid eyes, very natural skin texture, beige knit cardigan, soft afternoon-lit Tokyo coffee shop, blurred warm wood interior, 35mm f/2.0, documentary feel, 4:5. No anime style, no big round eyes.
```

## แหล่งที่มา
- [aitoolsguidebook — East Asian Beauty Portrait Prompts (12 templates, 6-field framework)](https://aitoolsguidebook.com/en/articles/east-asian-beauty-portrait-prompts/)
- [imagegpt — Asian Portraits: nationality differences (Thai/Korean/Japanese/Chinese)](https://imagegpt.cloud/learn/guides/asian-portraits-nationality-differences)
- [AI Video Bootcamp — Influencer Prompt Steal (Google Doc, 20+ realism prompts + universal add-on)](https://docs.google.com/document/d/193rR4_UfFdHz4fDG2-YzxGnSHNC-2u39EGXQm7jtyEM/edit)
- [AI Video Bootcamp — Y2K Prompt Steal (Google Doc, 6 Y2K digicam prompts + global negative)](https://docs.google.com/document/d/1A84jT-iAA5uWWPR5oCTDd_6SWsA7vK4MVqP5pa_rzZI/edit)
- [AI Video Bootcamp — "People think it's real" (Google Doc, elevated/European + POV set + reusable blocks/formula/guide)](https://docs.google.com/document/d/1gFl2zsp-HlyLAkZMzv0BzJyz7ewnHnVbr4CB0gw4BTg/edit)
- [AVB — Photorealistic AI Prompts Guide 2026 (8-category framework)](https://aivideobootcamp.com/blog/photorealistic-ai-prompts-guide-2026/)
- [Morphed — Realistic AI Image Generator: models that pass for photos 2026](https://morphed.app/blog/realistic-ai-image-generator)
- [Chomoi / Creative 1% — Realistic Faces & Skin deep dive](https://medium.com/creative-1/getting-realistic-faces-skin-in-midjourney-deep-dive-d85a63a62693)
- [Danex.ai — 8 Professional AI Influencer Prompts](https://danex.ai/ai-influencer-prompts/)
- [DesignHero — AI Art Direction Prompts FLUX & Midjourney](https://blog.designhero.tv/ai-art-direction-prompts-flux-midjourney/) *(เข้าไม่ได้ตอนเก็บ — 403)*
- [Alici.AI — How to Create an AI Influencer 2026: 10 prompt styles](https://alici.ai/blog/how-to-create-ai-influencer-2026-prompt-styles) *(เข้าไม่ได้ตอนเก็บ — 403)*
