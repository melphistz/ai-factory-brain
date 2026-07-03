---
name: ai-character-identity-lock
description: Recipe for consistent AI character — same face across many images/scenes (the hardest problem for AI influencer series)
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Identity Lock — หน้าเดิมข้ามหลายรูป/ฉาก (โจทย์ยากสุดของ AI influencer)

> 1 หน้าง่าย — **หน้าเดิม 50 รูปคือของจริง**. recipe นี้คือชิ้นส่วนที่ค้างมาตลอด.
> คู่กับ [[ai-influencer-image-prompt]] (วิธีเขียน realism) · [[storyboard-gpt-image-to-seedance]] (ภาพ→วิดีโอ). เก็บ มิ.ย. 2026

## หลักการ: identity = visual asset ไม่ใช่ text
- model **pattern-match กับ visual input** ไม่ใช่ reconstruct จาก description
- ยิ่งบรรยายหน้าเยอะ ยิ่ง drift — **reference sheet คุมแทน**
- เครื่องมือดีสุด: **GPT Image 2** (drift 6% + ชนะ 8-image grid จาก [[ai-influencer-image-prompt]] benchmark) · **Nano Banana Pro** (hold ได้ถึง 5 คน / 14 ref)

## ⭐ Method: Named Reference Sheet (ChatGPT / GPT Image 2)
**6 ขั้น:**
1. **รวม 2-3 รูปต้นแบบ** ที่หน้า/vibe ตรงเป๊ะ
2. **ทำ Face Sheet** — อัป ref แล้วสั่ง:
   ```
   Make a reference character sheet for [NAME] from these images. Show front view and side profile, clean background, with the name labelled at the top.
   ```
   ⭐ สำคัญ: **ป้าย NAME บนชีตจริงๆ** (ไม่ใช่แค่ชื่อไฟล์) — model ใช้ยึด
3. **Full-Body Sheet** (ถ้าต้องคุมชุด):
   ```
   Using [NAME]'s face sheet, make a full body character sheet showing front view and side profile. She is wearing [SIGNATURE OUTFIT].
   ```
4. ทำชีตแยกต่อ 1 ตัวละคร
5. ⭐ **เปิด conversation ใหม่ทุกครั้งที่เจน** — แนบเฉพาะชีตที่ใช้ → กัน drift จาก context สะสม
6. ⭐ **prompt สั้นประโยคเดียว** — ชีตคุม identity, prompt คุมแค่ action+location

**template scene:**
```
[NAME] [is] [ACTION] [at/in LOCATION]. [FORMAT]. [scene details].
```
เช่น `Kristina is sitting at a coffee shop reading a book. Landscape format, cinematic.`
- เปลี่ยนชุด: `Make them wear fitting clothes for the scene.`
- กัน text: เพิ่ม `no text in the image` (ChatGPT ชอบพิมพ์ชื่อตัวละครเป็น text)

## Identity-lock block (วางก่อน describe ฉากใหม่ — YouMind)
```
Use my uploaded face image as the primary identity reference. Preserve my exact facial identity, face shape, hairstyle, hair texture, skin tone, eye shape, eyebrows, nose, lips, and all unique facial details with maximum accuracy.
```

### ⭐ Strong version — 100% preservation + anatomy list (YouMind Gen-Z editorial prompt)
ยิ่งลิสต์ส่วนหน้าครบ ยิ่ง lock แน่น (แน่นกว่า "same face"):
```
Using the uploaded face image, preserve the person's facial identity with absolute accuracy
(100% identity preservation), maintaining the exact face shape, bone structure, forehead,
eyebrows, eyes, nose, lips, ears, jawline, hairline, facial hair, and hairstyle.
```
- ตัวอย่างจริงเสริม: "using the uploaded face as the **100% exact facial reference with no changes**" (mirror-selfie prompt)
- ดู prompt ต้นทาง: [[youmind-gpt-image-prompt-library]]

## Reference-sheet method (ทั่วไป — ก่อนเจนฉากแรก)
- ทำ **multi-angle sheet** ก่อนเจนฉากใดๆ (เหมือนสตูดิโอ animation ออกแบบตัวละครก่อน frame แรก) → identity กลายเป็น asset ที่ reuse ได้ เลิกอธิบายหน้าซ้ำ
- หน้า (face shape, proportion, presentation) คงข้าม viewpoint

## เครื่องมือตามระดับ
| ระดับ | เครื่องมือ |
|---|---|
| เร็ว/ง่าย หน้าเดิม | **GPT Image 2** named reference sheet (drift 6%) |
| realism + แต่งภาพ conversational | **Nano Banana Pro** (reuse persona image as ref, ≤5 คน/14 ref) |
| คุมสุด (pose/lighting เป๊ะ) | train **LoRA / FaceID-IPAdapter** ใน ComfyUI (Flux/SDXL) — setup หนัก |
| **input_fidelity** (GPT Image 2 Edit mode) | อัป ref + ตั้ง 0–1, **1.0 = preserve subject สูงสุด** |

## Two-tool workflow (advanced)
draft brief ละเอียด (lighting/atmosphere/camera) ใน **ChatGPT** → เจนจริงด้วย **Nano Banana** → ใช้ character sheet เดียวกันทั้ง 2 → ChatGPT คิด, Gemini ทำ

## Recipe เต็ม (ทำซีรีส์หน้าเดิม) = รวม 3 ส่วน
1. **identity** — named reference sheet (GPT Image 2) + identity-lock block + conversation ใหม่ทุกครั้ง
2. **realism** — สูตร [[ai-influencer-image-prompt]] (imperfection stack, 6-field เอเชีย, lane ที่เลือก)
3. **variety** — สลับ scene+prop+pose (15–30 รูปไม่ซ้ำ — [[ai-influencer-image-prompt]])
→ ต่อ: เบลอหน้า → animate ใน Seedance ([[storyboard-gpt-image-to-seedance]] · [[seedance-ugc-repository]])

## แหล่งที่มา
- [aimeetsgirlboss — Consistent Character Images in ChatGPT Images 2.0 (named reference sheets)](https://aimeetsgirlboss.substack.com/p/how-to-get-consistent-character-images)
- [aitoolsguidebook — Consistent AI Character Images Across Scenes (MJ V8.1 oref, Nano Banana Pro)](https://aitoolsguidebook.com/en/articles/ai-consistent-character-images/)
- [dev.to — GPT Image 2 Subject-Lock input_fidelity](https://dev.to/dylan_huang_2686f6cef827a/gpt-image-2-subject-lock-editing-a-practical-guide-to-inputfidelity-1mce)
- [opencreator — AI Character Reference Sheet (multi-angle)](https://opencreator.io/blog/ai-character-reference-sheet)
- [YouMind — GPT Image 2 Prompts gallery (Identity Preserving Portrait)](https://youmind.com/gpt-image-2-prompts)
