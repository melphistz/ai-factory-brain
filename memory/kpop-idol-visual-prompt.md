---
name: kpop-idol-visual-prompt
description: "Reusable realistic prompt — stunning 20yo K-pop female idol 'visual' (most-beautiful member); concrete-feature recipe + how to translate 'สวยจนลืมหายใจ' into terms a model understands"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 86c5776a-a91f-460f-9a7e-50481518b8ef
---

# Realistic K-pop Idol "Visual" — Beauty Portrait Prompt (07-06)

สูตรทำผู้หญิง idol อายุ 20 สวยระดับ visual ของวง แบบ realistic ไม่ปั้น. ดูคู่ [[ai-influencer-image-prompt]] · [[ai-character-identity-lock]] (ถ้าจะล็อกเป็นตัวละคร).

## กฎแปลง superlative → prompt
- คำ abstract ("สวยจนลืมหายใจ / ไม่มีจริง / หลงรัก") model **แปลไม่ออก** — ใช้ **ลักษณะรูปธรรม** แทน: harmonious balanced features · large almond eyes + double eyelid · slim high nose bridge · V-line jaw · full glossy gradient lips · **glass skin dewy glow** · magnetic gaze
- realism กันดูปั้น = ผิวมีรูขุมขน/peach fuzz/แก้มแดงบางๆ, NO airbrush/plastic — "flawless but real"
- idol visual = **คัดจากหลายรอบ** gen 5-6 ใบเลือก auto-beautiful สุด
- อยาก realistic ขึ้น = เพิ่ม "candid, natural light, phone photo" (แต่ glam ลดลง — visual มักต้อง polished นิด)

## Base prompt (GPT Image / Nano Banana) — paste-ready
```
Ultra-photorealistic beauty portrait of a 20-year-old Korean female K-pop idol, the "visual" (most beautiful member) of a girl group — editorial idol photocard quality, shot on a full-frame camera with an 85mm f1.4 lens.
FACE: strikingly beautiful, harmonious balanced features — large bright almond eyes with defined double eyelids and long natural lashes, a slim high nose bridge, small softly defined V-line jaw, smooth forehead, full glossy lips with a gentle gradient tint, delicate arched brows. Fair luminous "glass skin" with a healthy dewy glow.
SKIN: photoreal real skin — fine visible pores, soft natural texture, subtle cheek flush, faint peach fuzz, NO plastic or waxy CGI, NO heavy airbrush; flawless but real.
HAIR: long silky straight-to-softly-wavy black hair with light see-through bangs framing the face, natural shine and flyaways.
MAKEUP/STYLING: soft luminous K-beauty idol makeup, glossy lips, subtle shimmer, tiny elegant earrings; clean chic top.
EXPRESSION: calm, alluring, effortless — a soft magnetic gaze straight into the camera that holds attention.
LIGHT: soft professional beauty light, gentle catchlights in the eyes, delicate rim light on the hair, clean bright airy tone, seamless soft-gradient studio background.
STYLE: high-end idol beauty campaign, crisp micro-detail, true-to-life color, natural depth of field.
Negative: no plastic or waxy skin, no over-airbrushing, no doll-like uncanny face, no over-symmetry, no CGI or 3D render, no warped hands or fingers, no extra fingers, no text, no logo, no watermark.
```

## Variants ต่อยอด
- **full-body idol / stage / concept** — เปลี่ยน framing + outfit (stage costume / street / Y2K) คง FACE+SKIN block
- **ล็อกเป็นตัวละคร** — gen ใบสวยสุด → ทำ turnaround+expression sheet เป็น @ref (ดู [[characters/zhao-yu]] เป็น template)
- **hair color/theme** — ปรับ HAIR + LIGHT tone
