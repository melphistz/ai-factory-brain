---
name: rule-use-installed-skills
description: "RULE (Mirko สั่งตรง 07-14): ทำงานที่มี skill/agent ตรงอยู่แล้ว ต้องเรียกใช้ ห้ามเขียนสดใน main — ลงทุน build+audit ไป token เยอะแล้ว ต้องคุ้ม"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4bd13345-39cd-4398-af11-18f6b3b7ac15
---

# RULE: งานที่มี skill/agent ตรง → ต้องใช้ ห้ามเขียนสดเอง

**เริ่มงานใดๆ ที่ตรงกับ skill ที่ติดตั้ง / agent ใน fleet → เรียกใช้ตัวนั้น ไม่เขียนสดใน main conversation.**

**Why (คำ Mirko ตรงๆ 07-14):** "คราวหน้าทำงานต้องใช้ skill ที่เกี่ยวข้อง เพราะทำมาแล้ว burn token ไปเยอะ" — จับได้ว่าตลอด vid04 ผมเขียน image prompt ~10 ตัว + Seedance prompt + storyboard + teardown **ด้วยมือใน main ทั้งหมด** ทั้งที่มี `image-prompt-writer` / `seedance-2-pro-director` / `video-prompt-builder` / `storyboard-prompter` / `teardown-analyst` ที่ build+Fable-audit มาแล้ว. ของที่ลงทุนแพงต้องถูกใช้ ไม่ใช่นอนเป็น context tax.

**How to apply:**
1. **ตอนเริ่ม task ใหม่ → เช็คก่อนเสมอ:** [[skills-cheatsheet]] + รายการ skill/agent — มีตัวตรงไหม? มี = เรียกใช้เลย
2. mapping หลัก (จำ):
   - image prompt เดี่ยว → skill `image-prompt-writer`
   - Seedance single-shot → skill `seedance-2-pro-director`
   - brief → วางแผน ad ทั้งตัว → skill `video-prompt-builder`
   - screenplay → shotlist → skill `shotlist-builder`
   - เนื้อเพลงไทย → skill `thai-lyric-writer`
   - storyboard → prompt kit → agent `storyboard-prompter` · asset kit → `asset-prompt-builder`
   - teardown โฆษณา/ref → agent `teardown-analyst` · QA gen → `qa-inspector` · copy/hook → `script-hook-writer`
3. **ข้อยกเว้นเดียว:** แก้เล็กกลาง iteration สด (user ตีกลับทีละจุดในแชท) = ต่อใน main ได้ — แต่**รอบแรกของ deliverable ต้องผ่าน skill/agent**
4. คู่กับ [[rule-search-prompt-index-first]] (ค้นคลังก่อนเขียน) — สองกฎนี้ทำงานด้วยกัน: ค้น reference → route เข้าเครื่องมือ
5. โยง [[claude-subagents]] policy เดิม: "main = orchestrate เท่านั้น" — กฎนี้คือการบังคับใช้จริง
