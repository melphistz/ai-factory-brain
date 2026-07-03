---
name: seedance-prompt-repository
description: "Real Seedance 2.0 prompt examples and reusable style stacks, paired with seedance-knowledge theory"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Seedance 2.0 — Prompt Repository (คลังตัวอย่าง)

> รวบรวมจาก gallery ของ [YouMind — Seedance 2.0 Prompts Explore](https://youmind.com/seedance-2-0-prompts/explore) (เก็บ มิ.ย. 2026)
> ใช้คู่กับ [[seedance-knowledge]] (ทฤษฎี/สูตร) — ไฟล์นี้คือ "ตัวอย่างจริง"

## ⚠️ หมายเหตุสำคัญก่อนใช้
- เว็บต้นทางเป็น **gallery ไดนามิก** prompt เต็มที่ยาว ๆ ถูกตัดท้ายด้วย "..." → ที่เก็บได้ส่วนใหญ่เป็น **ส่วนเปิด (opening) + คีย์เวิร์ด + เทคนิค** ไม่ใช่ข้อความเต็มทุกคำ
- ต้องการ prompt เต็ม + ดูวิดีโอผลลัพธ์: เปิดที่เว็บต้นทางโดยตรง (มี ~3,969 ตัวอย่าง พร้อมพรีวิว)
- เว็บเป็นของบริษัท YouMind ไม่ใช่ทางการ ByteDance — ใช้เป็นแรงบันดาลใจ/แพตเทิร์นได้ แต่ตัวเลขข้อจำกัดยึดของทางการ

---

## 🎬 Cinematic Scene / Short Film

**1. Japanese Classroom Romance** *(หนังรักดราม่าญี่ปุ่น)*
> "15-second cinematic Japanese drama pure love ambiguous short film, ultra-realistic quality, warm golden sunlight in an empty classroom..."
- คีย์เวิร์ด: ultra-realistic, warm golden sunlight, fine dust motes, afternoon light through blinds
- เทคนิค: แสงบรรยากาศ + ฝุ่นละอองลอยในแสง (atmospheric lighting)

**2. Cinematic Street Racing** *(ซิ่งกลางคืน)*
> "cinematic street racing sequence at night, a focused driver inside a high-performance car grips the steering wheel..."
- คีย์เวิร์ด: intense eye focus, city lights reflecting on windshield
- เทคนิค: หลายมุมกล้องสร้างความตึงเครียด (multi-angle, tension building)

**3. Haute Couture Fantasy** *(แฟชั่นแฟนตาซี)*
> "Hollywood Haute Couture Fantasy blockbuster, 8K ultra-clear, Photorealistic, High-fashion Editorial Style, Unreal Engine 5..."
- เทคนิค: เรนเดอร์โฟโตเรียลลิสติก + เอฟเฟกต์ภาพลวงตา

---

## 📺 Brand / Product Commercial

**4. Modern Rural Healing** *(โฆษณาแนวฮีลใจ)*
> "Modern Rural Aesthetics, Cinematic Commercial quality, shot with Sony A7S3/cinema camera, 4K/8K ultra-clear, Extreme Macro..."
- คีย์เวิร์ด: extreme macro, natural transparent lighting, healing ASMR
- เทคนิค: มาโครคมชัด + อารมณ์ ASMR (ระบุชื่อกล้องจริงเพื่อคุมลุค)

---

## 🎵 Music Video

**5. Street Rap MV** *(แร็ปข้างถนน)*
> "16:9 horizontal screen, street rap MV style, neon purple and blue cool tones, explosive cool and fierce atmosphere..."
- คีย์เวิร์ด: neon purple/blue cool tones, explosive fierce atmosphere
- เทคนิค: คุมโทนสี (color grading) + บรรยากาศเข้มข้น
- หมายเหตุ: เริ่มด้วยการระบุอัตราส่วน (16:9) ชัดเจน

---

## ✨ VFX / Transformation / Fantasy

**6. Sand Woman → Dragon**
> "ethereal woman made of swirling black and white sand particles, wearing a flowing hooded cloak adorned with vibrant gems..."
- เทคนิค: particle effects + กล้องโคจรรอบ (orbital camera)

**7. Elemental Alien Orbs**
> "five (5) floating alien glass orbs slightly connected to one another, each orb has motion and is animated inside..."
- เทคนิค: physics simulation + พื้นผิวชีวภาพ
- หมายเหตุ: **ระบุจำนวนเป็นตัวเลข "five (5)"** เพื่อความแม่นยำ

**8. Giant Dragon City Destruction**
> "A gigantic winged serpent with metallic black scales, glowing blue lightning veins, cathedral-sized wings..."
- เทคนิค: หลายซับเจกต์โต้ตอบกัน + ฟิสิกส์การทำลายล้าง

---

## ⏱️ Timeline Prompts (เล่าเป็นช่วงเวลา) — เทคนิคขั้นสูง

**9. Frozen Coffee Toss** *(กาแฟลอยกลางอากาศ)*
> "0–3s: Someone throws coffee in the air..."
- โครงสร้าง: แบ่งช่วงเวลาเป็นวินาที สั่งแอ็กชันทีละช็อต
- เทคนิค: physics / fluid dynamics

**10. Giant Dragon (timeline version)**
> "0–4s: bursts out of dark storm clouds above a coastal city, diving..."
- โครงสร้าง: ใช้ timestamp คุมจังหวะหนัง (cinematic pacing)

**11. Elemental Tsunami Transformation**
> "15-second ultra-cinematic elemental transformation sequence on a storm-battered coastline at twilight..."
- เทคนิค: ฟิสิกส์สภาพแวดล้อมแบบไดนามิก

---

## 🎨 Reusable Style Stacks (หยิบไปวางในช่อง Style ได้เลย)

### Realistic Cinematic Look (ลุคหนัง realistic ระดับสูง — เหมาะแฟชั่น/สวิมแวร์/MV)
> "Ultra-realistic cinematic look, ARRI Alexa LF large-format texture, 50mm lens, shallow depth of field, soft volumetric window light, muted warm-green palette, high dynamic range, natural skin detail, realistic fabric fibers, hair strands catching rim light, subtle film grain."

**คำไหนคุมได้จริง vs คำไหนแค่ vibe:**
- ✅ *คุมได้จริง:* ARRI Alexa LF texture, soft volumetric window light, muted warm-green palette, natural skin detail, realistic fabric fibers, hair rim light, subtle film grain (พวกนี้ดันลุคได้ตรง + สู้ "ผิวพลาสติก/เนียนเกิน" ของ AI)
- ⚠️ *แค่ vibe ไม่ทำตามเป๊ะ:* การสลับรูรับแสงรายช็อต ("f/1.4 close-up / f/4 room") และระบุหลายเลนส์พร้อมกัน — โมเดลอ่านรวมเป็น "DOF ตื้น cinematic" เท่านั้น
- 🔁 *ตัดทิ้งได้ (ซ้ำซ้อน):* "shallow depth of field" ซ้ำ f/1.4 · "no cartoon/no game" ซ้ำ ultra-realistic (และ Seedance ไม่รองรับ negative prompt แบบดั้งเดิม) · "IMAX + Alexa LF" ผสม format กับ camera เลือกอันเดียวพอ
- ⚠️ *ทิศของ stack นี้ = slick สุดทาง* ตรงข้ามกับลุค "iPhone imperfections" → เสี่ยง dreamy/AI tell ถ้า motion ไม่มีชีวิต โชคดีที่ grain + skin/fabric detail ช่วยถ่วงไว้

### Anti-AI / Authentic Look (ลุคจริง ไม่เนียน — สู้ AI tell)
> "Shot on iPhone 14 Pro, imperfections present, natural available light, handheld, environment sound only."

**หลักการ:** ตรึง non-negotiables (identity/ชุด) ด้วย reference image → ปล่อยช็อตให้ฟรีสไตล์ → ลุคไม่เนียนช่วยให้ "มีชีวิต" (ดูหลัก Control vs Freestyle ใน [[seedance-knowledge]])

---

## 📌 แพตเทิร์นที่สรุปได้จากตัวอย่างทั้งหมด
(เอาไปใช้เป็นเช็กลิสต์เวลาเขียน prompt เอง — เสริมสูตรใน [[seedance-knowledge]])

1. **นำด้วยประเภท + ความยาว + คุณภาพ** เช่น "15-second cinematic… ultra-realistic quality / 8K"
2. **ระบุอัตราส่วนจอ** ตั้งแต่ต้น (16:9, 9:16)
3. **อ้างอิงกล้อง/เอนจินจริง** เพื่อล็อกลุค (Sony A7S3, Unreal Engine 5, cinema camera)
4. **ใส่ตัวเลขให้ชัด** เมื่อมีหลายวัตถุ — "five (5) orbs"
5. **คุมโทนสีเป็นคำเฉพาะ** — "neon purple and blue cool tones" ดีกว่า "สวย"
6. **Timeline prompting** ใช้ "0–3s / 0–4s" แบ่งช็อตเมื่อเป็นซีนหลายจังหวะ
7. **จุดแข็งของ Seedance ที่เว็บเน้น:** temporal coherence, physics simulation, multi-subject interaction → prompt ที่เล่นกับ fluid/particle/destruction มักได้ผลดี

---

## 🆕 เพิ่มจากรอบ explore (มิ.ย. 2026) — ของใหม่ที่ยังไม่มีข้างบน

**12. FPV Camera Path Guide** *(คุมเส้นทางกล้องด้วยภาพ)* ⭐ เทคนิคใหม่
> "Use the scene with the red path overlay as exact FPV..."
- เทคนิค: วาด **red path overlay** บนภาพ reference → โมเดลบินกล้องตามเส้นเป๊ะ (motion control แบบ visual ไม่ต้องบรรยายมุมกล้องเป็นคำ)
- ใช้เมื่อ: ต้องการ FPV / drone path เฉพาะ คุมยากด้วยคำ

**13. Wildlife Documentary — Snow Leopard Ambush** *(สารคดีสัตว์)*
> "National Geographic Wildlife Documentary, IMAX film quality..."
- stack ใหม่: **National Geographic + IMAX film quality + slow-motion** (ล็อกลุคสารคดี)
- เทคนิค: slow-motion จังหวะล่า + nature realism

**14. Sci-Fi Fighter Ring World** *(แอ็กชัน sci-fi สั้น)*
> "10-second cinematic sci-fi action sequence..."
- คีย์เวิร์ด: IMAX, physics-based
- หมายเหตุ: นำด้วยความยาว "10-second" ชัดเจน

**15. Cinematic Sci-Fi Orbital Megastructure**
> "Create a cinematic sci-fi film sequence in vast abandoned..."
- คีย์เวิร์ด: space, megastructure, scale มหึมา

**16. Fungal Bloom Bunker Invasion** *(sci-fi horror)*
> "Military underground bunker attacked by alien fungal organism..."
- เทคนิค: transformation + invasion + สิ่งมีชีวิตเติบโต (organic growth)

**17. Water Thunder Breathing Duel** *(อนิเมะ live-action)*
> "Live-Action Anime Adaptation · Breathing Technique Decisive Battle..."
- keyword genre ใหม่: **Live-Action Anime Adaptation** + special effects duel
- คู่กับ: "Cinematic Anime Story Sequence" (High-end cinematic anime) สำหรับลุค anime

---

## 🗂️ Category taxonomy (9 หมวดของ gallery — ใช้เป็น index หาแนว)
Cinematic Scene Showcase · Vlog/Social Lifestyle · Short Film · Music Video · Brand/Product Commercial · UGC/Talking Head Ad · Explainer/Tutorial · Channel Intro/Brand Asset · Game Cinematic/PV

> หมวดที่ยังไม่มีตัวอย่างเก็บ: **UGC/Talking Head Ad**, **Explainer/Tutorial**, **Channel Intro/Brand Asset** → ถ้าทำแนวพวกนี้ ต้องไป explore เพิ่ม

---

## 🔤 ข้อความ/label บนสินค้าให้ "อ่านออก" (โจทย์ยากของ AI video)
**สูตร:** `ข้อความเป๊ะ + โผล่ตอนไหน + ตรงไหน + หน้าตายังไง`
- title card/slogan: สั้น **2–4 คำ** → `At the end, the text "Pure Sound" appears center, clean white sans-serif, subtle fade-in`
- product label: บรรยายของ+ข้อความคู่กัน → `The bottle label clearly reads "LUMA" in simple black uppercase letters` + orbital camera
- **กฎให้อ่านออก:** เลี่ยงสัญลักษณ์แปลก/ตัวเลขยาว/หลายภาษาปนประโยคเดียว · typeface เรียบ · **วางข้อความใกล้กล้อง** · ลด motion ตอนต้องการความเป๊ะ · **เจนคลิปสั้นเทสก่อน** ค่อยเผา credit ยาว
- ⚠️ text render ใน Seedance ไม่นิ่ง (community เตือน) — งานสำคัญ (โลโก้/สโลแกน) แปะใน CapCut/edit ดีกว่า (= เหตุผลที่ [[valenshield-nurse-ad-project]] ทำโลโก้ใน CapCut ถูกแล้ว)

## 🎥 14 Camera techniques (มุมกล้องสวย — paste ชื่อ + ตัวอย่าง)
**พื้นฐาน:** Follow+Orbit (ตาม+โคจร, character reveal) · Rise+Tilt+Pan (เผย scale ใหญ่) · God's Eye/Overhead (top-down, crowd/pattern) · POV (มุมตัวละคร immersion) · LowAngleShot (มองขึ้น, ทำให้ดูยิ่งใหญ่/มีพลัง) · MacroShot (โคลสสุด, น้ำ/กลีบดอก)
**ขั้นสูง:** DollyZoom (เลื่อนเข้า+ซูมออกสวนกัน, ความรู้สึกหวั่น) · MatchCut (เชื่อม 2 ช็อตด้วยรูปทรง/มูฟเหมือนกัน) · SlowMotion (เผยรายละเอียดที่ตาไม่ทัน) · DutchAngle (เอียงกล้อง, ความไม่มั่นคง/อันตราย)
**คอมโพสิชัน:** Framing (frame in frame ผ่านหน้าต่าง/ประตู) · UltraWideAngle (กว้างสุด, space กว้างใหญ่/surreal) · TimeLapse (เวลาผ่าน) · Dolly (เลื่อนรางเข้า/ออก นุ่มนวล)
- เด็ด: LowAngle + backlit silhouette = HERO shot (ตรงแนว Valenshield) · Macro + translucent + refracting light = product สวย

## 📦 Product video structure (ecommerce ที่ขายได้)
`Hook (0–3s): มูฟแรงอันเดียว reveal สะอาด ไม่มี text · Proof (3–10s): โชว์ benefit/detail อันเดียว ไม่ใช่ทุกอย่าง · CTA (last 2–3s): สั้น อ่านออกบนมือถือ`
- product fail เพราะ: ของไม่ชัด / กล้องขยับเยอะ / ขอเป็น brand film แทน sales asset

## 🗣️ UGC templates เด็ด (dialogue เต็ม)
**Talking-head hook:** `Mid-twenties woman, shoulder-length brown hair, no makeup, cream crewneck, softly lit kitchen at golden hour. Phone front camera selfie framing, slight handheld micro-movement. She looks slightly off-camera then at the lens: "Okay I have to tell you about this — I genuinely cannot believe how well this worked."`
**Product-in-hand (reaction):** interrupted cadence แบบ TikTok → `"Wait — wait. I have to actually show you this."` + sitting on edge of bed, morning light, holding [PRODUCT], raised eyebrows, arm's length selfie
**Unboxing:** `sitting at sunlit white desk, small kraft-paper box, slides a finger under the seal, pulls it open, lifts out [PRODUCT], turns it slowly, laughs once` → single laugh = micro-expression จริง · `"Okay this is way nicer than I thought it would be."`

**⭐ Universal realism keywords (UGC):**
- `Ambient room tone, no music` (กัน stock music)
- **`Exactly two arms, five fingers per hand`** ← **ตัด hand artifact ~70%** (ตรงปัญหามือ Valenshield Clip 2/3 — [[valenshield-nurse-ad-project]])
- `Single-take recording, no cuts` (ต่อเนื่อง)

## แหล่งที่มา
- [YouMind — Seedance 2.0 Prompts Explore](https://youmind.com/seedance-2-0-prompts/explore) (gallery ~4,039 ตัวอย่าง + วิดีโอพรีวิว, อัปเดต มิ.ย. 2026)
- [seedancegen.com — text/title cards in video](https://seedancegen.com/blog/how-to-use-seedance-2)
- [jxp.com — 14 cinematic camera techniques](https://www.jxp.com/seedance/blog/seedance-2-0-camera-language-guide)
- [ugccopilot.ai — 14 UGC templates](https://ugccopilot.ai/blog/seedance-2-prompting-guide-templates/)
- [wavespeed.ai — product photo → ad video](https://wavespeed.ai/blog/posts/blog-product-photo-to-ad-video-seedance-2-0/)
