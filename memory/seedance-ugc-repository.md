---
name: seedance-ugc-repository
description: "How to write Seedance 2.0 prompts for realistic UGC talking-head ads that don't look AI"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Seedance 2.0 — UGC / Talking-Head Ads (คลังความรู้ + ตัวอย่าง)

> แนวทำคลิป UGC ดูจริง ไม่เหมือน AI. คู่กับ [[seedance-knowledge]] (สูตรทั่วไป) + [[seedance-prompt-repository]] (ตัวอย่างแนวอื่น)
> เก็บ มิ.ย. 2026. หมวด UGC/Talking-Head เป็นช่องว่างที่ [[seedance-prompt-repository]] ยังไม่มีตัวอย่าง

## ทำไม UGC ต่างจาก prompt ทั่วไป
- คลิป UGC ตาย ถ้าออกมา "stock actor แกล้งเป็น creator" — สว่างเกิน เนียนเกิน ไม่มี friction
- 4 จุดที่ต้องสั่งชัด: **camera identity + imperfection + dialogue ตรงเลนส์ + negative cue** — ขาดอันใดอันหนึ่ง = AI tell

## โครงสร้าง UGC prompt (4 layer)
1. **Subject & Scene** — บรรยายคน/ของอย่างน้อย 3 detail (อายุ, เชื้อชาติ, เสื้อผ้า, สถานที่)
2. **Hook (0–3s)** — action เปิดดึงสายตา + ประโยคแรกพูดเข้ากล้อง
3. **Product moment (4–10s)** — โชว์ของ, โชว์ label close-up
4. **Closing (11–15s)** — hero shot / ประโยคปิด / pull back

## Realism keywords (ตัวคุมลุค "จริง")
**Camera identity** (สำคัญสุด — นำหน้า prompt):
- `UGC creator` ตอนเปิด → bias เป็น handheld phone footage ทันที
- เสริม: `iPhone`, `shot on iPhone 14 Pro`, `handheld`, `handheld shaky cam`, `harsh sunlight`

**Imperfection cues** (สู้ "ผิวพลาสติก/influencer สวยเกิน"):
- `slightly imperfect skin texture`, `slight overexposure`, `grainy`, `natural available light`, `ring light warmth`, `no script energy`, `imperfections present`
- `casual clothing`, `eye contact pauses`, `ambient environmental audio` (ไม่ใช่เพลง)
- ⚠️ ขาด "natural lighting" / "imperfect skin" → ได้ glossy influencer หลุดจากแคมเปญความงาม

## Dialogue + lip-sync (Seedance ทำเสียง+ปากใน pass เดียว)
- เขียน `looks at camera, says,` แล้วใส่ประโยคใน **เครื่องหมายคำพูด** เช่น `She says directly to camera, "Okay I need to talk about this."`
- ประโยคสั้น **< 15 คำ/cut**
- creator จริงมองเลนส์ สบตา → สั่งออกมาเป็นคำ

## Negative cues (ปิดท้ายทุก prompt)
`No music, No logo, no text on screen` — กัน library music / watermark / text หลุดเข้าเฟรม (default พวกนี้ทำคลิป UGC พัง)

## Timestamp scripting
`0 to 3s: [action + dialogue]. 4 to 9s: [action]. 10 to 15s: [action + closing line].`
ทุก segment ใส่ camera move + detail

## Character / Product consistency
- **อัปหน้าได้ปกติ** (verified มิ.ย. 2026) — host ที่เราใช้ **Higgsfield + kie.ai รับรูปหน้าจริงเป็น reference ได้ ไม่บล็อก** ใช้คุมหน้า actor ตรงๆ (kie.ai โฆษณา "Realistic Human Support"). **ไม่ต้องเบลอ**
  - blur-face trick = เฉพาะ host ที่บล็อก (เช่น Segmind — เราไม่ได้ใช้) → ข้ามได้
- **@AssetN** — anchor ของ: `@Image1`, `@Video1` สำหรับ product ตรงพิกเซล. label/สี/รูปทรงคงที่ดี (text เล็กอาจเพี้ยน)
- **Omni-reference** — ยิ่งให้ภาพ reference เยอะ โมเดลยิ่งใช้จริง (unboxing เคสใช้ 6+ ภาพ consistency สูง)
- **Extension > regeneration** ⭐ — จุดแข็งสุดของ 2.0: gen คลิปที่ชอบแล้ว **feed กลับเป็น video reference สั่ง "continue"** → actor/เสียง/ของ/ฉาก เดิมต่อเนียน ดีกว่า gen ใหม่ 2 รอบ
- **Audio matching** — อัด voiceover ในที่ที่ ambient ตรงฉาก (ฉาก gym ต้องมีเสียง gym; อัดเงียบ = หลุดบรรยากาศ)

## 7 ecom use cases
1. Full Story UGC — product image + scripted VO → Seedance ด้น scene/cut/B-roll
2. Talking Head + Avatar Control — blurred actor ref + product image
3. Video Extension — feed clip ต่อ actor/เสียง/ของเดิม
4. Green Screen UGC — actor พูดหน้า background ภาพ (paper/screenshot)
5. Unboxing — feed 6+ ภาพ packaging/product/env
6. Lip-sync เสียงตัวเอง — อัปเสียงจริง → AI actor ลิปซิงค์คำเป๊ะ
7. Cinematic Ad — scene breakdown + face reference

---

## ตัวอย่างเต็ม (copy-paste ได้)

**A. Honest Review** *(รีวิวซื่อๆ เช้าๆ ไม่แต่งหน้า)*
```
A 26-year-old South Asian woman sits casually on her bathroom counter in the
morning, no makeup, just woken up. She holds a small amber glass serum bottle up
to the camera, squinting slightly like she is genuinely thinking.
0 to 3s: She says directly to camera, "Okay I need to talk about this." Handheld
camera, natural bathroom lighting, slightly overexposed.
4 to 9s: She presses two fingers to her cheek and shows the bottle label close up.
10 to 15s: She looks back at camera, grins, says "You will thank me later" and the
camera slowly pulls back.
Warm tone, documentary feel, 9:16 vertical, ambient morning sound.
```

**B. Founder Style** *(เจ้าของแบรนด์เล่า)*
```
A 35-year-old woman at a clean kitchen table, minimal branding visible in
background. She looks directly into camera with a calm, knowledgeable expression
and no script energy.
0 to 4s: "We built this because I could not find anything that actually worked for
me." She sets a product bottle on the table. Soft overhead lighting, fixed stable
camera.
5 to 10s: She slides it closer to camera and explains one thing about it.
11 to 15s: She looks up from the product to camera and says "That is why I made
this." Long beat. Holds eye contact.
Warm, premium feel, 9:16 vertical.
```

**C. Street Interview** *(สัมภาษณ์ข้างถนน)*
```
Outdoor street setting, busy sidewalk slightly blurred in background. A 22-year-old
man stops mid-walk, turns to camera. Hoodie, earbuds around his neck.
0 to 3s: "Someone just told me about this and I had to try it." He pulls the product
out of his jacket pocket. Handheld shaky cam, natural city sounds.
4 to 9s: He holds it up, turns it over once. "Okay it is actually exactly what they
said." Close-up on his face.
10 to 15s: He looks back at camera, laughing slightly, says "Yeah I am sold" and
walks off frame.
Authentic vibe, 9:16, no music, street ambient audio.
```

---

## เช็กลิสต์ก่อนกด generate (UGC)
- [ ] เปิดด้วย `UGC creator` / camera identity (iPhone, handheld)?
- [ ] มี imperfection อย่างน้อย 1 (overexposed / grainy / imperfect skin / natural light)?
- [ ] dialogue อยู่ในเครื่องหมายคำพูด + `says directly to camera` + < 15 คำ?
- [ ] timestamp แบ่ง 0–3 / 4–9 / 10–15?
- [ ] ปิดท้าย `no music, no logo, no text on screen`?
- [ ] aspect 9:16 (vertical) สำหรับ Reels/TikTok?
- [ ] product anchor ด้วย @Image1 ถ้าต้อง label เป๊ะ?

---

## 🏭 End-to-end UGC system (8-step) + meta-prompts (จาก AI Video Bootcamp guide)
> cross-validate ของเดิมเกือบหมด — เก็บเฉพาะ 3 อันใหม่ที่ของเดิมไม่มี

**8-step pipeline:** platform (Higgsfield/Freepik) → character ref image (Nano Banana 2 / GPT image, **identity เท่านั้น ไม่ใช่ scene** = reference-mode insight) → product ref (label คม, logo กลาง, lighting neutral, undistorted) → Seedance config (9:16, 15s, hyper-realistic, 1080p, ambient) → master prompt → hook → combine → scale

**5-beat timestamp structure:**
`0–3s Hook (pattern interrupt) · 3–6s Problem/Observation (relatable) · 6–10s Product Interaction (natural handling) · 10–13s Benefit Payoff (casual no hype) · 13–15s Casual Closing/CTA`

### ⭐ 1. Universal UGC Master Prompt (meta-prompt = prompt ที่สร้าง prompt)
วางใน Claude/GPT พร้อมแนบรูป product + character → ได้ Seedance prompt 1 อัน:
```
I'm attaching an image of my product and character. Act as an expert UGC ad director, TikTok scriptwriter, direct-response marketer, and Seedance 2.0 prompt engineer. Create one polished 15-second Seedance 2.0 prompt for a realistic UGC-style product ad for TikTok/Reels in vertical 9:16. Study the product image carefully and preserve exact shape, colour, packaging, branding, logo placement, label text, texture, size, proportions. Use the character reference for identity only. The final video should feel like a real creator casually filmed it on their phone in a believable everyday setting. Include: strong opening moment / natural product introduction / realistic product interaction / grounded benefit / casual final beat-CTA. Dialogue natural and unscripted. Avoid exaggerated claims or transformations. Specs: vertical 9:16, handheld phone movement, natural lighting, imperfect framing, realistic skin texture, believable environment, product interaction, ambient sound only, no music, no voiceover, no on-screen text. Output one timestamped Seedance 2.0 prompt.
OPTIONAL ADD-ON: target customer: [audience] · problem/desire: [pain point] · angle: [lifestyle/before-after/social proof]
```

### ⭐ 2. Viral Hook Generator (meta-prompt)
```
Act as an expert viral short-form creative director and Seedance 2.0 prompt engineer. Generate 10 chaotic hyper-realistic phone-camera hook ideas designed to instantly stop scrolling. Hooks must: feel raw and believable / include realistic physics / begin with a strong pattern interrupt / include a punchline line of dialogue / use ambient sound only / avoid cinematic polish. Output per hook: Title | Idea Summary | Why It Works | Seedance Prompt | Spoken Line | Sound Design | Realism Upgrades.
```
chaotic hook ที่เวิร์ก: ของหล่นจากเพดานเข้ากล้อง · ประตูกระแทกเดินเข้า · คนโผล่กลางเฟรมไม่ทันตั้งตัว · พูดอยู่โดนขัดจังหวะ · ขว้างของเข้าเลนส์

### ⭐ 3. Modular scaling (15–30 วิดีโอ/1 product)
**build once:** 1 character identity pack + 5 hook templates + 10 product-interaction scripts + 3 lighting environments → **mix any hook+script+env = 1 unique video** → 1 product = 15–30 คลิป

### Worked example (Diet Coke) — โครง prompt UGC เต็มที่ดี
identity (same face, pores, freckles, realistic hands) + product (preserve red branding, logo, "12 Cans", proportions, no warp) + 4 beat timestamp dialogue + `No music. No voiceover. No on-screen text. No cinematic lighting.`

## แหล่งที่มา
- [AI UGC Ads Complete Production Guide (Seedance 2.0) — Google Doc / AI Video Bootcamp](https://docs.google.com/document/d/1UcdHQioQXuQiEvM0t42jHIQ48etknLYt1oEH8vW6z_I/edit) — 8-step system, master prompt, hook generator, scaling
- [Atlabs — Make UGC Ads with a Single Prompt (15+ prompts)](https://www.atlabs.ai/blog/how-to-make-ugc-ads-with-a-single-prompt-using-seedance-2.0-(15-prompts)) — โครงสร้าง 4 layer, dialogue, ตัวอย่างเต็ม
- [Starpop / David Ishag — Make AI UGC Videos (7 ecom use cases)](https://starpop.ai/blog/articles/how-to-make-ai-ugc-videos-seedance-2-0) — blur face trick, extension, omni-reference
- [VideoAI.me — 7 UGC Templates to Steal](https://videoai.me/blog/seedance-2-0-ugc-prompts)
- [GitHub — YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) — 2000+ curated prompts (cinematic/anime/UGC/ads)
