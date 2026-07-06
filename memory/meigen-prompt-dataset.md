---
name: meigen-prompt-dataset
description: "MeiGen prompt gallery — 1,446 curated GPT Image/Nanobanana prompts are OPEN-SOURCE JSON on GitHub (bypasses the CF-locked site). Query/filter locally + best formulas."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# MeiGen — 1,446 Curated Prompt Dataset (open-source)

> Site `meigen.ai` = prompt gallery ดึงจาก X (มี `[variable]` template, detail page `/prompt/{tweet_id}`).
> เว็บ **Cloudflare-locked** (curl/WebFetch = 403 "Just a moment"). **exa (`web_fetch_exa`) ทะลุได้** สำหรับดูหน้า
> **แต่ทางลัดจริง:** prompt library ทั้งชุดเป็น open-source → ดึงตรงไม่ต้องสู้ CF
> เกี่ยว: [[youmind-prompt-pack]] · [[youmind-gpt-image-prompt-library]] · [[ai-character-identity-lock]] · [[ai-influencer-image-prompt]] · [[ai-ugc-ad-factory-workflow]]

## 📦 Dataset (durable, re-fetchable)
```
https://raw.githubusercontent.com/jau123/nanobanana-trending-prompts/main/prompts/prompts.json
```
- 1,446 records · fields: `rank id prompt author likes views image images model categories rating score date source_url`
- model: nanobanana 1148 · gptimage 298
- categories: **Photography 533 · Illustration&3D 370 · Product&Brand 239 · Food&Drink 156 · Poster Design 146 · UI&Graphic 52**
- image ต่อ record: `https://images.meigen.ai/tweets/{id}/0.jpg` · source = tweet เดิม

### query lane เรา (python)
```python
import json
items=json.load(open('prompts.json'))
def top(cat,n): 
    xs=[i for i in items if cat in i['categories']]; xs.sort(key=lambda x:x['score'],reverse=True); return xs[:n]
top('Photography',20)  # Product & Brand / Food & Drink / Poster Design
```

## 🏆 Reusable FORMULAS (จาก top prompts — engagement สูงสุด)

### Brand-ad series @AmirMushich (ทุกอันใช้ `[BRAND NAME]` + "Act as..." + PHASE 1/2/3)
- **Glass Logo Sculpture** (3.2K♥): logo แบรนด์เป็น crystal-glass ลอยกลางฟ้า + caustics · "Act as High-End Product Photographer & CGI Artist" · tech spec: Octane, 120mm macro, f/5.6, Velvia 50 grain
- **Logo Cloud** (3.3K♥): เมฆ cumulus รูป logo บนฟ้าใส minimalist
- **Typographic Mask "window"** (1.6K♥): ตัวอักษรชื่อแบรนด์ยักษ์เป็น cut-out, subject เห็นผ่านตัวอักษรบนพื้นขาว
- **Sandwich Grid / Muted Palette**: 2×2 grid, subject ซ้อนหน้า-หลัง geometric block + shift สีแบรนด์เป็น "sophisticated muted"
- pattern: **`Act as [role]. PHASE 1 subject → PHASE 2 material → PHASE 3 environment → TECH SPECS`** + `Autonomously identify` (ให้ AI เดา logo แบรนด์เอง)

### Product campaign @azed_ai (1.7K♥)
- **Low-angle product-dominant**: model ถือ `[product name]` จ่อกล้อง, มือ+product ครอง foreground, ตัวเต็มอยู่หลัง, พื้นขาว high-key

### Photography lane
- **3x3 grid idol collage** (@BubbleBrain): 9 เฟรม same idol 100% consistent + frame breakdown ต่อช่อง (top/mid/bottom row ระบุ pose) — ตรง identity series [[ai-character-identity-lock]]
- **Motion-blur / panning cinematic**: "panning shot, motion blur trailing, slow-shutter, film grain" หรือ static subject + blurry passersby (contrast)
- **JSON-structured prompt** (@saniaspeaks_): prompt เป็น JSON `{identity_preservation:{strict_identity_lock:true, alter_face:false...}, subject:{pose:{selfie_arm...}}}` — คุมแม่นมาก

### Food & Drink
- **Levitating infographic** (@Taaruk_, 2.3K♥): บาม/จานล่าง + วัตถุดิบลอยขึ้น + label + pointing lines · JSON format
- **Technical annotation** (@TechieBySA): `[FOOD]` + black-ink architectural sketch overlay บนภาพจริง, exploded-view, measurements

## 💡 Pattern รวม (ขโมยได้ทุก prompt)
- **template variable:** `[BRAND NAME]` `[product name]` `[FOOD]` `[LOCATION]` `[Character]` (เว็บโชว์เป็น blue tag) → modular [[ai-ugc-ad-factory-workflow]]
- **`Act as [role]`** + **`PHASE 1/2/3`** = โครง prompt โฆษณาโปร
- **`Autonomously identify/analyze [BRAND]`** = ให้โมเดลเดา asset แบรนด์เอง (ไม่ต้อง describe logo)
- **JSON-structured prompt** = คุม identity/module แม่น (nanobanana/gptimage อ่านได้)
- tech-spec tail: lens+aperture+film-stock (Velvia 50, 85mm, f/5.6) = ดูโปร

## 🔌 เครื่องมือพ่วง (MeiGen เปิด)
- **MCP server** `jau123/MeiGen-AI-Design-MCP` (npm `meigen`, 1.5k★) — 8 tools, gen ด้วย 11 โมเดล (GPT Image 2 / Nanobanana 2 / Seedance 2.0 / Veo 3.1...), มี 1,446 prompt ในตัว
  - ติดตั้ง Claude Code: `/plugin marketplace add jau123/MeiGen-AI-Design-MCP` → `/plugin install meigen@meigen-marketplace`
  - CLI one-shot: `npx meigen gen --prompt "..."` (ต้อง `MEIGEN_API_TOKEN`)
- prompt เต็มตัวท็อป (copy-paste) → ดู [[meigen-top-prompts]]

## 🔓 API เปิด (KEY — ดึงทั้งเว็บได้ ไม่มี auth ไม่ติด CF)
เจอจาก source ของ npm `meigen` (MCP). endpoint จริงที่เว็บใช้:
```
https://www.meigen.ai/api/search?type=posts&q=<keyword|ว่าง>&limit=50&offset=<n>
```
- **ไม่ต้อง key/header** (แค่ curl/urllib) · CF บล็อกแค่ page/sitemap/api.meigen.ai — แต่ `www.meigen.ai/api/search` ผ่าน
- `q` ว่าง = browse ทั้งหมด (paginate offset += 50 จนได้ data ว่าง ~offset 6000)
- คืน JSON `{success, data:[...]}` · fields: `id text(=prompt) thumbnail_url media_urls author_username likes views model prompt_ready image_width/height rank`
- ⚠️ **ไม่มี field `categories`** (param category ถูก ignore) → category ได้เฉพาะที่ overlap กับ 1446 เดิม
- `sortBy=rank` (default) · limit สูงสุด ~50/หน้า
- get full prompt ต่อ id อีกทาง: **FxTwitter** `https://api.fxtwitter.com/status/<id>` (id = tweet id; tweet text = prompt) — ข้าม meigen เลย

## 🏠 บ้านจริง = `/Volumes/PS Catches/prompt-library/` (external drive)
> ✅ **FDA ใช้ได้แล้ว (2026-07-06)** — tool อ่าน/เขียน external + Desktop/Documents ตรงได้, รัน `python3 sync.py` บน external ผ่าน background task ได้เลย
> ถ้ากลับมาติด `Operation not permitted` อีก: toggle FDA Terminal.app ปิด→เปิด + Cmd+Q Terminal แล้วเปิดใหม่ (TCC ส่งสิทธิ์ตอน launch เท่านั้น)
> orphan ที่ผู้ใช้ต้องลบเองใน Finder: `~/Documents/prompt-library` + `~/Desktop/prompt-library` (~870MB)

## staging (tool เข้าได้) = `/Users/Shared/prompt-library/` (ลบทิ้งแล้วหลัง copy)
> ⚠️ **tool ไม่มี Full Disk Access** → เข้าไม่ได้เลย: `~/Desktop`, `~/Documents`, `/Volumes/*` (external ทุกตัว) = `Operation not permitted`. ที่ก่อนหน้า "เขียนสำเร็จ" ที่ Desktop/Documents จริงๆ Finder มองไม่เห็น (sandbox)
> ✅ **ที่ tool เข้าได้จริง (read+write): `/Users/Shared` · `~/.claude` · `/private/tmp` (scratchpad)**
> → เก็บที่ **`/Users/Shared/prompt-library`** (Finder เห็นที่ Macintosh HD→Users→Shared)
> **ย้ายไป external ต้อง manual** (Finder ลากไป /Volumes/...) — tool เขียน external ไม่ได้จนกว่าจะให้ FDA (แม้ให้แล้วอาจไม่ผ่านถ้า harness รัน helper แยก)
> ⚠️ **foreground bash python พังเรื่อง import (PermissionError importlib)** — รัน python ผ่าน **background task** เท่านั้น
> orphan ต้องลบเองใน Finder: `~/Documents/prompt-library` + `~/Desktop/prompt-library` (~870MB)

### ไฟล์ใน library
- `meigen-all.json` — **6,519 records** (sync 2026-07-06: +481) · gallery รวม youmind = 7,358 cards
- `meigen-prompts-1446.json` — curated (category จริง)
- `thumbs/` — 360px (~434MB)
- `gallery.html` — filter model+category+search+copy
- `lib.py` — helper (API/classify/thumb) · `build_gallery.py` · `query.py`
- `init.py` — ตั้งครั้งแรก · **`sync.py`** — 🔄 incremental update

## 🔄 อัพเดตของใหม่ (incremental — ไม่อ่านทั้งเว็บ)
```
cd ~/Documents/prompt-library && python3 sync.py        # (รันผ่าน background task)
```
- ดึงจาก offset 0 (sortBy=date) → เก็บเฉพาะ id ที่**ยังไม่มี** → หยุดเมื่อเจอหน้า all-known ติดกัน 8 หน้า
- classify + โหลด thumb เฉพาะใหม่ → rebuild gallery
- `--full` = re-pull ทั้งหมด (นานๆที) · `--deep N` = สแกนลึกขึ้น
- ✅ ทดสอบแล้ว: เจอใหม่ 9 อัน merge เร็ว ไม่แตะของเก่า
- แนะนำรันสัปดาห์ละครั้ง (เว็บ refresh weekly)

## 🧪 LLM classify — ลองแล้ว ไม่คุ้ม (คง keyword 68%)
- Haiku validate 300 อัน = **49% แย่กว่า keyword 68%** + ช้า (agent 30นาที/300)
- เหตุ: category = **taxonomy เฉพาะของ MeiGen** ไม่ใช่สากล → keyword ที่จูนเข้าหา tag เดิม ชนะ LLM ที่ตัดสินตามความหมายทั่วไป (เช่น poster มีรูปคน → Haiku เรียก Photography)
- สรุป: **90% ไม่เกิดกับ taxonomy นี้** เว้นแต่ Sonnet + few-shot ต่อหมวด (~85%, แพง/ช้า). คง keyword 68% (auto flag `auto_category:true`)

## 💾 Local copy (เก่า — `~/Desktop/prompt-library/`)
- **`meigen-all.json`** — 🔥 **FULL 6,029 records** (ดึงหมดผ่าน API) · gptimage 3764 · nanobanana 1755 · midjourney 198 · z-image/flux2/seedream/grok ฯลฯ · 3671 tweet + 2358 community · category มีแค่ 1404
- `meigen-prompts-1446.json` — curated best (มี category ครบ)
- `thumbs/{id}.jpg` — thumbnail 360px
- **`gallery.html`** ⭐ — Pinterest browser: filter model+category + search + copy (เปิด browse อันนี้)
- `fetch_all.py` — re-pull ทั้งเว็บ (API paginate) · `classify.py` — จัดหมวด · `build.py` — โหลด thumb+resize+rebuild gallery · `query.py` — คัด CLI
- อัพเดตของใหม่: `python3 fetch_all.py && python3 classify.py && python3 build.py`

## 🏷️ Category (จัดครบ 6,029 แล้ว)
- API ไม่คืน category → เขียน **keyword classifier** (`classify.py`, weighted, tiered PRIO) จัดหมวดที่เหลือ
- **accuracy ~68% top-1** (วัดกับ 1,404 curated ที่รู้จริง, 6-class keyword) — real category ของ 1446 ไม่แตะ, auto ที่เหลือ flag `auto_category:true`
- dist สุดท้าย: Photography 2007 · Product&Brand 1230 · Illustration&3D 1149 · Poster 652 · Other 567 · Food&Drink 321 · UI&Graphic 153
- ⚠️ auto = เดา ~68% → filter category คร่าวๆ; อยากแม่นกว่านี้ต้อง embedding/LLM classify (keyword ตันที่ ~68%)
- gallery มีปุ่ม filter model + category ครบ (thumbs 437MB, resize 360px)
- thumbnail community = full-res ต้อง `sips -Z 360` (build.py resize sweep ทำให้แล้ว — กัน folder บวม 5.8GB→437MB)
