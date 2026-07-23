---
name: sec-car-transport-project
description: งานลูกค้า SEC Car Transport — AGV valet parking robot (VMR-CR5300GAW2) ทำเอกสาร/สื่ออธิบายการทำงาน
metadata: 
  node_type: memory
  type: project
  originSessionId: 3ccb8148-4343-4f76-98a3-4d73df154e2a
  modified: 2026-07-23T11:09:57.911Z
---

**SEC Car Transport** — งานลูกค้าเกี่ยวกับ **AGV valet parking robot รุ่น VMR-CR5300GAW2** (Smart Vehicle Handling Robot). ไฟล์งานอยู่ `/Volumes/WONYOUNG/SEC Car Transport/`.

**ตัวสินค้า:** หุ่นขนย้ายรถอัตโนมัติ — จับที่ **ล้อ ไม่แตะตัวถัง**, ไม่ต้องมี pallet. Split modular = 2 แผ่นแยก ปรับตาม wheelbase. สเปก: 3000 kg · Laser SLAM (ไม่ต้องฝัง magnet/QR ที่พื้น) · 24h.

**กลไกจับล้อ (จาก 4 ภาพ top-view ที่ Mirko ทำ + คลิป demo เจ้าอื่น RXB Fours):**
1. หุ่นเลื่อนเข้าใต้ท้องรถ 2. โมดูลแยกออกจากกัน ไปล้อหน้า/หลัง + กางแท่งเหล็ก 3. เลื่อนจนแท่งขนาบล้อพอดี 4. แขน (มีลูกกลิ้ง) หนีบล้อจากหน้า-หลัง บีบเข้าหากัน รีดล้อลอยขึ้น → ล้อพ้นพื้น เคลื่อนอิสระ. มี clamping-pressure sensor + ไฟ LED เขียว (safety status ต่อโมดูล).
- VMR: เข้าเป็นก้อนไปกลางคันก่อน → แล้วแยกโมดูล. คลิป RXB: แยกโมดูลตั้งแต่ก่อนเข้าจากด้านหน้ารถ. กลไกปลายทางเหมือนกัน.
- use case กว้างกว่าจอดรถ: คลิป demo เอาไปขนรถเข้าห้องพ่นสี (paint booth) ในโรงงาน + มี software dashboard (task reception → monitoring → loading → movement).

**เสร็จแล้ว (07-23):**
- `VMR-CR5300GAW2-คำอธิบายการทำงาน.md` — เอกสาร 7 ขั้นตอน + สเปก + safety (อยู่ในโฟลเดอร์ client)
- `loading-frames_0.15-0.22/` — 16 เฟรม (768px, ทุก 0.5วิ) แกะจากคลิป demo YouTube `nmOzHZiZU7c` ช่วง vehicle loading (f2@0:16 = จังหวะแยกโมดูลชัดสุด)

**Next (ยังไม่สั่ง):** เอกสารยังไม่รวมข้อมูลใหม่จากคลิป (software dashboard + use case โรงงาน) · อาจทำสื่อ AI video อธิบายการทำงาน (ยังไม่ยืนยัน format/ปลายทาง).

ref เครื่องมือดูคลิป = [[watch-skill-claude-video]]
