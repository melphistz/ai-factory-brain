---
name: seedance-knowledge
description: How to write prompts for Seedance 2.0 AI video model to get cinematic results
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Seedance 2.0 — Prompt Writing Knowledge

Seedance 2.0 = AI text/image-to-video model ของ ByteDance. ทำวิดีโอ cinematic จาก prompt. รองรับ multimodal reference (image/audio/video).

## 🎯 HOST ที่เราใช้: Higgsfield + kie.ai เท่านั้น
> spec อ้างอิง 2 host นี้ (ไม่ใช่ model-native ทั่วไป). ทั้งคู่ **รับรูปหน้าจริง** (kie.ai โฆษณา "Realistic Human Support")

| รายการ | **Higgsfield** | **kie.ai** |
|---|---|---|
| Ref assets | **≤12 รวม** (9 img / 3 vid 15s each / 3 audio) | 9 img / 3 vid / 3 audio |
| Duration | up to **15s/shot** (ต่อ multi-shot ได้) | up to 15s |
| Resolution | **native 4K** ⭐ | ตาม tier |
| variants | Enhanced / Enhanced Fast · **Seedance Unlimited** (30 วัน unlimited gen, BytePlus partner) | Seedance 2.0 / **Fast** (~4min) / **Mini** (ถูก/เร็วสุด) · ปกติ ~5min/gen |
| reference | character/face/clothing/style lock, auto-interpret role | `first_frame_url` + `asset://{assetId}` · consistent character |
| เข้าถึง | global ไม่มี waitlist, ไม่ต้อง business account | **API** (เหมาะ automate/scale) |
| หน้าจริง | ✅ รับ | ✅ รับ ("Realistic Human Support") |

**ร่วม (model-native):** FPS 24 fixed · aspect 16:9/9:16/1:1/4:3/3:4/21:9/9:21 (ignore ถ้าใส่ ref image) · prompt max 2000 chars · duration steps 4,5,6,8,10,12,15
- **Higgsfield** = UI + native 4K + Unlimited add-on → เหมาะงาน hands-on คุณภาพสูง
- **kie.ai** = API + Fast/Mini → เหมาะ automate/batch/ต้นทุนต่ำ

**สถาปัตยกรรม:** unified multimodal audio-video joint generation — text+image+audio+video เข้า pass เดียว ออกพร้อม **synchronized audio ในตัว** (ไม่ต้องใส่เสียงทีหลัง)

**ความสามารถใหม่ (2.0):**
- **native synced audio** — เสียง+ปาก sync ใน pass เดียว
- **web search grounding** — ดึงข้อมูลเว็บมาประกอบ
- **adaptive aspect ratio** mode
- **video extension** — ต่อคลิปจาก video reference
- **first frame / first+last frame** i2v mode
- modes: text-to-video · image-to-video · multimodal-reference-to-video

**⚠️ Content policy:** **Higgsfield + kie.ai อัปหน้าจริงได้ ไม่บล็อก** (verified มิ.ย. 2026) — เคลมเก่า "faces blocked" มาจาก Segmind (host ที่ไม่ได้ใช้) ไม่ใช่ universal · ไม่ต้องเบลอหน้า · ยังมี IP guardrail (กันคนดัง/ลิขสิทธิ์) + C2PA watermark

**ช่องทางเรา:** **Higgsfield** (UI, native 4K, Unlimited) + **kie.ai** (API, Fast/Mini) · official ref: higgsfield.ai/seedance/2.0 · kie.ai/seedance-2-0 · docs.kie.ai/market/bytedance/seedance-2

## Core formula (6 ขั้น)

`Subject → Action → Environment → Camera → Style → Constraints`

1. **Subject** — anchor ของวิดีโอ. ระบุละเอียด: appearance, อายุ, เสื้อผ้า. เช่น แทน "a woman" → "A young woman in her 20s with long black hair, wearing a white linen dress"
2. **Action** — verb เดียว present tense, 1 action ต่อ shot. quantify ความแรง. เช่น "she walks slowly toward the window" (ไม่รวมหลาย action)
3. **Environment** — location + lighting + atmosphere
4. **Camera** — primary instruction เดียวเท่านั้น
5. **Style** — visual reference เจาะจง (35mm, ARRI ALEXA aesthetic)
6. **Constraints** — negative prompt ตัดปัญหา

**Word count:** 60–100 คำ (มาตรฐาน). สั้นไปขาด detail, ยาวไป instruction ขัดกัน. แต่ฉาก complex (transformation/fight/animation) ใช้ 400–900 คำ shot-by-shot ได้.

## หลักสำคัญสุด

- **เปิดด้วย Subject + Action** — 20–30 คำแรกน้ำหนักมากสุด. model lock subject+action ก่อน process ที่เหลือ
- **Specific ชนะ generic** — ยิ่ง detail ยิ่ง consistent
- **1 action / 1 shot** — หลาย action ในคลิปสั้น = รีบ/มั่ว

## Camera movement (8 แบบ) — leverage สูงสุดต่อคุณภาพ

| Movement | ใช้เมื่อ |
|---|---|
| Push-in | เน้นอารมณ์ |
| Pull-out | เผยบริบทกว้าง |
| Pan | tracking แนวนอน |
| Tracking | ฉาก action ตามตัวละคร |
| Orbit | product/portrait |
| Aerial | landscape, scale |
| Handheld | documentary feel |
| Fixed | เน้น action ของ subject |

**กฎ camera:**
- ใช้ **camera move เดียว/shot** — "slow dolly push-in" หรือ "fixed camera". ห้าม "dolly in while panning + tilting" → jitter
- ต้อง compound: บอก primary แล้วตาม secondary — "camera low tracking shot then subtle rise"
- ใช้ **rhythmic words** (slow, smooth, stable, gradual, gentle) ไม่ใช่ technical spec (24fps, f/2.8, ISO 800)
- แยก camera motion ออกจาก subject motion ชัดๆ

## Lighting = leverage สูง

เพิ่ม lighting → คุณภาพขึ้นเยอะ. keywords: golden hour, rim light, natural light, neon, backlit, overcast.
เช่น "A person walking" → "A person walking in soft golden hour lighting"

## Multimodal reference (@-role)

upload asset แล้ว assign role ด้วย `@` — ต่างระหว่าง model เดา vs model รู้
- `@image is the first keyframe and style reference`
- "use the composition from Image 1" / "follow the action from Video 2"
- ปกติ 1–4 image/prompt
- VFX inline: ใส่ `[VFX: branching electric circuits pulsing with white-blue current]` แทนบรรยายแยก

## Shot structure (ฉากซับซ้อน)

ระบุบนหัว prompt: จำนวน shot, duration รวม (ปกติ 15s), aspect ratio (16:9).
Timed segments สำหรับ animation: `0–3s: WIDE SHOT...`, `3–6s: ...`
ปิดท้าย: `Total: 15s / 6 shots / 16:9`

## Pitfall checklist

- ❌ ซ้อน camera move ที่ขัดกัน
- ❌ ใช้ "fast" ลอยๆ → jitter
- ❌ fast camera + fast subject + complex scene พร้อมกัน
- ❌ adjective ฟุ่มเฟือย ("amazing", "beautiful")
- ❌ technical jargon (fps, ISO, focal length) ใน rhythm
- ✅ negative prompt จำเป็น: "avoid jitter", "avoid bent limbs", "avoid temporal flicker", "avoid identity drift"
- ✅ บังคับ realism: เพิ่ม "no 3D, no cartoon, no VFX"
- ✅ locked POV: บอกชัดว่า camera ไม่ทำอะไร

## Iteration loop (official)

1. baseline gen 2–3 options
2. เปลี่ยนทีละ 1 element
3. score ตาม continuity + instruction adherence
4. เลือกตัวคะแนนสูงสุด

## 🧪 เทคนิคจากชุมชน (secondhand จาก Reddit r/StableDiffusion + r/generativeAI)
> Reddit/X ค้นตรงไม่ได้ (ดู [[exa-mcp-setup]]) — พวกนี้มาจากบล็อกที่สรุป thread มาให้ (fliki, devtalk forum, studiolist อิง "thousands of generations")

**ของใหม่/คมกว่าเดิม:**
- **lighting = physical ไม่ใช่ emotional** — แทน "moody atmosphere" → "single focused spotlight descending from above, sharp circular pool of warm tungsten light, sharp falloff into deep shadow"
- **อารมณ์ = physical action** — แทน "she is afraid" → "her shoulders tense, her jaw tightens for half a second" (director mindset)
- **reflective surface = ได้ความซับซ้อนฟรี** ⭐ — wet pavement/polished floor บังคับ model render reflection → "double visual value for free" (= เหตุผลที่ Valenshield ใช้ glossy black floor ถูกแล้ว — [[valenshield-nurse-ad-project]])
- **@Audio reference คุม pacing** — อัปเพลง/VO เป็น @Audio → visual cut + camera sync เข้า beat
- **timecode บังคับกระจาย action** — ไม่มี timecode → Seedance ทิ้ง payoff ใน 2 วิแรก. format: `[0:00-0:03] ... [0:03-0:06] ...`
- **lens = compression จริง** — 24mm(wide)/50mm(std)/85mm(portrait)/135mm(tele) → model ปรับ bokeh+compression ตาม
- **cultural shorthand** — "Wes Anderson symmetry", "Ridley Scott atmosphere", ชื่อผู้กำกับ → ลุคทันที (เชื่อม [[director-styles-knowledge]] · [[mv-directors-knowledge]])

**6-section shot-plan (devtalk community):** Scene · Subject · Camera · Timeline · Style · Consistency constraints — "prompt ที่ดี = shot plan เล็กๆ ไม่ใช่แค่ยาว"

**known limitations (ชุมชนเตือน):**
- full-body shot artifact ง่ายกว่า medium/close-up (= เหตุผล Valenshield Clip 4 split-leap หินสุด — ใช้ medium/close ปลอดภัยกว่า)
- หน้าเพี้ยนใน sequence ยาว · character deform ตอน movement ซับซ้อน · text render ไม่นิ่ง

**ตอกย้ำกฎที่มีอยู่แล้ว (ชุมชนยืนยัน):** แยก camera/subject motion (กฎที่ beginner พังบ่อยสุด) · ห้าม "fast" ใช้ physics แทน · i2v บรรยายแค่ motion

**resource repos:** EvoLinkAI community repo (164 prompts) · GitHub 160+ curated prompts · [[seedance-prompt-repository]]

## 🎯 Input mode: reference vs first-frame vs first+last (เลือกก่อนเขียน — จากการลองจริง Valenshield)
> ตัดสินใจ **โหมด** ก่อนเขียน prompt — เลือกผิด = ผลพัง ไม่ว่า prompt ดีแค่ไหน
- **Reference image** = anchor identity/look แล้วให้ Seedance **generate action เอง** → เห็น action **ก่อน**ถึง pose ได้ (เช่น "วิ่งมาก่อนกระโดด"). lever = **prompt บรรยาย action arc ให้ชัด** (model สร้างตาม)
- **First frame** = ล็อก pose เปิดเป๊ะ animate ต่อ → **เห็นอะไรก่อนเฟรมนั้นไม่ได้** (ตั้งรูป split = เริ่มที่ split เลย ไม่มีวิ่งมา). เหมาะเมื่อเฟรม = จุดเริ่มจริง (เช่น landing เริ่มที่ลอยอยู่)
- **First + Last frame** = interpolate ระหว่าง 2 เฟรม → คุม A→B. แต่ 2 เฟรมห่างกันมาก (full-body → close) = morph สูง
- ⚠️ บทเรียน: "ใส่ reference แล้วไม่เริ่มจากรูป" ไม่ใช่ bug — reference ไม่ได้ล็อกเฟรมเปิด ถ้าอยากเริ่มจาก pose ต้องตั้ง **first frame**

## 🔍 Hyperzoom กลบ wide→close morph (จากการลองจริง)
อยากซูม wide→close ในคลิปเดียว (เช่น leap → ซูมรายละเอียด) — ปกติ morph เพราะตัวต้อง "ซูม" เอง:
- **slow push-in = เห็น morph ชัด** (ตัวละลายระหว่างทาง)
- ⭐ **hyperzoom เร็ว + motion blur = กลบ morph** (เบลอบังเฟรมกลาง) → ดีกว่า slow สำหรับเคสนี้
- สั่งผ่าน `rapid hyperzoom, heavy directional motion blur, whip-like push, settling sharp` — **ไม่ใช้ "fast" ลอยๆ** + เฟรมจบต้องคม (`keep final frame sharp, intentional motion blur only`)
- ถ้ายังเพี้ยน → fallback แยก 2 คลิป + cut/punch-in ใน CapCut (ชัวร์สุด)

## ✂️ Prompt-craft sharpeners (กลั่นจาก skill cinematic-prompt + video-prompt-builder)
> เก็บเฉพาะที่ช่วยจริง — ที่เหลือเรามีแล้ว/ขัดงาน identity (skill ห้ามบรรยายหน้า/อายุ/ชื่อผู้กำกับ = อย่าใช้กับ i2v identity-critical)

- ⭐ **mood = visual NOUN ไม่ใช่ emotional adjective** — แทน "melancholic/epic/moody" → ใช้ **golden haze, blue-grey mist, amber dust, silver overcast, halation, bloom, film grain**. ภาพ render ได้ ไม่ใช่นามธรรมที่ model เดา
- **specificity เป็นตัวเลข** — "frame rotates clockwise ~15-20°", "~20-25% speed", "low-angle push-in" > "tilt / slow / zoom". ระบุองศา/% ให้ model เป๊ะ
- **transitions = shots** — whip pan / bloom flash / motion-blur smear = creative beat ออกแบบ exit→entry (ชั้น edit/CapCut)
- **contrast = impact** — สลับ high/low density · slow-mo หลัง speed ramp กระแทกกว่า ramp ติดกัน (ดู [[video-prompt-builder-framework]])
- **signature + resolve** — ทุกชิ้นมี hero effect 1 อัน callout ชัด · เปิดแรงแค่ไหน จบต้อง land ตั้งใจ
- **prose director-briefing mode** (ทางเลือก) — เขียนเป็น paragraph ลื่นเหมือน brief DoP แทน shot-list — เหมาะ **mood/atmospheric piece ที่รูป anchor identity แล้ว** (ไม่ใช่ UGC/product ที่ต้องระบุหน้า/ชุด)
- **3-tool decision:** prose (cinematic-prompt) = mood scene · shot+effects ([[video-prompt-builder-framework]]) = วางทั้งโฆษณา · per-clip (ไฟล์นี้) = i2v identity-critical เนียน

## 😢 Verified worked-example — emotional arc i2v (timecoded micro-beats) ✅ ก.ค. 2026
> พิสูจน์แล้วบน Higgsfield Seedance 2.0, i2v 15s/720p. โจทย์: ผู้หญิงญี่ปุ่น golden-hour rooftop แสดงอารมณ์ไล่ ยิ้ม→เศร้า→น้ำตาไหล→ก้มเช็ด ใน 15 วิ. **ผล: arc ทำงานเกือบเป๊ะ + identity นิ่ง + น้ำตา realistic.**

**สูตรที่ได้ผล (reusable):**
- **แปลง % อารมณ์ → micro-beat ต่อ timecode** (0-3 / 3-7 / 7-11 / 11-15) — emotion = กล้ามเนื้อจริง (inner brow lift+draw together, lower-lid tighten, throat swallow, chin tremble, breath catch, tear spill, nostril flare, slow blink) ไม่ใช่ adjective
- **i2v: ไม่บรรยายหน้าซ้ำ** ใส่ positive identity-lock สั้นๆ + บรรยายแค่ performance/motion
- **motion-layer แยก 4 ชั้น** (subject perf / internal breath-blink-hair / camera / environmental) → คุมได้
- **น้ำตา + แว่น รับ golden hour = complexity ฟรี** (reflective) — ออกมาสวย
- final-frame cue ชัด (ก้มหน้า มือเช็ดใต้แว่น ตาเปียก restrained)

**tuning ที่เจอ (แก้รอบหน้า):**
1. "smile 20%" → model ยิ้มเปิดแรงกว่าตั้งใจ → ใช้ `faint closed-lip smile, barely there` + ลดคำ smile
2. "very slow push-in" → model reframe over-shoulder→tight เยอะ → `hold framing, minimal push-in` ถ้าอยากคงกรอบ
3. peak ปากเผยอเฉียด open-sob → `lips stay pressed, no open mouth` ถ้าต้อง contain กว่านี้
> เชื่อม MICRO_BEATS concept ใน [[shotlist-builder-skill]] + emotion=physical ใน [[seedance-2-pro-director-skill]]. prompt เต็มอยู่ใน session ก.ค. 2026.

## แหล่งที่มา

- [Apiyi — Official Prompt Guide: 6-step formula + 8 camera movements + pitfall checklist](https://help.apiyi.com/en/seedance-2-0-prompt-guide-video-generation-camera-style-tips-en.html)
- [Higgsfield — Complete Prompting Guide + full prompt library](https://higgsfield.ai/blog/seedance-prompting-guide)
- [invideo.io — How to Prompt Like a Pro](https://invideo.io/blog/seedance-2-0-prompt-guide/)
- [imagine.art — 70 ready-to-use prompts](https://www.imagine.art/blogs/seedance-2-0-prompt-guide)
- [Luma — How to Prompt Seedance 2.0](https://lumalabs.ai/learning-center/articles/how-to-prompt-seedance-2.0)
