---
name: skills-cheatsheet
description: "Cheat sheet — which installed skill runs for which ad task (seedance-2-pro-director / video-prompt-builder / shotlist-builder), how to force-pick, and how Claude auto-allocates"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

> ⚠️ บังคับใช้โดย [[rule-use-installed-skills]] (07-14): เริ่ม task ที่มี skill/agent ตรง → ต้องเปิดไฟล์นี้เลือกตัว route ห้ามเขียนสดใน main

Quick "which skill for which job" map for FF factory ad work. Claude auto-picks by reading each skill's `description` vs your intent; name a skill explicitly to force it. Details per skill: [[seedance-2-pro-director-skill]], [[shotlist-builder-skill]], [[video-prompt-builder-framework]].

## 3 Seedance skills — pick by JOB SIZE
| อยากได้ | พิมพ์แบบนี้ | skill |
|---|---|---|
| **1 shot เป๊ะ** (character lock, ตำแหน่งเฟรม, blocking) | "เขียน Seedance prompt: Ploy ถือมือถือ ล็อกซ้าย 9:16" | `seedance-2-pro-director` |
| **คลิปทั้งตัว จาก brief** (effects + จังหวะ + energy arc) | "อยากได้ ad 15 วิ เรื่อง X ใส่ effect ปังๆ" | `video-prompt-builder` |
| **script ยาว → หลาย scene** (แนบไฟล์) | แนบ script + "build shotlist scene 1-5" | `shotlist-builder` |

ตัวแยก: 1 shot → director · ทั้งคลิปจาก brief → video-prompt-builder · script file หลาย scene → shotlist-builder.

## แต่ละตัว
- **`seedance-2-pro-director`** — prompt อังกฤษ 1 shot: character anchor (x/y%, thirds, depth, gaze, contact points), state lock, camera plan, final frame, QA 12 ข้อ. (= Cannes 28-tips system prompt.)
- **`video-prompt-builder`** — 4 section: shot-by-shot effects timeline / effects inventory / density map / 3-act energy arc. คลิปโฆษณาทั้งตัวจาก concept.
- **`shotlist-builder`** ⚠️ — HTML shotlist หลาย scene, prompt **จีน**, default **21:9** (UGC สั่ง 9:16). stateful 4-phase (read→asset→blocking→HTML). output `~/Desktop/Ads/FF_factory/shotlists/`. patched for Claude Code.

## บังคับ / คุมเอง
- พิมพ์ชื่อตรงๆ ("ใช้ shotlist-builder ...") → ข้ามการเดา
- ถาม "อันนี้ควรใช้ skill ไหน" → บอกก่อนรัน
- กำกวม → Claude ถามก่อน ไม่เดามั่ว
- เช็คว่าเรียกถูก: ดู `Skill(...)` ใน tool call ตอนรัน

## reference ที่เกี่ยว (ความรู้ ไม่ใช่ skill)
[[higgsfield-3step-ai-ad-workflow]] (cinematic commercial tricks) · [[higgsfield-marketing-studio-workflow]] (Marketing Studio UGC/TV + luxury locations)
