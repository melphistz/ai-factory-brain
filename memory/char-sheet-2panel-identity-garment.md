---
name: char-sheet-2panel-identity-garment
description: "Char-sheet format: 2-panel split — beauty close-up (identity) + faceless front/back full-body lookbook (garment/fit). แยก identity ออกจาก garment ในใบเดียว"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4bd13345-39cd-4398-af11-18f6b3b7ac15
---

# Character Sheet — 2-Panel (identity + faceless garment views)

ฟอร์แมต char sheet อีกแบบ (**เสริม ไม่แทน** 4-view/3-angle เดิมใน [[ai-asset-library-workflow]] · [[ai-character-identity-lock]]). เก็บจากตัวอย่างจริง (K-fashion lookbook AI, ก.ค. 2026).

## หน้าตา
ภาพเดียว ~16:9 แบ่ง 2 พาเนลด้วยเส้นคั่นบาง บนพื้นเทาเรียบ (seamless grey):
- **ซ้าย (~45%)** = **beauty close-up** หัวไหล่ขึ้นไป, หน้าคมชัดเต็ม, ผม/เมคอัพครบ, มองกล้อง — **เห็นดีเทลปกคอ/เนคไลน์ของชุดใต้คาง**
- **ขวา (~55%)** = **full-body 2 ช็อตเรียงกัน: FRONT + BACK** สไตล์ e-commerce lookbook — ยืนตรง แขนแนบข้าง เท้าชิด เห็นหัวจรดรองเท้า
  - ⭐ **หน้าในช็อต full-body ถูก MASK** (วงรีเทาเรียบทับ) — **ผมยัง render ปกติ** รอบหน้าที่โล่ง

## ทำไมถึงดี (หลักการ)
- **แยกหน้าที่ชัดในใบเดียว:** โคลสอัพ = **IDENTITY** (หน้า/ผม/ผิว) · full-body หน้าโล่ง = **GARMENT + FIT ล้วน** ไม่แย่ง identity
- = **erase-face trick** ([[higgsfield-3step-ai-ad-workflow]]) แต่จัดเป็นระบบ — โมเดลไม่สับสนว่าหน้าไหนคือหน้าจริง เพราะมีหน้าเดียวในภาพ
- **front + back** พอสำหรับเสื้อผ้า (ไม่ต้อง 3/4 ก็ได้) — เห็นทรง/ตะเข็บหลัง/ความยาว/รองเท้า/ถุงเท้าครบ
- โคลสอัพยัง double เป็น **fabric/collar detail ref** (ผ้าถัก/ปก/โบ/เนคไท เห็นชัด)
- พื้นเทาเรียบ = คุมง่าย ไม่มีฉากมาแย่ง

## ใช้เมื่อไหร่
- ✅ **โฆษณาเสื้อผ้า / lookbook / try-on** ที่ต้องล็อกทั้งคนและชุด — แนบ sheet เดียวเป็น ref เดียวจบ
- ✅ คู่กับ [[seedance-marco-freestyle-method]] (Image 1 = sheet นี้, Image 2 = ห้อง)
- ❌ ถ้าต้องการมุม 3/4 หรือ turnaround ครบสำหรับ animate/3D → ใช้ 4-view/9-square เดิม ([[ai-asset-library-workflow]])

## ⚠️ VERDICT ฟอร์แมตนี้ (deep-research 07-15, 21 sources / 25 claims verify)
**16:9 sheet นี้ไม่ผิด แต่ sub-optimal** สำหรับ identity lock:
- **กลไกจริง (confidence สูง, OpenAI docs):** โมเดลย่อ reference เป็น patch grid ที่ resolution เพดานคงที่ (gpt-image-1 ย่อด้านสั้น→512px) แล้วนับ token สม่ำเสมอทั้งเฟรม → **หน้ากินพื้นที่น้อย = token น้อย = identity signal อ่อน** (เรขาคณิตตรงๆ)
- **token budget ไม่ face-aware** — โมเดลถ่วงทั้งเฟรมเท่ากัน ไม่รู้ตรงไหนหน้า (GPT high-input-fidelity เพิ่ม token แบบ flat ตาม aspect ratio ไม่ใช่ตามตำแหน่งหน้า) → นี่คือเหตุผลที่หน้าเล็กในชีต 16:9 กว้างเสียเปรียบ
- **ที่ดีกว่า:** anchor **แนวตั้ง/close-up-dominant** (หน้ากินเฟรมเยอะ) + **แยกหน้ากับ full-body/ชุดเป็น 2 ภาพ ref แยก** ไม่ยัดใบเดียว — ภาพแยกได้ native (GPT รับ 1,500 ภาพ, Nano Banana 14 ref/6 high-fidelity, Seedream 3-5 มุม)
- **anchor ควรเป็น** close-up frontal/3-4 คมชัด ไม่มี occlusion/เมคอัพหนัก (glam ไปอยู่ที่ output ไม่ใช่ที่ ref)
- **grey-oval mask:** ไม่มีหลักฐานทั้งช่วย+ทำร้าย → low-risk เก็บได้ถ้าช่วยคุมชุด แต่อย่าคาดหวังว่ามัน "isolate identity"
- **ถูก REFUTE หมด (0-3, blog คุณภาพต่ำ):** "หน้าต้อง 30-50% เฟรม" · "ref ต้อง ≥1024px" · "<512px พัง" · "collage ทำโมเดลสับสน" — **อย่าอ้างตัวเลขพวกนี้เป็นกฎ**
- **caveat:** หลักฐาน 32px-patch/ViT มาจาก vision-**understanding** encoder — generative reference pathway ของ gpt-image-1/Nano/Seedance ไม่มี doc ยืนยัน tokenization เป๊ะแบบเดียวกัน = inference หนักแน่นแต่ไม่ใช่ proof
- **dedicated pipeline (InstantID):** ดึง identity จาก face embedding ที่ **crop** มา ไม่ใช่ raw full-image pixel — ถ้า target model ทำแบบนี้ pixel-share หน้าจะสำคัญน้อยลง (แต่ไม่พิสูจน์ว่า 3 โมเดลนี้ทำ)
- **A/B ที่ควรลองเอง:** (1) 2 ภาพแยก vs ชีตรวม (2) mask vs ไม่ mask — ไม่มี source ตอบตรงๆ ต้องเทสเอง

## PROMPT (paste-ready) — สร้าง sheet ฟอร์แมตนี้
```
Create ONE image, 16:9 landscape, split into two panels by a thin vertical divider, everything on the same seamless light-grey studio backdrop with even soft studio lighting.

LEFT PANEL (about 45% of the width): a large beauty close-up portrait of the woman — head and shoulders, her face fully visible and sharp, natural editorial makeup, hair falling naturally around her face, looking calmly into camera. The top of the garment (its collar / neckline / tie detail) is clearly visible below her chin, sharp enough to read the fabric texture.

RIGHT PANEL (about 55%): two full-length e-commerce lookbook shots of the SAME woman in the SAME outfit, side by side on the same grey backdrop — FRONT view on the left, BACK view on the right. She stands straight and relaxed, arms loose at her sides, feet together, framed head to shoes with clean margins. IMPORTANT: in these two full-body shots her FACE IS MASKED OUT — replaced by a plain flat grey oval with no features — while her hair renders normally and naturally around it. Only the left-panel close-up shows her face.

The woman: [IDENTITY — age, face, hair, skin, build].
The outfit (identical in all three shots): [GARMENT — top, bottom, shoes, socks, accessories, colours, fabric, details].

Photorealistic e-commerce / lookbook photography, natural skin and fabric texture, unretouched, no beauty-filter gloss, consistent lighting and colour across all three shots.
No text, no captions, no labels, no logos, no watermarks anywhere in the image.
```

## ทิป
- ระบุ **"plain flat grey oval with no features"** ให้ชัด ไม่งั้นโมเดลจะเบลอหน้าแบบครึ่งๆ (ได้หน้าผี) หรือใส่หน้ากลับมา
- ผมต้อง render ปกติรอบหน้าโล่ง (บอกตรงๆ) — ตัวอย่างจริงผมเต็ม หน้าเป็นช่องว่าง
- ให้โคลสอัพ **โชว์ปก/เนคไลน์** เสมอ = ได้ collar reference ฟรี (สำคัญมากถ้าชุดต่างกันแค่ปก — เคส vid04 L2/L3 ปกซ้ำ)
- 1 ชุด = 1 sheet · หลายชุด = ทำหลายใบ คนเดิม (สลับ sheet ตอน gen วิดีโอ)
