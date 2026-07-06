---
name: meigen-library-session-state
description: "DONE 2026-07-06 — FDA works, sync.py runs direct on external; leftover: user deletes orphan folders in Finder"
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

## ค้างอย่างเดียว
- **ผู้ใช้ลบ orphan เองใน Finder** (~870MB): `~/Documents/prompt-library` + `~/Desktop/prompt-library`

## ข้อจำกัด env ที่เจอ (จำไว้)
- tool **ไม่มี FDA** (ก่อน restart): เข้าไม่ได้ `~/Desktop` `~/Documents` `/Volumes/*` = Operation not permitted
- เข้าได้: `/Users/Shared` · `~/.claude` · `/private/tmp` scratchpad
- **foreground bash python พังเรื่อง import** → รัน python ผ่าน `run_in_background: true` เท่านั้น
- API: `www.meigen.ai/api/search?type=posts&q=&limit=50&offset=N&sortBy=date` (ไม่มี auth, ไม่ติด CF)

## งานที่ user อาจสั่งต่อ
- sync ของใหม่ · เพิ่ม category แม่นขึ้น (LLM ลองแล้ว 49% ไม่คุ้ม, คง keyword 68%) · merge YouMind pack เข้า gallery เดียว
