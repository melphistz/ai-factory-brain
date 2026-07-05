---
name: grok-media-saver-project
description: Chrome extension ที่ D:\Downloads\grok-media-saver-v6.0 สำหรับ bulk download รูป/วิดีโอจาก Grok Imagine — แก้เป็น v6.1.1 เมื่อ 2026-07-05 ใช้งานได้จริงแล้ว (เครื่อง Windows)
metadata:
  type: project
---

Extension "Grok Media Saver" (unpacked, MV3, side panel UI ภาษาไทย) อยู่ที่ `D:\Downloads\grok-media-saver-v6.0` (เครื่อง Windows) — user ใช้โหลดภาพ gen จาก grok.com/imagine (วัตถุดิบงาน AI film)

คู่มือใช้งาน + ความรู้ฉบับเต็ม: [[grok-media-saver-knowledge]] (ย้ายเข้า repo memory จาก vault เก่า 2026-07-05)

สถาปัตยกรรม: `inject.js` (MAIN world, hook fetch/XHR + จับ asset-list API request) → postMessage → `content.js` (isolated, auto-scroll + **replay asset API ตาม nextPageToken = กลไกหลักที่ทำให้ครบ**) → `sidepanel.js` (UI, ดาวน์โหลด, dHash ตรวจซ้ำ, ประวัติใน chrome.storage `gms_library`)

แก้ 2026-07-05 (v6.0.0 → 6.1.1) ทดสอบผ่านจริงกับคลัง 1,130 ไฟล์:
- v6.1.0: ลบ `${dup}` ReferenceError ใน renderGrid (บั๊กหลัก — grid ว่าง + abort scan + UI ค้าง), replay API เพิ่ม retry/backoff + delay + เพดาน 1000 หน้า + รายงาน {complete, reason} โชว์บน status, เก็บ DOM ทุกรอบระหว่างเลื่อน (grid เป็น virtualized list), จับ headers/Request-object body, กู้ id ขยาย 300→2000 + probe หลายนามสกุล
- v6.1.1: **ดาวน์โหลดต้อง `credentials: "include"`** — assets.grok.com เป็นไฟล์ private, fetch ไม่มีคุกกี้โดน 401/403 ทุกไฟล์ทั้งที่ thumbnail แสดงปกติ (img แนบคุกกี้เอง) + retry 3 ครั้ง + โชว์ HTTP code ตอนพลาด

ยังไม่ได้แก้ (ตั้งใจเว้น): dHash hamming ≤6 อาจมองรูป variant จาก prompt เดียวกันเป็น "ซ้ำ" → เตือน user แล้วว่าอย่ากดตรวจซ้ำก่อนโหลดถ้าอยากได้ทุกรอบแก้; popup.* เป็นไฟล์ตายซากไม่ถูกใช้

เครื่อง Windows นี้**ไม่มี JS runtime เลย** (ไม่มี node/deno/bun/WSL) และ**ใช้ Obsidian เป็น node แทนไม่ได้** — Electron ของ Obsidian ปิด fuse ELECTRON_RUN_AS_NODE ไว้ เรียกแล้วเปิด GUI ขึ้นมาแทน (เคยพลาดมาแล้ว) → ตรวจ syntax ด้วยการอ่านไฟล์เต็ม + นับสมดุลวงเล็บ หรือแนะนำ user ติดตั้ง Node.js
