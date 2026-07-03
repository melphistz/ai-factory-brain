---
name: valenshield-nurse-ad-project
description: "Active project — Valenshield lavender nurse-uniform video ad, 5 clips, Seedance 2.0 pipeline"
metadata: 
  node_type: memory
  type: project
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# โปรเจกต์: โฆษณาวิดีโอชุดพยาบาล Valenshield (Seedance 2.0)

> ไฟล์ส่งต่อให้ Claude CLI ใช้ทำงานต่อ — รวมบรีฟ + ไปป์ไลน์ + กฎที่ได้จากการลองจริง + prompt ทั้ง 5 คลิป
> ใช้คู่กับ [[seedance-knowledge]] · [[seedance-prompt-repository]] · [[director-styles-knowledge]] · [[mv-directors-knowledge]]
> ⚠️ นี่คือ **แคมเปญ 1** (ลาเวนเดอร์ HERO มีนางแบบ). แคมเปญ 2 (no-person WHITE macro ASMR, 4 คลิป) แยกอยู่ที่ [[valenshield-macro-asmr-ad]] — อย่าปนสี/โทน
> source ต้นฉบับ: `/Users/working/Downloads/valenshield-nurse-ad-project.md` · อัปเดต: มิ.ย. 2026

## วิธีใช้ไฟล์นี้ (สำหรับ agent)
1. อ่านทั้งไฟล์ก่อนเริ่ม โดยเฉพาะหัวข้อ "กฎ& บทเรียน" — มันคือสิ่งที่ลองผิดลองถูกมาแล้ว
2. prompt ทุกอันในไฟล์เป็น **ภาษาอังกฤษ พร้อมก๊อปวาง** (อย่าแปลเป็นไทยตอนใช้งานจริง)
3. ลำดับงานต่อคลิป: เจน "รูปเปิด" ใน ChatGPT ก่อน → ออดิตรูป (หน้า/ชุด/สีตรงไหม) → เอารูปเป็น first frame ใน Seedance → เจน 4-6 รอบ → เลือกอันเนียน
4. ตัดสินคลิปที่ "การเคลื่อนไหว" ไม่ใช่เฟรมนิ่ง
5. ความเร็ว/บีต/โลโก้ ทำใน CapCut ไม่ใช่ Seedance

---

## 1. ภาพรวมโปรเจกต์
- **แบรนด์:** Valenshield (โลโก้ = ดอกแก้ว + ชื่อแบรนด์ + สโลแกน)
- **สินค้า:** ชุดพยาบาล/เครื่องแบบทางการแพทย์ที่มีฟังก์ชัน — **กันน้ำ/น้ำไม่ซึม, เอวยางยืด, ผ้ายืดเคลื่อนไหวคล่อง, เป้าแข็งแรง**
- **แนวงาน:** Editorial fashion ad แนว HERO เท่ๆ ฉากดำ ไฟดราม่า · pacing เร็ว ตัดกระชับ · เล่าด้วยภาพ+บีตเพลง ไม่มี voiceover
- **ฟอร์แมต:** 9:16 แนวตั้ง · รวม ~20 วินาที · จบด้วยโลโก้+สโลแกน (hard cut)
- **โครงสร้าง:** 5 คลิปแยก เจนทีละคลิป แล้วตัดรวมใน CapCut

## 2. การตัดสินใจที่ล็อกแล้ว (อย่าเปลี่ยนเอง)
- **สีชุด = ลาเวนเดอร์อ่อน/periwinkle (soft lavender) = สีจริงของสินค้า** (ยืนยันจาก approved sheet `Outfit01-1.jpg`) — *ไม่ใช่ขาว* · รองเท้าผ้าใบ = ขาว
  - ⭐ **ไม่ต้อง recolor** — เดิมเข้าใจผิดว่าต้นฉบับขาวต้อง recolor; จริงๆ สินค้าเป็นลาเวนเดอร์อยู่แล้ว ใช้ sheet ตรงๆ
  - ทั้ง 5 คลิปต้องเป็นลาเวนเดอร์ "เฉดเดียวกัน" ไม่งั้นตัดต่อแล้วสีเพี้ยนกลางเรื่อง
- 9:16 แนวตั้ง · ฉากพื้นดำเงาสะท้อน + ฉากหลังดำ + ไฟ key ดราม่าดวงเดียว
- เสียง: ambient/SFX + บีต (ใส่บีตจริงตอน edit) ไม่มีเสียงพูด

## 3. ตัวละคร & Reference Assets
- **นางแบบ:** หญิงฝรั่ง ~ปลาย 20s ผมบ๊อบสั้นสีน้ำตาลเข้มเป็นลอน (ยาวคาง) คิ้วเข้มคม สลิม — คนเดิมทุกคลิป
- ✅ **APPROVED reference sheet (ล็อกแล้ว):** `/Volumes/WONYOUNG/Dokkeaw/Outfit01-1.jpg` — 4 มุม (¾ซ้าย/หน้า/หลัง/¾ขวา), **ชุดลาเวนเดอร์อ่อน approved โดยตรง** (tunic notch-lapel แขนสั้น, กระดุมกลมเงิน 4, กระเป๋าปะสะโพก 2, กางเกงขาตรง, sneakers ขาว), bg เทาอุ่นอ่อน. = `@Image1` identity+wardrobe lock
- ⭐ **ไม่มีขั้น recolor:** ลาเวนเดอร์ = สีจริงของสินค้า (ยืนยัน "ในภาพคือสีจริง") ใช้ไฟล์นี้ตรงๆ (ยังต้องคุมเฉดให้ตรงข้ามคลิป)
- **`@Image2` (ออปชัน):** ถ้ามีรูปถ่ายผ้าจริง/ขอบเอวจริงของ Valenshield ใส่เพิ่มเพื่อให้เนื้อผ้า+จีบเอว render ตรงของจริง
- **ลิมิต reference ของ Seedance:** รูป ≤9 + วิดีโอ ≤3 + เสียง ≤3 (รวม ≤12)

## 4. ไปป์ไลน์ (Workflow)
```
ChatGPT (เจนรูปเปิดแต่ละคลิป + recolor ม่วง + ล็อกหน้า/ชุด)
   → ออดิตรูปนิ่ง (หน้าตรง? ชุดตรง? สีตรง? คอมโพสิชันสวย?)
   → Seedance 2.0 Fast: image-to-video, รูป = first frame, 8s max, unlimited
   → เจน 4-6 รอบ/คลิป เลือกอันเนียน (ตัดสินที่ "ตอนภาพเคลื่อน")
   → CapCut: เร่งจังหวะ + speed ramp + บีต + hard cut + แปะโลโก้/สโลแกน
```
**Seedance Fast ที่ใช้อยู่:** 8 วินาที/รอบ · ใส่รูปเป็น first frame ได้ (image-to-video) · เจนไม่จำกัดรอบ

**ทำใน CapCut เท่านั้น (Seedance ทำไม่ได้):**
- จังหวะเร็ว/ตัดกระชับ
- speed ramp (เข้าเร็ว → สโลว์โม) — ใช้ smooth slow motion ของ CapCut (frame interpolation) ช่วงช้าไม่ให้กระตุก
- ใส่บีตเพลง + ซิงค์จังหวะ
- โลโก้ + สโลแกน (AI วิดีโอเจนตัวอักษร/โลโก้เพี้ยน — ห้ามให้ Seedance ทำ)

## 5. กฎ & บทเรียน (สำคัญสุด — มาจากการลองจริง)
- **8 วิ/รอบ** → 20 วิ = 5 คลิปแยก ห้ามหวังเจนยาวรวดเดียว
- **1 prompt = 1 คลิป** อย่าวาง prompt 2 คลิปรวมกัน — Seedance จะยำเป็นคลิปเดียวแล้ว morph กลางคลิป (เคยเจอ: คลิปเท้า → จู่ๆ กลายเป็นมาโครผ้า)
- **image-to-video: prompt สั่ง "การเคลื่อนไหว" เท่านั้น** รูปกำหนดฉาก/หน้า/สีให้แล้ว อย่าบรรยายฉากซ้ำ และ **อย่าสั่งขัดกับเฟรม** (เช่นเฟรมน้ำกระเด็นเต็มแล้ว อย่าสั่ง "เหยียบลงไป")
- **คำว่า "fast" = ภาพรวน** ห้ามใช้ ใช้ "slow-to-medium" หรือสูตรแรงปะทะ: **"whips/snaps/bursts then settles into slow motion"**
- **physics ที่มีจังหวะในตัว (น้ำกระเด็น, ผ้าสะบัด) = ดูไดนามิกโดยไม่ต้องสั่ง fast** ใช้ "ปะทะ→พุ่ง→ตก" แทน (เหตุผลที่คลิปแรกดูมีชีวิต)
- **มือ = จุดพังอันดับ 1** (นิ้วเกิน/บิด/ลอย/มือที่สองโผล่/ทาบเฉยไม่ทำอะไร) โดยเฉพาะในมาโครที่มือใหญ่เต็มเฟรม
  - วิธีลดเสี่ยง: ให้มือเข้ามาตอนภาพ "ช้า" แล้ว · ขยับน้อยสุด ("pulls a few cm, releases") · เจนมือให้ครบสวยใน "รูปนิ่ง" ก่อน · อัด negative เต็ม · หรือ **เลิกใช้มือไปเลย** (โชว์ฟังก์ชันด้วยการเคลื่อนไหวแทน)
- **ท่ากระโดด/ฉีกขากลางอากาศ = แขนขาวาร์ปง่าย** → ล็อกท่าสวยใน "รูปนิ่ง" ก่อน ให้วิดีโอทำแค่ "ลอยค้าง→ตก→ลง" เช็กตอนลงพื้น (ขาทะลุพื้น/เข่าบิด) และปลายเท้า
- **ห้ามซูม/เปลี่ยนระยะช็อตในคลิปเดียว** → ทำให้หน้า/ตัว morph ให้ซูม/ครอปใน edit หรือแยกเป็นอีกช็อตแล้วตัด
- **สีเพี้ยน:** ChatGPT ดันขาว→ม่วง/ฟ้า ใต้ไฟดราม่า → ล็อกเฉดม่วง เจนรูป "ตั้งสี" ก่อน 1 ใบ แล้วรูปต่อไปสั่ง "match the exact lavender tone from the previous image"
- **negative ติดทุก prompt:** avoid warped hands/limbs, extra fingers, identity drift, melting/morphing fabric, water blobs, jitter, smearing
- **เจนรูปก่อน animate เสมอ** — รูปนิ่งถูก/เร็ว/แก้ง่ายกว่าวิดีโอ ออดิตที่ชั้นรูปให้ผ่านก่อนค่อยเผารอบเจนวิดีโอ
- **ตัดสินที่ motion ไม่ใช่ stills** — หยุดเฟรมดูมือ/ขา/ผ้า (บางทีดูเร็วๆ โอเค พอหยุดเฟรมเห็นเพี้ยน)

## 6. บล็อกใช้ซ้ำ (paste-ready)

**ChatGPT lead-in** (วางก่อนสั่งเจนรูปแต่ละใบ + แนบ reference sheet 4 มุม):
```
Use the woman and her uniform from the attached reference image — same face, same short dark wavy bob, same outfit design (short-sleeve notch-lapel tunic with front buttons and hip patch pockets, straight-leg trousers, white sneakers). Keep her identical.
IMPORTANT: recolor her entire uniform (tunic + trousers) to a soft light lavender — same design, lavender instead of white. Sneakers stay white. Keep the lavender tone consistent and identical across all images. Pure soft lavender — not blue, not lilac-grey, not purple.
Photorealistic editorial fashion advertising still, vertical 9:16. Set: glossy black reflective floor, seamless black backdrop, single hard dramatic key light, high-contrast lavender-on-black. Natural skin texture, clean undistorted garment.
```

**Seedance identity/look lock** (อ้างอิงเวลาคุมความสม่ำเสมอ / ใช้กับ text-to-video ถ้าจำเป็น — สำหรับ image-to-video ใช้ prompt ต่อคลิปด้านล่างพอ):
```
9:16 vertical, ultra-realistic editorial fashion ad for a functional lavender nurse uniform (brand Valenshield).
@Image1 = the model + her lavender uniform (short-sleeve notch-lapel tunic, front buttons, hip patch pockets, elastic pleated-waist lavender trousers, white sneakers). Keep her exact face, short dark wavy bob, garment identical and clean in every frame.
Setting: glossy black reflective floor, seamless black backdrop, single hard dramatic key light, high-contrast lavender-on-black, confident mood.
```

---

## 7. STORYBOARD 5 คลิป

### Clip 1 — HOOK: เหยียบน้ำเดินผ่าน (~4s)
- **จุดขาย:** กันน้ำ (ก้าวลุยน้ำ) · **สถานะ:** มีเวอร์ชันขาเดียวที่ดีแล้ว (น้ำสวยมาก) เก็บเป็น backup → กำลังทำเวอร์ชัน **2 ขาเดินผ่าน**
- **บทเรียน:** คลิปนี้ได้ฟีลเหยียบเร็ว-สโลว์ตอนยกเท้าเองจากฟิสิกส์น้ำ ไม่ต้องสั่ง fast

รูปเปิด (ChatGPT — เวอร์ชัน 2 ขา):
```
Same lavender uniform trousers and white sneakers, same set as before — glossy black reflective floor, seamless black backdrop, dramatic side light. Vertical 9:16, photorealistic editorial. Show BOTH lower legs from the knee down, side view, mid-stride as if walking briskly through a shallow water puddle: the front foot stepping down into the water with a splash beginning, the back leg lifted mid-stride behind. Lavender trousers, white sneakers, a few water droplets in the air. Keep the lavender tone consistent.
```
Animate (Seedance):
```
Animate in elegant slow motion: she strides forward through the shallow puddle, both feet stepping through in a natural walking rhythm, water splashing up around each sneaker, droplets arcing and falling onto the glossy black floor, ripples and mirror reflection shimmering. She keeps moving forward and walks out of frame.
Keep trousers lavender and sneakers white, fabric and shoes clean and undistorted, color unchanged.
Camera: low side tracking that follows the feet, near-locked with subtle movement — no fast or shaky motion.
Sound: deep cool bass beat + crisp water splashes and droplet ASMR with each step. No music vocals, no dialogue.
Avoid: warped or extra feet/legs, unnatural water blobs, melting or morphing, jitter, smearing.
```
- **ออดิต:** เลือกอันขาครบไม่งอก น้ำไม่เป็นก้อนเจลลี่

### Clip 2 — ผ้ากันน้ำ: น้ำเกาะแล้วปาดออกจนแห้ง (~4s)
- **จุดขาย:** น้ำไม่ซึม เช็ดออกง่าย · **สถานะ:** มือเคยออกมาเพี้ยน (มาทาบผิดทิศ) → ใช้ prompt บอกทิศแล้ว ยังไม่ยืนยันว่าผ่าน
- **first frame:** รูปมาโครผ้าม่วงมีหยดน้ำ (มีอยู่แล้ว)

Animate (Seedance — เวอร์ชันบอกทิศ):
```
Animate this still. The fabric shown is the thigh of a person's lavender trouser leg (a close macro of the leg). A hand enters from the top of the frame and sweeps downward along the length of the leg in one smooth motion, wiping the water droplets off the fabric; the beads roll away and are wiped clean, leaving the fabric completely dry and spotless — no streaks, no moisture left. Subtle slow motion.
The hand moves naturally, palm and fingers gliding flat along the fabric in the same direction as the leg, then lifts away out of frame.
Keep the fabric lavender and its weave texture exactly as in the image, color unchanged.
Camera: macro, near-locked, very slight push-in — no fast motion.
Sound: soft fabric-wipe ASMR + gentle beat. No music vocals, no dialogue.
Avoid: warped or extra fingers, distorted or floating hand, hand just resting without wiping, melting fabric, water turning into blobs, jitter, smearing.
```
- **Fallback ถ้ามือพัง:** ตัดมือออก → ให้หยดน้ำกลิ้ง/ไหลออกจากผ้าเองช้าๆ (โชว์ไม่ซึม) หรือถอยเฟรมให้เห็นว่าเป็น "ขา" ชัดขึ้น มือจะ generate ถูกทิศง่ายขึ้น

### Clip 3 — เอวยางยืด + ทรงสวย (~5s)
- **จุดขาย:** เอวยางยืด · **สถานะ:** มือพัง 2 รอบ → ตัดสินใช้สูตร **whip-twist (สะบัดแล้วสโลว์)** ไม่ซูม; มือเป็นออปชัน
- **first frame:** รูปนางแบบยืน ชายเสื้อบานเห็นขอบเอวยางยืด (มีอยู่แล้ว) — มีรูปครอปเฉพาะเอวด้วยถ้าจะทำช็อตแทรกแยก
- **บทเรียน:** หมุนเฉยๆ ดูเนือย → ใส่ "แรงสะบัด" (ผ้า/ผม) แบบเดียวกับน้ำกระเด็นคลิป 1

Animate — เวอร์ชัน A ไม่มีมือ (ปลอดภัย แนะนำก่อน):
```
Animate this still in dynamic motion. The body whips into a quick confident twist; the flared lavender tunic hem snaps and flares outward sharply from the rotation, hair swaying with the movement, then settles into graceful slow motion — the open hem revealing the elastic pleated waistband. The elastic ruching flexes naturally as the body moves. No hand reaching in.
Keep her exact face, hair, the lavender tone and fabric identical, color unchanged; garment clean and undistorted.
Camera: medium shot, one smooth move following the twist then easing into slow motion — no shaky motion, no zoom change.
Sound: cool beat + a sharp fabric whip then soft rustle. No music vocals, no dialogue.
Avoid: warped face or limbs, identity drift, melting or morphing fabric, jitter, smearing.
```
Animate — เวอร์ชัน B มีมือดึงเอว (ใช้ถ้าอยากโชว์ "ดึงแล้วเด้งกลับ" — เสี่ยงมือ เจน 5-6 รอบ):
```
Animate this still. The body whips into a quick confident twist; the flared lavender tunic hem snaps and flares outward from the rotation, hair swaying, then eases into graceful slow motion. During the slow part, one hand comes to the hip, pinches the elastic pleated waistband, gently pulls it outward a few centimeters to show the stretch, and releases so it snaps back — a small, deliberate, minimal hand motion.
Keep her exact face, hair, the lavender tone and fabric identical, color unchanged; garment clean and undistorted.
Camera: medium shot at a fixed distance, one smooth move following the twist then easing into slow motion — no zoom change, no shaky motion.
Sound: cool beat + a sharp fabric whip, then soft rustle and a soft elastic snap. No music vocals, no dialogue.
Avoid: warped or extra fingers, distorted or floating hand, hand resting without pulling, a second hand appearing, warped face, identity drift, melting fabric, waistband tearing, jitter, smearing.
```
- **ออดิต:** B เจนแล้วมือยังพังทุกอัน → ใช้ A · เช็กขอบเอวอย่า "ยืดแล้วขาด/ละลาย" · ชายเสื้ออย่าพลิ้วแบบยาง (ต้องเหมือนผ้า)

### Clip 4 — เป้าแข็งแรง/เคลื่อนไหวคล่อง: วิ่งมากระโดดฉีกขา (~5s) ★ หินสุด
- **จุดขาย:** ผ้ายืด เคลื่อนไหวคล่อง เป้าแข็งแรง · **สถานะ:** กำลังเจนรูป takeoff ยังไม่ animate
- **ท่าที่ต้องการ:** ฉีกขา **ด้านข้างแบบบัลเลต์ (grand jeté ขาหน้า-หลังเป็นเส้นตรงเดียว ปลายเท้าชี้)** ไม่ใช่ท่าฉีกขากว้างแบบ straddle
- **อยากได้ momentum "วิ่งมากระโดด" ไม่ใช่ลอยนิ่ง** → ใช้ "วิธี A: รูปจังหวะ takeoff"
- **ห้าม** เอารูป ballet จาก iStock ใช้ตรงๆ (มีลายน้ำ + คนละคน/คนละชุด) ใช้เป็น reference ท่าเท่านั้น

รูป takeoff (ChatGPT — วิธี A):
```
Use the same woman and her lavender uniform from the reference — exact face, short dark wavy bob, lavender notch-lapel tunic with front buttons, lavender trousers, white sneakers. Keep her identical.
Photorealistic editorial, vertical 9:16, glossy black reflective floor, seamless black backdrop, single dramatic key light.
Pose: caught at the explosive takeoff of a running leap, side profile, moving left-to-right — body launching forward and upward with strong horizontal momentum, front leg beginning to extend into a split, back leg still pushing off, hair and tunic hem streaming backward from the speed, arms driving. Dynamic, athletic, full of motion energy — clearly mid-launch, not floating still.
Keep the lavender tone consistent, garment clean.
```
#### 🔑 บทเรียนใหญ่จาก session (30 มิ.ย.) — Clip 4 แตกเป็น sequence หลาย beat
> วิ่ง→กระโดด→ฉีกขา→ซูมเป้า→ลง = **หลาย beat ทำคลิปเดียวไม่ได้** (morph). แยก beat ทำทีละคลิป → ตัด CapCut
> **input mode สำคัญสุด** (ดู [[seedance-knowledge]] §input mode):
> - อยากเห็น **"วิ่งมา" ก่อนโดด** → ใช้ **reference image** (model สร้าง action เอง) ไม่ใช่ first frame · prompt บรรยาย arc เต็ม `sprints → explodes into leap → split → slow-mo`
> - เริ่มที่ **apex (ลอยแล้ว)** → ตั้ง **first frame** = รูป apex → animate **apex→ลง** (อย่าสั่ง "launch up" เธอลอยแล้ว)
> - landing เริ่มที่ลอย → first frame = รูปลอย, reference = รูปท่า crouch เป้าหมาย

**4a — leap (reference mode, low-angle hero):**
- รูปเปิดดีสุด = **low-angle hero takeoff** (กล้องต่ำมองขึ้น + reflection ในพื้น = "double visual value")
- animate (reference): `She sprints forward then explodes into a powerful leap, legs into a wide mid-air running split at full stretch, hair/hem streaming, holds the split in smooth slow motion.` + camera low wide tracking · guard: `exactly two arms and two legs, anatomically correct knees, no broken/backward legs`
- ⚠️ match เฟรม: รูป running stride → สั่ง `running split` ไม่ใช่ `ballet split/toes pointed` (ขัดเฟรม = morph) · land เป็น **lunge** ไม่ใช่ one-knee (จาก momentum แนวนอน)

**4b — ซูมเป้า (โชว์ "เป้าแข็งแรง"):** ทำได้ 2 ทาง
- **(เชื่อถือได้) แยกคลิป + CapCut punch-in:** 4a ถึง slow-mo peak → cut เข้า insert เป้า → ตัดกลับ landing
- **(ลองได้) hyperzoom ในคลิปเดียว:** ⭐ hyperzoom เร็ว + **motion blur กลบ wide→close morph** (ดีกว่า slow push-in) — `rapid hyperzoom, heavy directional motion blur, whip-like push, settling sharp on the gusset` + `keep final frame sharp, intentional motion blur only`
- **insert เป้า:** ใช้รูป **rear-hip 3/4** (tasteful + โบนัสเห็นเอวยาง) หรือ macro **bar-tack `+` stitch** จากรูปผ้าจริง (โชว์ตะเข็บเสริมชัด = hero detail). animate: `fabric stretches taut across gusset, reinforced seam holds, then settles` · ⚠️ เฟรมเป็น inseam/ตะเข็บ "fabric only, no skin" กัน filter

**4-landing — ลง crouch (slow→fast→slow):**
- first frame = รูปลอย (apex/descending) + reference = รูป crouch pose
- animate ramp: `hangs at the top in slow motion → drops with sudden gathering speed, plummeting, quick sharp burst → the instant she lands, absorbing into a low athletic crouch, eases back into slow motion` (physics word ไม่ใช่ "fast")
- ⚠️ **ตัด "one hand down" ถ้ามือพัง** → ลงสองเท้า crouch เข่างอ (กันมือ #1) · guard ขา/เท้าทะลุพื้น

- **ออดิต:** เจน 5-6 รอบ · ช่วง "เร็ว"/hyperzoom = จุดเสี่ยงสุด หยุดเฟรมเช็กตัวไม่ละลาย + เฟรมจบคม + ขาตรง ไม่ 3 ขา

### Clip 5 — BRAND: ลุกขึ้นยิ้มมั่นใจ → โลโก้ (~4s)
- **จุดขาย:** ปิดแบรนด์ (ไม่ใช่ feature) · **สถานะ:** ยังไม่เริ่ม
- **โลโก้ "ดอกแก้ว + Valenshield + สโลแกน" แปะใน CapCut หลัง hard cut** — ห้ามให้ Seedance เจนตัวหนังสือ

รูปเปิด (ChatGPT — พอร์ตเทรต):
```
Vertical close-up beauty portrait of the same woman, lavender tunic collar visible, confident warm subtle smile, looking into camera, face exactly like the reference. Glossy black set, dramatic key light, soft catchlight in the eyes. Photorealistic editorial.
```
Animate — เวอร์ชันปลอดภัย (เริ่มจากพอร์ตเทรต):
```
Animate this still in subtle slow motion. She holds a confident, warm, genuine smile, eyes to camera, with gentle natural micro-movement — a slight head settle and soft hair movement. Camera: slow smooth push-in to her face.
Keep her exact face and the lavender garment identical, color unchanged.
Sound: a final cool beat hit, soft room tone. No music vocals, no dialogue.
Avoid: warped face, identity drift, uncanny expression, jitter.
```
- **เวอร์ชันต่อเนื่อง (ถ้าอยากเห็นลุกขึ้น):** first frame = ท่าคุกเข่า 1 ข้าง, animate = "rises gracefully from one knee to standing, camera pushes up to her face, confident warm smile" (motion เยอะกว่า เสี่ยงหน้ากว่านิด)

#### 🔑 อัปเดต Clip 5 (30 มิ.ย.) — ลุกขึ้น + ซูม
- **flow ที่ลงตัว:** ลุกจาก crouch/คุกเข่า → ขึ้นยืน → **ซูมช้า cinematic ครึ่งตัว (waist-up)** จบหน้านิ่ง calm (ไม่ต้องยิ้ม)
- **setup:** first frame = ท่า crouch · **last frame = รูปยืน hero (waist-up)** → first+last interpolate การลุก + จบเฟรม clean
- animate: `rises smoothly and gracefully to full standing height, calm composed still expression` + `camera: one slow smooth cinematic push-in, easing to a steady stop at waist-up half-body framing, no fast move`
- ⚠️ **ซูมแค่ครึ่งตัว (ไม่เข้า face close)** = face drift น้อยกว่า + ลุค editorial · `keep face sharp and consistent throughout, no shifting facial features` · เจน 5-6 รอบเช็กหน้า
- **frame portrait ปลอดภัยสุด** (มือซ่อนในกระเป๋า/นิ่ง) = เสี่ยงมือ #1 น้อยสุด
- จบครึ่งตัว calm → **hard cut logo CapCut**

---

## 8. จุดขาย → คลิป
| จุดขาย | คลิป |
|--------|------|
| กันน้ำ / น้ำไม่ซึม | Clip 1 (เหยียบน้ำ) + Clip 2 (ปาดน้ำออกแห้ง) |
| เอวยางยืด | Clip 3 |
| ผ้ายืด / เคลื่อนไหวคล่อง / เป้าแข็งแรง | Clip 4 (split leap) |
| ปิดแบรนด์ | Clip 5 |

## 9. Audit Checklist (ทุกคลิป)
- [ ] เจนรูปเปิดใน ChatGPT + ออดิตก่อน (หน้าตรง reference? ชุดตรง? **สีม่วงเฉดเดียวกับคลิปอื่น?** คอมโพสิชันสวย?)
- [ ] เจนวิดีโอ 4-6 รอบ (มือ/กระโดด เจน 5-6)
- [ ] หยุดเฟรมเช็ก: มือ/นิ้ว · แขนขา (ท่ากระโดด) · ผ้า (ไหลแบบยางไหม) · น้ำ (เป็นก้อนไหม) · หน้าเพี้ยน/ดริฟต์
- [ ] ไม่มี morph ตอนเปลี่ยนระยะ (ถ้ามี = อย่าซูมในคลิป)
- [ ] เลือกอันที่ "ตอนภาพเคลื่อน" ดีสุด ไม่ใช่เฟรมนิ่งสวย

## 10. สถานะปัจจุบัน & ขั้นต่อไป (อัป 30 มิ.ย.)
- **Clip 1:** ✅ backup ขาเดียว · ⏳ เวอร์ชัน 2 ขา
- **Clip 2:** ⏳ มือเพี้ยน → ลอง hands block `believable hand proportions, natural finger curvature, realistic grip` ([[ai-influencer-image-prompt]]) + `exactly two arms, five fingers per hand` / fallback ไม่มีมือ
- **Clip 3:** ⏳ มือพัง → whip-twist A ไม่มีมือ
- **Clip 4:** ⏳ แตกเป็น sequence (4a leap reference-mode low-angle · 4b ซูมเป้า hyperzoom/cut · landing crouch ramp) — **เจนรูป low-angle hero + ลอง animate ตามสูตรใหม่ session นี้**
- **Clip 5:** ⏳ flow ลงตัวแล้ว (ลุก→ซูมครึ่งตัว cinematic, first+last frame) — ยังไม่เจน
- **ประกอบ:** ◻️ ครบ 5 คลิป → CapCut: speed ramp + บีต + โลโก้/สโลแกน + hard cut

### 🔑 insight session 30 มิ.ย. (ใช้กับทุกคลิป)
- **input mode:** reference = ให้ model สร้าง action (วิ่งมาก่อนโดด) · first frame = ล็อกเฟรมเปิด · first+last = interpolate A→B (ดู [[seedance-knowledge]])
- **hyperzoom + motion blur กลบ wide→close morph** (ดีกว่า slow push-in)
- **hands block** + `exactly two arms/legs, five fingers` ลด hand/limb artifact ~70%
- **anatomy negative** (กันเอวเล็ก/สะโพกบาน) ถ้ามี body — [[ai-influencer-image-prompt]]
- **host:** Higgsfield (4K/Unlimited) + kie.ai (API) — อัปหน้าจริงได้ ไม่ต้องเบลอ
- รูปเปิดทำให้จริง/สวยขึ้น → ใช้ realism framework [[ai-influencer-image-prompt]] (เฉพาะ Valenshield = editorial lane HERO ฉากดำ ไม่ใช่ candid)

### ลำดับงานแนะนำต่อจากนี้
1. ปิด Clip 1 (เวอร์ชัน 2 ขา) ให้ผ่าน
2. ปิด Clip 2 (ลองมือบอกทิศ 5-6 รอบ ไม่ผ่านใช้ไม่มีมือ)
3. ปิด Clip 3 (whip-twist A)
4. เจนรูป takeoff Clip 4 → ออดิต → animate (หินสุด เผื่อเวลา/รอบ)
5. Clip 5
6. รวมตัดต่อ CapCut
