---
name: watch-skill-claude-video
description: "/watch skill (bradautomates/claude-video) — how Claude \"watches\" video; detail modes, frame budget, dedup, flags for ad teardown"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3ccb8148-4343-4f76-98a3-4d73df154e2a
  modified: 2026-07-23T02:41:27.841Z
---

`/watch` skill = repo [bradautomates/claude-video](https://github.com/bradautomates/claude-video) — ติดตั้งแล้ว (`watch:watch`). ให้ Claude ดูวิดีโอ: `yt-dlp` โหลด+caption → `ffmpeg` แตะเฟรม → Whisper (Groq/OpenAI) fallback ถ้าไม่มี caption → ส่งเฟรม+transcript ให้ Claude ตอบ. zero-config (auto-install ffmpeg/yt-dlp). รองรับ YouTube/TikTok/Loom/Vimeo/100+ platform + local file.

**Detail modes** (`--detail`): `transcript` = 0 เฟรม เร็วสุด (caption เท่านั้น) · `efficient` = 50 เฟรม keyframe · `balanced` = 100 scene-aware (default) · `token-burner` = uncapped.

**Frame budget** ตามความยาว: ≤30s→~30 · 30-60s→~40 · 1-3min→~60 · 3-10min→~80 · >10min→100 cap + sparse warning. cap 2fps.

**Dedup:** ทิ้งเฟรมที่ต่างจากเฟรมก่อนหน้า ≤2.0 (mean abs brightness diff, 16×16 grayscale thumb) — กันเฟรมนิ่งซ้ำกินโทเคน.

**Flags เด็ด:** `--start T`/`--end T` = เฟรมถี่ขึ้นเฉพาะช่วงโฟกัส · `--timestamps T1,T2,..` = จับจุดเจาะจง (เช่น presenter cue) · `--max-frames N` = override cap · `--no-whisper` = เฟรมล้วนไม่ transcribe.

**Token:** ~197 tokens/เฟรม (512px width บน 720p ≈ w×h/750). แม่นสุด = วิดีโอ <10 นาที. Whisper key ตั้งที่ `~/.config/watch/.env` (Groq ถูกกว่า).

ใช้กับ [[ads-contact-sheet-pipeline]]: watch = teardown ad คู่แข่งเร็ว (dedup+transcript อัตโนมัติ) · contact-sheet = จัดกริดเฟรมเองคุมได้ละเอียดกว่า. คู่กับ [[teardown-analyst]] agent สำหรับแกะโครง hook-body-CTA.
