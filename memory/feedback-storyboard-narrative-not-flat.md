---
name: feedback-storyboard-narrative-not-flat
description: "FEEDBACK: storyboard/ซีน ต้องคิดเป็น narrative flow มีมุมกล้อง+การเคลื่อนไหว ไม่ใช่สุ่มโพสยืนทื่อ แบนๆ เรียงช่อง"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4bd13345-39cd-4398-af11-18f6b3b7ac15
---

# FEEDBACK: storyboard = คิดเป็น flow หนัง ไม่ใช่ยืนโพสสุ่มๆ แบนๆ

เวลาออกแบบ storyboard / ซีน (โดยเฉพาะ grid prompt) **ต้องคิดเป็น shot sequence / narrative จริงแบบหนัง** — มีมุมกล้อง, reveal, การเคลื่อนไหว, จังหวะ jump-cut, arc เริ่ม→จบ. **ห้ามทำเป็นช่องยืนโพสตรงๆ สมมาตร arms-at-sides เรียงกันเฉยๆ** = แห้งแล้ง แบน ไม่มีชีวิต.

**Why:** vid04 ([[valenshield-dokkaew-styling-vid04]]) — ร่าง storyboard v1/v2 ทำเป็น grid "ยืน + โพส" ตรงๆ แต่ละช่อง Mirko ตีกลับ "แห้งแล้งมาก / ยืนทื่อๆ / ทำมาสุ่มๆ แบนๆ". ของจริงที่ต้องการมี narrative: POV จากในตู้ที่ปิด → ตู้เปิดเจอเธอมองเข้ามาร้องว้าว → มุมกว้างปัดนิ้วเลื่อนเลือก → จิ้ม → jump-cut เปลี่ยนชุด → โพสเล่นกล้อง 1-2 ท่า → jump ชุดถัดไป → หมุนตัวโชว์ → ยืนสวยจบ. เสียหลายรอบเพราะเริ่มจาก "โพสเรียงช่อง" แทนที่จะคิด flow ก่อน.

**How to apply:**
1. **คิด shot sequence ก่อนเขียน prompt** — ลำดับเล่าเรื่อง มีมุมกล้อง (POV/wide/medium/close), reveal, transition (jump-cut), จุดเริ่ม-จบ. เขียน beat list ก่อน แล้วค่อยแตกเป็น panel
2. **ทุก panel = mid-movement dynamic** — ก้าว/เอน/หมุน/hip pop/สะบัดผม/มือ expressive · **สลับ framing** (full-length + medium + POV/close) ไม่ให้ช่องซ้ำ stance
3. **ใส่ ENERGY block ใน prompt เสมอ** = "ALIVE and IN MOTION like a fashion reel, NOT stiff/symmetric/frozen, avoid arms-at-sides straight-on standing"
4. **ref ที่ลูกค้าให้ = อ่านเป็น template ของ FLOW/กลไก ไม่ใช่แค่ mood/สี** — ดูว่าเขาเปิดเรื่องยังไง เปลี่ยนช็อตยังไง เคลื่อนไหวยังไง แล้วก๊อปโครงนั้น
5. เกี่ยว [[storyboard-gpt-image-to-seedance]] · [[storyboard-knowledge]] · [[ugc-storyboard-sheet-template]] · [[ai-video-realism-hierarchy]] (motion = ตัวคูณ realism)
