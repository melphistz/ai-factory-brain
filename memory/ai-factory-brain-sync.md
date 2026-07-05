---
name: ai-factory-brain-sync
description: "Cross-machine sync repo ~/ai-factory-brain (git) — vault/agents/skills ตัวจริงอยู่ในนี้ + symlink กลับ path เดิม; sync = ./sync.sh ต้นและท้าย session"
metadata:
  node_type: memory
  type: reference
---

# ai-factory-brain — Cross-machine Sync Repo (2026-07-03)

`~/ai-factory-brain` = git repo เก็บความรู้ทั้งหมดข้ามเครื่อง (mac mini ↔ Windows PC)

## โครง + symlink map (mac mini)

- `memory/` = vault ตัวจริง ← symlink จาก `~/.claude/projects/-Users-working/memory`
- `agents/` = subagents ตัวจริง ← symlink จาก `~/.claude/agents`
- `skills/` = skills ตัวจริง ← symlink จาก `~/.claude/skills`
- `projects/FF_factory/` = **mirror** (canonical = `~/Desktop/Ads/FF_factory/` บน mac)
- `tools/` = `_ssim_scan.py` ฯลฯ · `setup/` = สคริปต์ตั้งเครื่องใหม่ · README.md = คู่มือเต็ม

## Junction map (Windows PC — ตั้งแล้ว 2026-07-05, repo อยู่ `D:\ai-factory-brain`)

- `%USERPROFILE%\.claude\agents` → repo agents · `\.claude\skills` → repo skills
- `\.claude\projects\D--ai-factory-brain\memory` → repo memory
- `\.claude\projects\D--Claude\memory` → repo memory (เพิ่ม 2026-07-05 — เปิดจาก vault เก่า [[legacy-vault-d-claude]] ก็ได้สมองเดียวกัน)

## Ritual

**เริ่ม+เลิกงานทุก session: `cd ~/ai-factory-brain && ./sync.sh`** (Windows: `.\sync.ps1`) — pull→commit→push จบในคำสั่งเดียว. Windows ต้องเปิด claude จาก folder repo เสมอ (memory ผูก cwd)

## ค้าง / caveat

- remote ✅ ต่อแล้ว: **https://github.com/melphistz/ai-factory-brain** (private, gh auth = melphistz, push แล้ว 2026-07-03)
- TCC block กลางเซสชัน 2026-07-03: harness อ่าน Desktop ไม่ได้อีก → avatar PNGs + `_batch.py` ยังไม่เข้า repo (checklist ใน README) — แก้ถาวร = ให้ FDA กับ app ที่รัน Claude Code
- ไม่เข้า repo: วิดีโอ/ไฟล์หนัก, MeiGen library (external drive), pordee plugin, credentials
