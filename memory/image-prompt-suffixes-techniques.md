---
name: image-prompt-suffixes-techniques
description: "Ready-made image-gen prompt suffixes + edit techniques (TVC white-tone, pose-transfer, character-swap, upscale) from ZenityX Thai prompt book — net-new bits not in the realism framework"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

Reusable GPT Image 2 / Nano Banana style **suffixes + multi-ref edit techniques** — kept only the parts NOT already in [[ai-influencer-image-prompt]] (realism framework) or [[ai-character-identity-lock]] (identity/reference sheets). Source: ZenityX Prompt Book (https://zenityx-prompt-book.netlify.app/, Thai).

## TVC white-tone suffix (commercial lane — high-key clean, net-new)
ต่อท้าย prompt หลักเมื่ออยากได้ TVC โทนขาวสะอาด ไฮคีย์ ผิวสว่าง แต่ยัง cinematic:
```
ultra-cinematic cinematography style, clean white tone TVC, highkey commercial, shallow depth of field, soft blurry background with creamy bokeh, subject in sharp focus, anamorphic lens, realistic film style, film lighting and shadow, movie still quality, professional cinema camera.
```

## Pose transfer (Pose Line Control) — technique
ให้ตัวใน image หลักโพสตาม reference pose/ลายเส้น. **ต้องระบุมุมกล้องทุกครั้ง** (ไม่งั้นเพี้ยน):
```
prompt: (เพศ/ตัวละคร) @image_1 โพสท่าออกมาให้เป็นแบบ @image_2 แบบ100เปอร์เซ็น
มุมกล้อง: (มุมสูง / มุมสายตา / มุมต่ำ / อื่นๆ)
```

## Character swap — technique
รวม background + คนจากคนละภาพ: ใส่ background = `@image1` แล้ววางตัวละคร = `@image2` ให้ integrate เนียน (ระบุ lighting/scale ให้เข้ากัน).

## Upscale prompts (vault ไม่เคยมี)
- **Product/general upscale:** "Upscale and enhance this low-resolution image to high clarity while maintaining [original identity/details]" — คงของเดิม ไม่เปลี่ยน subject.
- **Portrait upscale:** "hyper-detailed photorealistic upscale, extremely detailed skin texture, 8K" + negative params. ⚠️ ระวัง 8K/hyper-detailed ดันไปทาง over-render — ใช้กับงาน upscale เท่านั้น ไม่ใช่ gen ใหม่ (ขัดกฎ anti-AI ใน [[ai-influencer-image-prompt]]).

## Tool
- **Storyboard generator** — สร้าง 9-shot storyboard (แนวตั้ง+แนวนอน) จากภาพเดียว: `promptgen-7bhkz5r7.manus.space`

> ที่เหลือในเว็บ (cinematic suffix, real-photo/photojournalism, natural selfie, handheld shake, 4-view character sheet, character card, 9-panel lighting ref) = ทับของเดิมแล้ว จึงไม่เก็บ.
