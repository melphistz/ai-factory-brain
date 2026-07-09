---
name: feedback-drama-character-casting
description: "FEEDBACK - drama series character casting rule, all characters good-looking (leads + antagonists) but not over-the-top, keep realism"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5acbc9d1-f78e-4727-8b34-6fe6a1e3aea3
---

ตัวละครใน drama (ซีรีส์แนวตั้ง) ทุกตัวต้องหน้าตาดี — ตัวเอกสวย/หล่อ, นางร้ายก็ต้องสวย. ไม่มีตัวละครหน้าตาธรรมดา/น่าเกลียดในทีมหลัก. แต่ห้าม over — ยังต้องสมจริง ไม่ plastic/perfect เกินจริง.

**Why:** แนว vertical drama (ReelShort/DramaBox-style) ผู้ชมคาดหวังนักแสดงหน้าตาดีทุกตัว รวมนางร้าย/ตัวร้าย — เป็น genre convention ไม่ใช่แค่ตัวเอก. แต่ realism ยังสำคัญ (ดู [[ai-video-realism-hierarchy]]) ไม่งั้นภาพจะดูปลอม/AI เกินไป.

**How to apply:** ใช้ตอนเขียน character prompt สำหรับ [[smartaihub-drama-series]] หรือ genre pack ใดๆ (รวม revenge/vindication pack ที่ pending) — balance ความสวย/หล่อ กับ realistic skin/proportion cues จาก [[cute-face-charm-recipe]] / [[kpop-idol-visual-prompt]] / [[thai-localization-image-prompts]]. อย่าเขียน "average-looking" หรือ "plain" ให้ตัวประกอบหลัก/นางร้ายในดราม่าแนวนี้.

## Drama ≠ UGC — คนละ style คนละเหตุผลที่คนดู (07-09)

Reference จริงจาก DramaBox/Watch Drama Series (12 แคปจากเรื่องอื่น เก็บไว้ดูตัวอย่าง): ทุกตัวละคร (พระเอก/นางเอก/นางร้าย/ตัวประกอบ) หน้าตาระดับนักแสดงมืออาชีพ — ตาคมมี catchlight ชัด จมูกโด่ง ผิวมี glow+makeup finish, แสง **cinematic** (key+rim light, shallow DOF, bokeh, warm-cool contrast) ไม่ใช่ flat softbox แบบ UGC candid.

**Why:** คนดูละครมาดู "ความสวยความหล่อ" ของนักแสดง เป็นจุดขายหลักของ genre (ต่างจาก UGC ที่ต้อง "ดูไม่ AI/ดูจริง/เพื่อนถ่ายให้" เป็นจุดขาย) — สอง style เป้าหมายภาพคนละทาง แม้ทั้งคู่ต้อง realistic ไม่ plastic.

**How to apply:** เขียน prompt ตัวละคร drama ห้ามก๊อป template UGC ตรงๆ (เช่น "natural unretouched photograph", "neutral even softbox", "phone selfie") — ต้องใช้ cinematic-portrait vocabulary แทน: "cinematic drama-series character portrait", "soft key light with rim/edge light", "shallow depth of field, cinematic bokeh", "professional-actor tier skin", "subtle no-makeup makeup". Skin ยังต้องมี pores/realism (กัน plastic) แต่ lighting+focus+makeup ต้องยกระดับกว่า UGC. ดู [[ai-video-realism-hierarchy]] — motion/แสง/กล้อง เป็นตัวคูณ realism, หลักเดียวกันใช้ยกระดับ "ดูแพง/ดูมืออาชีพ" ได้ด้วย.

**Validated recipe:** ทดสอบผ่านจริง 3 รอบจนตรง DramaBox tier (idol glam makeup + dramatic key/rim light + sharp catchlights คือตัวชี้ขาด, ไม่ใช่แค่ cinematic vocabulary เฉยๆ) — สูตรเต็ม paste-ready อยู่ [[drama-dramabox-tier-portrait-recipe]].
