---
name: skills-cheatsheet
description: "Cheat sheet — which installed skill runs for which ad task (seedance-2-pro-director / video-prompt-builder / shotlist-builder), how to force-pick, and how Claude auto-allocates"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
  modified: 2026-07-30T01:27:01.937Z
---

> ⚠️ บังคับใช้โดย [[rule-use-installed-skills]] (07-14): เริ่ม task ที่มี skill/agent ตรง → ต้องเปิดไฟล์นี้เลือกตัว route ห้ามเขียนสดใน main

Quick "which skill for which job" map for FF factory ad work. Claude auto-picks by reading each skill's `description` vs your intent; name a skill explicitly to force it. Details per skill: [[seedance-2-pro-director-skill]], [[shotlist-builder-skill]], [[video-prompt-builder-framework]].

## Video skills — pick by JOB SIZE
| อยากได้ | พิมพ์แบบนี้ | skill |
|---|---|---|
| **1 shot เป๊ะ** (character lock, ตำแหน่งเฟรม, blocking) | "เขียน Seedance prompt: Ploy ถือมือถือ ล็อกซ้าย 9:16" | `seedance-2-pro-director` |
| **multi-shot cinematic 15s** (หนัง/MV/contest, hard cuts, CRITICAL blocks) | "เขียน prompt 3 shots 15 วิ เรื่อง X แบบหนัง" | `cinema-director` |
| **คลิปทั้งตัว จาก brief** (effects + จังหวะ + energy arc) | "อยากได้ ad 15 วิ เรื่อง X ใส่ effect ปังๆ" | `video-prompt-builder` |
| **script ยาว → หลาย scene** (แนบไฟล์) | แนบ script + "build shotlist scene 1-5" | `shotlist-builder` |
| **ฉากสัมภาษณ์/podcast 2 คน** (host+guest คุยไทย) | "ทำ podcast สัมภาษณ์รีวิว X" | `podcast` |

ตัวแยก: 1 shot → director · ซีเควนซ์หนังหลาย shot ใน prompt เดียว → cinema-director · ทั้งคลิปโฆษณาจาก brief (effects arc) → video-prompt-builder · script file หลาย scene → shotlist-builder.

## Image/character skills — pick by JOB
| อยากได้ | skill |
|---|---|
| **สร้าง/ล็อกตัวละครใหม่, แก้ผม/tattoo/expression, outfit, character sheet** (Higgsfield) | `character-builder` |
| **scene plate / photoreal still / outfit swap 2 ref** (Higgsfield Banana Pro/Soul/GPT-2) | `banana-pro-director-30` |
| **ภาพเดี่ยว ad-hoc** (GPT Image 2 / Nano Banana ตรง ๆ นอก Higgsfield pipeline) | `image-prompt-writer` |
| **world canon → skill ติดตั้งได้** (กัน prompt drift ทั้งโปรเจกต์) | `story-bible-builder` |

ตัวแยก: ตัวละคร → character-builder · ฉาก/still อื่น → banana-pro-director-30 · quick one-off → image-prompt-writer. รายละเอียด Joey pack: [[joey-cinema-skills-pack]]

## แต่ละตัว
- **`seedance-2-pro-director`** — prompt อังกฤษ 1 shot: character anchor (x/y%, thirds, depth, gaze, contact points), state lock, camera plan, final frame, QA 12 ข้อ. (= Cannes 28-tips system prompt.)
- **`video-prompt-builder`** — 4 section: shot-by-shot effects timeline / effects inventory / density map / 3-act energy arc. คลิปโฆษณาทั้งตัวจาก concept.
- **`shotlist-builder`** ⚠️ — HTML shotlist หลาย scene, prompt **จีน**, default **21:9** (UGC สั่ง 9:16). stateful 4-phase (read→asset→blocking→HTML). output `~/Desktop/Ads/FF_factory/shotlists/`. patched for Claude Code.
- **`podcast`** — prompt kit ฉากสัมภาษณ์ 3 part: still host+guest (identity lock + mirror trick), talking video ไทย (~4 ประโยค/15s), closing two-shot เงียบ (Kling). ที่มา = [[zenityx-interview-scene-workflow]].
- **`cinema-director`** — Joey pack: multi-shot Seedance/Higgsfield ใน prompt เดียว, house format (CRITICAL blocks, Subject/Prop Locks, World Plate, Cross-Frame Rules, Last Frame, Sound Bed, lipsync bilabial protocol). ใช้กับงานหนัง/MV/ซีเควนซ์ cinematic.
- **`character-builder`** — Joey pack: face lock → additions (ผม/makeup/tattoo/expression) → outfit + 3-panel sheet (headless front / rear / tight face). 18% gray flat plate, flattering-realism ceiling, มี cel-shade path ด้วย.
- **`banana-pro-director-30`** — Joey pack: still ทุกชนิดฝั่ง Higgsfield (Banana Pro/Soul Cinema/GPT-2) 6 โหมด — face lock, outfit, sheet, scene plate, detail shot, outfit replacement.
- **`story-bible-builder`** — Joey pack: interview → canon SKILL.md ติดตั้งเป็น skill ของโปรเจกต์ ทุก prompt ต่อไปรู้จักโลก/ตัวละครเอง.

## บังคับ / คุมเอง
- พิมพ์ชื่อตรงๆ ("ใช้ shotlist-builder ...") → ข้ามการเดา
- ถาม "อันนี้ควรใช้ skill ไหน" → บอกก่อนรัน
- กำกวม → Claude ถามก่อน ไม่เดามั่ว
- เช็คว่าเรียกถูก: ดู `Skill(...)` ใน tool call ตอนรัน

## reference ที่เกี่ยว (ความรู้ ไม่ใช่ skill)
[[higgsfield-3step-ai-ad-workflow]] (cinematic commercial tricks) · [[higgsfield-marketing-studio-workflow]] (Marketing Studio UGC/TV + luxury locations)
