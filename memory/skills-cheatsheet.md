---
name: skills-cheatsheet
description: "Cheat sheet — which installed skill runs for which ad task (seedance-2-pro-director / shotcaller-v2 / motiondojo-v1 / castkit-v1 / scenecraft-v1 / video-prompt-builder / shotlist-builder), how to force-pick, and how Claude auto-allocates"
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
| **multi-shot cinematic 15s** (3+ ตัวละคร/corps/wardrobe ข้าม cuts/MV/strobe) | "เขียน prompt 3 shots 15 วิ เรื่อง X แบบหนัง" | `shotcaller-v2` ⚠️ |
| **motion transfer Genjutsu** (เอาท่าเต้น/กล้องจากคลิป ref ใส่ตัวละครใหม่) | "เอาท่าเต้นคลิปนี้ใส่ 2 ตัวละครเรา บนดาดฟ้า" | `motiondojo-v1` |
| **คลิปทั้งตัว จาก brief** (effects + จังหวะ + energy arc) | "อยากได้ ad 15 วิ เรื่อง X ใส่ effect ปังๆ" | `video-prompt-builder` |
| **script ยาว → หลาย scene** (แนบไฟล์) | แนบ script + "build shotlist scene 1-5" | `shotlist-builder` |
| **ฉากสัมภาษณ์/podcast 2 คน** (host+guest คุยไทย) | "ทำ podcast สัมภาษณ์รีวิว X" | `podcast` |

ตัวแยก: 1 shot → director · ซีเควนซ์หนังหลาย shot ใน prompt เดียว → shotcaller-v2 · Genjutsu motion transfer → motiondojo-v1 · ทั้งคลิปโฆษณาจาก brief (effects arc) → video-prompt-builder · script file หลาย scene → shotlist-builder.

## Image/character skills — pick by JOB
| อยากได้ | skill |
|---|---|
| **สร้าง/ล็อกตัวละครใหม่, แก้ผม/tattoo/expression, outfit, character sheet** (Higgsfield) | `castkit-v1` |
| **scene plate / coverage หลายมุม / plate edit / people-in-scene first frame** (Banana Pro / Seedream 5.0 Pro / อื่นๆ) | `scenecraft-v1` |
| **ภาพเดี่ยว ad-hoc** (GPT Image 2 / Nano Banana ตรง ๆ นอก Higgsfield pipeline) | `image-prompt-writer` |
| **world canon → `projects/<slug>/00-bible.md`** (กัน prompt drift ทั้งโปรเจกต์) | `story-bible-builder` |

ตัวแยก: ตัวละคร (+ outfit replacement worn-in-photo) → castkit-v1 · ฉาก/plate → scenecraft-v1 · flat-lay outfit swap → [[outfit-swap-wichcraft-prompt]] · quick one-off / UGC / product → image-prompt-writer. รายละเอียด: [[joey-skills-v2-nov2026]] (v1 เก่า: [[joey-cinema-skills-pack]])

## แต่ละตัว
- **`seedance-2-pro-director`** — prompt อังกฤษ 1 shot: character anchor (x/y%, thirds, depth, gaze, contact points), state lock, camera plan, final frame, QA 12 ข้อ. (= Cannes 28-tips system prompt.)
- **`video-prompt-builder`** — 4 section: shot-by-shot effects timeline / effects inventory / density map / 3-act energy arc. คลิปโฆษณาทั้งตัวจาก concept.
- **`shotlist-builder`** ⚠️ — HTML shotlist หลาย scene, prompt **จีน**, default **21:9** (UGC สั่ง 9:16). stateful 4-phase (read→asset→blocking→HTML). output `~/Desktop/Ads/FF_factory/shotlists/`. patched for Claude Code.
- **`podcast`** — prompt kit ฉากสัมภาษณ์ 3 part: still host+guest (identity lock + mirror trick), talking video ไทย (~4 ประโยค/15s), closing two-shot เงียบ (Kling). ที่มา = [[zenityx-interview-scene-workflow]].
- **`shotcaller-v2`** ⚠️ — Joey v2 (house-patched 11-11, แทน cinema-director): Seedance 2.0/2.5 multi-shot, spine 16 slot, dialogue system (THE SCRIPT verbatim / one mouth at a time), video extension, lipsync-to-track, video char ref sheet (look+voice — UNVERIFIED). ใช้เมื่อศัตรูคือ **drift**: 3+ ตัว, wardrobe ข้าม cut, dialogue หลายคน, MV/strobe. **BOX mode ≤1,800 chars default** (H2). **ห้ามใช้**: talking-head ไทย (→ seedance-2-pro-director + Veo pacing) · mood/fashion/product 1-2 คน (→ marco freestyle)
- **`motiondojo-v1`** — Joey v2 (patched): Higgsfield Genjutsu motion transfer 3 form (Body Copy / Camera Copy / Body Copy New Camera) + hard mouth lock · core ≤1,800 chars default (limit จริง UNVERIFIED) · Kling recast ตัวเดียว → Higgsfield motion_control ไม่ใช่ตัวนี้
- **`castkit-v1`** — Joey v2 (patched, แทน character-builder): 5 station face lock → additions → outfit build → outfit replacement → sheet (3-panel dead-on, neckline test เลือก ghost mannequin/clean neck cut) · photoreal ↔ animated · lock = reference ห้ามส่งเป็น portrait → relight ผ่าน [[drama-dramabox-tier-portrait-recipe]]
- **`scenecraft-v1`** — Joey v2 (patched, แทน banana-pro scene mode): plate A environment / B people-in-scene / C coverage set / D plate edit · prose 5 ย่อหน้า · ไม่มี fog · Seedream HEX · ป้ายไทย gen text-free แล้วใส่ใน post · 9:16 = spherical (UNVERIFIED)
- **`story-bible-builder`** — Joey pack (patched): interview → canon doc ที่ `projects/<slug>/00-bible.md` โหลดผ่าน STATE.md (ไม่ติดตั้งเป็น skill)

## บังคับ / คุมเอง
- พิมพ์ชื่อตรงๆ ("ใช้ shotlist-builder ...") → ข้ามการเดา
- ถาม "อันนี้ควรใช้ skill ไหน" → บอกก่อนรัน
- กำกวม → Claude ถามก่อน ไม่เดามั่ว
- เช็คว่าเรียกถูก: ดู `Skill(...)` ใน tool call ตอนรัน

## reference ที่เกี่ยว (ความรู้ ไม่ใช่ skill)
[[higgsfield-3step-ai-ad-workflow]] (cinematic commercial tricks) · [[higgsfield-marketing-studio-workflow]] (Marketing Studio UGC/TV + luxury locations)
