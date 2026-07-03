---
name: ai-video-realism-hierarchy
description: "Realism ของ AI video = motion/lighting/camera เป็นตัวคูณ, skin detail เป็นแค่ pass/fail gate — พิสูจน์ด้วย case study MV ไทย AI ล้วนที่หลอกตาได้ที่ 720p"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f495e44a-04e5-4cac-94ed-83e0ab9d81c9
---

# AI Video Realism Hierarchy (2026-07-03)

สมมติฐาน Mirko (ยืนยันแล้วด้วย case study): ความสมจริงของ AI video **ไม่ได้อยู่ที่ detail ภาพ** (สิว รูขุมขน) แต่อยู่ที่ **motion / แสง / กล้อง**

## Hierarchy (เรียงน้ำหนัก)

1. **Physics** — น้ำหนักตัว, inertia ของของ, secondary motion (ผม/ผ้า/น้ำ), foot-ground contact
2. **Motion cadence** — ห้าม floaty/interpolated-smooth, คนจริงมี micro-jitter, pause, หายใจ
3. **กล้อง** — gimbal-smooth เนี้ยบ = AI tell; ต้อง handheld micro-shake, focus hunt, exposure ปรับตาม
4. **แสง behavior** — motivated single source, เงา + specular track ตามการเคลื่อน; "soft สวยทั่วเฟรม" = tell
5. **Human micro-behavior** — กะพริบ, saccade, จังหวะปาก, micro-expression
6. *(gate ไม่ใช่ตัวคูณ)* **Skin detail** — แค่ผ่านเกณฑ์ "ไม่พลาสติก/ไม่ beauty-filter" พอ เกินนั้นไม่เพิ่ม realism. Platform compression ฆ่า detail อยู่แล้วแต่ไม่ฆ่า motion

## Case study: MV situationship ไทย (AI ล้วน, 3:49, 720p, 24fps)

ไฟล์: Downloads/AQP2rzK...mp4 (FB download) — คู่นักศึกษาไทย เดินเรื่องตามเพลง "ทุกอย่างเหมือนแฟน ยกเว้นสถานะ"

**หลอกตาได้เพราะ:** น้ำกระเซ็นตอนเท้าแตะพื้นฝน + เงาสะท้อนพื้นเปียก track ทุกเฟรม, ย้อนแสงลอด tree canopy, set dressing แบรนด์จริง (BETREND/Anpanman), ตัดต่อ MV ช็อตละ 1-3 วิ, film grade + grain กลบ smooth — ทั้งที่ 720p ไม่มี detail ผิวเลย

**จุดที่ยังหลุด (ใช้เป็น QA checklist):**
- **Contact physics = จุดตายอันดับ 1** — นิ้วเขี่ยผมแล้วนิ้วละลายเข้ากลุ่มผม, กำปั้น knuckle เละ → ซูมตรวจทุกช็อตที่มือแตะของ/คน
- Watermark "AI" chip มุมซ้ายบนโผล่บางช็อต (ของ generator)
- หน้า archetype AI: ผิว porcelain ฐานเรียบ + โรยกระ/ไฝจงใจ

## Case study 2: AI influencer beauty-walk reel (11s, 9:16, 720p)

สาว douyin-archetype ชุดดอกไม้ appliqué เดินห้างกลางคืน + เสียงจีบไทย — motion สวยแต่จับได้จาก:
- **Wardrobe re-roll ข้ามช็อต = tell ใหม่อันดับ 2** — layout ดอกบนชุดคนละแบบระหว่าง scene (identity lock คุมหน้า+concept ชุด แต่ไม่คุม geometry ลายผ้า) → **QA: ซูมเทียบลายผ้า/กระดุม/ตะเข็บ/prop ข้ามทุกช็อต** — ตรงกับงาน Valenshield ที่ชุดต้องนิ่งทุก clip
- Contact แอบเลี่ยง: มือพิงราวแต่นิ้วหายหลังขอบพอดี (pattern หลบจุดยาก)
- ผิว porcelain zero-texture + ตา glassy, เดินไม่มี weight snap (ทุกอย่าง velocity เดียว)

## Case study 3: AI "Japan cat-girl vlog" (2 min, douyin archetype)

เนียนสุดใน 3 คลิป — contact physics ผ่านเกือบหมด (นิ้วกดขนแมวแนบ, มือกำ handlebar) ต้องจับชั้นอื่น:
- **Detail-inconsistency ที่ ECU = tell ใหม่สำคัญ** — ขนตาคมรายเส้นแต่ผิว/ปากข้างกัน wax เรียบสนิท; ฟุตเทจจริงผ่าน compression จะเบลอทุกอย่าง*เท่ากัน* → QA: ซูม ECU ดูว่า detail สม่ำเสมอทั้งเฟรมไหม
- หมวก re-roll: ช็อตถนน = plaid ธรรมดา, ช็อต studio แทรก = plaid เดียวกันงอกหูแมว
- **สัตว์เลี้ยง/สิ่งมีชีวิตประกอบ = prop ที่หลุดง่ายสุด** — แมวข้างถนนผอมลายเข้ม vs แมวที่อุ้มอ้วนฟูลายจาง (identity lock ไม่คุมสัตว์)
- Vlog สะอาดเกิน: ไม่มีคนผ่าน/ลมตีไมค์/ความพลาดใดๆ ใน 2 นาที

**แนวโน้ม:** model ใหม่ปิดจุดอ่อน physics/contact เรื่อยๆ → tell ที่ยั่งยืน = cross-shot consistency (ชุด/prop/สัตว์) + ECU detail-inconsistency (เป็นปัญหา architecture ไม่ใช่ training)

## ผล full-scan ระดับ signal (SSIM ทุกคู่เฟรม, 8,656 คู่ / 3 คลิป)

- **ไม่พบ frame-level morph/flicker เลยสักจุด** — anomaly ทั้งหมด decode เป็น: cut แฝง (โทนใกล้กัน ssim ไม่ต่ำพอ), fade, whip-pan blur, แขนผ่านหน้าเลนส์
- ข้อสรุป: gen รุ่น 2026 **coherent ระดับ signal แล้ว frame-diff จับไม่ได้อีกต่อไป** — เหลือแต่ semantic tells (ข้อบน)
- เครื่องมือ: `Desktop/Ads/videos/_ssim_scan.py` — scan ทุกคู่เฟรม + per-shot z-score + ดึง strip 4 เฟรมตรงจุดสงสัยมาส่องตา (ใช้ซ้ำได้กับทุกคลิป)

## ใช้กับ prompt

เทน้ำหนัก prompt ลง: camera imperfection (handheld micro-shake, focus breathing) + motivated lighting แหล่งเดียว + physics cue (น้ำหนักตัว ผ้าแกว่ง — physics-weight trick ใน [[higgsfield-3step-ai-ad-workflow]]) + micro-behavior + ปิดด้วย grain/phone-artifact

เกี่ยว: [[seedance-knowledge]] · [[seedance-ugc-repository]] · [[ai-influencer-image-prompt]] · [[ugc-ad-structure]]
