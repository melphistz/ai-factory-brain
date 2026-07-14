---
name: meigen-library-session-state
description: "DONE — FDA works (needs re-toggle after every reboot, known macOS external-volume TCC bug), sync.py runs direct on external. Latest sync 2026-07-08: 6,828 prompts."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# MeiGen Library — Session Resume State (2026-07-02)

> ผู้ใช้จะ **restart เครื่องเพื่อเปิด Full Disk Access (FDA)** แล้วกลับมาคุยต่อ. โน้ตนี้ให้ resume ได้.
> รายละเอียดเต็ม + scripts + API → [[meigen-prompt-dataset]] · prompt เต็ม → [[meigen-top-prompts]]

## ทำเสร็จแล้ว ✅
- ดึงทั้งเว็บ meigen.ai ผ่าน open API `/api/search` → **6,029 prompts** (full text + meta + thumbnails)
- keyword classify (~68%), gallery.html (filter model+category+search+copy)
- **library อยู่บน external: `/Volumes/PS Catches/prompt-library/`** (ผู้ใช้ copy manual แล้ว, ยืนยัน gallery เปิดได้ 5,994 รูป)
- ลบ staging /Users/Shared แล้ว

## ✅ จบแล้ว (2026-07-06)
1. **FDA ผ่าน** — tool อ่าน/เขียน external ตรงได้. เคล็ด: ถ้าติด `Operation not permitted` ทั้งที่ toggle เปิด → toggle Terminal.app ปิด→เปิด + Cmd+Q Terminal เปิดใหม่
2. **sync 07-06 สำเร็จ**: +481 ใหม่ → meigen 6,519 · gallery 7,358 cards (รวม youmind 839)

## ✅ sync 2026-07-13 (ล่าสุด)
- +592 ใหม่ → **meigen 7,420** · gallery **8,259 cards** (รวม youmind 839) · thumb ok 592/592 · 7 categories
- คำสั่ง: `cd "/Volumes/PS Catches/prompt-library/" && python3 sync.py` (run_in_background เสมอ)

## ✅ INTERNAL TEXT INDEX (13 ก.ค. — แก้ปัญหา "คลังไม่ถูกใช้")
- `sync.py` ต่อท้ายด้วย `export_index.py` แล้ว → ทุก sync จะ export **index text-only** ไป `~/ai-factory-brain/tools/prompt-index/prompt-index.jsonl` อัตโนมัติ (8,776 prompts = meigen+youmind+seedance, ~16MB, เข้า git)
- **ค้นได้เสมอไม่ติด FDA:** `search.py term1 term2` — กฎการใช้ = [[rule-search-prompt-index-first]]
- อัพที่เดียว (รัน sync.py) ได้ 2 ที่ (gallery external + index internal) · ความสด = `index-meta.json`

## sync 2026-07-08
- +309 ใหม่ → meigen 6,828 · gallery 7,667 cards

## ไม่มีอะไรค้าง
- orphan Desktop/Documents ลบไปแล้ว (ยืนยัน 07-06) — โปรเจกต์นี้ปิดสมบูรณ์ ใช้ต่อแค่ sync เป็นระยะ

## ⚠️ FDA ต้อง re-toggle ทุกครั้งที่ reboot เครื่อง (ไม่ใช่ครั้งเดียวจบ)
- **root cause (ยืนยัน 07-08):** macOS TCC bug เฉพาะ external/removable volume — FDA grant ไม่ persist ข้าม reboot (ต่างจาก internal disk ที่อยู่ยาว) ไม่เกี่ยว MDM/cleaning app (เช็คแล้วไม่มี)
- **แก้:** ทุกเช้าหลัง reboot → System Settings → Privacy & Security → Full Disk Access → toggle Terminal.app ปิด→เปิด → Cmd+Q ปิด Terminal ทั้งหมด → เปิดใหม่
- user ไม่ต้องการย้าย library เข้า internal disk (ทางแก้ถาวร) — ทนวิธี toggle ต่อไป

## ข้อจำกัด env ที่เจอ (จำไว้)
- tool **ไม่มี FDA** (ก่อน toggle): เข้าไม่ได้ `~/Desktop` `~/Documents` `/Volumes/*` = Operation not permitted
- เข้าได้เสมอ: `/Users/Shared` · `~/.claude` · `/private/tmp` scratchpad
- **foreground bash python พังเรื่อง import** → รัน python ผ่าน `run_in_background: true` เท่านั้น
- API: `www.meigen.ai/api/search?type=posts&q=&limit=50&offset=N&sortBy=date` (ไม่มี auth, ไม่ติด CF)

## งานที่ user อาจสั่งต่อ
- sync ของใหม่ (รันตามคำสั่งข้างบน) · เพิ่ม category แม่นขึ้น (LLM ลองแล้ว 49% ไม่คุ้ม, คง keyword 68%) · merge YouMind pack เข้า gallery เดียว
