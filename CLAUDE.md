# AI Factory Brain — คู่มือ orchestrator (โหลดอัตโนมัติทุก session)

ระบบนี้ = โรงงานผลิต AI video/ads แบบ **prompt-first / manual-gen**: Claude คิด prompt + QA + timeline, **Mirko เจนภาพ/วิดีโอเองทั้งหมด** ความรู้อยู่ `memory/` (Obsidian vault + Claude memory ก้อนเดียวกัน)

## กติกาเหล็ก (ทุกโมเดล ทุก session)

1. **Main loop = orchestrate เท่านั้น** (นโยบาย Mirko — ไม่ว่า main จะเป็นโมเดลไหน): ห้ามเขียน copy/prompt/QA เองใน main loop — dispatch ให้ subagent ตามตารางใน `projects/FF_factory/AGENT_OPS.md` เสมอ
2. **ห้ามเรียก generate_*/ยิงเครดิต MCP ใด ๆ** — การเจนทั้งหมดเป็นของ Mirko (manual) จนกว่า Mirko จะประกาศเปลี่ยนโหมดเอง
3. **ทุก output ของ subagent เซฟลงไฟล์ job ทันทีทั้งดุ้น** (กัน context หาย) แล้วค่อยสรุปสั้นให้ Mirko
4. อยากแก้งานของ agent → dispatch กลับไปที่ agent เดิมพร้อม feedback ไม่แก้เองใน main
5. งานเพลง/กวีไทย → ต้องวางสัมผัสจริงจังตาม `memory/thai-lyric-writing.md` + โชว์ rhyme map

## เปิดงานยังไง

- **งาน factory/ad ทุกชนิด:** อ่าน `projects/FF_factory/AGENT_OPS.md` ก่อน — มี flow เต็ม + ORCHESTRATION PROTOCOL (บทสั่งงาน agent ต่อขั้น copy ไปใช้ได้เลย)
- **job ad ใหม่:** ก๊อป `projects/FF_factory/jobs/_template/` → ตั้งชื่อ job → เดิน protocol ข้อ 1
- **งานหนัง/MV:** โปรเจกต์อยู่ `projects/<ชื่อ>/` (โครง 01-brief → 05) — flow เดียวกัน ใช้เลขช็อตแทน module tag
- **Mirko โยนภาพ/คลิปกลับมา:** ดู protocol หัวข้อ "เมื่อภาพกลับมา" ใน AGENT_OPS — QA ก่อน แล้วค่อยขั้นถัดไป
- **ต่อยอด/automation:** ห้ามเริ่มเองจนกว่า dry run จะผ่านเกณฑ์ (อยู่ท้าย AGENT_OPS)

## Fleet (รายละเอียด+ตารางความยาก = `memory/claude-subagents.md`)

opus: storyboard-prompter · asset-prompt-builder (2 เฟส) · script-hook-writer · deep-reasoner
sonnet: qa-inspector · teardown-analyst · timeline-builder · fast-worker

## โครง repo

`memory/` ความรู้+index (MEMORY.md) · `agents/` subagent จริง (junction เข้า ~/.claude) · `skills/` skills จริง · `projects/` งานทั้งหมด · `tools/` สคริปต์ (mac เป็นหลัก) · sync อัตโนมัติผ่าน hooks บน Windows / `./sync.sh` บน mac

ไฟล์หนัก per-machine: mac `~/Desktop/Ads/` · Windows `D:\Claude\90-Assets\` (vault เก่า D:\Claude เกษียณแล้ว — อย่าอ่านเป็นความรู้)
