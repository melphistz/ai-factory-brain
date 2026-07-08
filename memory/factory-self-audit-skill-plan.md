---
name: factory-self-audit-skill-plan
description: "PENDING (07-08) — plan to build a /factory-audit skill that scores ai-factory-brain's own health (memory freshness, fleet/skill audit status, stale session-state), inspired by AIS-OS repo's /audit pattern"
metadata: 
  node_type: memory
  type: project
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# Plan: `/factory-audit` skill สำหรับ ai-factory-brain — ยังไม่ทำ

## ที่มา
07-08: อ่าน repo [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS) (generic solopreneur AI-OS starter kit ของคนอื่น — ไม่เกี่ยวกับ video/ad โดยตรง) เจอไอเดียที่น่าเอามาปรับใช้: skill `/audit` ของเขาให้คะแนน 0-100 ระบบ AI ของตัวเองแบบ 4 มิติ (Context/Connections/Capabilities/Cadence) แล้วจัดอันดับช่องโหว่ด้วย **leverage = คะแนนที่เสีย × ตัวคูณผลกระทบ** ไม่ใช่แค่ list gap เฉยๆ

## ทำไมถึงน่าทำ
เทียบ 4 มิติกับ ai-factory-brain ตอนนี้: **Context** (memory ละเอียดมาก) กับ **Capabilities** (fleet 8 + skill 3 ที่เพิ่ง audit ไป 07-07) แข็งแรง แต่ **Cadence แทบไม่มีเลย** — ไม่มี automation รันเองตามกำหนด ทุกอย่างเริ่มเมื่อ Mirko เปิด session เอง นี่คือช่องว่างจริงที่ repo อื่นชี้ให้เห็น

## ขอบเขตที่วางแผนไว้
Skill เดียว (ไม่ใช่หลายไฟล์แบบ intel-pack) — อ่านสถานะ brain repo จริงแล้วให้คะแนน+รายงาน เช่น:
- memory ไหน stale (เทียบ timestamp/originSessionId เก่าเกินไป)
- fleet/skill ตัวไหนยังไม่เคยผ่าน audit (เทียบกับรอบ 07-07 ที่ทำไปแล้ว)
- session-state ค้างที่ควร archive (ตรง MEMORY.md section "Session State (volatile)")
- sync status (มี commit ค้าง ไม่ sync ไหม)

## Model/cost ที่ประเมินไว้
**Sonnet พอ ไม่ต้อง Fable/ultracode** เพราะเป็นการเขียนไฟล์เดียว (skill markdown ~200-500 บรรทัด) + ทดลองรันจริง 1 รอบ ไม่ใช่ของที่ freeze ใช้ผลิตซ้ำเป็นพันครั้งแบบ intel-pack เลยไม่ต้อง adversarial-verify 2 เลนส์ (ดู [[feedback-model-effort-strategy]]) — ประเมิน **~50-150K tokens** ถูกกว่างาน UI redesign ของ drama-app อีก ทำเป็น Agent เดียวจบได้ ไม่ต้องเปิด Workflow เต็มรูปแบบ

## สถานะ
ยังไม่เริ่มทำ — เซฟไว้รอคิว (Mirko ขอ save ไว้ก่อน 07-08) ไม่ผูกกับ drama-app หรือ Fable quota ใดๆ เริ่มได้ทันทีเมื่อพร้อม
