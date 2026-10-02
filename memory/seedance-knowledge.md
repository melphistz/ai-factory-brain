---
name: seedance-knowledge
description: How to write Seedance 2.0/2.5 video prompts — formula, camera, timeline golden rule (ลำดับบอก/มุมปล่อย), under-direct acting, host specs Higgsfield/kie.ai + Seedance 2.5 specs (30s, 50 ref, region-edit)
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

## 🆕 Seedance 2.5 (confirmed บน Higgsfield ส.ค. 2026)
> verify ด้วย official source (higgsfield.ai/blog/seedance-2-5-on-higgsfield-2026) 28-08-2026 — ไม่ใช่แค่ third-party aggregator

- **Live บน Higgsfield จริง** ตั้งแต่ ส.ค. 2026 (model picker มี "Seedance 2.5 — NEW" คู่กับ "Seedance 2.0 4K — TOP")
- **Duration: สูงสุด 30s/generation** (จากเดิม 15s ของ 2.0) — clip ยาวเดียวจบ ไม่ต้อง chain multi-shot สำหรับงานสั้น-กลาง
- **Resolution:** 480p/720p/1080p native + upscale 4K ได้ (ไม่ใช่ native 4K แบบ 2.0)
- **Aspect ratio:** เลือกอิสระ 9:16 ถึง 21:9
- **Reference:** สูงสุด **50 images/clips** ต่อครั้ง (จากเดิม ≤12 ของ 2.0) — คุม identity/wardrobe/lighting ข้ามหลายช็อตได้ดีขึ้นมาก
- **ของใหม่:** region-level edit (แก้เฉพาะจุดไม่ต้อง regen ทั้งคลิป), native audio pass เดียว, direct control selector (era/genre/lighting/physics) เป็นทางเลือกแทน text prompt, prompt adherence ดีขึ้น ~20%
- **ราคา (Higgsfield):** 10s@720p ≈ 65cr (~$3.25) · 480p ≈ 30cr · 1080p ≈ 90cr → scale ตาม duration ตรงๆ
- **Prompt structure หลัก (subject/action/camera/light/sound/timing/constraints) ยังใช้ได้เหมือน 2.0** — clip ยาวขึ้นแค่ต้องวาง timed-beat ชัดกว่าเดิม (30s คิดเป็น sequence ไม่ใช่ moment เดียว)
- **Draft mode (verify Higgsfield API 2026-10-02):** `draft: true` = เจน 480p ก่อน แล้ว finalize เป็น 1080p ได้ภายใน 7 วัน (`draft_job_id`) → ทดสอบช็อตเสี่ยงถูก · modes: `t2v` / `omni_reference` / `video_edit` / `video_extension` (forward/backward)
- **char cap ต่อ prompt:** ยังไม่ยืนยันตัวเลขจริงของ 2.5 (2.0 = 2000 chars) — งานที่ทำไปยังไม่เจอ error ที่ ~2000 chars

**⚠️ บทเรียน (28-08-2026):** ตอน verify ว่า Higgsfield มี 2.5 ให้ใช้หรือยัง — WebSearch แรกไปเชื่อสรุปจาก reapi.ai (คู่แข่งขาย API) ที่บอกว่า "ยังไม่มีบน Higgsfield" ทั้งที่ลิงก์ higgsfield.ai/blog เองอยู่ในผลค้นหาเดียวกันแล้วไม่ได้เปิดอ่าน → **เช็ค availability เฉพาะแพลตฟอร์ม ต้องเปิด official source ของแพลตฟอร์มนั้นตรงๆ เสมอ อย่าเชื่อ third-party aggregator/คู่แข่งที่พูดถึงแพลตฟอร์มอื่น**

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

**ตัวอย่างครบสูตร (โครง minimal):**
```
A skateboarder lands a clean trick in an empty dawn parking lot,
camera low tracking shot then subtle rise, modern cinematic contrast,
avoid jitter and bent limbs.
```
Subject → Action → Environment → Camera → Style → Constraints — ครบใน 3 บรรทัด

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

**หมวดสไตล์ (ช่อง Style):** Cinematic (film tone, 35mm) · Quality (4K, high detail) · Film (grain, analog, vintage) · Tone (warm, cool, desaturated) · Atmosphere (moody, dreamy, ethereal)

## Multimodal reference (@-role)

upload asset แล้ว assign role ด้วย `@` — ต่างระหว่าง model เดา vs model รู้
- `@image is the first keyframe and style reference`
- "use the composition from Image 1" / "follow the action from Video 2"
- **Text vs References แบ่งหน้าที่:** text เก่ง "พื้นที่/หน้าตา/อารมณ์" (spatial) · reference video เก่ง "จังหวะ/การเคลื่อนไหว" (temporal) → ใช้ text สร้างฉาก + วิดีโออ้างอิงคุมการเคลื่อนไหว
- ปกติ 1–4 image/prompt
- VFX inline: ใส่ `[VFX: branching electric circuits pulsing with white-blue current]` แทนบรรยายแยก

## Shot structure (ฉากซับซ้อน)

ระบุบนหัว prompt: จำนวน shot, duration รวม (ปกติ 15s), aspect ratio (16:9).
Timed segments สำหรับ animation: `0–3s: WIDE SHOT...`, `3–6s: ...`
ปิดท้าย: `Total: 15s / 6 shots / 16:9`

**Timeline prompting (multi-shot):**
- **อย่าเขียนพารากราฟยาวก้อนเดียว**แล้วหวังให้โมเดลหาจุดตัดเอง — ใส่ป้ายกำกับแต่ละช็อต (Shot 1, Shot 2) แต่ละช็อตมี 1 แอ็กชันหลัก + 1 คำสั่งกล้อง
- ใช้ลูกศรบอกลำดับจังหวะ: `action › action › action`
- จัดระเบียบ prompt รอบ timestamp + ทิศทางกล้อง = แยก "คลิปกระจัดกระจาย" ออกจาก "วิดีโอที่เป็นซีนจริง"

### ⭐ กฎทอง: จะบอกมุมกล้องในแต่ละบีตหรือไม่ (สำหรับ timeline)
**บอก "ลำดับ + แอ็กชัน" เสมอ — แต่ "มุมกล้อง" ไม่บอกก็ได้** เพราะ timeline ล็อกลำดับไว้แล้ว ปล่อยมุมให้โมเดลเลือก มันจะจับคู่มุมกับแอ็กชันเองและมัก**ออกมาเป็นธรรมชาติกว่า**สั่งเอง (จะไม่มั่ว เพราะปล่อยแค่มุม ไม่ได้ปล่อยลำดับ)

- ✅ **ปล่อยมุม** = ภาพมีชีวิต/เป็นธรรมชาติ, prompt สั้นลง
- ⚠️ ข้อแลก = สุ่มขึ้นนิด + คุมบีตเป๊ะไม่ได้
- 🔒 **ข้อยกเว้น: ล็อกมุมเฉพาะบีตที่ "ความหมาย/มุกพึ่งมุมนั้น"** เช่น `CUT to` ตอนเฉลยมุก, `push-in` ตอนเน้นอารมณ์, `holds a still beat` ตอนทิ้งจังหวะ — นอกนั้นปล่อยได้หมด

**สูตรจำง่าย:** ลำดับ+แอ็กชัน = บอกเสมอ · มุมกล้อง = ปล่อย ยกเว้นบีตสำคัญ

## ⭐ Under-direct อารมณ์/ท่าทาง (อย่าสั่งรีแอคแรงๆ)

**ยิ่งเขียนคำอารมณ์ตรงๆ โมเดลยิ่ง overact** — `panicked`, `wide eyes`, `fed-up face`, `exhales a long sigh` → ออกมาเว่อร์เหมือนละครเกินจริง ไม่เป็นธรรมชาติ (เป็น "AI tell" เวอร์ชันการแสดง หลักเดียวกับ over-direct มุมกล้อง)

**วิธีที่ถูก:**
- **บรรยายสถานการณ์/แอ็กชันกลางๆ** แล้วปล่อยให้รีแอคเกิดเอง → `she wakes, glances at her phone, gets out of bed` (ไม่ใช่ `she jolts awake panicked with wide eyes`)
- **เพิ่มบรรทัดคุมการแสดง:** `Underplayed, restrained, natural performance; minimal facial expression; no exaggerated reactions.`
- ปล่อยให้บริบท/จังหวะนิ่งเล่าอารมณ์เอง → `stands still for a long beat` ดีกว่า `makes a fed-up face and sighs`

### ⚠️⚠️ สำคัญ: under-direct ≠ "หน้านิ่งตลอดเรื่อง"
เคยเข้าใจผิดว่า "ลดอารมณ์" = สั่งให้หน้าเฉยทั้งเรื่อง → ผลออกมา **อืด ไม่มีชีวิต** (เจอกับ [[tuensai-project]] มาแล้ว)

**ความหมายที่ถูก:**
- **ระหว่างแอ็กชัน = ต้องมีอารมณ์จริง** — ตื่นก็ตกใจ, รีบก็รีบ, วิ่งมาก็เหนื่อยหอบ · แค่ให้ "จริง ไม่เว่อร์การ์ตูน" (`natural, genuine reactions — startled, flustered, out of breath — real but never exaggerated`)
- **deadpan = สงวนไว้ที่ punchline (ตอนจบ) เท่านั้น** — พีคของมุกคือ "ทุ่มสุดตัวมีอารมณ์เต็ม → แล้วมา flat ตอนรู้ความจริง" (`her face goes still and blank, a long held beat, then a small sigh`)

**สูตร deadpan comedy ที่ถูก:** อารมณ์จริงตลอดแอ็กชัน → **หน้านิ่ง + ทิ้งเฟรม + ถอนหายใจ เฉพาะตอนเฉลย** (ความตัดกันคือมุก ไม่ใช่หน้าเฉยตั้งแต่ต้น)

**กฎรวมเรื่อง "สั่งมาก vs สั่งน้อย":**
| องค์ประกอบ | ควร |
|---|---|
| ลำดับ + แอ็กชัน | **over-direct** (บอกชัด) |
| มุมกล้อง | ปล่อย ยกเว้นบีตสำคัญ |
| **อารมณ์/ท่าทาง** | **under-direct** = "จริง ไม่เว่อร์" (ไม่ใช่หน้าเฉย) · deadpan เก็บไว้ที่ punchline |

## Pitfall checklist

- ❌ ซ้อน camera move ที่ขัดกัน
- ❌ ใช้ "fast" ลอยๆ → jitter
- ❌ fast camera + fast subject + complex scene พร้อมกัน
- ❌ adjective ฟุ่มเฟือย ("amazing", "beautiful")
- ❌ technical jargon (fps, ISO, focal length) ใน rhythm
- ❌ มองว่าเป็นโมเดล text อย่างเดียว — ยัดทุกอย่างลงพารากราฟเดียว (มัน multimodal)
- ❌ ลืมเขียนเสียง (audio) ทั้งที่โมเดลรองรับ — เขียนตั้งใจ อย่าปล่อยให้เดา
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

## 📐 Resolution 480/720/1080/4K — ทำให้โมเดล "ฉลาด" ขึ้นไหม? (deep-research 13 ก.ค. 2026, verify 3-vote)
> **สรุป: ไม่ทำให้ฉลาดขึ้น แต่ก็ไม่ใช่แค่ "pixel เยอะขึ้น"** — res = fidelity/cost lever ไม่ใช่ intelligence lever

**สถาปัตยกรรม = cascade** (Seedance 1.0 tech report, [arXiv 2506.09113](https://arxiv.org/abs/2506.09113), primary):
> base DiT เจน **480p ก่อน** → 720p/1080p มาจาก **learned diffusion refiner แยกตัว** (init จาก base model, conditioned บน LR video ที่ upsample แล้ว + concat noise, มี RLHF ของตัวเอง) หน้าที่ = *"enhance visual details and textures"*
- → **composition / motion / semantics ตัดสินที่ base res แล้ว res สูงรับช่วงมาเติมดีเทล** = ความฉลาดไม่เพิ่ม

**Seedance 2.0** ([arXiv 2604.14148](https://arxiv.org/pdf/2604.14148)): **native output = 480p + 720p เท่านั้น** — **1080p/4K ไม่ใช่ native tier ที่มีเอกสาร** · เคลม "4K native ไม่ใช่ upscale" = **vendor marketing** (ถูก refute)
- ByteDance เองบอก res ≠ quality: **720p ติด #1 Elo ทั้ง T2V/I2V** (1450/1449) ชนะคู่แข่ง 1080p — *"motion dynamics and visual coherence are more perceptually significant than resolution alone"*

**prompt adherence / physics / มือ / identity ต่างกันตาม res ไหม → UNKNOWN** — tech report **ไม่มี resolution ablation เลย** (ทุก metric แยกตาม model ไม่ใช่ตาม res). ไม่ใช่ "พิสูจน์แล้วว่าเท่ากัน"

**BytePlus API** ([docs](https://docs.byteplus.com/en/docs/ModelArk/1520757)): res = enum บน endpoint เดียว **gate ตาม model variant** — `4k` เฉพาะ Seedance 2.0 เต็ม · `1080p` ไม่รองรับบน **Fast/Mini** · default = 720p · `4k` = 10-bit + H.265
- ⚠️ **`480p` ผูกกับ "draft" inference mode ที่ feature ลดลง** — ไม่ใช่แค่ภาพเล็กลง

### ⚠️⚠️ ที่กระทบ workflow เราตรงๆ: **Seedance 2.0 ไม่มี seed**
- → **ล็อก take ดีจาก low-res แล้ว re-roll ที่ high-res ให้เหมือนเดิม = ทำไม่ได้** (re-roll = คนละคลิป)
- คำแนะนำ "iterate ถูกๆ ที่ res ต่ำ แล้ว final ค่อย res สูง" (ByteDance/fal/Higgsfield พูดเอง) **ใช้กับ 2.0 ไม่ได้จริง**
- ✅ **กฎเรา: เจน 4-6 รอบเลือกอันเนียน = ต้องเจนที่ res สุดท้ายเลย** · iterate ถูกๆ ได้แค่ระดับ **prompt/direction** (ดูว่าทางถูกไหม) พอ direction นิ่ง → เจนจริงที่ res สูงหลายรอบ
- **อย่าใช้ 480p ตัดสิน motion/quality** (draft mode) → ใช้ **720p** เป็น baseline ประเมิน

## ⭐ Marco freestyle method — set the RULES not the SHOTS
> ต้นฉบับเต็ม + template = [[seedance-marco-freestyle-method]] ([@MarcoBorinEdit](https://x.com/MarcoBorinEdit/status/2068075513206174081))
- **prompt ละเอียด shot-by-shot + สั่งมูฟกล้องทุกช็อต = "the AI tell"** (ช้า ฝันๆ แข็ง) — ยืนยันจากการลองจริงของ Marco
- ถอดเหลือแค่ **กฎ** (FORMAT / REFERENCE ROLES / CAMERA / AMBIENCE / SOUND / SHOTS 1-2 บรรทัด) → มีชีวิตทันที
- **`Rare camera angles.` + ปล่อยให้มันเลือก** = ปลดล็อกมุมที่เราไม่มีวันเขียนเอง (over-under ผิวน้ำ / ground-level / macro)
- **CAMERA = อุปกรณ์/เท็กซ์เจอร์** (`iPhone 14 Pro, imperfections are present`) ไม่ใช่มูฟกล้อง
- ❌ ไม่ใช้กับบีตที่ต้องล็อกเป๊ะ (first+last frame, จุดจิ้มที่ AE ต้อง track, punchline reveal)

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
- [MindStudio — Timeline Prompting for Cinematic AI Video](https://www.mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video)
- [seedance2.ai — Prompt Guide](https://seedance2.ai/guide)
- [Media.io — Best Copy-Paste Guide](https://www.media.io/ai/image-to-video/seedance-2-0-prompts)
- [redreamality.com — Complete Prompt Engineering Playbook](https://redreamality.com/blog/seedance-2-guide/)
- [seedance2.so — prompt engineering guide](https://seedance2.so/blog/ai-video-prompt-engineering-guide)
