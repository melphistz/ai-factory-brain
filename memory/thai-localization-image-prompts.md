---
name: thai-localization-image-prompts
description: "Localization rules for making AI-generated images read as authentically Thai (not postcard-fake) — subject/setting specifics, the proven standard adaptation phrase (used on 112 production prompts), text-glyph verification rule, cultural specificity. Use whenever a gen request has a Thai subject/setting."
metadata:
  node_type: memory
  type: reference
---

# Thai Localization — Image Prompt Rules (07-09)

Source: AI Video Skool course production skill (Italian team, different environment, reviewed and adapted 2026-07-09). กฎทำให้ภาพ AI "อ่านออกว่าเป็นไทยจริง" สำหรับตลาด FF — ดูคู่ [[ai-influencer-image-prompt]] · skill `image-prompt-writer` มี nationality block พื้นฐานอยู่แล้ว (section 5) ไฟล์นี้เสริมส่วนที่ block นั้นไม่ครอบ: setting authenticity, standard adaptation phrase, text-glyph rule, culture.

## ⭐ Standard adaptation phrase (ของมีค่าที่สุดในไฟล์นี้ — ใช้ซ้ำแทบทุกครั้ง)

ต่อท้าย prompt เดิมที่มีอยู่แล้วเพื่อแปลงเป็นไทย โดยคง composition เดิมไว้ทุกอย่าง เปลี่ยนแค่ subject/location:

```
Adaptation: any person in the scene is Thai; any city or location is in Thailand (e.g. Bangkok). Keep every other detail exactly as specified in the prompt.
```

Validated ใน production จริง 112 prompts (source skill) — วิธีเร็วสุดเวลามี prompt แม่แบบอยู่แล้ว (เช่น UGC/editorial template ที่ทำงานดีอยู่) และแค่ต้องการ localize เป็นไทยโดยไม่อยากเขียนใหม่ทั้งหมด.

## Subject — คนไทยในภาพ

- ใช้ "Thai man/woman in his/her 20s-30s" + รายละเอียดรูปธรรม (ไม่ใช่ "Asian" เฉยๆ — model จะดริฟต์ไปทาง generic Western-Asian look)
- เสริมด้วย "natural Thai facial features, medium skin tone" กัน default ของโมเดลเอียงไปทางตะวันตก
- outfit: urban modern สำหรับฉาก BKK, uniform สมจริงสำหรับฉากงาน (ดู skill section 5 สำหรับ face-geometry block เพิ่มเติม — eyelid/nose/skin-tone specifics)

## Setting — ฉากที่ "อ่านออกว่าไทยจริง" vs postcard-fake

- **หลีกเลี่ยง stereotype โปสการ์ด** (ตุ๊กตุ๊ก+ช้างเต็มเฟรม) — คนไทยจับ fake-Thailand ได้ทันที
- **กรุงเทพจริงที่ใช้ได้ผล**: ถนนที่มีสายไฟพันกัน (signature ภาพ BKK), ตลาด, ฟู้ดคอร์ท, คอนโดสมัยใหม่, ออฟฟิศ open-space, มอเตอร์ไซค์, 7-Eleven, street food, BTS, คาเฟ่อินดี้แถว Ari/Thonglor
- **แสง**: "harsh tropical midday sun" หรือ "warm late-afternoon light" น่าเชื่อสุด; ฝน/มรสุมใช้ได้เวลาต้องการ mood
- **Interior**: คาเฟ่มินิมอล, บ้านไทยร่วมสมัย — ระวัง "resort หรู" ถ้ากลุ่มเป้าหมายคือ mass market ไม่ใช่ luxury

## Product & text ในภาพ

- Product ในภาพ: ใช้ brand สมมติที่ packaging ดูสมเหตุสมผลแบบไทย หรือ product generic — **ห้าม** ใช้ brand จริงโดยไม่มีสิทธิ์
- **ตัวอักษรไทยในภาพต้อง verify ทุกครั้ง** — model มักพลาด glyph ซับซ้อน (สระบน/ล่าง, วรรณยุกต์). ถ้า text สำคัญ (เช่น ต้องอ่านออก) → gen เวอร์ชันไม่มี text แล้วใส่คำในภายหลังผ่าน post (PIL/Canva) แทนการพึ่ง model เขียนไทยตรงๆ
- GPT Image 2 รับ prompt ภาษาไทยได้ (บรรยายเป็นไทยในตัว prompt ได้เลย); Nano Banana Pro ให้ผลดีกว่าถ้าเขียน prompt เป็นอังกฤษ + บรรยาย subject ว่าเป็นไทย

## Cultural specificity

- **ท่าทาง**: ไหว้เฉพาะบริบทที่สมเหตุผล (ทักทายทางการ) — รอยยิ้มธรรมชาติดีกว่าท่าโพสแข็งๆ
- **การแต่งกาย**: respectful ในบริบทวัด/office สาธารณะ; casual อิสระในบริบทอื่น
- **อาหาร**: จานที่จำได้ทันที (ผัดกะเพรา, ส้มตำ, หมูปิ้ง) ดีกว่า "generic asian food" คลุมเครือ

## Related

- `skills/image-prompt-writer/SKILL.md` — nationality-specific face block (section 5) + trigger note ที่ชี้มาไฟล์นี้
- [[ai-influencer-image-prompt]] — realism framework ทั่วไป
