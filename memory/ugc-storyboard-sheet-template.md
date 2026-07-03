---
name: ugc-storyboard-sheet-template
description: "Production-ready UGC storyboard-sheet template (3-part @10s) — layout that actually feeds Seedance, from real OOTD/pink-drink examples"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# UGC Storyboard Sheet — Production Template

> โครง storyboard sheet ที่ **แปลงเป็นวิดีโอได้จริง** (ต่างจาก agency deck ที่ AI อ่านไม่หมด).
> มาจากตัวอย่างจริง 3 อัน: OOTD di kamar, Outfit Showcase, Pink-drink transformation — ทั้งหมด 30s / 3 part @10s.
> เกี่ยว: [[storyboard-gpt-image-to-seedance]] · [[ai-ugc-ad-factory-workflow]] · [[seedance-ugc-repository]] · [[ugc-ad-structure]]

## ทำไม template นี้ดี (vs luxury agency deck)
- **แยกช่อง "PROMPT VIDEO (teks siap pakai)"** = prompt อังกฤษพร้อมป้อน Seedance จริง อยู่ข้างๆ ภาพ storyboard
- ทุกบรรทัดแปลงเป็น **action ได้** (walk toward camera, touch hair, drink→flex→dance) ไม่ใช่โพสนิ่ง
- ไม่มี floor-plan/side-elevation diagram (AI ไม่อ่าน) — ตัดทิ้งถูกแล้ว
- มี story arc + CTA (pink-drink: masalah → solusi → hasil/CTA)

## โครงมาตรฐาน (30s / 3 part @10s / 4 beat ต่อ part)
```
HEADER: title · durasi total · format (9:16 UGC / 16:9 YT) · tema · konsep · tone
PART 1 (0:00–0:10) — HOOK / MASALAH        [4 thumbnail + caption + timecode]
PART 2 (0:10–0:20) — DETAIL / SOLUSI/AKSI  [4 thumbnail ...]
PART 3 (0:20–0:30) — POSE&CLOSE / HASIL·CTA[4 thumbnail ...]
ข้างๆ: PROMPT VIDEO ต่อ part (EN, character-lock + sequence timecode + audio + style)
ท้าย: CATATAN PRODUKSI (lokasi/waktu/kamera/fokus) + ASMR audio note
```

## Prompt-per-part format (ป้อน Seedance)
```
[Character lock verbatim: age, ethnicity, hair+streak, top, bottom, shoes].
[Scene/room + light]. Camera: smartphone vertical, static tripod.
Sequence:
  0:00–0:02  [action + motion]
  0:02–0:05  [action + camera motivation]
  ...
Audio: [ASMR footsteps, fabric rustle, no music].
Style: natural, realistic, clean, no-makeup look.
```
- **character description copy verbatim ทุก part** (ห้าม paraphrase) → consistency
- audio note ต่อ part (Seedance 2.0 gen เสียงได้)

## กฎแก้ก่อนใช้ (4 จุดพลาดที่เจอในตัวอย่างจริง)
1. **ซอย clip สั้น 2–3s** — อย่าสั่ง Seedance 10s รวด (drift หลัง ~8-10s). 1 part = gen 4 clip สั้นแล้วตัดต่อ
2. **ลบ typo ในภาพ** ก่อน copy prompt: เจอ "LighR", "woalen flooe", "detalsic", "question m k" → AI อ่านผิด
3. **doodle/sticker (heart, sparkle, ✨) AI ไม่วาดตาม** → แปะตอนตัดต่อ (CapCut) ไม่ใช่ใน Seedance
4. **aspect ratio ให้ตรงปลายทาง**: reels/tiktok = 9:16 · YouTube = 16:9

## ระดับความละเอียด "พอดี"
- อะไรที่ AI ไม่อ่าน (ผังกล้อง top-down, mood-board สี swatch, marketing message) = **doc สำหรับคน แยกไฟล์** อย่าปนใน storyboard sheet
- storyboard sheet = เฉพาะสิ่งที่ gen ใช้จริง: reference identity + beat + motion + prompt + audio
