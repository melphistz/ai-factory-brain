---
name: ai-asset-library-workflow
description: AI short-drama asset library workflow (character/scene/prop/color categories) from Chinese tutorial video — solves character/scene consistency at scale
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5acbc9d1-f78e-4727-8b34-6fe6a1e3aea3
---

หลักการ: AI short drama พังเพราะไม่มี "資產庫 (Asset Library)" — ติดอยู่แค่ random generation. ปัญหาใหญ่ไม่ใช่มุมกล้อง แต่คือ "หน้าตัวละครไม่เหมือนเดิม" + "ตรรกะฉากไม่ตรงกัน". จาก tutorial video (D:\Downloads\Video, วิเคราะห์ผ่าน Higgsfield video_analysis 2026-07-09, 2:11 นาที).

## 3 core asset categories

1. **Character (人物)** — แก้ 99% ปัญหา consistency
   - Face assets: ถ่าย 3 มุม (ตรง/45°/ข้าง) พื้นขาว = ล็อกหน้า
   - **9:16 แนวตั้ง ดีกว่า 16:9** สำหรับ face sheet — รายละเอียดหน้าใหญ่ชัดกว่า (มี side-by-side comparison ใน video ยืนยัน)
   - Action assets: collage ท่าโพส/ปฏิกิริยา ไว้ใช้ตามสถานการณ์ต่างๆ
2. **Scene** — grid "9-square" (3x3) ถ่ายฉากเดียวกันหลายมุม + ผัง floor plan 2D คู่กัน กันพื้นที่ผิดตรรกะข้ามช็อต
3. **Props (道具)** — ทั้งของจริง+virtual ทำ turnaround (หมุนรอบวัตถุ) เช่นตัวอย่างกรวยจราจรส้ม
4. **Color board** (เสริมนอก 3 core) — กำหนด hex code + ชื่อสี (Deep Blue, Warm Yellow) ตาม property/scenario ไม่ใช่สุ่มสี

## กฎปิดท้าย

อย่าใช้ asset น้อยเกินไปสำหรับทำทั้งเรื่อง แต่ต้อง keep simple — ความเสถียรมาจากชุด asset ที่เรียบง่าย ไม่ใช่ปริมาณ.

## Corroborates casting rule

Demo footage ใน video เดียวกัน (ตัวอย่าง output จากระบบนี้) — ตัวละครหญิง/ชายที่ใช้โชว์ **หน้าตาดีมากทั้งคู่** แม้เป็นแค่ demo ทั่วไปไม่ใช่ตัวละครหลักดราม่า — ยืนยัน [[feedback-drama-character-casting]] ว่า convention ของวงการนี้ (แม้ tutorial/demo ก็ยังเลือกหน้าตาดี ไม่ใช่ average).

## Related

- [[ai-character-identity-lock]] — หลัก identity lock เดิมที่มีอยู่ (reference sheet), ไฟล์นี้เสริมรายละเอียด 9:16/9-square/prop-turnaround/color-hex ที่ยังไม่มี
- `asset-prompt-builder` subagent — ตัวที่ implement pipeline นี้จริงในงาน production
- [[feedback-drama-character-casting]]

> เกี่ยว: [[char-sheet-2panel-identity-garment]] — ฟอร์แมต 2-panel (close-up identity + faceless front/back garment) สาย fashion/lookbook, เสริมกับ face-3-angle/9-square ในไฟล์นี้
