# AI Factory Brain — Mirko's portable knowledge base

ทุกอย่างที่ Claude Code + Mirko สร้างร่วมกัน (vault ความรู้, subagents, skills, project docs, tools)
ใช้ข้ามเครื่อง mac mini ↔ Windows PC ผ่าน git

## Layout

| folder | คืออะไร | canonical |
|---|---|---|
| `memory/` | Obsidian vault / Claude memory (35+ notes + MEMORY.md index) | repo (เครื่องไหนแก้ก็ sync) |
| `agents/` | subagents: storyboard-prompter (opus) · deep-reasoner (opus) · fast-worker (sonnet) | repo |
| `skills/` | seedance-2-pro-director · shotlist-builder · video-prompt-builder | repo |
| `projects/FF_factory/` | Fox-Funnels factory docs | ⚠️ mirror — ตัวจริงอยู่ mac mini `~/Desktop/Ads/FF_factory/` |
| `tools/` | `_ssim_scan.py` (AI-video temporal scan) ฯลฯ | repo |
| `setup/` | สคริปต์ตั้งเครื่องใหม่ | — |

บนเครื่อง mac mini: ของจริงอยู่ใน repo แล้ว symlink กลับไปที่ path เดิมของ Claude Code
(`~/.claude/agents`, `~/.claude/skills`, `~/.claude/projects/-Users-working/memory`) — Obsidian ก็เปิด path เดิมได้

## Sync ritual (ทั้งสองเครื่อง)

```
เริ่มงาน:  ./sync.sh   (Windows: .\sync.ps1)
เลิกงาน:   ./sync.sh   (Windows: .\sync.ps1)
```

แก้ชนกัน (นานๆที): git จะบอก conflict → เปิดไฟล์แก้ตาม marker แล้ว `git add -A && git rebase --continue && git push`
หรือโยนให้ Claude แก้: "แก้ conflict ให้หน่อย"

## ตั้งเครื่อง Windows ครั้งแรก

1. ติดตั้ง git + Claude Code + login บัญชีเดิม
2. `git clone <remote-url> ai-factory-brain`
3. รัน `claude` หนึ่งครั้ง (สร้าง `%USERPROFILE%\.claude`) แล้วปิด
4. `powershell -ExecutionPolicy Bypass -File .\setup\setup-windows.ps1`
5. **ทำงานโดยเปิด claude จาก folder repo เสมอ** (memory ผูกกับ cwd)
6. Obsidian บน Windows: เปิด vault ที่ `ai-factory-brain\memory`

## สิ่งที่ไม่อยู่ใน repo (โดยตั้งใจ)

- **วิดีโอ/ไฟล์หนัก** — competitor ads, gen results, thumbs → อยู่เครื่องใครเครื่องมัน / external drive
- **MeiGen prompt library** (6,038 records + gallery + thumbs 437MB) → external drive `PS Catches/prompt-library/` — เสียบเครื่องไหนก็ใช้ที่นั่น
- **pordee plugin** — ติดตั้งแยกต่อเครื่อง
- Higgsfield/MCP credentials — login ต่อเครื่อง

## Manual checklist (mac mini — ค้างจาก TCC block)

- [ ] ลาก 2 รูป identity ใน Finder: `Desktop/Ads/FF_factory/avatar/{concept1_presenter_anchor,FFCORE01_Ploy_identity_sheet}.png` → `ai-factory-brain/projects/FF_factory/avatar/`
- [ ] copy `Desktop/Ads/videos/_batch.py` → `ai-factory-brain/tools/`
- [ ] System Settings → Privacy & Security → **Full Disk Access** ให้ app ที่รัน Claude Code (Terminal/iTerm) — แก้ทั้งปัญหา Desktop TCC และเปิดทาง external drive (MeiGen sync)
