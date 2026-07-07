# drama-app — STATE

- **โปรเจกต์:** สร้างระบบ web app ผลิตซีรีส์ละครแนวตั้งของเราเอง (ต้นแบบ = case study `memory/smartaihub-drama-series.md`)
- **stage (2026-07-07): INTEL PACK = READY ✅** — `intel-pack/` ครบ 9 ไฟล์ (00-contracts → 08-qa-gates) ผ่าน ultracode เต็มวง: draft → skeptic 2 เลนส์/ไฟล์ → revise (64 findings/17 critical) → coherence ข้ามไฟล์ → apply คำตัดสิน 3 ข้อ → recheck ตาใหม่ (แก้เศษตกค้าง 11 จุดใน 05/08) — เขียนด้วย Fable ทั้งหมดก่อนโควต้าหมด
- **คำตัดสินสถาปัตยกรรมที่ล็อกแล้ว (อย่าเปิดใหม่โดยไม่มีเหตุ):**
  1. identity anchor เต็มก้อน verbatim = เฉพาะ **keyframe prompt** · video prompt (i2v) ใช้ **short positive lock** 1 บรรทัด (ข้อยกเว้น: ช็อต reference-mode ใช้ anchor ย่อกลาง)
  2. **LedgerEntry มี single writer = ชั้น ledger ของแอป** — endpoint 02 ส่งแค่ "ledger:" flags, 04 ส่ง ledger_draft เป็นวัตถุดิบ
  3. **state_locks = object keyed** (ห้าม array) — validator diff ข้ามช็อตรายคีย์
- **known gap (cosmetic ไม่ block):** ประโยค single-writer ใน 00 §5 ยังไม่เอ่ยถึง ledger_draft (wardrobe) ของ 04 ชัดๆ — ความหมายไม่ขัด แก้ตอน build ได้
- **ถัดไป:** (1) Mirko รีวิว pack (เริ่มจาก 00-contracts + 07-video-prompt) → (2) dispatch **Opus/Codex สร้างตัวแอป** (UI + DB Supabase + call LLM/Higgsfield/kie.ai) โดยใช้ intel-pack เป็น system prompts ตรงๆ — **ไม่ต้องใช้ Fable อีก**
- **กติกา:** ไฟล์โปรเจกต์อยู่ในโฟลเดอร์นี้เท่านั้น · 1 ไฟล์ intel-pack = 1 endpoint/skill · แก้ pack = ต้องรัน recheck ข้ามไฟล์ซ้ำ
