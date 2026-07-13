---
name: seedance-marco-freestyle-method
description: "Marco method (ORIGINAL source) — Seedance prompting by setting RULES not SHOTS; let the model freestyle framing. Detailed shot-by-shot = 'the AI tell' (stiff, dreamy, dead)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4bd13345-39cd-4398-af11-18f6b3b7ac15
---

# Marco method — "I let Seedance freestyle the creativity. I just set the rules."

**ต้นฉบับ: [@MarcoBorinEdit บน X](https://x.com/MarcoBorinEdit/status/2068075513206174081)** — AI swimwear ad อิตาลี 15 วิ · **2 reference images + 6 บรรทัด + 1 generation** · Seedance 2.0 ผ่าน kie.ai
> `projects/tuensai/04-prompts.md` §V3 = derivative ของวิธีนี้ (ไม่ใช่ต้นฉบับ) · เกี่ยว [[seedance-knowledge]] (กฎทอง ลำดับบอก/มุมปล่อย) · [[tuensai-project]]

## สิ่งที่เขาทดลอง (pipeline จริง)
1. **prompt ละเอียด shot-by-shot เขียนมูฟกล้องทุกช็อต** → ผลออกมา **ช้า ฝันๆ แข็ง = "the AI tell"** ❌
2. **ถอดออกให้เหลือแค่กฎ** (กล้อง/สถานที่/เสียง/บรีฟ) แล้วปล่อยให้ Seedance invent ช็อตเอง → **มีชีวิตขึ้นทันที** ✅
3. **ขอ "rare camera angles" แล้วปล่อยให้มันเลือก** → มันคิดเอง: over-under ที่ผิวน้ำ, ground-level pass บนกรวด, macro ลายผ้า — **framing ที่เราไม่มีวันเขียนเอง** ⭐

## หลัก (ใจความ)
- **SET THE RULES, NOT THE SHOTS** — กำหนดกรอบ ไม่กำหนดภาพ
- **CAMERA = อุปกรณ์/เท็กซ์เจอร์ ไม่ใช่มูฟ** — `Shots on an iPhone 14 Pro, imperfections are present` (ไม่ใช่ "slow dolly push-in")
- **SHOTS = 1-2 บรรทัด** บอกว่า "ต้องเห็นอะไร" ไม่ใช่ shot list / ไม่มี timecode / ไม่มีมุม
- **`Rare camera angles.` = คำปลดล็อก** — เชิญให้มันคิดมุมแปลก
- **reference image ล็อก identity/สินค้า · prompt วางกฎ** — แบ่งหน้าที่ชัด
- **AMBIENCE = เขียนให้มีกลิ่น ไม่ใช่แค่สถานที่** — `A small deserted Puglia cove at golden first light. Lived-in, the locals' sea.`
- เสียง = ระบุเสมอ (`Environment sound only, no music.`)

## ต้นฉบับเต็ม (paste-ready template)
```
FORMAT
15-second video, 16:9

REFERENCE ROLES
Image 1 = the woman; stage every shot as her, full identity from this image.
Image 2 = the swimsuit she wears; she wears exactly this piece throughout, print and cut and colorway from this image.

CAMERA
Shots on an iPhone 14 Pro, imperfections are present.

AMBIENCE
A small deserted Puglia cove at golden first light. Lived-in, the locals' sea.
AMBIENCE SOUNDS
Environment sound only, no music.

SHOTS
Several shots showing the swimsuit on the woman, both close details and full looks.
Rare camera angles.
```

## ใช้เมื่อไหร่ / ไม่ใช้เมื่อไหร่
- ✅ **ใช้:** งาน mood/fashion/product ที่ "ความมีชีวิต + มุมแปลก" สำคัญกว่าคุมบีตเป๊ะ · reference ล็อก identity ให้แล้ว · อยากได้ variety จาก 1 gen
- ❌ **ไม่ใช้:** บีตที่ความหมายพึ่งมุม/จังหวะเป๊ะ (เช่น กดจิ้มจุดที่ AE ต้อง track, hand-off prop, punchline reveal, first+last frame lock) — พวกนี้ต้องล็อก
- **ผสมได้:** ปล่อยมุม + ล็อกเฉพาะบีตสำคัญ (กฎทองใน [[seedance-knowledge]]: **ลำดับ+แอ็กชัน = บอกเสมอ · มุมกล้อง = ปล่อย ยกเว้นบีตสำคัญ**)
