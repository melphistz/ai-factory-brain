---
name: youmind-gpt-image-prompt-library
description: YouMind GPT Image 2 prompt library — browsable/filterable prompt gallery; useful filters for our UGC/product-ad lane
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# YouMind — GPT Image 2 Prompt Library

URL: https://youmind.com/gpt-image-2-prompts/explore

> Prompt gallery กรองได้ (filter by use-case / style / subject). Featured cards ส่วนใหญ่ = anime/game/poster (ไม่ใช่ lane เรา) — **ของดีอยู่หลัง filter**.
> เกี่ยว: [[ai-influencer-image-prompt]] · [[seedance-ugc-repository]] · [[image-prompt-suffixes-techniques]] · [[storyboard-gpt-image-to-seedance]]

## filter ที่ตรงงานเรา (กดไขว้)
- Style: **Photography · Cinematic/Film Still**
- Subject: **Influencer/Model · Product · Food/Drink · Fashion Item**
- Use case: **Product Marketing · E-commerce Main Image · Comic/Storyboard**
- ไขว้ที่คุ้ม: Photography×Influencer/Model (UGC), Photography×Product (ad shot), Storyboard×Cinematic (keyframe)

## ⚙️ วิธี crack ดึง prompt เต็ม (WebFetch มองไม่เห็น — ใช้ curl+python)
เว็บ = Next.js App Router SSR, prompt เต็มฝังใน RSC payload ของ HTML (ไม่ต้อง JS render):
1. `curl "https://youmind.com/gpt-image-2-prompts/explore?categories=<cat>"` → grep `\"slug\":\"..."` + `/prompts/<slug>-<id>` = URL card จริง
   - category URL เปลี่ยนผลจริง (WebFetch แค่มองไม่เห็น)
2. `curl "https://youmind.com/prompts/<slug>-<id>"` → หน้า detail (~550KB)
3. prompt เต็มอยู่ 2 ที่: **T-chunk** `\w+:T<hex>,<text>` (อ่าน hexlen bytes) · หรือ **inline `<span>` highlight** (คำ variable)
4. python: replace `\\"`→`"`, strip `<[^>]+>`, ตัด RSC noise `"])</script>...push([1,"` → ได้ prompt ดิบ
   - boilerplate ซ้ำหลายหน้า (flame demo, roast deck, "Goal: luxurious poster") — dedup ด้วย freq หรือ match keyword จาก slug
5. script ที่ใช้จริง: `scratchpad/pull.py` + `extract.py` (session 1700360a)

## 🎯 Prompt เต็มที่ดึงมาแล้ว (lane เรา — เก็บ pattern)
- **Gen-Z Editorial** = identity-lock (100% + anatomy list) + `{argument name="furniture color"}` → เต็มใน [[ai-character-identity-lock]]
- **Tropical Leaf**: oversized palm leaf เป็น *sculptural fan-shaped backdrop prop* เต็มเฟรม + rim light · vertical 4:5
- **Golden-Hour Rooftop** (male): low angle, sky ~70% frame, faint contrail, oversized crewneck streetwear
- **Industrial Loft**: editorial ใน laundromat (chrome drum doors, black pole แบ่ง left-third) + `{argument name="model identity"}`
- **Tennis Club**: 2-subject blocking เต็ม (foreground+behind, mid-stride, rim light) · vertical 3:4 waist-to-thigh
- **Coquette Tea Room**: feminine detail-heavy (exactly 3 tea-time items, prop list เป๊ะ)
- **Blueberry Pop-Art poster**: 90s diner food ad (halftone dots, stacked type "BLUEBERRY BLAST")
- **Style presets** (restyle รูปเดิม 1 บรรทัด): Cinematic Drama · Golden Hour · Product Hero · Editorial Cut · Neon Portrait · Action Motion

## 💡 Pattern ที่ขโมยได้ (ใช้ซ้ำทุก prompt)
- **`{argument name="x" default="y"}`** = template ตัวแปร → ตรง modular hook-swap [[ai-ugc-ad-factory-workflow]]
- **negative tail มาตรฐาน:** `no text, no watermark, no extra people`
- **crop ระบุชัดเสมอ:** vertical 4:5 / 3:4 · waist-to-thigh / bust-length framing
- **นับ prop เป๊ะ:** "exactly 3 tea-time items", "show exactly two women" → กัน AI ใส่มั่ว
- **prop เป็น backdrop:** ของชิ้นใหญ่ (ใบไม้) เป็น sculptural background = composition trick ง่าย

## caveat
- ค่า = หา angle/composition/template ใหม่มาเสริม **ไม่ใช่แทน** repo prompt ที่เรามี (ลึกกว่าด้าน realistic UGC)
- library เคลม 11,000+ prompts / multi-model (Nano Banana Pro, Seedream 4.5, GPT Image 1.5/2)

## 💎 เทคนิคที่ขโมยได้ (จาก social-media-post + profile-avatar filter)

### 1. Identity-preservation clause แบบลิสต์ anatomy (แน่นสุด)
"100% identity preservation, exact face shape, bone structure, forehead, eyebrows, eyes, nose,
lips, ears, jawline, hairline, facial hair, hairstyle" → เก็บเต็มใน [[ai-character-identity-lock]]

### 2. Realistic UGC selfie framing (anti-AI look)
- **Mall selfie:** "iPhone-style ultra-wide photo, shot at chest height, front-facing mirrorless selfie"
- **Mirror selfie (reels):** "ultra-realistic mirror selfie, vertical 9:16, mid-torso to upper-thigh crop"
- **Bedroom close-up:** "ultra-realistic casual smartphone selfie, close-up horizontal 16:9"
- ต่อยอด realism stack ใน [[ai-influencer-image-prompt]]

### 3. Variable/template syntax
prompt ใช้ `{argument name="hair style"}` = ทำ prompt reusable เปลี่ยนตัวแปรได้ → ตรงกับ modular hook-swap [[ai-ugc-ad-factory-workflow]]

### Card ตรง lane (bookmark)
Casual Mall Selfie · Realistic Shy Bedroom Selfie · Realistic Indian Man Mirror Selfie (9:16) ·
High-End Gen-Z Editorial (identity-lock) · Cinematic Golden Hour Backlit · Cozy Job Offer Celebration (lifestyle golden hour)
> ข้าม: anime / cyberpunk / comic / horror — ไม่ใช่ lane

## sibling site
- youmind.com/skills = skill marketplace สาย academic/investment/การศึกษา — **ไม่เกี่ยวงานเรา** (เช็คแล้ว ไม่เก็บ)
