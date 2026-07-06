---
name: char-zhao-yu
description: "Character profile — Zhao Yu (趙宇) Korean idol, pink Y2K; identity spec + 4 gen prompts (portrait / turnaround / expression sheet / cover)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f8192bbf-f14d-45c5-96e5-c7fa1058eb28
---

# Zhao Yu (趙宇) — Korean Idol Character

สร้าง 2026-07-06 จากธีม TREND ICON pink Y2K cover. ตัวละคร reusable ล็อกหน้าข้ามภาพ — ดู [[ai-character-identity-lock]], [[ai-influencer-image-prompt]].

## Identity Spec (ล็อกทุกภาพ — copy ท่อนนี้เข้าทุก prompt)

> young Korean idol named "Zhao Yu (趙宇)", early 20s, oval face, glossy dewy skin, soft luminous makeup, glossy pink lips, defined double eyelids, long straight black hair with wispy see-through bangs falling past the chest

- **สัญชาติ/วัย:** เกาหลี, ต้น 20s
- **ทรง:** ผมดำตรงยาว, ปัดหน้าม้าบางซีทรู
- **หน้า:** oval, ตาสองชั้น, ผิวฉ่ำ dewy, ปากชมพูฉ่ำ, เมคอัพนวล
- **ธีมสี signature:** pink + silver chrome

## Signature Outfit (Y2K K-fashion)

white lace-trim crop cami + pink star graphic · oversized pink varsity bomber off-shoulder · layered silver heart-charm chains · tiered pink-and-black ruffle mini skirt + studded belt · silver metallic star handbag

---

## Prompt 1 — Portrait เดี่ยว (clean, พื้น pink)

```
Ultra-sharp K-fashion editorial portrait, single subject, vertical 3:4, 8K.
CHARACTER: [identity spec]
OUTFIT: [signature outfit]
POSE: three-quarter body, standing, slight lean toward camera, one hand raised near shoulder gripping the jacket, cool confident idol posture, calm direct gaze.
LIGHTING: high-contrast studio flash, soft dewy highlights, crisp fabric texture.
BACKGROUND: clean seamless soft-pink studio backdrop, no text, no graphics, no collage.
STYLE: photoreal luxury fashion campaign, ultra-crisp.
```

## Prompt 2 — Turnaround Sheet (lock identity)

```
Character reference sheet, same single person in every panel, identical face/hair/outfit across all views, neutral even lighting, clean seamless soft-pink background, no text.
CHARACTER: [identity spec]
OUTFIT (same all panels): [signature outfit]
LAYOUT — row of full-body turnaround + row of face close-ups:
- Full body FRONT, neutral standing, arms relaxed
- Full body THREE-QUARTER
- Full body SIDE profile
- Full body BACK (hair + jacket back)
- Face CLOSE-UP front, neutral
- Face CLOSE-UP three-quarter
Consistent proportions/height, model-sheet turnaround, photoreal, even studio light, reference-sheet clarity.
```

## Prompt 3 — Expression Sheet

```
Character expression sheet, same single person every panel, identical face/hair/makeup, clean seamless soft-pink background, even neutral studio light, no text.
CHARACTER: [identity spec]
LAYOUT — grid of head-and-shoulders close-ups, same framing/scale, only expression changes:
neutral · bright smile teeth · playful wink tongue-out · pouty bratty eyes-away · soft laugh crescent eyes · cool serious chin-down · surprised wide eyes · shy smile looking down
Consistent face structure/makeup all panels, photoreal, even light.
```

## Prompt 4 — TREND ICON Magazine Cover (pink Y2K)

ธีม: Korean idol mag, chrome liquid-metal masthead "TREND ICON", pink Y2K collage (chrome/sparkle/heart/barcode/Windows-98 popup "Loading Confidence 100%"). ชื่อไอดอลเป็น **coverline ตัวใหญ่ใต้ masthead/ข้างหน้า** ("ZHAO YU 趙宇" chrome ชมพู) — ไม่ซ่อน barcode. เต็ม prompt อยู่ในแชต session 2026-07-06.

## Canonical Reference Images (gen 2026-07-06, identity locked ✅)

`characters/zhao-yu-refs/` — ลาก @ref จากไฟล์พวกนี้ตอนทำภาพใหม่ ไม่ต้อง gen ซ้ำ:
- `zhao-yu-turnaround-sheet.png` — **@ref หลัก** (front/3-4/side/back + close-up) ล็อกหน้า+outfit
- `zhao-yu-expression-sheet.png` — 8 อารมณ์ close-up
- `zhao-yu-portrait.png` — portrait เดี่ยว pose เท่
- `zhao-yu-trend-icon-cover.png` — TREND ICON pink Y2K cover (ตัวอย่าง output จริง)

## Realistic RAW-UGC variant (07-06) — สำหรับปั้นบัญชี IG แนว cherryhikiko
เวอร์ชัน "คนจริง candid" (ไม่ใช่ idol glam) = idol identity + realism stack. อ้างอิงลุค [[veo-google-flow-knowledge]] + [[ai-influencer-image-prompt]] + teardown cherryhikiko.
- **anchor ใหม่:** gen `zhao-yu-realistic-sheet.png` (turnaround+expression, bright even light, ผิว matte มีรูขุมขน) → ใช้เป็น @ref แทน turnaround idol เดิมเวลาทำโพสต์ UGC
- ตัวอย่าง gen ที่ผ่าน: `~/Downloads/ChatGPT Image Jul 6, 2026, 05_45_04 PM.png` (bright bedroom selfie, satin lace cami)

### กฎ realism (คีย์ให้ "ไม่ดู AI")
1. **phone front-cam selfie** — wide barrel distortion, handheld, grain, compression, soft นิด, แขนยื่นถือมือถือ
2. **ผิว unretouched** — รูขุมขน, ฝ้า/กระบางๆ, ไฝ, มัน T-zone, **matte ไม่วาว** (NO smoothing/airbrush)
3. ⭐ **แสงสว่าง แบน โอเวอร์นิดๆ** (แบบ cherry) — daytime window / ไฟห้องสว่าง, neutral-cool WB. **ห้าม moody/dark/low-key** (บทเรียน 07-06: recipe เดิมสั่ง "underexposed/moody" → ออกมามืดหมด ผิด ref)
4. ฉากชีวิตจริง (เตียง/ห้อง/รถ), framing casual off-center

### sexy tasteful preset (suggestive-clothed)
- wardrobe: black lace bralette / satin cami / robe เลื่อนไหล่ / crop+midriff · pose: นั่งขอบเตียง/นอน over-shoulder/mirror selfie · gold necklace + hoops
- ⛔ **ceiling:** suggestive-clothed = สุด. explicit/nude = (ก) mainstream tool บล็อกหมด (ข) เราไม่ทำ. ดัน "variety" (มุม/wardrobe/mood/สว่าง) ไม่ใช่ "โป๊ขึ้น"
- tool ทน suggestive: Nano Banana > Seedance > GPT Image (strict สุด)

## Caveat

- CJK (趙宇 + ฮันกึล) model render เพี้ยนบ่อย — ถ้าเป๊ะสำคัญ gen พื้น+latin ก่อน แปะ CJK ทีหลังใน editor
- gen sheet 2+3 ก่อน → ใช้เป็น @ref ตอนทำ cover/scene อื่น หน้าจะนิ่ง
