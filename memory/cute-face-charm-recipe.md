---
name: cute-face-charm-recipe
description: สูตรทำหน้าน่ารักมีเสน่ห์ (Korean dong-an/aegyo) สำหรับ realistic UGC gen — แก้ปัญหา realism ผ่านแต่หน้าไม่น่ารัก; cute-face geometry block + full prompt
metadata: 
  node_type: memory
  type: reference
  originSessionId: 86c5776a-a91f-460f-9a7e-50481518b8ef
---

# Cute-Face Charm Recipe — หน้าน่ารักมีเสน่ห์ (07-07)

แก้เคสคลาสสิก: **realism ผ่านแล้ว** (ผิว/รูขุมขน/หน้าอกเหมือนจริง) **แต่หน้าไม่น่ารัก** — gen ออกมาเป็น "สาวธรรมดา realistic" หน้ายาว ตาเล็ก จมูกกว้าง+แดง ยิ้มเห็นเหงือกฝืน. ปัญหาไม่ใช่ realism แต่ **cute-face geometry หาย** → ต้องฉีดกลับ. ดูคู่ [[characters/zhao-yu]] realistic variant · [[ai-influencer-image-prompt]] · lesson จาก teardown cherryhikiko.

## กุญแจหน้าน่ารัก (เกาหลี 동안 dong-an / 애교 aegyo) — เรียงตามพลัง
1. ⭐ **aegyo-sal (애교살)** = ไขมันนูนใต้ตา = สร้างเสน่ห์อันดับ 1 (ยิ้มแล้วตาเป็นเสี้ยวมีประกาย)
2. **หน้าสั้นกลม** — โหนกแก้มอวบ baby fat, ส่วนล่างสั้น (คางเล็ก, philtrum สั้น)
3. **ตากลมโต** ห่างกำลังดี หางตาตกนิดๆ (puppy eyes) + **ตายิ้มโค้งเสี้ยว** ตอนยิ้ม
4. **จมูกเล็กมน** ปลายกลม — NOT wide, NOT flat, NOT red
5. **ปากเล็ก** มุมปากยกขึ้น ยิ้มหวานไม่เห็นเหงือกเยอะ
6. **ลักยิ้ม + ฟันกระต่ายนิดๆ** + จัดฟัน = น่าเอ็นดู

## FACE block (drop-in — แทน FACE ท่อนเดิม, เก็บ realism stack ไว้)
```
FACE — cute charming Korean "dong-an" (baby-face) geometry: short rounded face with soft full cheeks and baby fat, short lower third, small delicate rounded chin. Large round bright eyes set slightly wide apart with a gentle downturn at the outer corners (puppy eyes), prominent aegyo-sal (soft puffy fat pads under the eyes) that push up into happy crescent eye-smiles when she grins. Small rounded button nose with a soft round tip (NOT wide, NOT flat, NOT red). Small mouth with upward-curling corners, sweet soft smile showing just a hint of metal braces, NOT a wide gummy grin. Faint single dimple, subtle bunny front teeth. Warm genuine smile that reaches the eyes — soft, endearing, charming.
```

## กับดักที่ทำ gen พัง (แก้ด้วย)
- **จมูกแดง/สิวเยอะ** ทำลายความน่ารัก → เก็บแค่ "fine pores + faint peach fuzz + 1-2 tiny moles" (realistic แต่ไม่พัง)
- ยิ้มสั่ง **"soft warm eye-smile, crescent eyes"** ไม่ใช่ "big smile teeth" → กันยิ้มฝืนเห็นเหงือก
- **negative ต้องมี:** `no long face, no narrow squinty eyes, no wide flat nose, no red nose, no wide gummy forced smile, no harsh under-eye shadows, no tired plain expression`

## FULL PROMPT — cherryhikiko cute-UGC (paste-ready, Nano Banana / GPT Image)
```
Ultra-photorealistic phone selfie of a cute, charming 20-year-old East-Asian girl, shot on an iPhone front camera, casual candid mirror-selfie vibe, vertical 9:16.

FACE — cute charming Korean "dong-an" (baby-face) geometry: short rounded face with soft full cheeks and baby fat, short lower third, small delicate rounded chin. Large round bright eyes set slightly wide apart with a gentle downturn at the outer corners (puppy eyes), prominent aegyo-sal (soft puffy fat pads under the eyes) that push up into happy crescent eye-smiles when she grins. Small rounded button nose with a soft round tip (NOT wide, NOT flat, NOT red). Small mouth with upward-curling corners, sweet soft smile showing just a hint of metal braces, NOT a wide gummy grin. Faint single dimple, subtle bunny front teeth. Warm genuine smile that reaches the eyes — soft, endearing, charming.

EYEWEAR: thin round gold-wire glasses sitting naturally on the nose.

SKIN: real photoreal skin — fine visible pores, faint peach fuzz, one or two tiny natural moles, subtle soft dewy texture, natural rosy cheek flush, NO airbrush, NO plastic CGI, NO heavy acne or red blotches; flawless-looking but human.

HAIR: glossy jet-black hair tied up loosely with a matte claw clip, soft wispy see-through bangs and thin flyaway strands framing the face.

STYLING: cute Y2K / soft-girl fashion — pastel pink gingham lace-trim cami with a tiny bow, dainty silver heart necklace, tiny pearl earrings.

LIGHT: bright even daytime light, soft and slightly OVEREXPOSED, flat airy clean tone, neutral-cool white balance — bright bedroom by a window. NOT moody, NOT dark, NOT low-key.

SETTING: real everyday bedroom — white bed, plush capybara toy, plain warm-white wall, soft window light behind.

STYLE: candid handheld phone photo, mild lens softness, faint grain and phone compression, natural imperfect framing, true-to-life color.

Negative: no plastic or waxy skin, no heavy airbrush, no long face, no narrow squinty eyes, no wide flat nose, no red nose, no wide gummy forced smile, no harsh under-eye shadows, no tired plain expression, no doll uncanny face, no studio glam lighting, no dark moody tone, no CGI or 3D render, no warped hands or fingers, no extra fingers, no text, no logo, no watermark.
```

## ต่อยอด
- ล็อกเป็นตัวละคร reusable → gen ใบสวยสุด ทำ turnaround + expression sheet เป็น @ref (template [[characters/zhao-yu]])
- variant ฉาก (pool/เตียง/mirror/คาเฟ่) คง FACE+SKIN block เปลี่ยน SETTING+STYLING
