---
name: youmind-scrape-session-state
description: "ARCHIVED — DONE 2026-07-03 — YouMind merged into galleries (img 909, vid 84). Optional leftovers: 44 img fetch-fail + youmind video undercount"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# YouMind Scrape — DONE (2026-07-03)

> รวม youmind เข้า gallery เดิมเรียบร้อย (ไม่แยกเว็บ). ทุกไฟล์ `/Volumes/PS Catches/prompt-library/`.
> เกี่ยว: [[meigen-prompt-dataset]] · [[youmind-gpt-image-prompt-library]]

## ผลรวมสุดท้าย
| source | ได้ | เพดาน | หมายเหตุ |
|---|---|---|---|
| meigen image | 6,038 | ~6,029 ทั้งเว็บ | ครบ |
| meigen video | 294 | 294 (console) | ครบ |
| youmind image | 909 | 953 sitemap EN | ขาด 44 (fetch fail) |
| youmind video | 84 | ไม่รู้ | undercount |

- **gallery.html** = 6,877 cards (meigen 6,038 + youmind 839 dedup by tweet_id) · 7 categories · AND-filter source/model/category+search
- **seedance-gallery.html** = 363 cards (meigen 294 + youmind 69 unique) · ▶ เล่น .mp4 · badge YM · video models: Seedance 2.0 / Grok Imagine / Veo 3.1 / grok-video

## ค้าง (optional — ผู้ใช้สั่งพักก่อน)
- **A** retry 44 youmind image ที่ fetch fail (เร็ว เสี่ยงต่ำ) — rerun `youmind_scrape.py`
- **B** เจาะ youmind video ให้ครบ: หา API endpoint ของ `/seedance-2-0-prompts/explore` (infinite-scroll โหลดผ่าน API ไม่อยู่ใน static HTML) แทน BFS → ได้เยอะกว่า 84
- เก็บเพิ่มต้องช้า ≥1.5s ไม่งั้นโดน CF 1015 ซ้ำ

## บทเรียน rate-limit
- youmind แบนไว (~1000 req รัว = 1015) ต่างจาก meigen (6k ไม่โดน). delay 1.5s single-thread = รอด
- video ไม่มี sitemap → BFS จาก static HTML ได้แค่ที่ link ถึง (undercount). ต้องหา API ถึงจะครบ
