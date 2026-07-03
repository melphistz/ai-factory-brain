---
name: valenshield-walkingpad-tifu-vid02
description: "Active — Valenshield nurse vid02: walking-pad + TIFU-flip cute ad (20s 9:16). Storyboard sheet done; next = Seedance animate"
metadata:
  node_type: memory
  type: project
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# Valenshield พยาบาล — vid02 (walking-pad TIFU) 

> แคมเปญที่ 3 ของ Valenshield (คนละ lane กับ [[valenshield-nurse-ad-project]] = editorial ดำ HERO, และ [[valenshield-macro-asmr-ad]] = no-person). อันนี้ = **cute relatable action ฉากขาว/ครีม**.
> ใช้ workflow [[storyboard-gpt-image-to-seedance]] · sheet template [[ugc-storyboard-sheet-template]]. อัปเดต 2 ก.ค. 2026.

## คอนเซปต์
- **20 วิ · 9:16 · ไม่มีเสียงพูด** (เพลง upbeat + SFX เท่านั้น)
- **USP = ผ้าสะท้อนน้ำ (water-repellent)** = กลไกที่ "พลิก TIFU"
- **TIFU-flip narrative:** เวรวุ่น(setup) → ทำน้ำยาหกใส่ตัวเอง = TIFU "จบเห่แน่!" → **น้ำเกาะเม็ด/กลิ้งหลุด = USP reveal** → ปาดแห้ง → ผ้าสะท้อนน้ำของจริง → มั่นใจ → hero+โลโก้. (TIFU ปกติจบหายนะ แต่สินค้าเซฟไว้)
- **ฟอร์แมต walking-pad:** เดินอยู่กับที่บนลู่วิ่งเล็กกลางเฟรม กล้องนิ่งล็อก, สถานการณ์ซ้อนบนการเดิน → consistency สูง + through-line + โชว์ผ้าเคลื่อนไหว. อ้างอิงฟีล UNIQLO AIRism (ref: `/Volumes/WONYOUNG/Dokkeaw/ref/03.mp4`) แต่ **ไม่ lip-sync** (action-focus)

## ตัวละคร (เปลี่ยนจากโน้ตเก่า!)
- **นางแบบใหม่:** char sheet 4 มุม `/Volumes/WONYOUNG/Dokkeaw/Generated Image July 02, 2026 - 5_49PM.jpg` (Front/3-4/Back/Half-body) — ผมสั้นบ๊อบสีดำ~น้ำตาลเข้ม, ชุดลาเวนเดอร์เดิม. **ไม่ใช่** `Outfit01-1.jpg` (คนเก่า)
- ชุด = ลาเวนเดอร์อ่อน notch-lapel แขนสั้น กระดุมเงิน 4 กระเป๋าปะ 2 กางเกงขาตรง sneakers ขาว

## 9 beat (grid 3×3, panel 9:16)
1 รีบดูนาฬิกา ถือแฟ้ม · 2 เช็กคนไข้(clipboard) · 3 ถือถาดมีขวดน้ำยาเหลือง · 4 **TIFU! ทำถาดเอียง น้ำยาหกใส่อกตัวเอง** · 5 [มาโครบนเสื้อ] น้ำเกาะเม็ด · 6 [มาโครบนเสื้อ] มือปาดน้ำกลิ้งหลุด ผ้าแห้ง (คัตเด็ด) · 7 เงยหน้าทึ่งยิ้ม · 8 เดินมั่นใจ ชี้ชุด+ถือแฟ้ม · 9 hero หน้าตรง→โลโก้
- ของเหลว = **เหลืองอำพัน (betadine) ห้ามแดง** กัน FB; คำ "เลือด/สารคัดหลั่ง" อยู่ใน caption
- caption TIFU tone: "เวรนี้เอาแน่ 💀" / "หกใส่ตัวเองซะงั้น 😱" / "เดี๋ยว… น้ำกลิ้งเฉย?!" / "ผ้าสะท้อนน้ำ ของจริง!"

## บทเรียน grid (GPT Image 2) — สำคัญ
- **ทิศทาง 3/4 prompt text ล็อกยาก** — "left shoulder toward camera" กำกวม model พลิกช่อง. **แก้: anchor ชัด "faces & walks toward the LEFT edge, nose points left" + ย้ำต่อช่อง "facing left" + negative "do not flip to right" + ขึ้น session GPT ใหม่** → ได้ทิศตรงกันจริง
- fallback ถ้ายังพลิก = **flip แนวนอนตอน edit** (ชุดเกือบสมมาตร พลิกไม่เพี้ยน)
- **เฉดม่วงเพี้ยนระหว่างช็อต** (แถบเต็มตัวออกขาว) → gen รอบใหม่ให้ "EXACT same lavender shade all panels" คุมได้
- **macro ต้องระบุ "fabric ON HER TUNIC + เห็นกระดุม/ตะเข็บ"** ไม่งั้นดูเป็นผ้าเปล่าลอย
- **เท้า+ลู่ = จุดเสี่ยง** → beat เต็มตัวเช็กเท้าอยู่บนสายพาน

## วิธีทำ storyboard SHEET ให้ลูกค้า (reusable pipeline)
**toolkit ส่วนกลาง (ไม่อยู่ในโฟลเดอร์ลูกค้า):** `/Volumes/PS Catches/storyboard-toolkit/` = `build_sheet.py` + `STORYBOARD-GRID-TEMPLATE.md`
สคริปต์ `build_sheet.py` (PIL + Chrome headless)
1. slice grid เป็น panel (NCOLS×NROWS, มี FLIP set กันช่องหันผิด)
2. HTML sheet: header+chips, 3 part bar, การ์ด (timecode/ชื่อ/desc/caption กล่องเหลือง), endbanner โลโก้, footer โปรดักชัน+เสียง — ฟอนต์ไทย Thonburi
3. render: `Google Chrome --headless=new --screenshot --force-device-scale-factor=2 --window-size=1680,5400` (สูงพอ 3×3 9:16 ไม่งั้นตัด)
4. PIL trim ขอบขาว → PNG
- output: `/Volumes/WONYOUNG/Dokkeaw/vid02/storyboard-valenshield-nurse.png`

## ขั้นต่อไป
- [ ] จัดสี/audit keyframe → เจน keyframe เต็ม 9:16 ต่อ beat (step 1b ของ [[storyboard-gpt-image-to-seedance]])
- [ ] Seedance animate ทีละ beat (first_frame_lock, clip <4s, prompt motion-only) → เดินต่อเนื่อง+physics splash/wipe
- [ ] CapCut: caption + doodle + เพลง + hard cut โลโก้ (ดอกแก้ว+สโลแกน) · flip คลิปให้ทิศตรงถ้าจำเป็น
