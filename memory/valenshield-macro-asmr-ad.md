---
name: valenshield-macro-asmr-ad
description: "Active — Valenshield (ดอกแก้ว) 2nd campaign: 4-clip set, no-person macro ASMR fabric ads. Fabric = real soft LAVENDER (not white). Clip 2 defined (water-repellent bead demo). Separate from lavender HERO project."
metadata: 
  node_type: memory
  type: project
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

# Valenshield — Macro ASMR white-fabric campaign (แคมเปญ 2)

Valenshield brand (โลโก้ = ดอกแก้ว + สโลแกน) but a SEPARATE deliverable from the lavender HERO model ad in [[valenshield-nurse-ad-project]]. This campaign = **4 clips**, no person, QUIET ASMR, minimal music, 9:16, ~20s each. Modeled on a UNIQLO LifeWear macro reference (`/Volumes/WONYOUNG/Dokkeaw/ref/02.mp4` — grey fabric, water beading → packshot). Uses [[seedance-knowledge]] rules + realism from [[ai-influencer-image-prompt]] + macro teardown of the UNIQLO ref.
- ⚠️ **COLOR FIX:** brief said "ผ้าขาว" แต่สีจริง = **soft pale LAVENDER (periwinkle)** ตาม approved sheet `/Volumes/WONYOUNG/Dokkeaw/Outfit01-1.jpg` (= same real fabric as campaign 1). Macro shots crop fabric + silver buttons จาก sheet นี้ได้เลย. ทุก prompt ใช้ lavender ไม่ใช่ white.

## Campaign structure
- 4 clips total. **Clip 1 = ✅ DONE. Clip 2 = 🔄 กำลังทำ (defined below). Clips 3, 4 = TBD.**
- Each clip: 9:16, ~20s, no VO, ASMR + minimal music, ends logo (ดอกแก้ว + ผ้าวาเลนชีลด์ + สโลแกน).

## Clip 2 — hard-sell water+STAIN-repellent fabric (pale lavender), macro, no person
20s = 5 internal shots × ~4s, each a SEPARATE Seedance i2v gen (1 prompt = 1 clip rule), concat in CapCut.
- ⭐ **น้ำ = translucent RUSTY ORANGE-BROWN water** (Shot 2-5). Clip 1 = ไม่เปลี่ยน. ผลดี: (1) contrast ส้ม-สนิม vs ลาเวนเดอร์ = ชัด แก้ปัญหา low-contrast เกือบหมด (2) selling แรงขึ้น = กันน้ำ + **กันคราบ** (น้ำสกปรกกลิ้งออก ผ้าไม่เปื้อน).
- ⚠️ **negative บังคับ:** `no rust stain, no orange/brown discoloration, no soaking` — น้ำมีสีแล้ว model จะอยากให้ผ้าติดสี ต้องกันแรง ไม่งั้น anti-stain proof พัง.
- shots (shallow DoF โฟกัสบางหยด หลังเบลอ; หยดไหล physics ธรรมชาติ ไม่นิ่ง; **lotus/superhydrophobic** = หยดกลม high-contact-angle กลิ้งเหมือนบนใบบัว ไม่ซึม ไม่ทิ้งคราบ):
  1. 0-4s ECU dry lavender fabric, light sweep across DIAGONAL TWILL weave (ไม่มีน้ำ)
  2. 4-8s หลายหยด rusty ตกสโลว์โม → เกาะเม็ด → กลิ้ง/ไหล/บาง merge, shallow DoF ★ หินสุด (fluid sim)
  3. 8-12s หลายหยด rusty รวม→กลิ้ง, ผ้าไม่เปื้อน
  4. 12-16s **มาโครส่วนหนึ่งของเสื้อจริง** (ไหล่→แขน หรือ อก+placket+กระดุมเงิน, on invisible mannequin, มี slope) → หยด rusty กลิ้งแบบ lotus ไหลออกหมด ไม่เกาะติด → ผ้าสะอาดแห้ง
  5. 16-20s ชุดลาเวนเดอร์เต็มตัวหมุน **cinematic slow-motion** (พื้น charcoal เข้ม) → หยด rusty บนไหล่/อกกลิ้งไหลออกเองระหว่างหมุน (lotus) → หยุดหันหน้าตรง → hard cut logo (CapCut). ไม่มีสาดน้ำ/ไม่มีคน. หมุนช้า = morph น้อยกว่าหมุนเร็ว; เร่งจบ speed-ramp CapCut ได้
> Full English per-shot prompts (rusty/lotus/shallow-DoF) written in session ก.ค. 2026.
> **First-frame packshot Shot 5:** `/Volumes/WONYOUNG/Dokkeaw/20260701/vid02/ChatGPT Image Jul 1, 2026, 05_16_13 PM.png` (ชุดเต็ม พื้น charcoal) — ต้อง regen variant ให้มี **หยด rusty เกาะไหล่/อก** ก่อน animate (i2v ต้องมีหยดใน first frame ให้ไหล)

## Assets (reference for image gen)
- **Garment/identity:** `/Volumes/WONYOUNG/Dokkeaw/Outfit01-1.jpg` (approved 4-view)
- **Fabric macro (สี/เนื้อ/ตะเข็บจริง):** folder `/Volumes/WONYOUNG/Dokkeaw/ภาพสินค้าดอกแก้วและข้อความ/` — twill ลาเวนเดอร์ diagonal weave + satin sheen, buttonhole, keyhole placket, bar-tack "+" stitch, cuff seam. แนบเป็น reference ตอนเจน macro stills เพื่อ lock สี+weave+ตะเข็บให้ตรงของจริง.

## Feasibility ~80% + risks (from vault)
- ✅ **No person = removes Valenshield's #1 failure (hands/face/legs)** — this concept dodges all the pain of the lavender project.
- ✅ **contrast แก้แล้วด้วย rusty orange-brown water** (ส้มสนิม vs ลาเวนเดอร์ = ตัดกันชัด) — ไม่ต้องพึ่ง raking light หนักเท่าเดิม. แต่ยังต้องกัน **rust stain ติดผ้า** (negative แรง).
- ⚠️ **Shot 2 droplet impact/bounce + Shot 3 coalescence = fluid sim** — AI tends to jelly/blobs (memory). Gen 5-6×; try reference mode for the fall.
- ⚠️ **Shot 5 rotating full white garment + "snap"** = full-garment morph + "fast"=jitter. Use "whips/snaps then settles"; fallback = slow rotate + CapCut speed-ramp.
- **Text/logo = CapCut only** (Seedance text unstable). **ASMR + music = layered in CapCut.**
- Continuity: same white tone/weave every shot — lock via reference still + identical lighting.

## Lessons (จากการลองจริง)
- ⚠️ **AI default ผ้าเป็น plain weave / ตาราง 90°** (linen crosshatch) แม้สั่ง "twill". ของจริง = **fine diagonal twill (ริ้วเฉียง ~45° ทางเดียว)**. แก้: ระบุ "continuous parallel diagonal ribs at ~45°, one direction, like gabardine/chino twill" + negative `plain weave, basketweave, linen crosshatch, perpendicular 90-degree grid` + **ถอย zoom** (thread-level ใกล้ไป twill หาย) + raking light ตามแนวทแยง + **ใช้ Nano Banana Pro** (texture-from-reference ดีกว่า GPT Image 2).

## Shot 5 — current prompt (reference mode, dew version, ก.ค. 2026)
first frame ไม่ล็อก (reference mode) → คุมหยดที่ prompt ได้. start side profile → หมุนมาหน้า cinematic slow-mo. ผ้า reference = packshot `Outfit01-1.jpg` หรือ front packshot `.../vid02/ChatGPT Image Jul 1, 2026, 05_16_13 PM.png`.
```
Use the attached image as a style/appearance reference for the uniform (pale lavender, silver buttons, diagonal twill, dark charcoal background) — NOT a fixed frame; regenerate the scene.
A full pale-lavender Valenshield nurse uniform on an invisible mannequin, covered in a fine dew of countless tiny water droplets, like fresh morning dew on a leaf — very small, densely and evenly scattered, each far smaller than a button, translucent rusty orange-brown 3D beads resting on top of the weave.
The uniform slowly rotates from a side profile toward the front in smooth CINEMATIC SLOW MOTION, easing to a graceful stop facing forward. The fabric is superhydrophobic like a lotus leaf — the tiny dew droplets bead up, gather, and roll and sheet straight down and off the surface under gravity as it turns, running off completely, leaving the uniform clean, bone-dry, spotless pale lavender — no rust stain, no orange mark, no wet patch, no trace.
Only the uniform and the dew droplets are in the scene, nothing floating in the air around it, plain clean charcoal background. Locked camera, full garment in frame, luxurious cinematic slow motion, dramatic soft key light with a gentle rim. Keep the exact pale lavender tone, silver buttons and diagonal twill identical. NO text, NO logo.
Sound: soft rolling-water ASMR + final music resolve (edit).
Avoid: oversized droplets, large beads, sequins, flat discs, gemstones; any fog, mist, smoke, haze, vapor or airborne particles; orange or rust stains, smears or discoloration on the fabric; water soaking in; any person or hands; fast rotation; folds morphing; jitter; text or logo.
```
> ถ้า dew ยังใหญ่ → ทาง 2: มาโคร Shot 2-4 โชว์หยด, packshot mood อย่างเดียว.

## Lessons — water droplet size on wide/packshot shots (ก.ค. 2026, ลองจริงเยอะ)
- ⚠️ **wide full-garment shot → model เรนเดอร์หยดใหญ่เสมอ** ไม่ว่าสั่ง "1-4mm" หรือเทียบกระดุม ("1/6 of a button") — numeric/scale-anchor **ไม่ค่อยได้ผล** บน framing กว้าง.
- ⚠️ **"spray bottle / fogger / mist" = model วาดหมอก/สเปรย์คลุ้งออกมา** (naming = drawing; "no mist appeared" ไม่ช่วย). ทำให้หยดเล็กจริงแต่แถมหมอกที่ไม่ต้องการ.
- ✅ **กฎ: อย่าเอ่ยสิ่งที่ไม่อยากเห็นใน positive body — บอกผลลัพธ์ (หยดบนผ้า) ไม่ใช่สาเหตุ (สเปรย์)**. สิ่งไม่อยากเห็น → ใส่ Avoid อย่างเดียว.
- ลองคำ **"fine dew / morning dew on a leaf"** = เล็กโดยธรรมชาติ + ไม่ trigger หมอก (candidate ดีสุดที่เหลือ).
- 🎯 **ทางแก้จริง = แบ่งหน้าที่ (limitation ยอมรับ):** โชว์ beading/physics หยดเล็กสมจริงใน **มาโคร Shot 2-4** (สเกลถูก) · **packshot Shot 5** ยอมรับหยดกลาง/mood หรือหมุนโชว์ชุดเฉยๆ.
- rusty water → ระวัง model ทำเป็น **คราบส้มติดผ้า** → อัด negative `orange/rust stains, smears, discoloration` เสมอ.

## Pipeline (same as lavender project)
เจนรูป macro นิ่งก่อน (ChatGPT/GPT Image) → audit → Seedance i2v first-frame, ~4s, 4-6 gens → judge on MOTION not stills → CapCut (speed ramp + ASMR + music + logo + hard cut). Host: Higgsfield (4K/Unlimited) + kie.ai.
