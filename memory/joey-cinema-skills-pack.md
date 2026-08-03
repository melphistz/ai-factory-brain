---
name: joey-cinema-skills-pack
description: "Joey's 4 Higgsfield/Seedance skills (installed 2026-08-03): character-builder, banana-pro-director-30, cinema-director, story-bible-builder — what each does, how they stack, routing vs existing skills, + Notion doc learnings (character lock method, contest prompt template, HF T&C verdict)"
metadata:
  type: reference
---

# Joey Cinema Skills Pack (installed 2026-08-03)

ที่มา: Notion doc ของ Joey (YouTuber AI filmmaking) — "Everything You Need to Start Building Your AI Cinematic World" + Dropbox skill files. ติดตั้งจาก `~/Desktop/Joey's Cinema Skill Files/` → `skills/` (hardlink เข้า `~/.claude/skills/` ตาม convention)

## 4 skills — stack กัน

1. **`character-builder`** — ตัวละคร: face lock → additions → outfit → 3-panel sheet. ครอบ flat 18% gray plate, flattering-realism ceiling, cel-shade stack. **ตัวละคร = ใช้ตัวนี้ ไม่ใช่ banana-pro**
2. **`banana-pro-director-30`** — still ทุกชนิด (Banana Pro / Soul Cinema / GPT-2), 6 โหมด: face lock / outfit / sheet / scene plate / GPT-2 detail / outfit replacement. เน้นใช้กับ **scene plates**
3. **`cinema-director`** — วิดีโอ Seedance/Higgsfield multi-shot, house format: header → capture cadence → CRITICAL blocks → Subject/Prop/Crowd Locks → World Plate → Atmosphere (depth only, ห้าม fog) → timecoded SHOTs → Cross-Frame Rules → Last Frame → Sound Bed → Camera & Capture Realism. มี lipsync bilabial protocol + phone/BTS capture mode
4. **`story-bible-builder`** — interview → canon doc เป็น SKILL.md ติดตั้งได้ → กัน prompt drift ทั้งโปรเจกต์

แนวคิด: bible ถือ *who/why* · character-builder ถือ *ตัวละคร* · banana pro ถือ *scene* · cinema-director ถือ *วิธีถ่าย*

## Routing vs skill เดิม (อยู่ใน [[skills-cheatsheet]] แล้ว)

- 1 shot เป๊ะ → `seedance-2-pro-director` · multi-shot cinematic → `cinema-director` · ad ทั้งตัว effects arc → `video-prompt-builder` · screenplay file → `shotlist-builder`
- ตัวละคร Higgsfield → `character-builder` · scene/still Higgsfield → `banana-pro-director-30` · one-off GPT Image 2 → `image-prompt-writer`

## ความรู้จาก doc (ใช้ได้แม้ไม่เรียก skill)

- **Character lock** = ภาพเดียวมีแต่หน้า: 18% gray seamless, black tank, chest-up, แสง flat ไร้เงา, neutral face — "boring on purpose" เพราะ model ไม่มี memory ระหว่าง gen; ทิ้ง scene ไว้ = มันก๊อป scene ไปด้วย. Lock = original, sheet = working copy
- **3-panel sheet**: headless ghost-mannequin front / full rear / tight face re-anchor — ต่อยอด [[char-sheet-2panel-identity-garment]]
- **"Relight from scratch overriding any reference lighting"** block + "Photographed not generated" + background เป็น flat color field (no floor, no wall, no plane) — ก้อน copy ได้เลย
- **Contest prompt template** (3 ตัวเต็มใน scratchpad/notion_page.md + skill): negative แบบไล่ทุก synonym, timing เป็นวินาที, contradiction เป็นเนื้อหาช็อต, scale เทียบในเฟรมเดียว, anime split cadence (ตัวละคร on twos/threes, BG on ones)
- **HF T&C (July 31, 2026)**: Joey ยืนยันกับทีม — user own outputs, commercial OK, HF ไม่ claim ownership; update คือเรื่อง product ใหม่ + rewrite ภาษาเก่า (private stays private, license = run service เท่านั้น)
