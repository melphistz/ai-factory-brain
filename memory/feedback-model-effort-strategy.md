---
name: feedback-model-effort-strategy
description: "FEEDBACK — จัดโมเดล/effort ตามประเภทงาน: intelligence-asset (freeze ยาว) = โมเดลฉลาดสุด+ultracode verify · build/production = Opus/Sonnet ถูกกว่าทำได้เท่ากัน · effort สูง=คิดนานไม่ใช่เร็ว"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

Mirko ถามเรื่อง "งานนี้ต้องใช้โมเดลไหน / effort ระดับไหน" ซ้ำหลายรอบ (07-07) — decision framework ที่ตกผลึก:

**แบ่งงาน 2 ประเภทก่อนเลือกโมเดล:**
- **Intelligence-asset (freeze ครั้งเดียว ใช้ยาว):** system prompts, skills, prompt packs, สถาปัตยกรรม/สัญญากลาง, กลั่นความรู้เป็น Gem — คุณภาพขึ้นกับ intelligence ของโมเดลจริง → ใช้**โมเดลฉลาดสุดที่มี + ultracode** (adversarial verify 2 เลนส์: fidelity + operability) เพราะทำครั้งเดียวได้ประโยชน์ตลอด token ไม่ใช่ข้อจำกัด
- **Build/production (ทำซ้ำ, mechanical):** เขียนโค้ด, แก้บั๊ก, สร้าง UI, rename, งานตาม spec ละเอียด → **Opus/Sonnet ถูกกว่าและทำได้เท่ากัน** ไม่ต้องใช้โมเดลแพงสุด · มีเกท verify (build/test/skeptic) การันตีคุณภาพแทน effort

**effort ≠ ความเร็ว:** high→xhigh→ultra = คิดนานขึ้น = **ช้าลง+เปลืองขึ้น** ไม่ใช่เร็วขึ้น · งาน mechanical ที่ spec ชัด+มีเกท verify ใช้ high ก็พอ · อยากเร่ง = **ลด** effort ไม่ใช่เพิ่ม

**ความช้าของ build workflow มาจาก subprocess (npm build/smoke test/tsc) ไม่ใช่โมเดล** — เพิ่ม effort/เปลี่ยนโมเดลไม่ช่วย เพราะ subprocess กินเวลาคงที่ · นี่คือราคาของเกท "ต้อง build+smoke ผ่าน" ซึ่งคุ้มกว่าได้โค้ดเร็วแต่รันไม่ได้

**07-08 (verified จากตรวจโค้ด script จริง — grep+read ยืนยัน): ultracode/Workflow กับ effort เป็นคนละมิติ แยกอิสระ**
- **concurrency (parallel() ในสคริปต์) คือตัวย่นเวลา ไม่ใช่ effort** — effort แค่ทำให้ 1 ครั้งเรียกช้าลง (คิดนานขึ้น) ไม่เปลี่ยนจำนวนงานที่วิ่งพร้อมกันได้ · เช็คจริงพบว่า 2/5 workflow เมื่อคืน (intel-pack-decisions, fleet-skills-audit) **ไม่มี parallel() เลย** (grep=0) — รันเรียงทีละตัวอยู่แล้ว "fan-out เยอะ" ≠ "ขนานทุกจุด"
- **call-count (fan-out × adversarial-verify 2 เลนส์ × conditional-revise) คือตัวขับ token หลัก ไม่ใช่ effort-per-call** — design จริงจำกัด effort='high' ไว้แค่ verify/revise/review เท่านั้น ส่วน draft/scaffold ไม่ตั้งค่า (inherit session) → ต้นทุน $500 เมื่อคืนมาจาก "จำนวนครั้งเรียก" เป็นหลัก
- **บีบเป็น 1 conversation + max/xhigh ทุก call แทน fan-out: ไม่ประหยัดชัดเจน มีโอกาสแพงกว่าเดิม** (จุดที่เคยถูก เช่น draft/scaffold จะแพงขึ้นทันทีทุกตัว) **และคุณภาพต่ำกว่า** สำหรับงานที่มีหลาย unit + ต้องเช็ค coherence ข้าม unit เพราะ (1) เสี่ยง compaction ตัดข้อมูลงานช่วงแรกทิ้งแบบ lossy ตรงจุดที่ step หลังต้องอ้างอิงกลับพอดี (2) effort สูง = คิดนานขึ้นตามเส้นทางเดิม (anchoring bias) ไม่ใช่มุมมองที่สอง จับ blind spot ตัวเองไม่ได้เหมือน agent แยกที่สั่งให้หักล้างจาก context สด — งานเล็ก sequential ล้วน (ไม่มี parallel, ไม่มี cross-unit check) ความต่างแทบไม่มีนัย
- **สรุปสั้น:** ultracode (เปิด Workflow tool) กับ effort (max/xhigh) เป็นคนละสวิตช์ ใช้ร่วมกันได้ (อย่างที่ทำเมื่อคืน) แต่ไม่ใช่ตัวแทนกัน — ultracode คุม "กี่คนช่วยทำ" effort คุม "แต่ละคนคิดลึกแค่ไหน"

**Why:** เผาโมเดลแพง/effort สูงกับงาน build = เปลืองเปล่าไม่ได้คุณภาพเพิ่ม · ใช้โมเดลถูกกับงาน intelligence-asset = เสียโอกาส freeze ของดีถาวร · จัดผิดทางได้แต่ช้าลง

**How to apply:** งานใหม่ให้ถามตัวเองก่อน "นี่ freeze เป็นสมองถาวร หรือ production ซ้ำๆ" → asset=ฉลาดสุด+ultracode+verify 2 เลนส์ · production=Opus/Sonnet+high+เกท build/test · main loop=orchestrate เสมอ (นโยบาย [[claude-subagents]]) · ดู pattern จริงที่พิสูจน์แล้วใน [[smartaihub-drama-series]] (intel-pack freeze ด้วย Fable → Opus/Codex build แอปครอบ) · timeline+ตัวเลข findings จริงของคืนที่ทำ = [[drama-app-fable-ultracode-retrospective]]
