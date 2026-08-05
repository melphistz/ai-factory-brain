---
name: cinedance-v4-seedance-system
description: CINEDANCE V4 — ระบบเขียน prompt Seedance 2.0/Higgsfield ทางเลือก (แยกจาก seedance-2-pro-director เดิม) เจอในไฟล์ SEC Car Transport vid ref เอามาศึกษาเป็นความรู้เสริม
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3f2542e5-4024-4852-bd76-5ec9e3468e71
  modified: 2026-08-05T03:08:01.877Z
---

# CINEDANCE V4 — Seedance 2.0 Prompt Director System

Source: `/Volumes/WONYOUNG/SEC Car Transport/vid ref/CINEDANCE HIGGSFIELD SKILL.md` (external drive, เจอ 08-05)

ระบบ prompt-director แบบเดียวกับ [[seedance-2-pro-director-skill]] แต่คนละสำนัก — เก็บไว้ศึกษา/หยิบเทคนิคมาผสม ไม่ใช่ skill ที่ install จริง

## จุดเด่นที่ต่างจาก skill ที่ใช้อยู่

**4-D methodology (silent, ไม่โชว์ user):** Deconstruct (ดึงแค่ shot ปัจจุบัน ตัด @tag/character ที่ไม่ใช้ทิ้ง) → Diagnose (เช็ค failure risk ล่วงหน้า เช่น first frame ว่าง, gaze reverse, left/right flip) → Develop (ลำดับ 16 ส่วนตายตัว) → Deliver (output แค่ prompt สุดท้าย ไม่โชว์ reasoning/QA/checklist)

**Optics เป็น diagonal FOV (องศา) ไม่ใช่ mm/f-stop** — ต่างจาก skill เดิมที่ใช้ mm (24/35/50/85mm):
- 47° = standard normal (documentary action)
- 84° = classic wide (environmental, camera 1-1.5m)
- 107° = wide rectilinear (extreme foreground, camera 0.5-0.8m)
- 29° = short telephoto portrait (compress bg, camera 4-6m)
- 18° = classic telephoto (tight emotional CU)
- 8° = super-telephoto observation (paparazzi/wildlife feel, camera 20-25m, ต้อง foreground occlusion)
- กฎ: ห้ามผสม content class (portrait+environment+macro) ใน beat เดียว — lens จะ drift

**Landmark proximity lock** — ห้ามใช้คำอ่อน (near/around/beside/nearby) ต้องระบุระยะจริง: "within 1 meter", "touching", "boots inside root circle", "hand on handle"

**Format mode decision (silent):** default = SINGLE CONTINUOUS TAKE เสมอ เปลี่ยนเป็น MULTI-SHOT เฉพาะเมื่อ user ขอ cut/montage/insert หรือ blocking ทำใน camera position เดียวไม่ได้จริงๆ — ตรงข้าม intuition ที่มักคิด multi-shot ก่อน

**Cut types จำกัดแค่ 6 แบบ:** HARD CUT / SMASH CUT / MATCH CUT / INSERT CUT / REVERSE CUT / WHIP CUT — ห้าม fade/crossfade/dissolve เว้น user ขอ

**Lighting priority lock** — แสงเป็น constraint ไม่ใช่ decoration โดยเฉพาะ backlit/contre-jour: "camera stays on shadow side", "face falls into crushed shadow", "no frontal key, no beauty fill" — ถ้า gen ก่อนหน้าแบนไป ให้เพิ่ม "exposed for the backlight, not for the face"

**Physics lock ละเอียดกว่า** — แยกเป็น walking (heel contact/hip shift/toe push-off), running, weapons (wrist angle reacts to mass), liquids (parabolic arcs, viscosity), particles (wind direction, 3 depth layers)

**Negative constraints = local inline เท่านั้น** ไม่ทำ standalone block ใหญ่ท้าย prompt (หลักการเดียวกับ skill เดิม "positive over negative")

## ตัดสินใจ: หยิบมาผสมส่วนไหนดี

จุดที่คุ้มเอามาเสริม skill เดิม:
1. **FOV เป็นองศาแทน mm** — Seedance ตอบสนอง observable optical outcome ดีกว่า metadata ตัวเลข mm/f-stop (อ้างว่า verified) — น่าทดลอง
2. **Format mode decision default = single take** — กัน over-cutting โดยไม่จำเป็น
3. **4-D silent diagnose step** — เช็ค failure risk ก่อนเขียนจริง (gaze reverse, left/right flip, first-frame empty) เป็น checklist ที่ดี เอามาเสริม QA checklist เดิมได้

ยังไม่ merge เข้า skill จริง — รอ user สั่งถ้าจะเอาไปทดสอบ/รวม

## เทียบกับ skill seedance-2-pro-director (08-05)

**เหมือนกัน:** positive>negative constraint, character anchor block, timecode shot, reference-role discipline, hand-fix/contact-point grounding, style=visual noun ไม่ใช่ adjective

**CINEDANCE V4 แน่นกว่า:**
- Format decision step: default = SINGLE TAKE เสมอ, ขยับ multi-shot เฉพาะมีเหตุผล (skill เราไม่มี decision step นี้ มักตาม user ตรงๆ)
- Cut type จำกัด 6 แบบ (HARD/SMASH/MATCH/INSERT/REVERSE/WHIP) ห้าม fade/dissolve นอกขอ
- Diagnose step ก่อนเขียน (silent) เช็ค failure risk ล่วงหน้า — proactive กว่า QA ท้ายสุดของ skill เรา
- Landmark proximity: ห้ามคำอ่อน (near/around/beside) บังคับระยะจริง
- Lighting priority lock แยกหัวข้อชัด + escalation line ถ้า gen แบน
- Context isolation: ตัดคำ "previous/continues/as above" ออกทุก shot กัน leak

**skill เราแน่นกว่า:** under-direct acting formula + emotional-arc micro-beat, Marco freestyle mode, host facts จริง (Higgsfield/kie.ai fps/duration/char-cap/no-seed), on-screen text template, hyperzoom morph-fix

**แผนถ้าจะ merge (ยังไม่ทำ):** ดึง 3 จุด — FOV องศาแทน mm (ทดลองก่อน), default-single-take decision step, silent diagnose-before-write checklist. ไม่ดึง: ซ่อน QA/blocking map ทั้งหมด (skill เราตั้งใจโชว์ให้ user เช็ค เหมาะกับ workflow นี้กว่า)
