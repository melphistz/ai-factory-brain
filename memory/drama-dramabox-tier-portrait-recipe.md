---
name: drama-dramabox-tier-portrait-recipe
description: "Validated paste-ready prompt recipe for DramaBox/ReelShort-tier drama character portraits — cinematic key+rim light, idol glam makeup, sculpted features; tested on throwaway test character \"Fon\" (not a locked production character)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5acbc9d1-f78e-4727-8b34-6fe6a1e3aea3
---

Prompt recipe ทดสอบผ่านจริง 2026-07-09 — gen แล้วเทียบกับ 12 reference caps จาก DramaBox/Watch Drama Series ตรง tier. ทดสอบบนตัวละคร "ฝน (Fon)" ซึ่งเป็นแค่ **ตัวทดสอบ prompt เฉยๆ ไม่ใช่ตัวละครที่ล็อกไว้ใช้งานจริง** (ไม่มี identity-lock/turnaround ทำให้) — ไฟล์นี้เก็บไว้คือ**สูตร/เทมเพลต** ไปใช้กับตัวละครตัวจริงทีหลัง ดูคู่ [[feedback-drama-character-casting]] (กฎ) และ [[ai-character-identity-lock]] (วิธีล็อกหน้าเมื่อจะใช้จริง).

## วิวัฒนาการ 3 รอบ (บทเรียนสำคัญ)

1. **รอบแรก (พัง):** "natural unretouched photograph" + "neutral even softbox" + "low double eyelid/soft nose/facial asymmetry" → จืดชืด ไม่น่าจดจำ (ผิดกฎ casting)
2. **รอบสอง (ดีขึ้น):** เปลี่ยนเป็น cinematic vocabulary (key+rim light, shallow DOF) + concrete beauty cues (large eyes/slim nose/full lips) → ผ่านเกณฑ์พื้นฐานแต่ตายังดู tired/ไม่มี catchlight ชัด
3. **รอบสาม (DramaBox tier — WIN):** เพิ่ม "idol glam makeup" (winged eyeliner/contour/highlighter) + "dramatic key+strong rim+warm-cool grade" + "sharp focus locked on eyes" → ตรง tier reference ยืนยันด้วยภาพจริง

## Template (paste-ready — สลับแค่ CHARACTER block ตามตัวละครใหม่)

```
9:16 vertical cinematic drama-series character portrait, shot on ARRI Alexa with 50mm lens f1.8, shallow depth of field

CHARACTER: [name/age/nationality], natural [nationality] facial features, [skin tone] skin with a luminous healthy glow. Soft oval face with a refined, sculpted V-line jaw. Large bright almond eyes with a defined double eyelid, sharp vivid catchlights reflecting the key light, long natural lashes, a soft alluring downturn at the outer corners. Slim straight nose bridge with a delicate refined tip. Full natural lips with a soft rosy-brown gloss tint, upward-curling corners even at rest. [identity marks e.g. mole]. [hair description]. [build].

SKIN: photoreal skin with a luminous dewy glow, professional-actor tier — fine visible pores kept subtle, soft under-eye highlight, gentle contour and highlight sculpting, subtle natural cheek flush, NO plastic or waxy CGI, NO heavy airbrush; flawless-looking but human.

MAKEUP: soft glam "idol drama" makeup — defined winged eyeliner sharpening the eye shape, subtle eyeshadow wash, groomed defined brows, glossy tinted lips, faint highlighter on cheekbones and nose bridge.

OUTFIT: [outfit].

POSE: [pose], eyes alert and alive — not blank, not tired.

LIGHTING: dramatic cinematic key light with a strong rim/edge light separating her/him from the background, warm-cool color contrast (cool ambient, warm key), soft directional falloff sculpting the face — moody, high-production-value, NOT flat, NOT a plain even studio wash.

BACKGROUND: softly blurred moody interior with hints of warm practical lights, shallow depth of field, rich cinematic bokeh.

STYLE: high-end Asian drama-series hero-character still (DramaBox/ReelShort flagship-tier), crisp sharp focus locked on the eyes and face, cinematic color grade, subtle film grain, glossy premium finish.

Negative: no long dull face, no narrow tired eyes, no flat wide nose, no plastic or waxy skin, no heavy airbrush, no digital-art render, no flat lighting, no forgettable expression, no harsh under-eye shadows, no text.
```

## กับดักที่ห้ามทำซ้ำ

- ห้ามใช้ "natural unretouched photograph" / "neutral even softbox" / "facial asymmetry" ของ UGC template — ดันหน้าไปทาง plain ทันที
- ต้องมี "sharp vivid catchlights" ชัดเจนในตา ไม่งั้นจะดู tired แม้ features อื่นดีแล้ว
- makeup ต้องระบุ "idol glam" ไม่ใช่ "no-makeup makeup" — ตัวนี้คือจุดต่างสำคัญระหว่างรอบ 2 (ผ่านพื้นฐาน) กับรอบ 3 (ตรง tier)

## Related

- [[feedback-drama-character-casting]] — กฎต้นทาง (ทุกตัวละครสวย/หล่อ, drama ≠ UGC)
- [[ai-character-identity-lock]] — ใช้เมื่อจะล็อกเป็นตัวละครจริง (ไม่ใช่แค่เทส)
- [[ai-asset-library-workflow]] — pipeline เต็มถ้าจะทำ turnaround+asset library ต่อ
