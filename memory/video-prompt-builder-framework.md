---
name: video-prompt-builder-framework
description: "4-section structured framework for planning whole Seedance video ads (energy arc, effects map) — planning layer, not per-clip"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Video Prompt Builder — 4-Section Framework (ชั้นวางแผนทั้งโฆษณา)

> มาจาก Claude Code skill `video-prompt-builder` (ลงที่ `~/.claude/skills/video-prompt-builder/`, auto-trigger เมื่อพูดถึง Seedance/shot list/brand film)
> reference = **Hoka athletic brand film 21s** (genre เดียวกับ [[valenshield-nurse-ad-project]])
> **ใช้ชั้นวางแผน/CapCut edit — ไม่ใช่ per-clip Seedance prompt** (per-clip เขียน simple ดู [[seedance-knowledge]]). effect ส่วนใหญ่ในนี้เป็น edit ไม่ใช่ gen

## ⚠️ ขอบเขต
- skill stack effects ต่อ shot (whip pan, mirror, stroboscopic clone, bloom, frame rotation) = **CapCut effect** ไม่ใช่สิ่ง Seedance gen
- ขัดกฎ "1 prompt = 1 คลิป simple" → **อย่าเอา output ไป Seedance ตรงๆ** ใช้วาง energy arc + effect map + shot list ของทั้งเรื่อง

## Output 4 ส่วน (เรียงเป๊ะ ห้ามข้าม)

### 1. Shot-by-shot Effects Timeline
ต่อ shot:
```
SHOT [N] ([timestamp]) — [ชื่อ shot]
• EFFECT: [primary] + [secondary ถ้า stack]
• [เกิดอะไรทางภาพ]
• [camera: angle/movement/lens]
• [speed/timing — ระบุ % เช่น "20-25% speed"]
• [exit ยังไง → next entry ยังไง = transition]
```
- shot ละ 1–4s · ตั้งชื่อ effect เป๊ะ ("speed ramp (deceleration)" ไม่ใช่ "speed ramp")
- callout shot เด่น = **"SIGNATURE VISUAL EFFECT"**
- บรรยาย "visual result" ไม่ใช่ software ("frame scales inward rapidly" ไม่ใช่ "keyframe scale in AE")

### 2. Master Effects Inventory
list effect ทั้งหมด: ชื่อ · ใช้กี่ครั้ง (used 3x) · shot ไหนบ้าง · บทบาท 1 บรรทัด. group เป็นหมวด (speed / camera / digital / transition / optical)

### 3. Effects Density Map
แบ่ง 3–6s ต่อช่วง rate:
- **HIGH** = 4+ effect stack / rapid-fire
- **MEDIUM** = 2–3 effect
- **LOW** = 1 effect / clean
```
[timestamp] = [LEVEL] ([effects] — [count] effects in [duration])
```

### 4. Energy Arc (3-act)
- **Act 1** opening — ดึงสายตายังไง
- **Act 2** middle — develop + signature moment
- **Act 3** resolution — energy ลงจบยังไง
(ปรับจำนวน act ตามความยาว: 5s = 2 beat, 30s = 4)

## หลักสร้าง (creative principles)
1. **Contrast = impact** — สลับ high/low density. slow-mo หลัง speed ramp กระแทกกว่า ramp ติดกัน 2 อัน
2. **Signature moment** — ทุกวิดีโอต้องมี hero effect 1 อัน distinctive จดจำได้ callout ชัด
3. **Transitions are shots** — whip pan / bloom flash / motion blur smear = creative moment ไม่ใช่ตัวเชื่อมทิ้งๆ
4. **Specificity** — "rotates clockwise ~15-20°" > "tilts" · "~20-25% speed" > "slow motion"
5. **Energy must resolve** — เปิดแรงแค่ไหน ตอนจบต้อง land ตั้งใจ ไม่ใช่งบ effect หมด

## Duration calibration
- 5–10s: 4–7 shots, 1 signature
- 10–20s: 8–14 shots, 1–2 signature
- 20–30s: 12–20 shots, full 3-act, 2–3 signature
- default ถ้าไม่ระบุ = 15–20s

## Hoka reference — เทคนิคที่ยกมาใช้ได้ (athletic brand film 21s)
genre เดียวกับ Valenshield. shot เด่น:
- speed ramp (deceleration) + heavy motion blur เปิด explosive
- vertical mirror/symmetry (kaleidoscope)
- white bloom flash entry + digital zoom scale-in + camera shake (3 stack = จุดแรงสุด)
- speed ramp (acceleration) จาก slow→normal "organic power building"
- whip pan exit = transition แทน cut
- slow-mo 20-25% เน้น muscle tension
- **stroboscopic clone** (8+ ตัว ghosting opacity ไล่) = SIGNATURE
- digital zoom "pump" + jitter ทำ shot นิ่งให้มีพลัง
- rack focus (optical) · foot impact slow-mo 15-20% · frame rotation 15-20° · zoom scale-out จบ aspirational
- จบ: fade → brand card/logo → product macro · "effects energy resolved completely"

## ใช้กับ Valenshield
รัน format นี้กับ 5 คลิป → ได้ **master 20s timeline**: energy arc (hook น้ำ → feature → split leap signature → brand) + density map + CapCut effect plan (speed ramp/whip/beat sync). per-clip ยังเขียน simple แยก. ดู [[valenshield-nurse-ad-project]]
