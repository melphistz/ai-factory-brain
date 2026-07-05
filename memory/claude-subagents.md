---
name: claude-subagents
description: "Installed Claude Code subagents + MODEL POLICY — Fable = orchestrate/plan only, subagents = Opus/Sonnet by task difficulty (never Fable)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f495e44a-04e5-4cac-94ed-83e0ab9d81c9
---

# Claude Code Subagents — fleet ครบ 6 ตัว (2026-07-05)

ไฟล์จริงอยู่ `<brain repo>/agents/` (junction เข้า `~/.claude/agents` ทั้งสองเครื่อง) — ใช้ได้ทุก project · ทุกตัวอ่าน brain ด้วย dual path (mac `/Users/working/ai-factory-brain/` · Windows `D:\ai-factory-brain\`) · **orchestration playbook เต็ม = `projects/FF_factory/AGENT_OPS.md`** (pipeline→ผู้ทำ, เกท, fan-out, data contract)

## MODEL POLICY (Mirko กำหนด 2026-07-03)

**Fable = วางแผน/orchestrate ใน main loop เท่านั้น — subagent ห้ามใช้ Fable** จัดตามความยาก: ยาก = Opus, tool-driven/ง่าย = Sonnet

| ยาก→ง่าย | งาน | agent | model |
|---|---|---|---|
| 1 | storyboard → prompt คู่ (ภาพ+วิดีโอ) + continuity | storyboard-prompter | opus |
| 2 | copy ไทย / hook bank / SPINE script (modular contract) | script-hook-writer ✅ 07-05 | opus |
| 3 | debug pipeline / architecture | deep-reasoner | opus |
| 4 | QA 2 เกท: pre-motion + post-render (checklist + ffmpeg + ssim) | qa-inspector ✅ 07-05 | sonnet |
| 5 | teardown โฆษณาคู่แข่ง + feedback loop ผลแอด | teardown-analyst ✅ 07-05 | sonnet |
| 6 | mechanical (rename/format/simple edit) | fast-worker | sonnet |

กฎร่วมทุกตัว: no generation/no credits (main loop ยิง gen หลัง Mirko สั่งเท่านั้น) · final message = deliverable เดียวที่ orchestrator เห็น · agent ใหม่มีผล session ถัดไป (โหลดตอนเริ่ม session)

- **storyboard-prompter** — model **Opus**. แปลง storyboard → ต่อ shot: IMAGE prompt (GPT Image 2 first-frame) + VIDEO prompt (Seedance 2.0) + final-frame spec + QA hooks. มี continuity ledger (identity/wardrobe/direction lock), โหลด skill seedance-2-pro-director + vault notes เอง, crop panel ด้วย ffmpeg ดูรายช่อง. Storyboard = source of truth (ข้อกำกวม → ⚠ ASK ไม่เดาเอง). ห้ามยิง generate เอง
- **deep-reasoner** — model **Opus**. งานคิดหนัก: architecture decision, debug ซับซ้อน, algorithm design, trade-off analysis. Tools: read-only + Bash + web, **ห้าม edit ไฟล์** — ส่งกลับเป็น Conclusion → Recommended action → Why → Confidence & risks ให้ orchestrator ทำต่อ
- **fast-worker** — model **Sonnet**. งาน mechanical ที่ spec ชัด: boilerplate, tests, formatting, renames, simple edits. Tools: Read/Edit/Write/Bash/Grep/Glob. กติกาในตัว: no scope creep, match codebase style, verify แคบๆ หลังแก้, รายงานแค่ what changed + verification

เรียกใช้: บอกงานปกติ (Claude เลือกตาม description อัตโนมัติ) หรือสั่งตรง เช่น "ใช้ deep-reasoner หา root cause"

เกี่ยว: [[skills-cheatsheet]] (skills = ความรู้เฉพาะทางใน conversation หลัก, subagents = แยก context/แยก model ทำงานขนาน)
