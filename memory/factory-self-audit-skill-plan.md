---
name: factory-self-audit-skill-plan
description: "DONE 07-09 — /factory-audit skill built + trial-run verified against live repo. Original plan below, kept as spec reference."
metadata: 
  node_type: memory
  type: project
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# Plan: `/factory-audit` skill สำหรับ ai-factory-brain — ✅ ทำแล้ว (07-09)

**สถานะล่าสุด:** สร้างเสร็จที่ `skills/factory-audit/SKILL.md` (196 บรรทัด, fast-worker Sonnet high) + **trial run จริงกับ repo สด** เจอ findings จริง (overall 69/100): memory ขัดแย้งสถานะ (ไฟล์นี้เองกับ skill-candidates เคยบอก "ยังไม่ทำ" ทั้งที่ตอนนั้นกำลังสร้างอยู่พอดี), 2 skill ใหม่ยัง untracked ใน git, session-state 2 รายการค้างใน volatile section ทั้งที่ DONE แล้ว, orphan wikilink 1 จุด, missing back-link 3 คู่ — แก้ตามด้านล่างนี้แล้วในรอบ sync เดียวกัน

โครงแผนเดิม (เก็บไว้เป็น spec อ้างอิง):

## ที่มา
07-08: อ่าน repo [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS) (generic solopreneur AI-OS starter kit ของคนอื่น — ไม่เกี่ยวกับ video/ad โดยตรง) เจอไอเดียที่น่าเอามาปรับใช้: skill `/audit` ของเขาให้คะแนน 0-100 ระบบ AI ของตัวเองแบบ 4 มิติ (Context/Connections/Capabilities/Cadence) แล้วจัดอันดับช่องโหว่ด้วย **leverage = คะแนนที่เสีย × ตัวคูณผลกระทบ** ไม่ใช่แค่ list gap เฉยๆ

**07-08 (เพิ่ม):** อ่าน [Karpathy's LLM-Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (เอกสารเชิงแนวคิด ไม่มีโค้ด/template จริง) — พบว่าระบบ memory ของเราตรงกับ pattern "raw sources → wiki (markdown + `[[wikilink]]`) → schema (CLAUDE.md)" ของเขาเกือบเป๊ะอยู่แล้ว (MEMORY.md = index.md, กติกา "log updates" = Ingest, การตอบคำถามแล้วเซฟผลลัพธ์กลับ = Query) **ช่องว่างเดียวที่ทั้งสองแหล่ง (AIS-OS + Karpathy) ชี้ตรงกันโดยไม่รู้จักกัน = ไม่มี "Lint" operation** (เช็กสุขภาพ wiki: ขัดแย้งกันเอง/ไฟล์กำพร้า/ลิงก์ขาด/ล้าสมัย) → เสริมเข้าขอบเขตของ skill นี้แทนที่จะแยกเป็นงานใหม่

## ทำไมถึงน่าทำ
เทียบ 4 มิติกับ ai-factory-brain ตอนนี้: **Context** (memory ละเอียดมาก) กับ **Capabilities** (fleet 8 + skill 3 ที่เพิ่ง audit ไป 07-07) แข็งแรง แต่ **Cadence แทบไม่มีเลย** — ไม่มี automation รันเองตามกำหนด ทุกอย่างเริ่มเมื่อ Mirko เปิด session เอง นี่คือช่องว่างจริงที่ repo อื่นชี้ให้เห็น

## ขอบเขตที่วางแผนไว้
Skill เดียว (ไม่ใช่หลายไฟล์แบบ intel-pack) — อ่านสถานะ brain repo จริงแล้วให้คะแนน+รายงาน แบ่ง 2 กลุ่มเช็ก:

**กลุ่ม AIS-OS-style (คะแนน 4 มิติ + leverage ranking):**
- memory ไหน stale (เทียบ timestamp/originSessionId เก่าเกินไป)
- fleet/skill ตัวไหนยังไม่เคยผ่าน audit (เทียบกับรอบ 07-07 ที่ทำไปแล้ว)
- session-state ค้างที่ควร archive (ตรง MEMORY.md section "Session State (volatile)")
- sync status (มี commit ค้าง ไม่ sync ไหม)

**กลุ่ม Karpathy-style (Lint — เช็กสุขภาพ wiki):**
- **orphan `[[wikilink]]`** — ลิงก์ชี้ไปชื่อไฟล์ที่ไม่มีจริงในระบบ
- **orphan files** — ไฟล์ memory ที่มีอยู่จริงแต่ไม่ถูกอ้างใน MEMORY.md index เลย
- **contradictions** — สองไฟล์ memory บอกสถานะ/ข้อเท็จจริงเดียวกันไม่ตรงกัน (เช่นไฟล์หนึ่งบอก "เสร็จแล้ว" อีกไฟล์บอก "ยังไม่เริ่ม")
- **missing back-links** — ไฟล์ A ลิงก์ไป B แต่ B ไม่ลิงก์กลับ A ทั้งที่เนื้อหาเกี่ยวกันชัดเจน (ตรวจแบบ heuristic ไม่ต้องเป๊ะ)

## Model/cost ที่ประเมินไว้
**Sonnet พอ ไม่ต้อง Fable/ultracode** เพราะเป็นการเขียนไฟล์เดียว (skill markdown ~200-500 บรรทัด) + ทดลองรันจริง 1 รอบ ไม่ใช่ของที่ freeze ใช้ผลิตซ้ำเป็นพันครั้งแบบ intel-pack เลยไม่ต้อง adversarial-verify 2 เลนส์ (ดู [[feedback-model-effort-strategy]]) — ประเมิน **~50-150K tokens** ถูกกว่างาน UI redesign ของ drama-app อีก ทำเป็น Agent เดียวจบได้ ไม่ต้องเปิด Workflow เต็มรูปแบบ

## สถานะ
ยังไม่เริ่มทำ — เซฟไว้รอคิว (Mirko ขอ save ไว้ก่อน 07-08) ไม่ผูกกับ drama-app หรือ Fable quota ใดๆ เริ่มได้ทันทีเมื่อพร้อม
