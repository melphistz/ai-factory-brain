---
name: zenityx-interview-scene-workflow
description: "ZenityX Studio handbook — AI podcast/interview scene workflow: 4-block image prompt (identity lock) → Thai talking-head video (Grok Imagine 1.5) → Kling 3.0 two-shot closing. Source: zenityx-handbook.netlify.app (+/practice)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 71b89552-9c0d-4b88-b544-81e35f265a9b
  modified: 2026-07-30T01:21:45.457Z
---

# ZenityX — AI Interview/Podcast Scene Workflow (learned 2026-07-30)

Source: https://zenityx-handbook.netlify.app/ (วิธี) + https://zenityx-handbook.netlify.app/practice (แบบฝึกหัด)
Platform: studio.zenityx.com (browser, credit-based) · เกี่ยวข้อง: [[storyboard-gpt-image-to-seedance]] [[veo-google-flow-knowledge]] [[ugc-storyboard-sheet-template]]

## ภาพรวม flow 3 ขั้น
1. **Character + Scene still** — character sheet → ภาพนั่งสัมภาษณ์ในสตูดิโอ (4-block prompt)
2. **Thai talking video** — still → คลิปพูดไทย 15s lip-sync (dialogue ใน quotation marks)
3. **Closing two-shot** — wide 2 คน มองกล้อง → Kling 3.0 วิดีโอปิด 5–6s ไม่มีพูด

ตัวอย่างเต็ม 1 ตอน (~1:24, opening + 2 Q&A + closing) ≈ 300 credits

## Lab 1 — 4-block IMAGE prompt (Nano Banana Pro, 9:16 4K, ~5 cr/ภาพ)
- **Block 1 Identity Lock:** "must have the EXACT same face as the reference character sheet — same eye shape, nose, lips, jawline, skin tone, and the same [hair]. Do not alter or stylize her face."
- **Block 2 Scene:** podcast living room — "light gray fabric sofa, soft beige cushions, warm wooden wall, wooden door softly blurred, soft natural window light from camera-left, warm high-key tone"
- **Block 3 Action & Outfit:** ท่านั่ง relaxed เอียงเข้า camera-right, ตามองเฉียงขวา off-camera, warm genuine smile while speaking + **microphone boom เข้า frame จาก bottom-right foreground** + outfit spec
- **Block 4 Composition:** "Photorealistic medium shot, waist-up, eye-level, 50mm lens look, shallow depth of field, subject slightly off-center with nose room toward camera-right."

**เคล็ด 2 ตัวละคร (mirror trick):** ฉากเดียวกันเป๊ะ กลับทิศ — A มองขวา/ไมค์ขวา, B มองซ้าย/ไมค์ซ้าย → ตัดสลับแล้วดูเหมือนคุยกัน

**Face distort fix:** ref ชัด 1–3 ภาพ · ใส่ IDENTITY LOCK ทุกครั้ง · เลี่ยงคำ "stylize/artistic" · เจนซ้ำหลายรอบเลือกอันดีสุด

## Lab 2 — 4-block VIDEO prompt (Grok Imagine Video 1.5, พูดไทยได้, 720p 9:16, 3 cr/s → 15s = 45 cr)
- **Block 1 Role & Action:** บทบาท (HOST/GUEST) + energy + gesture + ตำแหน่งคู่สนทนา off-camera
- **Block 2 Dialogue (หัวใจ):** คำพูดไทยใน quotation marks พูดต่อเนื่องเต็ม 15s · **กติกา pacing: ~4 ประโยคไทย / 15 วิ** กันช่วงท้ายเงียบ
- **Block 3 Ending:** ท่าปิด เช่น "keeps talking until the very end of the clip, ending with an expectant friendly smile toward the guest"
- **Block 4 Motion & Camera:** "Natural subtle motion: blinks, head tilts, welcoming hand gestures. Static camera, medium shot, photorealistic, warm podcast atmosphere, natural room ambience."

ตัวอย่าง dialogue host: "สวัสดีค่ะ วันนี้เรามาคุยกับศิษย์เก่าของ ZenityX Studio… เล่าให้ฟังหน่อยได้ไหมคะ ว่าตอนนี้ทำอะไรได้บ้างแล้ว"
Cost tip: ลอง 5s (15 cr) ก่อนค่อยยิง 15s เต็ม

## Lab 3 — Closing two-shot (still ใน Nano Banana Pro → วิดีโอใน Kling 3.0)
- Still: upload ref ทั้ง 2 คน + spatial lock ชัด ๆ: "guest … FAR LEFT … host … FAR RIGHT … clear GAP in the middle with a small low wooden coffee table" · ทั้งคู่หันมองกล้อง ยิ้ม
- Composition: "very wide two-shot, eye-level, one subject on the left third and one on the right third, empty middle showing the set, 28mm lens look, deep depth of field, vertical 9:16"
- Video (Kling 3.0, 5–6s): "NEITHER of them speaks — mouths stay closed, no dialogue at all." + ซ้ายโบกมือเบา ๆ ขวาพยักหน้า, blinks + clothing movement

## Post
รวมใน CapCut/Premiere → host ถาม / guest ตอบ สลับกัน + closing + logo

## Platform notes (ZenityX Studio)
- Modes: Image Generator · Video Generator · Voice Studio (TTS ไทย, emotion tags เช่น "[softly]" "[laugh]", dialogue mode ≤10 คน) · Avatar & Motion (Motion Control = copy ท่าจาก ref video, **Infinitetalk** = lip-sync ตามไฟล์เสียง) · Upscale+
- Credits ไม่หมดอายุ · ภาพ 1 cr · วิดีโอ 15s = 45 cr (Grok) · เสียง 8 cr/1,000 ตัวอักษร · แพ็ก ฿350–฿10,000
