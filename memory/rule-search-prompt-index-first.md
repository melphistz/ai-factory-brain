---
name: rule-search-prompt-index-first
description: "RULE: ก่อนเขียน image/video prompt ใหม่ทุกครั้ง ต้องค้น prompt-index (internal, 8.7k prompts) หา reference/สูตรใกล้เคียงก่อน — คลังมีไว้ใช้ ไม่ใช่แค่เก็บ"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4bd13345-39cd-4398-af11-18f6b3b7ac15
---

# RULE: ค้น prompt-index ก่อนเขียน prompt ใหม่เสมอ

**ก่อนเขียน image/video prompt ใหม่ (ทุก skill/ทุกงาน) → ค้นคลัง prompt-index หา reference ที่ใกล้เคียงก่อน** แล้วค่อยเขียน — เอาโครง/คำ/เทคนิคจากของจริงที่ได้ผลมาประกอบ ไม่ใช่เขียนสดจากศูนย์ทุกครั้ง.

**Why:** Mirko สร้างคลัง MeiGen 8,776 prompts ([[meigen-prompt-dataset]]) แต่พบว่า (13 ก.ค.) ตลอดงาน vid04 ผมไม่เคยเปิดใช้เลยสักครั้ง — เพราะคลังอยู่บน external (FDA หลุดบ่อย) + เป็น gallery.html ที่ query ไม่ได้ + ไม่มีกฎให้ใช้. คลังใหญ่แต่ไม่ถูกใช้ = ศูนย์เปล่า.

**How to apply:**
1. **index อยู่ internal เข้าได้เสมอ:** `~/ai-factory-brain/tools/prompt-index/prompt-index.jsonl` (8.7k prompts: meigen 7.4k + youmind 993 + seedance 363, text-only 16MB)
2. **วิธีค้น:** `cd ~/ai-factory-brain/tools/prompt-index && python3 search.py [-n N] [-f] [-s meigen|youmind|seedance] term1 term2` (AND terms, ranked ด้วย frequency+likes) — หรือ grep JSONL ตรงๆ
3. ใช้ทั้งตอน: เขียน prompt ใหม่ · หา style stack · หาคำ/technique เฉพาะทาง (macro, product, UGC, fashion...) · เช็คว่าสูตรไหน likes สูง
4. **update = อัตโนมัติ** — `sync.py` (บน external) export index ใหม่ให้เองทุกครั้งที่ sync, ไม่ต้องอัพมือ 2 ที่ · ความสดดูที่ `index-meta.json`
5. เจอของดี → ดึงโครงมาปรับ ไม่ก๊อปดื้อๆ (กฎ originality ใน [[skill-candidates-image-lyrics]] ยังใช้)
