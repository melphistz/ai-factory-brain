# สถาปัตยกรรมใหม่ drama-app — แยก "แนวเล่า" กับ "โลก" เป็น 2 แกน

## 1. หัวใจของไอเดีย (พูดสั้นๆ)

ทุกวันนี้ pack แนวหนึ่งก้อน = "วิธีเล่า + หน้าตาโลก" มัดรวมกัน (revenge ถูกล็อกเป็นโลกคนรวยยุคใหม่ไปแล้ว) พอ Mirko อยากได้ "comedy ในโลกไหนก็ได้" เลยทำไม่ได้ ต้องเขียนใหม่ทั้งก้อน

ทางแก้ = **หั่น pack เป็น 2 กอง แล้วเอามาประกบกันตอนใช้งาน**
- **กอง "แนวเล่า" (genre)** = จังหวะ/ฮุก/บีต/การแสดง/ปมค้าง/ความเร็ว → ไม่ผูกกับโลก (6 แนวเดิม)
- **กอง "โลก" (setting)** = สี/แสง/ของ/ชื่อ/หน้าตานักแสดง → ไม่ผูกกับแนว (9 โลก)

เขียนแค่ **6 + 9 = 15 ก้อน** แต่ผสมกันได้ **54 คู่** — ไม่ต้องเขียน 54 ก้อน

แอปมี 2 ช่องเลือก (แนว × โลก) → หยิบ 2 ก้อนมาแปะประกบ ยิงเข้า endpoint 01/02 เหมือนเดิม

> **กติกาเหล็กที่ไม่แตะ:** ทั้ง 2 ก้อนเป็นแค่ "ชั้นรสชาติ" ห้ามไปทับ schema §1 / budget §3 / หลักการร่วม §6 · ไม่เลือกอะไรเลย = แอปทำงานเหมือนเดิมเป๊ะทุกตัวอักษร

---

## 2. ใครถืออะไร (แบ่งราย section)

pack เดิมมี 8 หัวข้อ (a–h) เราแยกเป็น 2 ชุดตามเจ้าของจริง:

| หัวข้อเดิม | เจ้าของใหม่ | หมายเหตุ |
|---|---|---|
| a) HOOK WEIGHTING | **แยกครึ่ง** (ดูข้อ 3) | ตารางน้ำหนัก+ตรรกะ = genre · แต่ "ภาพเปิดแบบขัดสถานะ" = โลกช่วยเติม |
| b) BEAT FLAVOR | **genre** | แต่ "ของ/prop" ในบีตถอดชื่อออก ให้โลกเติม (ดู S6) |
| c) ACTING GRAMMAR | **genre ทั้งดุ้น** | ยกมาเหมือนเดิม (verbatim) |
| d) VISUAL & LIGHTING | **แยกเป็น 2** | จังหวะแสงตามบีต (flip/มืดลง/แบน) = genre แต่เขียนเป็น **"คำอธิบายหน้าที่แสง"** ไม่ใช่ชื่อหลอด · ส่วนหลอดไฟ/วัสดุ/สีพื้น/หน้าตานักแสดง = โลก |
| e) DIRECTOR PRESETS | **แยกเป็น 2** | มุมกล้อง/การเคลื่อน/กฎใส่ชื่อผู้กำกับ = genre · palette + ชื่อผู้กำกับที่ให้ "ลุคของโลก" = โลก |
| f) CLIFFHANGER | **genre** | ถอดชื่อ prop ออก ให้โลกเติม |
| g) AI-GEN PITFALLS | **แยก 3 ทาง** (ดูข้อ 7) | สากล→§6 · เรื่องคน/วัสดุ/ยุค→โลก · เรื่องการแสดง/จังหวะ→genre |
| h) PACING | **genre ทั้งดุ้น** | ยกมาเหมือนเดิม |

### แกน GENRE ถือ (ไฟล์เดิม 09 ผอมลง)
a-ครึ่ง (ตารางน้ำหนักฮุก + นิยาม slot ฮุก) · b (บีต + หน้าที่ของ plot-device) · c (การแสดง เต็ม) · d-ครึ่ง (แสงเป็น "คำหน้าที่" ล้วน ห้ามชื่อหลอด) · e-ครึ่ง (กล้อง/การเคลื่อน + กฎ 🟢/🔴 ใส่ชื่อผู้กำกับ) · f (ปมค้าง หน้าที่) · g-ที่เหลือเฉพาะแนว · h (ความเร็ว เต็ม)

### แกน SETTING ถือ (ไฟล์ใหม่ 10)
S1 สีพื้น+อารมณ์ · S2 หลอดไฟ/วัสดุ/พื้นสะท้อน · S3 หน้าตานักแสดงประจำโลก · S4 palette+ชื่อผู้กำกับที่ให้ลุค · S5 นิยาม "อะไรคือของแปลกที่/ขัดสถานะ" ในโลกนี้ · S6 ของ+ชื่อ+บริบท · S7 pitfalls เรื่องคน/วัสดุ/ยุค

---

## 3. จุดยากที่ 1 — ภาพเปิด (hook) ใครเป็นเจ้าของ [แก้ blocking #2]

**ผิดถ้าโยน "ภาพเปิดขัดสถานะ" ทั้งหมดไปให้โลก** เพราะภาพเปิดมี 2 พันธุ์คนละเจ้าของ:

**พันธุ์ A — ขัดใจ/ขัดความสัมพันธ์ (genre เป็นเจ้าของ ภาพอยู่ในก้อน genre เลย):**
- romance: "เจ้าสาวเต็มยศยืนคนเดียว"
- family: "โต๊ะครบแต่เก้าอี้ว่าง 1 ตัว / จานเกินมา 1 ใบ"
- thriller: "เฟรมปกติที่มีสิ่งผิดที่ 1 จุด"
→ ความหมายมาจาก "ความสัมพันธ์ระหว่างคน" ไม่ขึ้นกับโลก → **เก็บภาพจริงไว้ในก้อน genre** (ไม่งั้น romance ที่ default โลก real-urban จะสร้าง "เจ้าสาวยืนคนเดียว" กลับมาไม่ได้ = ภาพเซ็นเนเจอร์หาย)

**พันธุ์ B — ขัดสถานะทางสังคม (โลกเป็นเจ้าของผ่าน S5):**
- revenge: "คนชุดโทรมกลางงานหรู" → อะไรคือ "ชุดโทรม" อะไรคือ "งานหรู" = แล้วแต่โลก
- comedy: "แต่งตัวไม่เข้ากับที่" → "ที่" นิยามความผิด = แล้วแต่โลก

**วิธีเขียนให้ไม่รั่ว = ทำ S5/S6 เป็น "พจนานุกรมแบบมีช่อง (slot-keyed)" ไม่ใช่ลิสต์ลอยๆ:**
- genre ก้อน a **ตั้งชื่อช่อง (slot)** ว่าฮุกตัวเองต้องการอะไร เช่น revenge ประกาศ slot `status-contradiction`, period-anachronism ฯลฯ
- โลกเติม "ผิว" **เฉพาะช่องที่ genre เรียกเท่านั้น** เช่น S5 ของ high-society ตอบ slot `status-contradiction` = "คนชุดพนักงานยืนกลางแขก VIP"
- ผลลัพธ์: thriller ที่ใช้โลก real-urban **จะไม่ดูด prop ของ romance เข้ามามั่ว** เพราะ thriller ไม่ได้เรียก slot ของ romance → โลกไม่จ่ายผิวให้ช่องที่ไม่มีคนเรียก

พูดเป็นสูตร: **genre นิยามช่อง / setting ทาผิวช่อง** (genre-defines-slot, setting-skins-slot)

---

## 4. จุดยากที่ 2 — เวลา genre กับ setting พูดเรื่องเดียวกันแล้วชน [แก้ blocking #3, minor #8]

### หลักคิด: "โลกถือของฐาน · แนวถือการปรับเทียบกับฐาน"
- **โลก (setting)** บอกว่า "ในโลกนี้แหล่งแสง/วัสดุจริงคืออะไร" (หลอดฟลูออเรสเซนต์ / หลอดไส้ / คริสตัลเรืองแสง / คบเพลิง+เทียน)
- **แนว (genre)** บอกว่า "แสงต้องทำหน้าที่อะไรตามบีต" เป็น **คำหน้าที่ล้วน** (แข็งกดจากบน→พลิกอุ่น+ขอบสว่างตอนเผย / แสงถอยหนีบีบพื้นที่ตอนขู่ / แบนเรียบรับหน้านิ่ง) **ห้ามพิมพ์ชื่อหลอดในก้อน genre เด็ดขาด**

พูดคนละชั้น = ส่วนใหญ่ไม่ชนตั้งแต่ต้น

### บันได 4 ขั้น (ชั้นบนชนะชั้นล่างเสมอ — เขียนลง §6)
1. **HARD** — schema §1 / budget §3 / หลักการร่วม §6 ชนะทุกอย่าง (2 ก้อนเป็นแค่รสชาติ)
2. **GENRE หน้าที่** ชนะ setting — พฤติกรรมแสง/สี/จังหวะตามบีตเป็นของแนว
3. **SETTING หลอด/วัสดุ/สีพื้น** ชนะ genre — โลกจ่ายว่าแหล่งแสงจริงคืออะไร
4. **GENRE plot-device (หน้าที่ของกลไก)** ชนะ · **SETTING ผิวของ prop** ชนะ — "ผลตรวจสายเลือด = กลไกพลิกสถานะ" เป็นของแนว ห้ามทิ้ง · แต่หน้าตาของมัน (ตราเทพ/ม้วนสาสน์) เป็นของโลก

### กรณีชนตรงๆ + ทางออก 2 ชั้น (นี่คือจุดที่ verify เตือน)
ตัวอย่าง: revenge สั่งแสง humiliation แข็งเย็นแบบสถาบัน แต่โลก fantasy ไม่มีหลอดไฟเลย

**ทางออก A (บังคับทุกโลก) — "หลอดสำรองแข็ง":** ทุกโลกใน S2 **ต้องมีแหล่งแสงแข็ง/ไม่สวยอย่างน้อย 1 ตัวเสมอ** ให้ genre function ไปเกาะได้:
- high-society → ฟลูออเรสเซนต์ทางเดินหลังบ้าน/ห้องครัวโรงแรม
- fantasy → แสงคริสตัลจ้าเย็น (cold crystal-glare)
- period → แดดเที่ยงแข็ง / คบเพลิงเปลือย
→ ดังนั้น "harsh flat unflattering humiliation key → พลิกอุ่น+ขอบสว่าง" มีหลอดจริงในโลกให้เกาะเสมอ · **ต้อง verify เฉพาะจุด: revenge × high-society ตอน humiliation ต้องยังอ่านว่าเย็น/สถาบัน**

**ทางออก B (ทางหนีเฉพาะกรณี) — แท็ก `genre-fixture-override`:** ถ้าหลอดนั้นเป็นหัวใจดราม่าของบีตจริง (ไม่ใช่แค่ของประจำโลก) genre พิมพ์ชื่อหลอดได้ โดยแท็กว่า override → บันไดถือเป็น MODULATION: โลก realize ให้ถ้าเป็นไปได้ ถ้าไม่ได้ genre ชนะ

### ความจริงเรื่อง "deterministic" [แก้ minor #8]
อย่าโฆษณาเกินจริงว่า "ลำดับ inject รับประกันอัตโนมัติ" — การ inject คือ **เอา 2 ก้อนมาต่อกันเฉยๆ ไม่มีตัวไหนไป merge คำ** ความสะอาดมาจาก 2 อย่างจริงๆ:
1. **วินัยตอนเขียน + lint:** ก้อน genre ต้องมี **ศูนย์ชื่อหลอด/ศูนย์ชื่อวัสดุ** (มีแต่คำหน้าที่) — ต้องมีสคริปต์ตรวจ (grep คำต้องห้าม) เป็น gate ตอน build pack
2. LLM ที่ปลายทางเป็นคนรวมคำหน้าที่ (genre) + หลอด (setting) เข้าด้วยกันเอง

พูดตรงๆ ในเอกสาร: **ลำดับ inject อย่างเดียวไม่ได้ทำ tie-break — lint + LLM ต่างหากที่ทำ**

---

## 5. แกน SETTING — มีโลกอะไรบ้าง (9 โลก) [แก้ minor #4]

แบ่ง 2 กลุ่ม:

**กลุ่ม A — 6 โลก "แกะจากของเดิม" (carve ตรงจาก d/e ของ 6 pack → เป็นฐานทดสอบว่าของไม่หาย):**
1. `real-urban` (default ของ romance) — อพาร์ตเมนต์/ถนนเปียก/นีออน/ฝนบนกระจก
2. `real-home` (default ของ family) — ครัว/โต๊ะอาหาร/แสงหลอดไส้ประตู/ไอร้อน
3. `real-minimal` (default ของ comedy) — ขาวโล่งแดดส่อง/สีซีดจาง/แสงแบน
4. `real-dim` (default ของ thriller-horror) — หลอดไส้เปลือย/สีเย็นเดี่ยว/ทางเดินมืด
5. `real-gritty` (default ของ action) — ฝุ่นสีอำพัน/ดาดฟ้าฝนโคลน/แสงจริงอลังการ
6. `high-society` (default ของ revenge) — หินอ่อน/กระจก/งานกาลา/หน้านักแสดง idol-glam

**กลุ่ม B — 3 โลก "เขียนใหม่สด" (ไม่มี default ผูก):**
7. `rural-poor` (คนจน) — หน้าคนสมจริงมีร่องรอย/แสงธรรมชาติ/ของเรียบ
8. `fantasy` (แฟนตาซี) — **2 register ในโลกเดียว** (แก้ minor #4):
   - **celestial** (สว่างเทพ) — คริสตัลเรืองแสง/ตราเทพ
   - **gothic** (มืดสยอง) — แสงจันทร์/เลือด/หลอดโกธิค → รองรับ werewolf(#8)/vampire(#15)/xianxia palace มืด
   - S1/S2 แยก 2 ชุดชัดในไฟล์เดียว
9. `period` (ย้อนยุค) — ตะเกียง/เทียน/ผ้าไทย/ชื่อโบราณ

### ทำไม 9 ไม่ใช่ 8
- แยก `rural-poor` ออกจาก `real-gritty` เพราะ Mirko ระบุ "คนจน" เป็นตัวเลือกโลกเอง · และ "gritty แบบ action" (ฝุ่น/อลังการ/ดาดฟ้า) ≠ "จนจริง" → ถ้ายุบรวม การ reconstruct ของ action จะเพี้ยน หรือ rural-poor จะแบก flavor อลังการที่ไม่ควรมี
- แยก `real-dim` เป็นโลกจริง ไม่ใช่แค่ "โหมดกลางคืน" → เปิดทาง horror×real-urban (สยองในเมือง) และ comedy×high-society (ตลกคนรวย) ได้

### UX — ช่อง dropdown จัด 5 หมวด (ซ่อน sub) ตรงหัว Mirko
- **สมจริง** ▸ {real-urban / real-home / real-minimal / real-dim / real-gritty}
- **คนรวย** ▸ high-society
- **คนจน** ▸ rural-poor
- **แฟนตาซี** ▸ fantasy (เลือก register สว่าง/มืดได้)
- **ย้อนยุค** ▸ period

### แผนที่ default (backward-compat)
romance→real-urban · comedy→real-minimal · thriller-horror→real-dim · action→real-gritty · family→real-home · revenge→high-society

---

## 6. หน้าตาไฟล์ setting pack (7 หัวข้อ S1–S7)

โครงคนละชุดกับ genre (มีเฉพาะที่โลกเป็นเจ้าของ ไม่มี hook-table/beat/acting/pacing) budget **≤3,500 chars/โลก**

| หัวข้อ | ถืออะไร |
|---|---|
| **S1** สีพื้น+อารมณ์ | คำภาพ EN สีเกรดฐานของโลก (luxury sheen / golden haze / blue-grey mist / crystalline glow) = ครึ่ง "base" ของ d เดิม |
| **S2** หลอด·วัสดุ·พื้นสะท้อน | แหล่งแสงที่โลก "มีจริง" + วัสดุ + พื้นสะท้อน · physical ล้วน · **ต้องมีหลอดแข็ง/ไม่สวยอย่างน้อย 1 ตัว** (ข้อ 4) · **[แก้ minor #5] real-dim S2 ต้องมีกฎ "ห้ามสั่งดำสนิท ล็อกแหล่งแสงจริง 1 จุด ให้ความมืด=falloff"** (ย้ายมาจาก thriller g เพราะเป็นข้อเท็จจริงเรื่องหลอด/วัสดุ ไม่ใช่จังหวะ) — cross-ref จาก §6 |
| **S3** หน้านักแสดงประจำโลก | beauty-tier + หน้าตา (idol-glam vs สมจริงมีร่องรอย) · **เฉพาะ house-style** · กฎ "ตัวร้ายห้ามหน้าน่าเกลียด" เป็นของ genre revenge ไม่ใช่ที่นี่ |
| **S4** palette+ชื่อผู้กำกับให้ลุค | คำ palette/ลุค + ชื่อผู้กำกับที่ให้ "หน้าตาโลก" (neon-WKW/luxury-interior/cold-sterile/lush-nature) = ครึ่ง "look" ของ e เดิม |
| **S5** พจนานุกรม "ของแปลกที่/ขัดสถานะ" | **slot-keyed** (ข้อ 3) — ตอบเฉพาะช่องที่ genre เรียก |
| **S6** ของ·ชื่อ·บริบท | **slot-keyed** ผิวของ prop ที่เสียบเข้ากลไก b/f (identity-proof-token → modern: ผลตรวจสายเลือด / fantasy: ตราเทพ / period: ม้วนสาสน์) + ทะเบียนชื่อตัวละคร/สถานที่ |
| **S7** pitfalls ของโลก | เรื่องประชากร/วัสดุ/ยุค (ฝูงคน deform / อายุเพี้ยนข้ามรุ่น / อาหารบนโต๊ะเปลี่ยนเอง / golden-hour ต่อเนื่อง / ของผิดยุค / VFX แฟนตาซีไม่คงเส้น) |

หัวทุก setting pack ต้องมีบรรทัด guard เหมือน genre: *"flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6"* · หัวไฟล์ 10 เก็บแผนที่ default + วิธี inject (setting ก่อน → genre ทับ)

### เพดานล้นทำไง [แก้ minor #10]
โลกเขียนใหม่ (fantasy/period/rural-poor) เสี่ยงเกิน 3,500 เพราะ world-vocab เยอะ → fallback:
1. ตอน STEP 7 **นับตัวอักษรจริงก่อน ship**
2. ถ้าเกิน: ตัด S6 (ของ/ชื่อ) ก่อนเป็นอันดับแรก
3. fantasy ที่มี 2 register อาจต้องระวังสุด — ถ้าล้น แยกเป็น 2 entry (fantasy-celestial / fantasy-gothic) แทนยัดไฟล์เดียว

---

## 7. §6 หลักการร่วม — ขยาย 5→7 ข้อ

### +ข้อ 7 LAYER PRIORITY
เขียนบันได 4 ขั้น + สูตร "GENRE@FUNCTION / SETTING@FIXTURE" ตามข้อ 4 ทั้งหมด

### +ข้อ 6 UNIVERSAL AI-GEN PITFALLS — แต่ต้อง audit ก่อนยก [แก้ blocking #7]
**อันตราย:** §6 มีผลกับ **ทุก endpoint แบบไม่มีเงื่อนไข** (เป็นชั้น HARD) แต่วันนี้ pitfalls พวกนี้มีผล **เฉพาะตอน inject pack** → ถ้ายกของที่ "เดิมอยู่ใน pack เท่านั้น" ขึ้นมา §6 = **เปลี่ยน baseline ตอนไม่ส่ง pack** = ผิดกติกาเหล็ก "ไม่ส่งอะไร = เหมือนเดิมเป๊ะ"

**เงื่อนไขบังคับก่อนยก (เพิ่มเป็น pre-condition ของ STEP 5):**
- ไล่เช็ครายตัวเทียบ base intel-pack **04/05/06** ว่าข้อนั้น "บังคับอยู่แล้วที่ baseline" หรือไม่
- **ยกได้เฉพาะข้อที่พิสูจน์ว่ามีอยู่แล้วที่ baseline** (= แค่รวม/ลดซ้ำ ไม่ใช่เลื่อนขั้น)
- ข้อไหน "อยู่ใน pack เท่านั้น" **ห้ามยก** → คงไว้ใน genre g หรือ setting S7 เพื่อให้ baseline ไม่เปลี่ยนแม้แต่ตัวอักษรเดียว

รายการที่จะพิจารณายก (ต้องผ่าน audit ก่อน): two-body impact-split · หลีก text-glyph · 'fast'→physics-jitter · deadpan-hold drift · positive-lock live-action

---

## 8. จุดยากที่ 3 — g pitfalls แบ่งยังไงไม่ให้ตกหล่น [แก้ minor #11]

g มีข้อก้ำกึ่งเยอะ ต้องมี **rubric ตัดสินเจ้าของ** (ติดแท็กตอน review STEP 4/5):

| ลักษณะข้อ | เจ้าของ |
|---|---|
| บังคับเรื่องหลอด/แหล่งแสงจริง (เช่น "ห้ามดำสนิท ล็อก 1 แหล่ง") | **setting** (S2/S7) |
| มุมกล้อง/จังหวะเวลา/ความหนาบีต | **genre** |
| คน/วัสดุ deform (ฝูงคน/อายุ/โต๊ะอาหาร/golden-hour) | **setting** (S7) |
| การแสดงเกิน/หน้า drift/deadpan | **genre** |
| สากลจริง (two-body/text-glyph) + ผ่าน audit ข้อ 7 | **§6** |

---

## 9. การทดสอบว่า "ของไม่หาย" — นิยามใหม่ [แก้ blocking #1 + #6]

**ปัญหาเดิม (verify จับถูก):** แผนบอกว่า gate คือ `composed = pack เดิม แบบ byte-equivalent` — **เป็นไปไม่ได้โดยธรรมชาติ** เพราะ STEP 2 เขียนคำใหม่ (หลอด→คำหน้าที่), STEP 1 ทำ hook เป็น slot, STEP 4 ถอดชื่อ prop · การต่อ 2 ก้อนที่มีหัว S1–S7/a–h ยังไงก็ไม่มีวันเท่าก้อนเดียวเดิม → gate ผ่านไม่ได้ตลอดกาล = ไม่มี gate จริง

**นิยามใหม่ = "ข้อมูลไม่หาย / ความหมายเท่าเดิม" (semantic) ตรวจโดยคน+LLM ไม่ใช่ byte:**

Gate ผ่านเมื่อ (เช็คลิสต์ต่อแนว G, ใช้ default[G]):
- (a) **จังหวะ 5 บีตเหมือนเดิม** — hook/setup/conflict/twist/cliffhanger ทำงานเท่าเดิม
- (b) **หน้าที่แสงเดิมยังอยู่ แต่ realize ผ่านหลอดของโลก** — เช่น humiliation ยังเย็น/สถาบัน, reveal ยังพลิกอุ่น+ขอบสว่าง
- (c) **prop เดิมยังอยู่ผ่าน slot-skin** — ทุก prop noun เดิมของ pack ต้องหาเจอที่ใดที่หนึ่ง (setting ∪ genre ∪ §6)
- (d) **สัดส่วน % pacing เท่าเดิม**
- **เช็คลิสต์ตัวจริง:** "ทุกชื่อหลอด + ทุกคำหน้าที่แสง/บีต จาก d/e ของ pack เดิม ต้องรอดอยู่ที่ใดที่หนึ่งในซองรวม" — คนรีวิวยืนยันว่าแสงที่ประกอบกลับอ่านเท่ากัน

**เก็บ byte-diff ไว้เฉพาะ 2 section ที่ยกมา verbatim จริง (c การแสดง, h pacing)** — 2 อันนี้ต้องเท่าเป๊ะระดับตัวอักษร ถ้าเพี้ยน = ผิด

พูดตรงในเอกสาร: **byte-equivalent เป็นไปไม่ได้โดยโครงสร้าง (STEP 2 เขียนคำใหม่) — ลบคำว่า byte-equivalent ออกจาก STEP 6**

---

## 10. ลุคของโลกจะถึงภาพจริงไหม (endpoint 05/06) [แก้ minor #9]

รอบนี้ inject เข้าแค่ **01/02 (ขั้นวางแผนข้อความ)** — แต่ตัวที่ render ลุคจริงคือ 05 (keyframe) / 06 (video) ซึ่งรับลุคผ่าน `style_stack` + shot-spec ที่ 01/02/04 ปั้นออกมาเท่านั้น → เสี่ยงลุคโลก (S1/S4) หายระหว่างทาง ทั้งที่เราลงทุน decompose e หนักเพราะอยากได้ "comedy×fantasy ดูแฟนตาซีจริง"

**Guard บังคับ (ทางเบา เลือกทำรอบนี้):** เพิ่มกฎให้ **endpoint 01 ต้องพับคำจาก S1 + S4 ของโลกเข้า `style_stack` ที่มันสร้าง แบบ verbatim** → ลุคโลกติดไปกับ style_stack ที่ทุก endpoint ปลายน้ำใช้ต่อ = ไม่หาย

**ทางหนัก (open question ให้ Mirko เลือก):** ขยาย inject setting look (S1/S2/S4) เข้า 05 และ genre camera-grammar เข้า 04/06 โดยตรง — แพงกว่าแต่ลุคคมกว่า

---

## 11. สรุปการแก้ contracts (00-contracts.md)

**§1.1 SeriesBible** — เพิ่ม field `setting` (optional, enum 9 ค่า ขนาน `genre` เป๊ะ) + ตารางแผนที่ default (6 แถว) · 4 กรณี:
- (ก) ไม่ส่งทั้ง genre+setting = pipeline เดิมทุกตัวอักษร
- (ข) ส่ง genre ไม่ส่ง setting = เติม default_setting อัตโนมัติ แล้ว inject 2 ก้อน (= reconstruct พฤติกรรมเดิม, override ได้)
- (ค) ส่ง setting ไม่ส่ง genre = inject setting เดี่ยว (โลกจ่ายลุค การเล่ากลางเดิม)
- (ง) setting นอก enum = ใช้ default_setting ของ genre ที่เลือก

**§1.7 PromptEnvelope** — เพิ่ม field `setting_pack` (optional string ≤3,500, ถ้อยคำ guard เดียวกับ genre_pack) + ประกาศ INJECT ORDER: setting ก่อน (BASE) → genre ทับ (MODULATION); ทั้งคู่หลัง bible_digest ก่อน shot_spec; รอบนี้ inject 01/02 เท่านั้น

**§3 budget** — +แถว "setting pack ≤3,500 chars/โลก" + note "genre+setting รวม ≤~8,000 เข้าแค่ 01/02 ห้ามเบียด prompt cap 3,200/1,800" · genre_pack คง ≤4,500 (จริงจะหดเพราะถอด d/e base ออก)

**§5 hand-off** — +แถว 10 = setting-packs (static reference ไม่ใช่ endpoint) ขนานแถว 09 · แก้ note แถว 09 = "inject 2 ก้อนประกบ order setting→genre"

**§6** — ขยาย 5→7 ข้อ (ข้อ 6 universal pitfalls หลัง audit, ข้อ 7 layer priority) ตามข้อ 4/7 ด้านบน

---

## ขั้นตอน implement (migration steps)
1. STEP 0 — AUDIT §6 ก่อนทุกอย่าง (แก้ blocking #7): ไล่เช็ค two-body / text-glyph / fast-jitter / deadpan-drift / positive-lock ทีละตัวเทียบ base intel-pack 04/05/06 ว่า 'บังคับที่ baseline อยู่แล้วหรือไม่' — ทำ list ว่าตัวไหนยกขึ้น §6 ได้ (มีอยู่แล้ว=แค่ dedup) ตัวไหนห้ามยก (pack-only=ต้องคงใน g/S7). ผลของ step นี้เป็นเงื่อนไขล็อกของ STEP 5. [Opus 4.8 + high]
2. STEP 1 — KEEP→genre (verbatim ที่ทำได้): เก็บใน 09 ผอม = a(ตารางน้ำหนัก+ตรรกะ · เปลี่ยนแถว visual-hook เป็นการประกาศ slot ฮุกตามข้อ 3 · ฮุกพันธุ์ A เก็บภาพไว้ในนี้) · b(5 บีต + หน้าที่ plot-device, แทนชื่อ prop ด้วย generic + ชี้ไป S6) · c(ทั้งดุ้น verbatim) · f(หน้าที่ปมค้าง ลบชื่อ prop) · h(ทั้งดุ้น verbatim). [Opus 4.8 + ultracode]
3. STEP 2 — REFACTOR d (จุดแก้จริงจุดที่ 1): genre เหลือแค่ 'จังหวะแสงตามบีต' แต่ REWRITE ชื่อหลอด→คำหน้าที่ (flip/contrast/receding/flat-even) · ถอด base (สีพื้น→S1, หลอด/วัสดุ/สะท้อน→S2, หน้านักแสดง→S3) ออกไปโลก. รัน lint ยืนยัน genre เหลือ 'ศูนย์ชื่อหลอด'. [Opus 4.8 + ultracode]
4. STEP 3 — DECOMPOSE e (จุดแก้จริงจุดที่ 2, เสี่ยงสุด ทำก่อน net-new): genre เก็บกล้อง/การเคลื่อน/กฎ 🟢🔴 ใส่ชื่อผู้กำกับ · ถอด palette/ลุค + ชื่อผู้กำกับที่ให้ลุค→S4. preset เดิมมัด mood+look แน่น ต้องผ่าตัดทุกตัว. [Opus 4.8 + ultracode + verify]
5. STEP 4 — CARVE→setting + ติดแท็กเจ้าของ g (แก้ minor #11): a visual-hook พันธุ์ B→S5 (slot-keyed) · b&f prop-noun→S6 (slot-keyed) · g เรื่องคน/วัสดุ/ยุค→S7 · thriller 'ห้ามดำสนิท ล็อก 1 แหล่ง'→real-dim S2/S7 (แก้ minor #5). ใช้ rubric ข้อ 8 ติดแท็กทุกข้อก้ำกึ่ง. ก้อน d-base+e-look+S5/S6/S7 = 6 setting anchor แรก (ยกข้อความเดิมเกือบ verbatim). [Opus 4.8 + ultracode]
6. STEP 5 — LIFT→§6 (ทำตามผล STEP 0 เท่านั้น): ยกเฉพาะ pitfalls ที่ audit ยืนยันว่ามีที่ baseline อยู่แล้ว ขึ้น §6 ข้อ 6 · ข้อที่ audit บอก pack-only = คงไว้ใน g/S7. เขียน §6 ข้อ 7 layer-priority (บันได 4 ขั้น + GENRE@FUNCTION/SETTING@FIXTURE). [Opus 4.8 + high]
7. STEP 6 — ACCEPTANCE TEST แบบ SEMANTIC (แก้ blocking #1/#6 — gate ของ 'ของไม่หาย'): ทุกแนว G ประกอบ inject(setting[default[G]]→genre[G]) แล้วเช็คลิสต์ (a)บีตเท่าเดิม (b)หน้าที่แสงเดิม realize ผ่านหลอดโลก (c)ทุก prop noun+ทุกชื่อหลอด+ทุกคำหน้าที่แสงจาก d/e เดิมหาเจอในซองรวม (d)% pacing เท่าเดิม · byte-diff เฉพาะ c/h ที่ยก verbatim · ไม่ผ่าน=migration ยังไม่ผ่าน. ตรวจเน้น revenge×high-society humiliation ต้องยังเย็น/สถาบัน (แก้ blocking #3). [Opus 4.8 + xhigh + verify 2 เลนส์]
8. STEP 7 — AUTHOR NET-NEW 3 โลก (fantasy 2 register / period / rural-poor): เขียนสดตาม S1–S7 · นับตัวอักษรจริงเทียบ ≤3,500 ก่อน ship, เกินให้ตัด S6 ก่อน / แยก fantasy เป็น 2 entry ถ้าล้น (แก้ minor #10) · smoke: pair(revenge, fantasy-celestial)='แก้แค้นในโลกเทพ' อ่านรู้เรื่อง + คำหน้าที่ genre เกาะหลอดใหม่ได้ · ยืนยันทุก S2 มี 'หลอดแข็ง/ไม่สวย' อย่างน้อย 1 (แก้ blocking #3). [Opus 4.8 + ultracode + verify]
9. STEP 8 — WIRE แอป (build/production): 2 dropdown (แนว × โลก UX 5 หมวด) → เลือก genre auto-fill default_setting (override ได้) → อ่าน 2 block → inject order setting→genre เข้า 01/02 · เพิ่ม lint 'genre pack = 0 ชื่อหลอด' เป็น build gate (แก้ minor #8) · เพิ่ม guard '01 พับ S1/S4 เข้า style_stack verbatim' (แก้ minor #9) · แก้ contracts §1.1/§1.7/§3/§5/§6 · copy 09ผอม+10ใหม่+00 เข้า D:\drama-app\prompts\ + rerun build/smoke (ไม่ส่งอะไร=200 เหมือนเดิม). [Sonnet + high + build gate]

---

## Model/effort ต่อขั้น

แบ่งตาม feedback-model-effort-strategy: งานนี้ = intelligence-asset ข้ามหลายไฟล์+สถาปัตยกรรม (asset จริง ไม่ใช่ additive เล็ก) → แกนใช้ Opus 4.8 + ultracode + verify 2 เลนส์ · ส่วน wire แอปเป็น build/production → Sonnet พอ.\n\nต่อขั้น:\n- STEP 0 audit §6 vs base 04/05/06 = Opus 4.8 + high (ตัดสินความถูก baseline, ไม่ต้อง fan-out) — เบา\n- STEP 1 KEEP verbatim = Opus 4.8 + ultracode (แต่ mechanical มาก อาจ Sonnet+high ได้ถ้าอยากประหยัด เพราะแค่ยก+genericize)\n- STEP 2 REFACTOR d (rewrite หลอด→function) = Opus 4.8 + ultracode — จุดแก้จริง ต้องฉลาด\n- STEP 3 DECOMPOSE e = Opus 4.8 + ultracode + verify — เสี่ยงสุด เผา effort จุดนี้คุ้ม\n- STEP 4 CARVE→setting + แท็ก g = Opus 4.8 + ultracode\n- STEP 5 LIFT→§6 = Opus 4.8 + high (ตามผล STEP 0 แล้ว mechanical)\n- STEP 6 ACCEPTANCE TEST = Opus 4.8 + xhigh + verify 2 เลนส์ (fidelity+operability, adversarial) — เป็น fidelity gate ต้อง adversarial จริง\n- STEP 7 AUTHOR net-new 3 โลก = Opus 4.8 + ultracode + verify — creative จากศูนย์ ต้องฉลาดสุด\n- STEP 8 WIRE แอป = Sonnet + high + build/smoke gate — mechanical ตาม spec ชัด\n\nเตือนตาม memory: effort สูง=ช้าลงไม่ใช่เร็ว · ความช้าจริงมาจาก subprocess (npm build/smoke) ไม่ใช่โมเดล · ultracode(กี่คนช่วย) กับ effort(คิดลึกแค่ไหน) คนละสวิตช์ · เผา Opus เฉพาะ STEP 2/3/4/6/7 (จุด asset) ที่เหลือ Sonnet/high คุ้มกว่า.\n\nประเมิน token คร่าว: หนักกว่า 'เติม pack ที่ 6' (858K) เพราะแตะ 6 pack + ไฟล์ใหม่ 10 + contracts 5 section + wire — น่าจะ ~1.2–1.8M ถ้าทำ ultracode workflow เต็ม. แบ่ง 2 รอบได้: รอบ 1 = STEP 0–6 (asset/สถาปัตยกรรม, Opus) ให้ 6 anchor ผ่าน gate ก่อน · รอบ 2 = STEP 7–8 (net-new + wire) หลัง Mirko ดูผลรอบแรก.

---

## setting/โลก ชุดแรกควรเขียนตัวไหน

เขียน 6 โลก 'แกะจากของเดิม' (real-urban/real-home/real-minimal/real-dim/real-gritty/high-society) ก่อนทั้งหมด เพราะมันแค่ carve+regression ไม่ใช่งานสร้างสรรค์ใหม่ — ยกข้อความ d/e เดิมมาเกือบ verbatim แล้วทำ acceptance test (STEP 6) ให้ผ่านทั้ง 6 แนวก่อน = พิสูจน์ว่า 'ของไม่หาย' และ backward-compat จริง ก่อนจะเสี่ยงอะไรใหม่.\n\nในกลุ่ม 6 นี้ ให้เขียน real-dim เป็นตัวที่ระวังพิเศษ (จุดก้ำกึ่งสุด): โลกจ่ายแค่ 'หลอด+สีพื้นมืด+กฎห้ามดำสนิท' — ความรู้สึก dread/แสงถอยหนี เป็นของ genre thriller ห้ามเขียนความมืดซ้ำ 2 ที่. และ high-society ต้องเป็นตัวที่ verify หนักสุด เพราะเป็นคู่ทดสอบ revenge×high-society (humiliation ต้องยังเย็น/สถาบัน) = จุดที่ verify ชี้ว่าเสี่ยง.\n\nพอ 6 anchor ผ่าน gate แล้วค่อย author 3 โลกใหม่ (fantasy/period/rural-poor) — เริ่ม fantasy ก่อน (มี 2 register ต้อง smoke cross-combo กับ revenge = ตรงกับ 17 links teardown ที่เป็นโลกเทพ/มังกร/แวมไพร์) แล้ว period แล้ว rural-poor.\n\nถ้าอยากทำ 'ชิ้นแรกสุดชิ้นเดียว' เพื่อ validate สถาปัตยกรรมก่อนลุยครบ = ทำ high-society ตัวเดียว (carve จาก revenge d/e) + acceptance test revenge×high-society จุดเดียว — เป็น smoke test สถาปัตยกรรมที่ถูกและตรงจุดเสี่ยงที่สุด ก่อน commit เขียนอีก 8 โลก.

---

## คำถามที่ต้องให้ Mirko ตัดสิน

**Q1.** ยืนยันจำนวนโลกก่อนไหม? ผมเสนอ 9 โลก (สมจริง 5 แบบ + คนรวย + คนจน + แฟนตาซี + ย้อนยุค) โดย 'สมจริง' ซอยเป็น 5 ย่อย (เมือง/บ้าน/มินิมอล/มืด/ดิบ) ซ่อนใน dropdown หมวดเดียว — โอเคไหม หรืออยากได้ 'สมจริง' ก้อนเดียวไม่ซอย (จะทำให้ reconstruct ของเดิมเพี้ยนบางแนว)

**Q2.** แฟนตาซีอยากให้เป็นโลกเดียวมี 2 หน้า (สว่างแบบเทพ + มืดแบบผี/มังกร/แวมไพร์) หรือแยกเป็น 2 โลกไปเลย? ที่แกะละครจริง (17 links) มีทั้งเทพสว่างและแวมไพร์/หมาป่ามืด — ผมเสนอรวมเป็นโลกเดียว 2 register แต่ถ้าล้นเพดานตัวอักษรจะแยก

**Q3.** ย้อนยุค = ไทยโบราณ (ตะเกียง/ผ้าไทย/ชื่อไทยโบราณ) เป็น default ใช่ไหม? หรืออยากได้จีนวังหลวง (xianxia) ด้วย — ผมตั้งใจ localize เป็นไทยก่อน ไม่ก๊อป xianxia 1:1 (ตลาดไทย) ยืนยันได้ไหม

**Q4.** รอบนี้เอาลุคของโลกเข้าแค่ขั้นวางแผน (01/02) แล้วให้มันไหลลงภาพผ่าน style_stack (ทางเบา) — หรือยอมลงทุนต่อท่อลุคเข้า endpoint สร้างภาพ 05/06 โดยตรง (คมกว่า แต่งานเยอะกว่า)? ผมแนะทางเบาก่อน

**Q5.** อยากทำ 'ชิ้นทดสอบสถาปัตยกรรม' ก่อนไหม — ทำโลก high-society ตัวเดียว + ทดสอบคู่ revenge×high-society จุดเดียว ให้เห็นว่าแยก 2 แกนแล้วของไม่หายจริง ก่อน commit เขียนอีก 8 โลก? ถูกและกันพลาด

**Q6.** แบ่งทำ 2 รอบไหม — รอบ 1 (ของแพง Opus): แยก 6 pack เดิม + ทดสอบว่าไม่พัง · รอบ 2 (ของถูก Sonnet): เขียน 3 โลกใหม่ + ต่อ dropdown ในแอป — หรืออยากรวดเดียวจบ

**Q7.** กติกา 'ก้อน genre ห้ามมีชื่อหลอดไฟเลย' ผมจะทำสคริปต์ตรวจอัตโนมัติ (lint) เป็นด่านตอน build — โอเคไหม หรือมีหลอดบางตัวที่เป็นหัวใจของแนวจริงๆ ที่อยากให้พิมพ์ชื่อได้ (ผมเปิดช่อง override ให้อยู่แล้ว)


---

## verify (adversarial 2 เลนส์)
- fidelity: REVISE · operability: REVISE · blocking พบ 5 → **Plan phase แก้ครบใน migration steps แล้ว** (STEP 0/2/3/6/7 อ้าง blocking ที่แก้)
