---
name: ai-platform-content-limits
description: "Content policy limits for revealing/suggestive clothing on GPT Image, Nano Banana, Seedance — what's allowed vs blocked"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# AI Platform Content Limits — revealing/suggestive clothing (clothed fashion)

> เส้นแบ่งสำหรับงาน fashion/influencer (คน clothed). เก็บ มิ.ย. 2026 ผ่าน Exa. เกี่ยวกับ [[ai-influencer-image-prompt]] · [[seedance-ugc-repository]]
> ⚠️ explicit/nudity = ทำไม่ได้ทุกแพลตฟอร์ม (by design). นี่คือขอบเขตของ "clothed fashion" เท่านั้น

## เส้นแบ่ง revealing
| ระดับ | สถานะ |
|---|---|
| fitted clothing, deep V / low neckline, **cleavage**, crop top | ✅ ปกติผ่าน (framing fashion/non-sexual) |
| **bikini / swimwear** | ✅ ผ่านถ้า non-sexual setting (beach/pool) · ⚠️ gray ถ้า context ส่อ |
| boudoir-adjacent + non-intimate framing | ⚠️ gray |
| **lingerie / underwear-only** | ⚠️→❌ gray ที่มักโดนบล็อก (Nano Banana บล็อกแม้ ecommerce ปกติ) |
| nipple / nudity / sexual-suggestive pose / implied sexual | ❌ hard blocked ทุกแพลตฟอร์ม |

**เพดานที่เชื่อถือได้ (clothed fashion):** cleavage / deep-neck / bikini / crop top — เกินนี้เข้าโซน gray→block

## ความเข้มตามแพลตฟอร์ม
- **Nano Banana / Gemini** = เข้มสุด — IMAGE_SAFETY บล็อกแม้ lingerie/underwear fashion ecommerce ปกติ (over-block ช่วงนี้ มี report เยอะใน Google AI forum)
- **GPT Image 2** = ปานกลาง — บล็อก lingerie/swimwear แม้ commercial บางครั้ง
- **Seedance 2.0 (วิดีโอ)** = บล็อก lingerie sexual context + ท่าส่อ · อนุญาต swimwear non-sexual + fitted fashion · รัน 3 filter (text prompt / reference face / brand-IP)

## วิธีอยู่ในเส้น (max ที่ผ่านได้)
- frame เป็น **"editorial fashion photography / professional fashion shoot"**
- ใช้ภาษา **photographer** (camera/lighting/lens spec)
- ⚠️ **เลี่ยง trigger words:** `sensual, seductive, provocative, intimate, sexy` → ดันเข้าโซน block
- setting **non-sexual** + expression neutral

## ✅ Verified passing pattern (ทดสอบจริง มิ.ย. 2026)
**bikini ผ่าน** เมื่อ: setting beach non-sexual + `casual holiday lifestyle / travel Instagram` + `simple triangle bikini, casual beachwear` + expression `relaxed calm` + negative `no sexual or suggestive posing` + **ไม่มี** trigger word (sensual/seductive/sexy/intimate)
- ทดสอบบน GPT Image (ChatGPT) — ผ่าน, ได้ full-body bikini beach Korean realistic
- ✅ ยืนยันเพิ่ม: **9:16 + triangle bikini มาตรฐาน (ปกติ ไม่ใช่ high-waist)** ก็ผ่าน — full-body candid travel
- recipe นี้ = template ปลอดภัยสำหรับ swimwear content (ทั้ง 4:5 และ 9:16, bikini ปกติ)

## ข้อจำกัดเชิงระบบ
- **ไม่มี published rulebook สำหรับ gray zone** → prompt เดียวกันผ่าน/ไม่ผ่านได้ตาม timing + model update
- "find the edges by trial and error" — ไม่ใช่ workflow ที่ stable
- งาน glamour/boudoir จริงจัง → แพลตฟอร์ม mainstream ไม่เหมาะ (by design)

## แหล่งที่มา
- [Picasso IA — Seedance 2.0 NSFW Policy for Adult Creators](https://blog.picassoia.com/seedance-2-0-nsfw-policy-adult-creators)
- [apipass — Avoid Content Policy Violations on GPT Image 2](https://apipass.dev/blogs/how-to-avoid-content-policy-violations-gpt-image-2)
- [Google AI forum — Nano Banana Pro blocking non-NSFW fashion/lingerie](https://discuss.ai.google.dev/t/nano-banana-pro-non-nsfw-fashion-images-blocked-due-to-aggressive-image-safety-filtering/121805)
- [TheSource — Seedance 2.0: what the filters block](https://thesource.com/2026/04/15/seedance/)
