---
name: claude-subagents
description: "Installed Claude Code subagents + MODEL POLICY — Fable = orchestrate/plan only, subagents = Opus/Sonnet by task difficulty (never Fable)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f495e44a-04e5-4cac-94ed-83e0ab9d81c9
---

# Claude Code Subagents — fleet 8 ตัว (2026-07-05 · **Fable audit ยกระดับทั้ง fleet 07-07**)

> 07-07 (วันสุดท้าย Fable): audit→revise→verify ทุกตัว + coherence ข้าม fleet — อัดความรู้ verified ล่าสุด (กฎทองมุมกล้อง, under-direct ฉบับแก้, short-lock i2v, budget 1,800, ลำดับ QA tells, hook 4 ประเภทสายละคร) เข้า agent ที่เกี่ยว · 3 skills ก็ถูกยกระดับ (shotlist-builder ถอน claude.ai deps เก็บตก) · `projects/_template` จัดโครงตรง AGENT_OPS แล้ว · diff ทั้งหมดใน git 07-07

ไฟล์จริงอยู่ `<brain repo>/agents/` (junction เข้า `~/.claude/agents` ทั้งสองเครื่อง) — ใช้ได้ทุก project · ทุกตัวอ่าน brain ด้วย dual path (mac `/Users/working/ai-factory-brain/` · Windows `D:\ai-factory-brain\`) · **orchestration playbook เต็ม = `projects/FF_factory/AGENT_OPS.md`** (โหมด v2 prompt-first/manual-gen: flow 5 ขั้น, hand-off, fan-out)

## MODEL POLICY (Mirko กำหนด 2026-07-03 · ปรับ 2026-07-05: ไม่ผูกกับ Fable)

**Main loop = orchestrate เท่านั้น ไม่ว่าโมเดลไหน** (Fable กำลังจะหมดสิทธิ์ใช้ — ต่อไป main เป็น Opus ก็ใช้กติกาเดิม): ห้ามเขียน copy/prompt/QA เองใน main, dispatch ตาม `projects/FF_factory/AGENT_OPS.md` PROTOCOL · โมเดล main ห้ามใช้เป็น subagent · subagent จัดตามความยาก: ยาก = Opus, tool-driven/ง่าย = Sonnet · แผนทั้งหมดวางจบแล้ว — session ใหม่อ่าน CLAUDE.md (โหลดเอง) + AGENT_OPS.md แล้วรันได้เลยไม่ต้องวางแผนใหม่

| ยาก→ง่าย | งาน | agent | model |
|---|---|---|---|
| 1 | storyboard/ภาพจริง → video prompt + continuity | storyboard-prompter | opus |
| 2 | 2 เฟส: A = brief → prompt char (portrait+sheet)/scene + GEN ORDER · B = ภาพจริงโยนกลับ → storyboard frame prompts (@Image map) | asset-prompt-builder ✅ 07-05 | opus |
| 3 | copy ไทย / hook bank / SPINE script (modular contract) | script-hook-writer ✅ 07-05 | opus |
| 4 | debug pipeline / architecture | deep-reasoner | opus |
| 5 | QA 2 เกท: ภาพก่อนไปต่อ + คลิปหลังเจน (ffmpeg + ssim, ดู pixel จริง) | qa-inspector ✅ 07-05 | sonnet |
| 6 | teardown โฆษณาคู่แข่ง + feedback loop ผลแอด | teardown-analyst ✅ 07-05 | sonnet |
| 7 | timeline JSON ครอบโมดูล (J-cut/captions/fx → Remotion/Hyperframe) | timeline-builder ✅ 07-05 | sonnet |
| 8 | mechanical (rename/format/simple edit) | fast-worker | sonnet |

กฎร่วมทุกตัว: no generation/no credits (โหมดปัจจุบัน Mirko เจน manual ทั้งหมด) · final message = deliverable เดียวที่ orchestrator เห็น · agent ใหม่มีผล session ถัดไป (โหลดตอนเริ่ม session)

- **storyboard-prompter** — model **Opus**. แปลง storyboard → ต่อ shot: IMAGE prompt (GPT Image 2 first-frame) + VIDEO prompt (Seedance 2.0) + final-frame spec + QA hooks. มี continuity ledger (identity/wardrobe/direction lock), โหลด skill seedance-2-pro-director + vault notes เอง, crop panel ด้วย ffmpeg ดูรายช่อง. Storyboard = source of truth (ข้อกำกวม → ⚠ ASK ไม่เดาเอง). ห้ามยิง generate เอง
- **deep-reasoner** — model **Opus**. งานคิดหนัก: architecture decision, debug ซับซ้อน, algorithm design, trade-off analysis. Tools: read-only + Bash + web, **ห้าม edit ไฟล์** — ส่งกลับเป็น Conclusion → Recommended action → Why → Confidence & risks ให้ orchestrator ทำต่อ
- **fast-worker** — model **Sonnet**. งาน mechanical ที่ spec ชัด: boilerplate, tests, formatting, renames, simple edits. Tools: Read/Edit/Write/Bash/Grep/Glob. กติกาในตัว: no scope creep, match codebase style, verify แคบๆ หลังแก้, รายงานแค่ what changed + verification

เรียกใช้: บอกงานปกติ (Claude เลือกตาม description อัตโนมัติ) หรือสั่งตรง เช่น "ใช้ deep-reasoner หา root cause"

**07-08 (PENDING, ไม่เร่งด่วน): วิเคราะห์ว่าตัวไหนย้ายไป Haiku ได้** — ไม่มีตัวไหนใน fleet ใช้ Haiku ตอนนี้เลย
- **candidate ชัดสุด: fast-worker** — งาน mechanical spec ชัด ตรง sweet spot Haiku พอดี เสี่ยงน้อย
- **ทดสอบก่อนย้ายถาวร: timeline-builder** — กึ่งกลไกกึ่งครีเอทีฟ (pacing/contrast) ต้องเช็คผลก่อน
- **ไม่ควรย้าย: qa-inspector, teardown-analyst** — ตัดสินใจกระทบเงิน/เครดิตจริง ต้องการ nuance ไม่ใช่ classification
- **Verdict: ไม่จำเป็นต้องทำ** — ประหยัดได้จริง (~3 เท่า) แต่ fast-worker เป็นงานเล็กอยู่แล้ว ต้นทุนรวม fleet มาจาก opus-tier เป็นหลัก ไม่ใช่ priority

เกี่ยว: [[skills-cheatsheet]] (skills = ความรู้เฉพาะทางใน conversation หลัก, subagents = แยก context/แยก model ทำงานขนาน) · [[drama-app-fable-ultracode-retrospective]] (fleet audit 07-07 เป็นส่วนหนึ่งของคืนนั้น)
