---
name: seedance-buffer-microgesture
description: "Seedance 2.5 craft tips from the Galatea page (user-shared 2026-11-11): Head/Tail Buffer (0.5–2s padding + motion hand-off between separately generated clips) and Micro-Movement / Micro-Gesture / natural blinking as secondary action — with per-shot blink caution"
metadata:
  type: reference
---

# Buffer + Micro-Movement / Micro-Gesture (Seedance 2.5)

ที่มา: โพสต์ Tip จากเพจ Galatea (user ส่งมา 11-11) — ผู้เขียนบอกเองว่าเป็นประสบการณ์ส่วนตัว ไม่ใช่สูตรรับประกัน · ใช้จริงแล้วใน EVIL ELLE `00_bible/director_notes_v1.md` §4.1 + §6 ([[evil-elle-project]])

## 1. Buffer — เผื่อเวลาก่อน/หลัง Main Action

- **Head buffer** = ต้นช็อตเล่น movement/สถานะเดิมที่ช็อตก่อนส่งมาต่ออีกนิด (เดิน/วิ่ง/หันตัว/กล้องเคลื่อน) ก่อนเข้า action ใหม่ → ตอนตัดมี motion overlap ให้เลือกจุด cut · ลดความรู้สึก "เจนแยกคลิป"
- **Tail buffer** = main action ต้อง**จบก่อนคลิปหมด** แล้วปล่อย follow-through: ตัวละครตั้งหลัก, ผม/เสื้อผ้ายังเหวี่ยง, ฝุ่น/effect จาง, กล้องเลื่อนต่อนิด, reaction สั้น ๆ → กัน AI ทำ action ไม่ทันจบ/โดนตัดกลางทาง
- **Hand-off design:** ท้ายช็อตให้ตัวละคร/กล้อง*เริ่ม* motion ที่ช็อตหน้าจะรับต่อ (เริ่มหัน, เริ่มออกจากตำแหน่ง, มองทิศใหม่, กล้องเริ่ม track ทิศเดียวกับช็อตหน้า)
- **คิด 3 คำถามต่อช็อต:** ช็อตนี้เกิดอะไร? · ช็อตก่อนส่งอะไรเข้ามา? · ช็อตนี้ส่งอะไรต่อ?
- **ยาวเท่าไหร่:** ขั้นต่ำ ~0.5–1s · movement เยอะ/กล้องแรง ~1–2s · ต้นทุน = เจนยาวขึ้น (action 8s → เจน 10s แล้วใช้จริงแค่ส่วนที่ต้องการ)
- **ไม่ต้องใส่ทุกช็อต:** ช็อตที่ตั้งใจ cut กระแทก/เริ่มทันที ไม่ใส่ head buffer
- **House add:** บทพูดต้องจบก่อน tail buffer เริ่ม (กันเสียงขาดกลางคำ) · คู่กับ Thai pacing "จบพูดใน 5–6s ของ 8s" ใน [[seedance-knowledge]] — หลักเดียวกัน

## 2. Micro-Movement / Micro-Gesture = Secondary Action

แนวคิดจาก animation principle *Secondary Action*: มนุษย์ไม่ได้มีแค่ primary action แต่มีการขยับย่อยคู่กันเสมอ

- **Micro-Movement:** หายใจจนอก/ไหล่ขยับ · ถ่ายน้ำหนักขาข้างหนึ่ง→อีกข้าง · ขยับศีรษะเล็กน้อยขณะฟัง
- **Micro-Gesture:** เหลือบตา · ขมวดคิ้วเล็กน้อย · เม้มปาก · ขยับนิ้วตอนประหม่า
- **Natural blinking:** คนจริง ~15–20 ครั้ง/นาที ไม่เป็นจังหวะตายตัว · AI มักลืมตาค้างทั้งช็อต (โดยเฉพาะตัวที่ไม่พูด/ไม่ทำอะไร) → ดูแข็ง
- **ตัวอย่างประโยค (verbatim):** แทน "The character stands and speaks." ใช้ `Subtle breathing, natural eye movements, slight head tilts, occasional natural blinking, small facial reactions, and subtle shifts in body weight while speaking.`
- หลัก: บอก AI ไม่ใช่แค่ "ทำอะไร" แต่ "มีปฏิกิริยาอย่างไรระหว่างทำ"

## House cautions (จากงานจริง)

- **ห้ามสั่ง blinking/micro-motion รวมทั้งคลิป** เมื่อมีตัวละครที่ต้องนิ่ง (หุ่นเชิด/สิ่งเหนือธรรมชาติ/ช็อตน่ากลัว) → สั่ง**ทีละช็อต ทีละคน** ว่าใครกะพริบ/ไม่กะพริบ
- **ใช้ความต่างเป็นเครื่องมือ:** ใส่ micro-motion เต็มให้คนปกติ แล้ว**ตัดเป็นศูนย์**ในจังหวะที่ตัวร้ายต้องน่ากลัว → คนดูขนลุก (EVIL ELLE director notes §4.1)
- ตรงกับ realism hierarchy ข้อ 5 human micro-behavior ใน [[ai-video-realism-hierarchy]] · ระวังขัดกับ `shotcaller-v2` "No mouth mechanics for generated speech" — micro-gesture ใบหน้า/ตัวได้ แต่ไม่ต้องสั่งรูปปากตอนพูด
