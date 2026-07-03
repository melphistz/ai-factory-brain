---
name: storyboard-gpt-image-to-seedance
description: "Workflow — make storyboard/keyframes with GPT Image 2, then animate in Seedance 2.0"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Storyboard Workflow: GPT Image 2 → Seedance 2.0

> ทำ storyboard/keyframe ด้วย GPT Image 2 (คุม composition+identity) แล้วป้อนเข้า Seedance 2.0 animate.
> **ยืนยันด้วยเทสจริง:** @mariaveydiaries (X) เทส prompt เดียวกัน มี vs ไม่มี storyboard → **มี storyboard ดีกว่าชัด**.
> เกี่ยวข้อง: [[seedance-knowledge]] · [[ai-influencer-image-prompt]] · pipeline เดียวกับ [[valenshield-nurse-ad-project]] (รูปเปิดต่อคลิป = storyboard นี่แหละ)

## ทำไมต้อง storyboard ก่อน
- storyboard frame **fix character + lighting + wardrobe + environment + lens** ให้ → animation กลายเป็น "constraint problem" ไม่ใช่ generate จากศูนย์ → stable + คุมได้
- แบ่งงาน: **GPT Image 2 = storyboard/keyframe/character sheet/title card** · **Seedance 2.0 = image-to-video/motion**
- GPT Image 2 เก่ง: composition สะอาด, character silhouette คงที่, lighting นิ่ง — **แต่ไม่ใช่ตัวเรนเดอร์ผิว final** (ดู benchmark ใน [[ai-influencer-image-prompt]])

## STEP 0 — แตก script เป็น beat (ก่อนเปิดเครื่องมือ)
- 1 beat = 1 visual moment: ปูฉาก / รีแอ็กชั่น / แอ็กชั่น / เผยไต๋ / มุก
- เขียน beat เป็นประโยคเดียวก่อน แล้วค่อย map → panel
- rule of thumb: **6–10 เฟรม ต่อ ~15 วิ**

## STEP 1 — สร้าง storyboard ใน GPT Image 2

### Multi-panel grid (จุดแข็ง GPT Image 2)
- **ขอ grid วาดทั้งแผ่น pass เดียว** → ทุก panel แชร์ lighting/character/style อัตโนมัติ (ดีกว่าเจน 9 รูปแยก)
- ระบุ geometry ชัด: **"2×3 grid of 6 panels"** (ไม่ใช่ "6 panels") + reading order + gutter
- **load-bearing instruction:** `Every panel features the SAME subject, vary only camera angle`
- 9 shot มาตรฐาน 3×3: wide establishing · medium · extreme close-up · over-the-shoulder · low angle · high angle · profile · action · hero beauty
- **cap ที่ 9 panel** (เกินนี้ quality ตก) · color grade เดียวทั้งแผ่น · panel เสีย → regen โดยใช้ grid เป็น reference
- 📌 GPT Image 2 Thinking mode (paid) = ได้ถึง 8 consistent images/prompt · free Instant mode ไม่รองรับ multi-image

### Product storyboard
- ป้อน product photo เป็น reference → `Keep the product 100% identical in every panel (shape, label, color — do not redesign)` แล้ว vary scene รอบๆ

### Consistency tricks (สำคัญสุด)
- เขียน shot description **ทุกอันเป็นประโยคเดียว ก่อนเจน** frame ไหน
- **copy character description verbatim ทุก frame** — ห้าม paraphrase
- lock lighting ใน shared style clause
- ใช้ **1 reference image เป็น anchor** ของทุก frame downstream
- repeat "lock phrase" ท้าย prompt · เลี่ยง text/label ในภาพ (garbled) หรือขอ caption สั้นมาก

### ตัวอย่าง GPT Image 2 (frame เดี่ยว)
```
Wide cinematic shot of a lone desert nomad walking across orange dunes
toward a distant oasis, golden hour. Anamorphic film look, warm skin tones,
traditional robe, consistent with [shared style clauses].
```

## STEP 2 — ป้อน storyboard เข้า Seedance 2.0
- ใช้ **omni/multimodal reference mode** ไม่ใช่ text-to-video ล้วน
- ป้อน frame เป็น reference image (**≤9 ภาพ**)
- 2 mode: **First/Last Frame** (อัปรูปเดียว = first frame เริ่มแล้ว animate) · **multimodal reference** (หลายภาพ tag role)
- clip **ต่ำกว่า 10s** ลด drift · 720p social / 1080p YouTube

### Seedance prompt เน้น "ขยับยังไง" ไม่ใช่ "ภาพเป็นยังไง"
- storyboard บอกภาพแล้ว → video prompt สั้นได้: `follow exact story/characters/framing shown in @image1, maintain consistency + natural camera movement`
- **ใส่ motivation ทุกครั้งที่กล้องขยับ** (ขยับเพราะอะไร) + timestamp action progression
- แก่น: **GPT Image = ภาพเป็นยังไง · Seedance = ขยับยังไง**

### Multi-shot prompt format
```
[Scene + visual style + consistency note].

Shot 1 (4s) [Image 1]: [frame description + motion]
Shot 2 (6s) [Image 2]: [frame description + motion]

[Transition instruction].
```

### ตัวอย่างเต็ม Seedance (2 ช็อตจาก 2 storyboard frame)
```
Cinematic two-shot golden hour desert sequence, anamorphic film look,
consistent character and lighting throughout.

Shot 1 (4s) [Image 1]: wide establishing — the nomad walks across the
orange dune toward the distant oasis, robe trailing in the wind, slow
steady camera.

Shot 2 (6s) [Image 2]: medium close-up at the oasis — the nomad kneels
and slowly cups water, lifting it toward his face, droplets fall back
into the pool, dust particles drift in the light, gentle slow push-in.

Match-cut transition between shots.
```

## Reference tag syntax (Seedance — lock identity/motion/style)
**Image:**
- `[reference_image: file]` + `[identity_lock]` → คุมหน้า/ตัวให้เหมือนเดิม
- `[reference_image: file]` + `[first_frame_lock]` → เริ่มคลิปด้วยเฟรมนั้นแล้ว animate
- `+ [style_transfer]` (เอาลุค) · `+ [composition_lock]` (คงเลย์เอาต์ เปลี่ยน env)

**Video:** `[reference_video: file]` + `[camera_copy]` (ก๊อปมูฟกล้อง) / `[motion_transfer]` (ย้าย motion subject) / `[sequence_extend]` (ต่อคลิป)

**Audio:** `[reference_audio: file]` + `[beat_sync]` (visual ตรง beat) / `[lip_sync]`

> หมายเหตุ: บางแพลตฟอร์มใช้ `@Image1/@Video1/@Audio1` (ดู [[seedance-ugc-repository]]) บางที่ใช้ `[reference_image:...]` + lock tag — **syntax ต่างตาม host** เช็ก UI ที่ใช้จริง

**หลัก:** เริ่มด้วย reference type เดียว เจน base clip ก่อน → ค่อยเพิ่ม reference อื่นรอบถัดไป (อย่าซัดทุก reference รอบแรก)

## 🧪 เทสจริง @mariaveydiaries (มี vs ไม่มี storyboard)
**conclusion เต็ม:** "storyboard images **do make a difference, even if subtle** — ช่วยดึงวิดีโอเข้าใกล้สิ่งที่ตั้งใจ ด้าน **worldbuilding, color tone, character atmosphere**"
> ผลต่างไม่ดราม่า (subtle) แต่ดีขึ้นจริงด้านโทน/บรรยากาศ/โลก — คุ้มกับการทำ storyboard ก่อน

**prompt จริงที่ใช้ (vlog collage หลายเฟรม — travel UGC):**
```
realistic Italy vlog collage, imperfect smartphone camera feel, tropical humidity haze,
motion blur, authentic travel storytelling, casual handheld framing, realistic textures,
natural ambient light, no studio polish, candid social media realism

Frame Breakdown includes:
- cave restaurant table selfie with sea echoes
- wrong-turn Tuscany road map check
- Amalfi lemon farm walk from behind
- wobbly Venice gondola selfie at dusk
- Cinque Terre terrace lunch candid
- cramped Capri boat selfie with blue glow
- Lake Como dinner toast with crooked framing
- Florence hill windblown selfie with city haze
- Sicilian seafood table moment with messy plates
Final frame: Rome alley bar aperitivo as streetlights flicker, shaky laughing phone capture
```
**สังเกต:** ใช้ "Frame Breakdown" list ต่อเฟรม (ไม่ใช่ timecode) + realism stack แบบ anti-AI (imperfect smartphone, motion blur, no studio polish) — ดู [[ai-influencer-image-prompt]]
> อ่าน X ฟรีด้วย `read_x.py` (ดู [[exa-mcp-setup]])

## เชื่อมกับ Valenshield
pipeline Valenshield (รูปเปิด ChatGPT ต่อคลิป → first frame Seedance) = storyboard workflow นี่เอง — **ทำถูกแล้ว**. อัปเกรดได้: ใช้ GPT Image 2 grid เจน 5 รูปเปิด 5 คลิป **pass เดียว** → สี/หน้า/ชุด consistent กว่าเจนแยกทีละใบ (แก้ปัญหา "ม่วงเฉดเพี้ยนกลางเรื่อง" ใน §5)

## แหล่งที่มา
- [Vicsee — GPT Image 2 + Seedance storyboard workflow](https://vicsee.com/blog/gpt-image-2-seedance-storyboard-workflow)
- [gpt-img2.com — storyboards & grids in GPT Image 2](https://gpt-img2.com/blog/gpt-image-2-storyboards-and-grids)
- [MagicHour — Seedance 2.0 reference tag guide](https://magichour.ai/blog/seedance-20-reference-guide)
- [oimi.ai](https://oimi.ai/en/blog/gpt-image-2-seedance-2-workflow) · [evolink.ai](https://evolink.ai/blog/gpt-image-2-with-seedance-2-0-workflow-2026) · [nemovideo.com](https://www.nemovideo.com/blog/gpt-image-2-storyboard)
- เทสจริง: [@mariaveydiaries X post](https://x.com/mariaveydiaries/status/2064565749096800720) (มี vs ไม่มี storyboard)
