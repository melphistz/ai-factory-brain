---
name: outfit-swap-wichcraft-prompt
description: Wichcraft prompt = เปลี่ยนเสื้อผ้าภาพเดี่ยว 2-ref (@img1=นางแบบ/identity + @img2=เสื้อผ้า/wardrobe) → full-body catalogue-flat 9:16 · โครง 7 บล็อก + เทมเพลตสั่ง GPT/Gemini เรียนโครงก่อนแล้วสวม ref ตัวเอง
metadata: 
  node_type: memory
  type: reference
  originSessionId: 26b86e17-f999-4d69-8c4b-150b4d1f94bc
---

# Wichcraft Prompt — เปลี่ยนเสื้อผ้าภาพเดี่ยว (2-ref outfit swap)

Prompt สวมชุดใหม่ให้นางแบบเดิม **ภาพเดี่ยว** (ไม่ใช่ sheet) จาก 2 ref: `@img1`=นางแบบ (identity/body), `@img2`=เสื้อผ้า (wardrobe flat-lay). Output = full-body studio ref, catalogue-flat lighting, เหมาะ **9:16**. เอาไป composite/animate ต่อได้สะอาด.

**คู่กับ** [[char-sheet-2panel-identity-garment]] (แบบ sheet 2-panel), [[image-prompt-suffixes-techniques]] (pose-transfer/character-swap), [[ai-character-identity-lock]].

## โครง 7 บล็อก (เรียงตายตัว)
1. **Declaration + aspect** — 1 บรรทัด บอกผลลัพธ์ + `vertical 9:16 framing`
2. **Identity lock (@img1)** — ล็อกหน้า/โครงกระดูก/ตา/คิ้ว/จมูก/ปาก/ผิว/ผม/สัดส่วนตัว · **ปลดชัด:** `original clothing, footwear, pose, layout, background are NOT part of the identity lock` ← กันลอกชุดเดิม
3. **Wardrobe lock (@img2)** — `Translate the flat-lay items into one coherent outfit worn naturally... preserving construction, proportions, materials, colors, details:` แล้ว **item-by-item ทีละชิ้น ละเอียดสุด** (cut/neckline/seams/สี/ผ้า/distressing/hardware 1 ประโยค/ชิ้น)
4. **Bridge identity↔garment** — ผมโผล่ยังไงเมื่อสวมชุดใหม่ + `physically wearable` (layering/thickness/folds/tension/weight/contact) ← กันชุดลอย/แปะ 2D
5. **Pose + framing** — full-body หัวจรดเท้า, มุมตัว ~20°, ลงน้ำหนักสะโพก, ตำแหน่งมือ/prop, `entire outfit + both shoes clearly visible unobstructed`
6. **BG + lighting** — 18% neutral-gray flat (no seam/gradient/hotspot/vignette/falloff) + shadowless catalogue-flat (frontal + fill ซ้ายขวาเท่ากัน, no contact shadow)
7. **Realism finish** — matte skin/fabric, true colors, texture (peach fuzz/subsurface/hair strands/weave/stitching), 50mm, film grain, `Photographed, not illustrated or rendered`

## หัวใจที่ต้องรักษาตอนดัดแปลง (ห้ามตัด)
1. **แยก @img1=identity / @img2=wardrobe เด็ดขาด** + ประโยค "NOT part of identity lock" ปลดชุดเดิม
2. **"Translate flat-lay → worn naturally"** — แปลง lay-flat เป็นใส่จริง ไม่ใช่แปะ
3. **item-by-item ละเอียดสุด** — โมเดลลอกตาม *ที่เขียน* ไม่ใช่ที่เห็น เขียนขาด=มันเดา
4. **physically wearable block** — กันชุดลอย/2D
5. **flat catalogue lighting** — ได้ ref สะอาด composite/animate ต่อได้

## วิธีใช้ (สั่งโมเดลเรียนโครงก่อน)
นำหน้าด้วย: `Learn the STRUCTURE below, then rewrite to match MY model in @img1 and MY outfit in @img2. Keep all 7 blocks and their function; only swap identity details + item-by-item wardrobe. Output finished prompt only.` แล้วแปะโครงเต็มตาม.

## เทมเพลตว่าง (paste-ready)
```
Create one photorealistic full-body studio fashion reference of the exact same woman from @img1, vertical 9:16 framing.

Use @img1 strictly as the identity and body anchor. Preserve her exact facial identity, facial proportions, bone structure, eyes, brows, nose, lips, skin tone, hair, and body proportions, and overall recognizable appearance. Her original clothing, footwear, pose, layout, and background are NOT part of the identity lock.

Use @img2 strictly as the wardrobe, footwear, and accessory design reference. Translate the flat-lay items into one coherent outfit worn naturally on her body while preserving their visible construction, proportions, materials, colors, and details:
[ITEM-BY-ITEM: describe every garment/shoe/accessory from @img2 — cut, neckline, seams, color, fabric, distressing, hardware — one sentence each]

Her hair stays fully recognizable, falling naturally as she wears the new outfit. Keep the outfit physically wearable with believable layering, fabric thickness, seams, folds, tension, weight, and natural contact with the body.

Single woman, centered full-body framing from head to shoes, comfortable headroom and floor space. Body angled ~20 degrees from camera, weight on one hip, arms relaxed, [hand/prop placement]. Chin level, eyes to camera, calm neutral expression. The entire outfit and both shoes remain clearly visible and unobstructed.

Background is an even 18% neutral-gray seamless studio, completely flat — one uniform value corner to corner, no seam, gradient, hotspot, vignette, or falloff. Relight from scratch with flat shadowless illumination: one huge soft frontal source at camera, equal fill from left and right at identical intensity, balanced fill above and below. Both sides of the face and body read at the same brightness. Zero shadow on background, no contact shadow under feet. Extremely low-contrast, milky, catalogue-flat lighting.

Skin and fabric read matte and natural. Preserve her true skin tone and the outfit's true colors against the neutral gray. Real fine skin texture, peach fuzz at jaw and hairline, subsurface scattering, individually resolved hair strands and flyaways, authentic fabric weave, drape, stitching, and construction. Clean 50mm prime field of view, natural proportions, even sharpness, gentle film grain, real photographic finish. Photographed, not illustrated or rendered.
```

## ทิป
- อยากได้หลายมุม → แยก gen หรือใช้ [[char-sheet-2panel-identity-garment]] · ตัวนี้ = **ภาพเดี่ยว** เน้นแม่นสุด
- 1 นางแบบ + N ชุด = แปะ @img1 เดิม สลับ @img2 → ได้ทั้ง set คนเดิม
- item-by-item = จุดตาย เขียนละเอียดเท่าไหร่ ลอกตรงเท่านั้น

---

# Variant B — Wichcraft 3-Panel Sheet (headless front + rear + portrait)

wichcraft family เดียวกัน (2-ref img1=identity / img2=wardrobe) แต่ออกเป็น **character sheet 3 พาเนล** ในเฟรมเดียว แทนภาพเดี่ยว. ใช้ตอนต้องล็อกทั้งคน+ชุด+เห็นหน้า-หลัง-หน้าคมในใบเดียว.

## 3 พาเนล
- **LEFT** = full-body **FRONT, HEADLESS** — คอตัดเรียบคมแบบ dress-form mannequin (`clean, flat, sharply defined horizontal edge at base of throat`), ไม่มีหัว/ผม, เหนือคอ = พื้นเทาโล่ง, **เก็บ headroom เต็ม** (หัวถูกลบ ไม่ใช่ crop) → โฟกัสชุดล้วน ไม่มีหน้าแย่ง
  - **หมวก/headwear** (ที่ต้องมีหัว) → โชว์แยกเป็น accessory ตั้งข้างเท้า โชว์โครงครบ
- **CENTER** = full-body **REAR + มีหัว** — ถ่ายจากหลังตรง, ผมแยกเป็น section ให้เห็นตะเข็บหลัง/ขอบเอว, `infer only functional rear seams/closures` (ห้ามเติม decoration ใหม่)
- **RIGHT** = **chest-up portrait, identity lock max fidelity** — หน้าเต็มพาเนล มองกล้อง, ล็อกตา/คิ้ว/จมูก/ปาก/ผิว/hairline/ผม
- ทั้ง 3 พาเนล: gray 18% flat + shadowless catalogue-flat เหมือนกันเป๊ะ + realism finish เดียวกัน · ไม่มี label/text/logo

## กลไกเด่น (ต่างจากภาพเดี่ยว/2-panel)
- **headless clean neck-cut** (front) = erase-face อีกวิธี — คมกว่า grey-oval mask, ได้ชุด front ล้วนไม่มี identity conflict
- **แยกหน้าที่ 3 พาเนล:** front=garment · rear=fit/back-construction · portrait=identity → โมเดลไม่สับสน
- **หมวกโชว์แยก** เพราะ front ไม่มีหัวใส่ไม่ได้ (rule: accessory ที่ต้องมีหัว → วาง prop ข้างตัว)
- **"infer only functional rear seams, no unrelated decoration"** = กันโมเดลมั่วลายหลัง

## เทมเพลต Variant B (paste-ready — สั่งโมเดลเรียนโครงก่อน)
```
Create one photorealistic three-panel character reference sheet as a single horizontal frame, three equal vertical panels side by side with thin clean separators. Same woman and same coordinated outfit consistent across all three panels.

Use @img1 strictly as the identity and body anchor. Preserve the exact same adult woman: recognizable facial identity, facial structure, eyes, brows, nose, lips, skin tone, build, body proportions, and hair. Preserve her natural minimal makeup and calm neutral presence. Disregard the original clothing, footwear, poses, composition, and background from @img1.

Use @img2 strictly as the wardrobe, footwear, headwear, and accessory design source. Translate the flat-lay pieces into a coherent physically wearable outfit while preserving their visible colors, materials, construction, silhouette, scale, and details:
[ITEM-BY-ITEM description of every piece from @img2]
Preserve authentic weave, seams, stitching, fabric weight, folds, tension, and natural contact with the body.

LEFT PANEL — full-body FRONT outfit view, HEADLESS with a clean neck cut. Full figure squared to camera from shoulders down to soles, arms relaxed, hands loose, weight even. [prop in hand] hangs naturally without covering the outfit. There is no head and no hair; the neck rises a short distance above the shoulders and terminates in a clean, flat, sharply defined horizontal edge at the base of the throat, exactly like a headless dress-form mannequin, with no anatomy visible. Above the edge is only empty mid-gray backdrop. Preserve generous full headroom so the figure is scaled like a normal full-body portrait; the head is removed, not cropped. Because [any headwear] requires a head, display it as one separate upright wardrobe accessory beside the figure's foot, showing its construction completely. All other pieces stay worn on the body.

CENTER PANEL — full-body REAR view WITH the head attached. Same woman from directly behind, standing straight, arms relaxed, weight even, framed from the top of [headwear/hair] down to the soles. Complete identical outfit. Hair consistent with @img1, separated into controlled sections so rear construction and waistband remain readable. Show coherent rear construction using the same materials from @img2; infer only the functional rear seams and closures needed to make the garments wearable, no unrelated decoration.

RIGHT PANEL — tight chest-up portrait and identity lock. Frame from just above [headwear] down to the collarbones. Face fills most of the panel as a true close-up. Squared to camera, head level, eyes into camera, lips closed, calm neutral expression. Preserve the exact facial identity from @img1 at maximum fidelity — eye shape and color, brows, nose, lips, facial proportions, skin tone, hairline, hair, natural makeup, lashes, lip texture, fine skin detail all clearly readable.

Apply one identical 18% neutral-gray seamless studio backdrop uniformly across all three panels — one flat uniform value corner to corner, no seam, gradient, hotspot, vignette, or falloff, same gray in every panel. Relight from scratch with completely flat shadowless illumination across all three: one enormous soft frontal source at camera, equal fill from left, right, above, and below; both sides of face and body at identical brightness; clean flat backdrop behind every figure. Extremely low-contrast, milky, catalogue-flat, identical across panels.

Render skin at identical value and hue across face, neck, back, arms, hands in every panel. Identical fabric colors across views. Skin and fabric matte and natural. Fine pore texture, peach fuzz at jaw and hairline, subsurface scattering, individually resolved hair strands and flyaways, authentic weave, stitching, and construction. Natural anatomy and proportions, clean 50mm prime field of view, even sharpness, gentle film grain, real photographic finish. Photographed, not illustrated or rendered.

Exactly three photographic panels with clean separators. No labels, text, captions, measurements, logos, watermarks, diagrams, or interface elements.
```

---

# ✅ VALIDATED — Variant C: re-clothe 2-panel sheet (Dokkeaw nurse, 07-16)

โปรเจกต์จริง Dokkeaw/vid04: ใช้ **@img1 = 2-panel char sheet เดิม (นางแบบ Nok บ็อบดำ)** เป็น identity anchor แล้ว re-clothe เป็นชุดพยาบาลลาเวนเดอร์หลายแบบ — **หน้าไม่เพี้ยนเลยข้าม 3+ ชุด** (Mirko ยืนยัน). กระดุมโลหะเงินตราสัญลักษณ์ติดครบทุกใบ.

## สูตรที่เวิร์ก (multi-ref outfit swap → 2-panel sheet output)
Output = **recreate 2-panel sheet เดิม** (ซ้าย=close-up identity โชว์หน้า+ปก · ขวา=full-body front+back หน้า mask grey oval) แต่เปลี่ยนชุด. Ref stack:
- `@img1` = **char sheet เดิม** (identity+body anchor) — ปลดชุด/ฉาก/pose เดิมทิ้ง, keep แค่ หน้า/ผม/ตัว/รองเท้า
- `@img2` = เสื้อใหม่ (dress-form flat) — collar/seam/pocket
- `@img3` = **button override** (กระดุมโลหะ) — ย้ำ `METAL, reflective, NOT fabric-covered` + นับจำนวนเม็ด
- `@img4` = ท่อนล่าง (กางเกง/กระโปรง flat)
- `@img5` = **ภาพสวมจริง (fit target)** — ผูกเป็น proportion/length/sleeve ref (สำคัญเมื่อ @img2/@img4 วางแนวนอนอ่านทรงยาก)

## ทำไมหน้าไม่เพี้ยน (บทเรียน)
- **@img1 เป็น close-up-dominant sheet เดิม** = หน้าคมกินพื้นที่ใหญ่ในซ้าย → identity signal แรง (ตรงกับ VERDICT [[char-sheet-2panel-identity-garment]]: close-up-dominant anchor ดีกว่าหน้าเล็ก)
- **recreate layout เดิม** = โมเดลลอก composition + หน้าจาก ref โดยตรง ไม่ต้องเดาใหม่
- **face-mask grey oval ใน full-body** = ไม่มีหน้าที่ 2 มาแย่ง → หน้าเดียวในภาพ = หน้าจริง
- output เป็น anchor ตัวใหม่ได้อีก (ใช้เป็น @img1 รอบถัดไป — คนเดิมสะสมชุด)

## override ที่ยืนยันว่าคุมได้
- **สลับปก:** notched lapel ↔ rounded club/Peter-Pan → ระบุ collar type ตรงๆ คุมได้
- **แขนสั้น→ยาว:** "THE ONE CHANGE: replace short sleeves with LONG SLEEVES to wrists" ตาม fit photo → เวิร์ก
- **กระดุมหุ้มผ้า→โลหะ:** button-override block + "clearly METAL, reflective" → ติดกระดุมตราสัญลักษณ์เงาถูก
- **สลับท่อนล่าง:** กางเกง↔กระโปรง(pencil/เข่า) → คุมด้วย @img4 + @img5 fit ref

## เลือกใช้ตัวไหน
- **ภาพเดี่ยว (Variant A)** = ชุดเดียว เอาไปแอนิเมท/composite ต่อเร็ว, identity แม่นสุด
- **3-panel (Variant B)** = ต้องการ front+rear+portrait ใบเดียวเป็น ref pack — เหมาะ lock ก่อนทำงานยาว · headless-front = garment ref สะอาด
- ทั้งคู่ = พื้นฐานเดียวกัน ต่างที่ layout · หลัก 5 หัวใจด้านบนใช้ร่วม
