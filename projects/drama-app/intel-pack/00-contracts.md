# 00 — CONTRACTS กลาง (intel pack · drama-app)

> **สัญญากลางของ intelligence pack** — ไฟล์ 01–08 ทุกไฟล์ต้องอ้าง schema / ID / budget / นโยบายจากไฟล์นี้เท่านั้น ห้ามนิยามซ้ำ ห้ามขัด · ขัดเมื่อไหร่ = แก้ที่นี่ก่อนแล้วไล่ลง
> **ที่มาข้อเท็จจริง (4 ไฟล์):** `memory/smartaihub-drama-series.md` [SAH] · `projects/FF_factory/AGENT_OPS.md` [OPS] · `memory/vertical-drama-basics-dramy.md` [DRM] · `memory/gemini-gem-seedance-director.md` [GEM] (Instructions + §FIXED FACTS) — ตัวเลขทุกตัวในไฟล์นี้ trace กลับ 4 ไฟล์นี้ได้

## 0) Pipeline + ผังเลข endpoint

```
brief ─▶ 01 series bible ─▶ 02 สคริปต์ตอน ─▶ (03 GEN GATE) ─▶ 04 shot list
      ─▶ 05 keyframe image prompt ─▶ (03 GEN GATE) ─▶ 06 Seedance video prompt
      ─▶ (03 GEN GATE) ─▶ 07 QA ─▶ 08 continuity ledger update ─▶ ตอนถัดไป/ช็อตถัดไป
```

- **03 = GEN GATE ไม่ใช่ LLM endpoint** — จุดที่เจนภาพ/วิดีโอจริง (char sheet · scene plate · keyframe · คลิป) ตามแนว factory ขั้น 3A/3B "manual gen" [OPS] · ใน app คือ call gen API แล้วรอ asset กลับ
- หลัก **"board first, render second"** [OPS]: keyframe (ภาพนิ่ง) ต้องผ่าน QA ก่อนจ่ายค่าเจนวิดีโอ · keyframe จริง = first frame ของ i2v [OPS Phase B]
- แก้งาน = **re-roll หน่วยเล็กสุด** — QA ต้องชี้หน่วย + prompt ที่ต้องแก้เสมอ [OPS กติกาเหล็ก 4]

## 1) Entity Schemas

### 1.1 SeriesBible

| field | คำอธิบาย |
|---|---|
| `series_id` | slug kebab-case อังกฤษ/ทับศัพท์ [OPS] |
| `title_th` | ชื่อเรื่องไทย |
| `logline` | "สถานการณ์" ที่เห็นภาพชัด 1–2 ประโยค — ห้ามไอเดียกว้างแบบ "เรื่องรัก/คนอกหัก" [DRM] |
| `genre_tone` | แนว + โทนเรื่อง |
| `genre` | **optional (ส่วนขยาย GENRE)** — enum: `romance-drama` / `comedy` / `thriller-horror` / `action` / `family` / `revenge-vindication` · ไม่ส่ง = ไม่ inject (พฤติกรรมเดิม) · ค่านอก enum = ปฏิบัติเป็น `romance-drama` · มาจากที่ user เลือกตอนสร้าง series · ใช้แค่ให้แอปเลือก block จาก `09-genre-packs.md` (§5 แถว 09) — **ไม่ส่ง field นี้ = pipeline ทำงานเหมือนเดิมทุกประการ** |
| `hook_type` | 1 ใน 4: `visual` / `emotional` / `curiosity` / `conflict` [DRM] + เหตุผล 1 บรรทัดว่าเนื้อเรื่องพาไปหาคำตอบของ hook นี้จริง (เกณฑ์เลือก hook [DRM]) |
| `selling_point` | จุดขายของเรื่อง [DRM เช็กก่อนเริ่ม] |
| `central_conflict` | ความขัดแย้งหลัก [DRM] |
| `characters` | `Character[]` — ตัวละครหลัก **≤3** [DRM] |
| `locations` | `Location[]` — สถานที่หลัก **≤2** [DRM] |
| `episode_plan` | แผนรายตอน (default เป้า **10 ตอน** [SAH]): ต่อตอน = ep_no + beat หลัก + cliffhanger ค้าง (บังคับทุกตอน [DRM]) |
| `style_stack` | visual style keywords ภาษาอังกฤษ ใช้ซ้ำทุก prompt — keywords ทำงานเสมอ, ชื่อผู้กำกับ = โบนัสเฉพาะรายที่ training data หนา [GEM] |
| `format` | ค่าตายตัวของ series: `9:16` · ตอนละ 60–120s [DRM] · 24fps [GEM FIXED FACTS] |
| `bible_digest` | ฉบับย่อ (logline + tone + hook_type + selling_point + style_stack + format + รายชื่อ char/loc โดยต่อ character แนบ `voice_delivery` + `arc_note`) — ก้อนที่ PromptEnvelope inject |

### 1.2 Character

| field | คำอธิบาย |
|---|---|
| `char_id` | `char01_<ชื่อโรมัน>` เช่น `char01_fon` [OPS ASSET MAP] |
| `name_th` / `name_en` | ชื่อไทย (ใช้ในบท) / โรมัน (ใช้ใน prompt) |
| `role` | role tag: ตัวเอก / คู่ / แม่ / ตัวร้าย / มาสคอต ฯลฯ (แนวการ์ดตัวละคร [SAH]) |
| `identity_anchor_en` | **ก้อนบรรยายตัวตนภาษาอังกฤษ ใช้แบบ verbatim** (หน้า/ผม/รูปร่าง/silhouette) — endpoint ฝั่งภาพ copy เต็มก้อนลง prompt ตรง ๆ ห้าม paraphrase (หลักการร่วมข้อ 1) · video prompt i2v ใช้ short lock ตาม §1.5 |
| `wardrobe_default` | ชุดประจำ + state เริ่มต้น (เป็น state lock ตั้งต้นของ ledger) |
| `voice_delivery` | โน้ตเสียง/วิธีพูด — ใช้เป็น delivery direction ต่อบรรทัด dialogue [SAH] |
| `sheet_asset` | asset id ของ character sheet เช่น `char01_fon_sheet.png` [OPS] |
| `arc_note` | arc ข้ามตอน (ให้ 02/04 ใช้วางพัฒนาการ) |

### 1.3 Location

| field | คำอธิบาย |
|---|---|
| `loc_id` | `scene01_<slug>` เช่น `scene02_school` [OPS ASSET MAP] |
| `name_th` / `name_en` | ชื่อไทย / อังกฤษ |
| `plate_asset` | clean plate เช่น `scene02_school.png` [OPS] |
| `lighting_anchor` | แสงหลักเชิง **physical** (แหล่งกำเนิด/ทิศ/อุณหภูมิ) ห้ามคำอารมณ์ [GEM LIGHTING] |
| `key_props` | prop ประจำฉากที่ต้อง continuity (เข้า ledger) |
| `variants` | สภาพ/ช่วงเวลา (กลางวัน/กลางคืน/ฝน) ที่มีใช้ในเรื่อง |

### 1.4 Episode

| field | คำอธิบาย |
|---|---|
| `ep_id` | `ep03` (2 หลัก) |
| `ep_no` / `title_th` | ลำดับ + ชื่อตอน |
| `target_sec` | 60–120 [DRM] |
| `structure` | โครง 5 ช่วงบังคับ: `hook → setup → conflict → twist → cliffhanger` [DRM] |
| `script_lines` | บรรทัดสคริปต์เต็ม ต่อบรรทัด: ช่วงเวลา / ภาพ / เสียง+บทพูด / อารมณ์ตัวละคร / หมายเหตุการสร้าง (ฟอร์แมต [DRM]) |
| `cliffhanger` | จุดจบค้าง (บังคับทุกตอน [DRM]) + สะพานไป hook ตอนถัดไป |
| `chars_used` / `locs_used` | รายการ `char_id` / `loc_id` ที่ปรากฏ |
| `status` | `draft` / `locked` / `gen` / `done` (แนว STATE.md [OPS]) |

### 1.5 Shot

| field | คำอธิบาย |
|---|---|
| `shot_id` | `ep03_shot05` |
| `ep_id` + `beat_ref` | ตอน + beat ที่มา — **1 beat = 1 shot** (หลักการร่วมข้อ 3) |
| `duration_sec` | หนึ่งใน **4/5/6/8/10/12/15s** [GEM FIXED FACTS] · <10s drift น้อยกว่า [GEM i2v] |
| `shot_size` | WS/MS/MCU/CU/ECU — **default = medium shot** สำหรับซีรีส์ [DRM] (full-body เสี่ยง artifact [GEM PITFALLS]) |
| `camera` | **move หลักเดียว** + motivation [GEM CAMERA] · ตาม GOLDEN RULE: บอก order+action ปล่อยมุมให้โมเดล ยกเว้น beat ที่ความหมาย/มุกต้องการล็อก [GEM] |
| `chars_in_frame` | `char_id[]` + ตำแหน่ง: thirds + x/y% + frame-occupancy% [GEM CHARACTER ANCHOR] |
| `loc_id` | ฉากที่ใช้ |
| `action` | **1 action ต่อช็อต** เขียนเป็นสถานการณ์/กล้ามเนื้อ ไม่ใช่คำอารมณ์ [GEM ACTING] |
| `dialogue` | **≤2 เทิร์น** · เทิร์นละ **<15 คำ** · ไทย ใน quotes + emotion tag + delivery direction ต่อบรรทัด [SAH]+[GEM AUDIO] |
| `audio_events` | เสียงเป็นเหตุการณ์รูปธรรม — เขียนตั้งใจทุกช็อต (หลักการร่วมข้อ 4) |
| `keyframe_prompt` | EN ≤3,200 chars (budget §3) |
| `keyframe_asset` | `sb_ep03_shot05.png` |
| `video_prompt` | EN ≤1,800 chars · i2v: **ห้ามบรรยายภาพซ้ำ** — identity-lock บวกสั้น + motion 4 ชั้น (subject/internal/camera/environment) เท่านั้น [GEM i2v] |
| `final_frame` | cue เฟรมจบ (บังคับ [GEM i2v]) — เป็นจุดต่อของช็อตถัดไป |
| `ledger_refs` | `LedgerEntry` ids ที่มีผลกับช็อตนี้ |
| `qa_status` | `pending` / `PASS` / `REDO` + `redo_note` (ชี้หน่วยเล็กสุด + prompt fix [OPS]) |

### 1.6 LedgerEntry (continuity ledger ข้ามช็อต-ข้ามตอน — จุดยากที่สุดของระบบ [SAH])

| field | คำอธิบาย |
|---|---|
| `ledger_id` | `led_ep03_01` (นับต่อภายในตอน) หรือ `led_series_01` (ระดับเรื่อง) |
| `scope` | `shot` / `episode` / `series` |
| `entity` | `char_id` / `loc_id` / ชื่อ prop |
| `state_locks` | **object keyed รายคีย์** (shape ตาม 03 §2 — validator diff ข้ามช็อตเป็นรายคีย์ได้) ครอบคลุมล็อกตาม [GEM CHARACTER ANCHOR]: costume, hair, wet/dry, object-in-hand, gaze/eyeline, ฝั่งจอ (2 ตัวละครห้ามสลับฝั่ง/ห้ามข้ามแกนกลาง), posture, body tension |
| `source` | `planned` (จากบท) vs `pixel-verified` (อ่านจากภาพ/คลิปจริง — ledger ตรง pixel [OPS Phase B]) |
| `valid_range` | ช่วง shot/ep ที่ล็อกมีผล (เช่น `ep03_shot02 → ep03_shot09`) · ปลายเปิดใช้ token `OPEN` (เช่น `ep03_shot05 → OPEN`) · `scope: series` ละได้ = คลุมทั้งเรื่อง |
| `note` | เหตุการณ์ที่เปลี่ยน state (เช่น "เปียกฝนตั้งแต่ shot04") |

### 1.7 PromptEnvelope (แอป inject เข้า endpoint **ทุกครั้ง**)

| field | คำอธิบาย |
|---|---|
| `bible_digest` | SeriesBible ฉบับย่อ (§1.1) |
| `identity_blocks` | `identity_anchor_en` แบบ verbatim เฉพาะ char ที่อยู่ในงานชิ้นนี้ |
| `ledger_slice` | เฉพาะ `LedgerEntry` ที่ `valid_range` คลุม shot/ep นี้ — ไม่ส่งทั้ง ledger |
| `shot_spec` | `Shot` ปัจจุบัน (endpoint 05/06/07) หรือ `Episode` (endpoint 02/04) |
| `budget_block` | ตาราง §3 ทั้งก้อน — endpoint ต้อง validate ก่อนคืนค่า |
| `language_flag` | นโยบาย §4 |
| `ref_plan` | @ImageN role map: ทุก ref มี role เดียวชัด (identity/costume/environment/composition) [GEM REFERENCES] · เพดาน ≤9 img / 3 vid / 3 audio, Higgsfield รวม ≤12 [GEM FIXED FACTS] |
| `prior_context` | keyframe/คลิป/final_frame ของช็อตก่อนหน้า (ใช้ใน 05/06/07/08) |
| `genre_pack` | **optional (ส่วนขยาย GENRE)** — string block ที่แอปอ่านจาก `09-genre-packs.md` ตาม `SeriesBible.genre` แล้ว inject เป็นชั้น "รสของแนว" (≤4,500 chars ตาม §3) · เป็น flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 · **ไม่มี field นี้ = endpoint รับ input เดิมเป๊ะ = พฤติกรรมเดิมทุกตัวอักษร** |

## 2) ID / Naming convention (แนวโรงงาน [OPS])

| สิ่ง | รูปแบบ | ตัวอย่าง |
|---|---|---|
| series | slug kebab-case อังกฤษ/ทับศัพท์ | `kaew-klang-fon` |
| episode | `ep<nn>` 2 หลัก | `ep03` |
| shot | `<ep>_shot<nn>` | `ep03_shot05` |
| character | `char<nn>_<ชื่อโรมัน>` | `char01_fon` |
| char sheet asset | `char<nn>_<ชื่อ>_sheet.png` | `char01_fon_sheet.png` |
| location + plate | `scene<nn>_<slug>` (.png) | `scene02_school.png` |
| keyframe asset | `sb_<ep>_shot<nn>.png` — แนว `sb_<module>_<nn>` โดยงานหนัง/ละครใช้เลขช็อตแทน module [OPS] | `sb_ep03_shot05.png` |
| คลิปวิดีโอ | `vid_<ep>_shot<nn>.mp4` | `vid_ep03_shot05.mp4` |
| ledger entry | series `led_series_<nn>` · episode `led_<ep>_<nn>` · shot `led_<ep>_shot<nn>_<nn>` | `led_ep03_01` · `led_ep03_shot05_01` |

กฎแยกโปรเจกต์ [OPS]: ทุก asset/ไฟล์ของ series อยู่ใต้โฟลเดอร์ series ตัวเองเท่านั้น ห้ามปนข้าม series

## 3) Budget กลาง (ทุก endpoint validate ก่อนคืนค่า)

| รายการ | working budget | hard cap | ที่มา |
|---|---|---|---|
| keyframe image prompt | **≤3,200 chars** | เพดานแอป 3,500 [SAH] | margin rule ล่างสุด |
| video prompt | **≤1,800 chars** | เพดาน Seedance 2,000 [SAH]+[GEM] | margin rule ล่างสุด |
| เนื้อ prompt มาตรฐาน | 60–100 คำ · 20–30 คำแรกน้ำหนักสูงสุด เปิดด้วย Subject+Action | — | [GEM CORE FORMULA] |
| dialogue | **≤2 เทิร์น/ช็อต** · **<15 คำ/เทิร์น** — ไทยนับด้วยการตัดคำแบบพจนานุกรม หรือเทียบเท่า **≤40 ตัวอักษรไทย/เทิร์น** (ไม่รวม emotion tag) — เกณฑ์นับนิยามที่นี่จุดเดียว ทุก endpoint อ้างตาม | — | [SAH] บทเรียน 3 เทิร์นเสี่ยง lip-sync พัง + [GEM AUDIO] |
| duration ต่อช็อต | steps **4/5/6/8/10/12/15s** เท่านั้น · max 15s (ยาวกว่า = ต่อช็อต) · แนะนำ <10s | — | [GEM FIXED FACTS]+[GEM i2v] |
| ความหนา beat | 4–8s = 1 action · 8–12s = action+reveal · 12–15s = 2–3 beats · เกินนั้นแตกช็อต | — | [GEM CORE FORMULA] |
| ตอน | **60–120s** · **9:16** · 24fps | — | [DRM]+[GEM FIXED FACTS] |
| scope เรื่อง | ตัวละครหลัก **≤3** · สถานที่หลัก **≤2** · เป้า episode_plan 10 ตอน | **≤12 ตอน/call** — brief ขอเกิน = วางแผน 12 ตอนแรก + แจ้งใน `scope_notes` (กัน output ล้น max tokens) | [DRM]+[SAH] · cap = margin rule |
| references | ≤9 images / 3 video / 3 audio · Higgsfield รวม ≤12 | — | [GEM FIXED FACTS] |
| genre pack block (`genre_pack` — optional) | **≤4,500 chars ต่อแนว** | — | ส่วนขยาย GENRE นิยามที่นี่จุดเดียว — เป็น optional layer ห้ามเบียด budget prompt หลัก · ไม่ inject = ไม่กิน budget ใดเลย |

**Margin rule:** ห้ามส่ง prompt ชนเพดาน hard cap — บทเรียนตรงจาก [SAH]: แอปต้นแบบยิง video prompt 1,973/2,000 จนไม่เหลือที่แก้ · working budget ข้างบนคือเส้นจริงที่ endpoint ต้องเคารพ

## 4) นโยบายภาษา

| ชั้น | ภาษา |
|---|---|
| story / bible / สคริปต์ / dialogue (01, 02, 04 + ทุกอย่างที่คนอ่าน) | **ไทย** |
| generation prompts (05 keyframe, 06 video) | **อังกฤษล้วน** — prompt สุดท้ายเป็น EN เสมอ [GEM] |
| ข้อยกเว้นใน prompt EN | ฝังชื่อไทย/บทพูดไทยใน quotes ได้ — dialogue อยู่ใน quotes + delivery direction [GEM AUDIO] |
| `identity_anchor_en` / `style_stack` | อังกฤษเสมอ (copy ลง prompt ตรง ๆ) |
| `wardrobe_default` / `key_props` / `variants` | อังกฤษ — feed `state_locks` ของ ledger ที่ถูก copy ลง prompt EN · `variants` = EN slug คงที่ เช่น `day` / `night-rain` |
| ข้อความคุยกับ user ใน UI | ไทย (ตอบภาษาผู้ใช้ [GEM INTERACTION]) |

## 5) ตาราง hand-off ระหว่าง endpoint

ทุก endpoint รับ `PromptEnvelope` ประกบ input หลักเสมอ (§1.7)

| endpoint | ชื่อ | รับ (นอกจาก envelope) | คืน |
|---|---|---|---|
| **01** | series-bible | brief (free text จาก user) | `SeriesBible` + `Character[]` + `Location[]` + `Episode[]` (stub แผนรายตอน) |
| **02** | episode-script | `Episode` stub + ledger ระดับ series | `Episode` เต็ม (script_lines 5 ช่วง + cliffhanger, สถานะ `draft`) — เหตุการณ์เปลี่ยน state ถูก flag `"ledger:"` ใน `prod_note_th` ของบีต (ตาม OUTPUT ของ 02 — ไม่คืน `LedgerEntry[]`) |
| **04** | shot-list | `Episode` (locked) | `Shot[]` spec ครบ (ยังไม่มี prompt) — 1 beat = 1 shot + `ledger_draft` (วัตถุดิบ state change ราย shot — ไม่ใช่ `LedgerEntry[]`) |
| **05** | keyframe-prompt | `Shot` | `Shot.keyframe_prompt` (EN ≤3,200) + `ref_plan` ที่ใช้ |
| **06** | video-prompt | `Shot` + `keyframe_asset` (pixel จริง = first frame) | `Shot.video_prompt` (EN ≤1,800) + `final_frame` cue |
| **07** | qa | `Shot` + asset (keyframe หรือคลิป) | verdict `PASS`/`REDO` + หน่วยเล็กสุดที่ต้องแก้ + prompt fix → เขียนกลับ `qa_status` |
| **08** | ledger | `Shot`/`Episode` ที่ QA ผ่าน + asset | `LedgerEntry[]` create/update (อัป `source` → `pixel-verified`) |
| **09** | genre-packs | **ไม่ใช่ endpoint — static reference file** (`09-genre-packs.md` · ไม่มี LLM call) | แอปอ่าน block ของ `SeriesBible.genre` (default `romance-drama`) → ใส่ `PromptEnvelope.genre_pack` (§1.7) ก่อนเรียก endpoint · ไฟล์ 09 ต้องเคารพ contracts เหมือนไฟล์อื่น · **ไม่มี genre = ไม่ inject = พฤติกรรมเดิมทุกประการ** |

- **Gate mapping ของ 07** [OPS]: Gate 0 = user อนุมัติ script (หลัง 02) · Gate 1 = ภาพ (identity/continuity/composition/text — เช็คก่อนจ่ายค่าวิดีโอ) · Gate 2 = คลิป (lip-sync ถ้ามีพูด, contact physics, drift, รอยต่อ) · ลำดับเช็ค: **contact physics ก่อน** แล้วค่อยมือ/นิ้ว → wardrobe/prop ข้ามช็อต → identity drift → text [GEM OUTPUT FORMAT ④]
- 08 รันหลัง QA PASS เท่านั้น — ledger ที่ downstream ใช้ต้องมาจาก pixel จริง ไม่ใช่แผน [OPS Phase B]
- **Single writer ของ `LedgerEntry`:** ชั้น ledger ของแอปเป็นผู้ materialize `LedgerEntry[]` `source: planned` จาก flags `"ledger:"` ของ 02 + `ledger_draft` ของ 04 (03 §5 ขั้น PLAN) — endpoint ฝั่งเขียนบท/ช็อตห้ามคืน `LedgerEntry[]` ตรง ๆ

## 6) หลักการร่วม 5 ข้อ (ทุก endpoint ต้องเคารพ)

1. **Identity verbatim** — `identity_anchor_en` ของตัวละคร copy ลง prompt ตรง ๆ ทุกครั้งที่ใช้ anchor ห้าม paraphrase/ย่อ (จุดที่ใช้ anchor เต็มก้อน = keyframe/image prompt · video prompt i2v ใช้ short lock — §1.5/§6 ข้อ 5); ref ทุกตัวมี role เดียวชัด และประกาศ priority เมื่อชนกัน [GEM CHARACTER ANCHOR + REFERENCES]
2. **Under-direct acting** — ห้ามเขียนคำอารมณ์ตรง ๆ (โมเดล overact = AI-tell) ให้บรรยายสถานการณ์/การกระทำ แล้วผูกอารมณ์เป็นกล้ามเนื้อจริงต่อ timecode; deadpan เก็บไว้ที่ punchline เท่านั้น [GEM ACTING]
3. **1 beat = 1 shot** — 1 action ต่อช็อต ตามสเกลความหนา §3; beat เกิน = แตกช็อต ไม่ใช่ยัด prompt; ยัดบทพูดเกิน 2 เทิร์น = เสี่ยง lip-sync พังแบบแอปต้นแบบ [GEM]+[SAH]
4. **เสียงเขียนตั้งใจ** — โมเดลออกเสียง sync ในตัว จึงห้ามปล่อยเสียงตามยถากรรม: เขียนเป็นเหตุการณ์รูปธรรม, dialogue ใน quotes <15 คำ/คัต, ปิดด้วย room tone ที่ตั้งใจ [GEM AUDIO]
5. **Positive locks** — เขียนข้อห้ามทุกข้อเป็นล็อกเชิงบวก ("keeps the same face, hair, costume, proportions, silhouette throughout" ไม่ใช่ "no face change") — Seedance ไม่มี negative-prompt field จริง [GEM POSITIVE > NEGATIVE] · **scope:** บังคับเต็มกับ video prompt (06) และ `identity_anchor_en` (short lock ใน video prompt และตัว anchor เองต้องเป็น positive ล้วน) — ส่วน **image prompt (endpoint 05 keyframe + character-architect [ไฟล์ 04 ของ pack]) อนุญาต negative tail สั้นท้าย prompt ได้** (เหตุผลของกฎผูกกับ video model) แต่ห้ามฝัง negative ไว้ใน anchor
หมายเหตุ scope ของ anchor: video prompt (06, i2v) ไม่วาง `identity_anchor_en` เต็มก้อน — ใช้ short positive lock 1 บรรทัดอ้าง start frame (ตาม §1.5) · anchor เต็มก้อน verbatim ลงที่ keyframe prompt (05) — แต่ตัว anchor เองต้อง positive-only เสมอ เพราะยังถูกใช้ในช็อต reference-mode ที่ anchor ย่อลง video prompt ได้ (03 §3 ข้อ 5)
