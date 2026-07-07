# 03 — Continuity Ledger (architecture spec)

ไฟล์นี้คือ **spec เชิงสถาปัตยกรรมของ continuity ledger** — ไม่ใช่ endpoint (เลข 03 ใน pipeline = GEN GATE ตาม `00-contracts.md` §0) แต่เป็น "กระดูกสันหลังข้อมูล" ที่ endpoint 05/06/07/08 ใช้ร่วมกัน
**Input:** เหตุการณ์ในบท (จาก 02/04) + ข้อเท็จจริงจาก pixel จริงหลัง QA PASS (จาก 07→08) · **Output:** `LedgerEntry[]` ต่อ series ที่แอป slice แล้ว thread เข้า `PromptEnvelope` ของทุก prompt ปลายทางอัตโนมัติ
**ใครใช้:** แอปตอนประกอบ `PromptEnvelope` (§1.7) · endpoint 05 (keyframe prompt) · 06 (video prompt) · 07 (QA checklist) · 08 (เขียน ledger กลับ)
**ภารกิจ:** กัน identity / wardrobe / prop drift ข้ามช็อต-ข้ามตอน — จุดยากที่สุดของระบบตาม contracts §1.6 และเป็น tell ที่ยั่งยืนที่สุดของวิดีโอ AI (model รุ่นใหม่ปิด physics ได้เรื่อย ๆ แต่ cross-shot consistency เป็นปัญหา architecture — จับได้เสมอ)

---

## 1) หลักการราก (ทำไม ledger ต้องเป็นแบบนี้)

1. **Identity = visual asset ไม่ใช่ text** — model pattern-match กับ visual input ไม่ใช่ reconstruct จากคำบรรยาย ยิ่งบรรยายหน้าเยอะยิ่ง drift → ตัวล็อกหลักคือ **reference sheet** (`sheet_asset` ของ Character) ส่วน text anchor เป็นตัวล็อกรอง ที่ต้อง **copy verbatim ลง keyframe/image prompt ทุกใบ ห้าม paraphrase** (หลักการร่วมข้อ 1 ใน contracts §6 — ฝั่ง video prompt i2v ใช้ short lock ตาม §3 ข้อ 5)
2. **Stateless ต่อ gen call** — บทเรียนจาก named-reference-sheet method: "เปิด conversation ใหม่ทุกครั้งที่เจน แนบเฉพาะชีตที่ใช้" กัน drift จาก context สะสม → ในแอปแปลว่า ทุก gen call รับเฉพาะ `ledger_slice` (LedgerEntry ที่ `valid_range` คลุมช็อตนี้) + ref ที่ใช้จริง — **ห้ามส่งทั้ง ledger** (contracts §1.7)
3. **Text คุม concept แต่ไม่คุม geometry** — case study จริง: identity lock คุมหน้า + concept ชุดได้ แต่ layout ดอกบนชุด/ลายผ้า re-roll ข้ามช็อต → ของที่ micro-geometry สำคัญ (ชุด, prop ประจำตัว) ต้องมี **canonical image asset** เป็น ref ไม่ใช่พึ่ง text อย่างเดียว
4. **Ledger ตรง pixel ไม่ใช่ตรงแผน** — state ที่ downstream ใช้ต้องมาจากภาพ/คลิปที่ QA ผ่านแล้ว (`source: pixel-verified`) ไม่ใช่จากบท (contracts §5: 08 รันหลัง QA PASS เท่านั้น)

---

## 2) LEDGER SCHEMA

ทุก entry ใช้โครง `LedgerEntry` ตาม contracts §1.6 เป๊ะ (`ledger_id` / `scope` / `entity` / `state_locks` / `source` / `valid_range` / `note`) — ส่วนนี้ spec **รูปร่างภายในของ `state_locks`** ต่อชนิด entity

**Semantics ของ `valid_range` / `ledger_id` (ให้ filter "valid_range คลุม shot นี้" รันได้ทุกกรณี):**

- ช่วงปิด: `ep03_shot05 → ep03_shot09` · ช่วงเปิด (ยังไม่รู้จุดจบ): `ep03_shot05 → OPEN` — ขั้น CLOSE (§5) ค่อยแทน `OPEN` ด้วยช็อตสุดท้ายที่ lock มีผล
- `scope: series` ละ `valid_range` ได้ = คลุมทั้งเรื่อง (ตีความเท่ากับ `series_start → OPEN`)
- format `ledger_id` ต่อ scope (sync กับ contracts §2): series = `led_series_<nn>` · episode = `led_<ep>_<nn>` (เช่น `led_ep03_02`) · shot = `led_<ep>_shot<nn>_<nn>` (เช่น `led_ep03_shot05_01`)

### 2.1 ต่อ Character (`entity` = `char_id` เช่น `char01_fon`)

| ก้อน | เนื้อหา | กฎ |
|---|---|---|
| `identity_ref` | pointer ไป `Character.identity_anchor_en` + `Character.sheet_asset` | **anchor text เป็นก้อน verbatim ก้อนเดียวต่อตัวละคร** — เก็บที่ Character (§1.2) ที่เดียว ledger ชี้ไปหา ไม่ copy มาแก้ · keyframe/image prompt ปลายทาง render ลงไปคำต่อคำ (video prompt = short lock ตาม §3 ข้อ 5) |
| `wardrobe` | ชุด **ต่อตอน/ต่อฉาก**: base = `wardrobe_default` + override รายฉาก (ชุดนักเรียน→ชุดอยู่บ้าน) + **condition** (สะอาด/เปื้อน/ขาด/เปียกครึ่งตัว) | เปลี่ยนชุด = ปิด entry เก่า เปิด entry ใหม่ (ดู §5) · ชุดที่ลายผ้า/กระดุม/ตะเข็บสำคัญ ต้องมี costume ref image ของตัวเอง (เข้า slot costume ตามลำดับจอง §3 ข้อ 2) |
| `hair` | ทรง + สภาพ (รวบ/ปล่อย, แห้ง/เปียก/ลู่ลม, กิ๊บ/ยางมัด) | ผมคือ silhouette — หลุดแล้วตาเห็นทันที |
| `wet_dry` | แห้ง / เปียกส่วนไหน / เหงื่อ / คราบน้ำตา | สืบทอดข้ามช็อตจนกว่าจะมีเหตุการณ์ลบ (เช็ดตัว, ตัดข้ามเวลา) |
| `object_in_hand` | ของในมือ ข้างไหน + สภาพของ (ซองจดหมายยับ/โทรศัพท์จอแตก) | ของหายจากมือกลางคัต = continuity break คลาสสิก |
| `residual_emotion` | **อารมณ์ค้างจากช็อตก่อน เขียนเป็นร่างกาย** ไม่ใช่คำอารมณ์ — "ตาแดงขอบเปียกจาก shot03, กรามยังเกร็ง" ไม่ใช่ "ยังเศร้าอยู่" | ตาม under-direct acting (contracts §6 ข้อ 2) — คำอารมณ์ตรง ๆ ทำ model overact |
| `screen_side` / `eyeline` | ฝั่งจอ + ทิศสายตา ณ จุดจบช็อตก่อน (2 ตัวละครห้ามสลับฝั่ง/ห้ามข้ามแกนกลาง — contracts §1.6) | ต่อเนื่องกับ `final_frame` ของ Shot ก่อนหน้า |
| `posture` / `body_tension` | ท่าค้าง + ความเกร็งของร่างกาย | รายการล็อกครบชุดตาม contracts §1.6 |

### 2.2 ต่อ Location (`entity` = `loc_id` เช่น `scene02_school`)

| ก้อน | เนื้อหา | กฎ |
|---|---|---|
| `lighting_state` | สืบจาก `Location.lighting_anchor` (แหล่งกำเนิด/ทิศ/อุณหภูมิ — physical เท่านั้น ห้ามคำอารมณ์ ตาม §1.3) + variant ที่ active ตอนนี้ (กลางวัน/กลางคืน/ฝน จาก `variants`) | เวลาในเรื่องเดินหน้าอย่างเดียวภายใน sequence — แดดบ่ายห้ามกลับเป็นแดดเช้าในฉากต่อเนื่อง |
| `time_of_day` | ช่วงเวลาในเรื่อง ณ ช็อตล่าสุดของฉากนี้ | |
| `props_state` | สภาพ/ตำแหน่งของ `key_props` ประจำฉาก (แก้วน้ำครึ่งแก้ววางฝั่งไหน, ประตูเปิด/ปิด, ร่มพิงตรงไหน) | prop ที่ตัวละครขยับแล้ว ต้องอยู่ที่ใหม่ในช็อตถัดไป |
| `plate_ref` | pointer ไป `plate_asset` — ใช้เป็น environment ref (slot ตามลำดับจอง §3 ข้อ 2) ทุก prompt ของฉากนี้ | plate เดียวกันทั้งฉาก = แสง/ฉากหลังนิ่งเอง |

### 2.3 ต่อ Prop สำคัญ (`entity` = ชื่อ prop ตาม contracts §1.6)

- **key คงที่:** ใช้ชื่อ EN สั้นคงที่เป็น entity key (เช่น `white_envelope`, `silver_locket`) — ชื่อเดียวกันนี้คือคำที่ใช้เรียกใน prompt ทุกครั้ง ห้ามเปลี่ยนคำเรียก
- `canonical_desc_en` — ก้อนบรรยาย EN verbatim ของ prop (รูปทรง/สี/ตำหนิ) ใช้ซ้ำทุก prompt แบบเดียวกับ identity anchor
- `ref_asset` — asset id ของ canonical image ref (เช่น `prop_white_envelope.png`) — **บังคับ** สำหรับ prop ที่ micro-geometry สำคัญ (หลักการราก §1 ข้อ 3: text คุม concept แต่ไม่คุม geometry) และสัตว์ทุกตัวที่โผล่เกิน 1 ช็อต · prop อื่น optional · เข้า slot @ImageN ตามลำดับจอง §3 ข้อ 2
- `holder_or_location` — ตอนนี้อยู่กับใคร (`char_id`) หรืออยู่ที่ไหน (`loc_id` + ตำแหน่ง)
- `condition` — สภาพสะสม (ยับ/เปื้อน/ฉีกครึ่ง) — เดินหน้าอย่างเดียวจนกว่าบทจะสั่งซ่อม/เปลี่ยน
- **สัตว์เลี้ยง/สิ่งมีชีวิตประกอบ = prop ที่หลุดง่ายที่สุด** (case study จริง: แมวข้างถนนผอมลายเข้ม vs แมวที่อุ้มอ้วนฟูลายจาง — identity lock ไม่คุมสัตว์) → สัตว์ทุกตัวที่โผล่เกิน 1 ช็อต **ต้องขึ้นทะเบียนเป็น entity + มี ref image ของตัวเอง** ห้ามปล่อยเป็นฉากหลัง

---

## 3) THREAD RULES — ledger เข้า prompt ปลายทางยังไง

แอป render `ledger_slice` เป็น **CONTINUITY BLOCK** แล้วประกบเข้า prompt ที่ 05/06 สร้าง — endpoint ไม่ต้องคิดเอง continuity มาจากระบบ

**กฎบังคับ:**

1. **Identity verbatim ใน keyframe prompt ทุกครั้ง** — `identity_anchor_en` ของทุก char ที่อยู่ในเฟรม ลงไปคำต่อคำใน keyframe prompt ห้าม paraphrase/ย่อ/สลับคำ (contracts §6 ข้อ 1 + consistency trick ของ storyboard workflow: "copy character description verbatim ทุก frame") · ฝั่ง video prompt (i2v) ใช้ short lock ตามข้อ 5 — ไม่วาง anchor เต็ม
2. **@ImageN role allocation ของ pack นี้** (ตาม `ref_plan` §1.7 — ทุก ref มี role เดียวชัด): จอง slot ตาม**ลำดับตายตัว**ต่อไปนี้ — ref ชั้นไหนไม่มี เลข Image ไหลลง (re-number) ห้ามเว้นช่องว่าง:
   1. **identity** ของทุก char ใน `chars_in_frame` เรียงตามลำดับ (char `sheet_asset`) — คุมหน้า/ตัว
   2. **costume/product** ต่อ char เฉพาะที่มี costume ref (§2.1 — จำเป็นเฉพาะชุดที่ลายผ้า/กระดุมสำคัญ) — คุมชุด/สินค้า (geometry)
   3. **prop/pet ref** (`ref_asset` §2.3) ที่ active ในช็อต — ใช้ slot ถัดไปที่ว่าง (ภายใต้เพดาน ≤9) และประกาศ role ชัดใน ref_plan เช่น "Use Image 4 as the white_envelope prop reference. Image 4 controls the envelope's shape and creases only."
   4. **environment** (loc `plate_asset`) — คุมฉาก/แสง
   5. **composition** (ถ้ามี — เช่น keyframe ช็อตก่อนหรือ grid panel) — ท้ายสุดเสมอ
   - ตัวอย่าง 2 ตัวละคร 1 ชุด (char02 มี costume ref, ไม่มี prop ref): Image 1 = char01 identity · Image 2 = char02 identity · Image 3 = char02 costume · Image 4 = environment
   - เพดานตาม contracts §3: ≤9 images / 3 video / 3 audio (Higgsfield รวม ≤12) — เกินเพดานให้ตัดจากท้ายลำดับจอง (composition ก่อน)
3. **ประกาศ priority เมื่อ ref ชนกันเสมอ** — อ้างเลขตาม slot ที่จองจริงในข้อ 2 เช่น "The identity from Image 1 takes priority over all other references. The outfit from Image 2 replaces the outfit in Image 1. The environment from Image 3 replaces the background."
4. **Positive locks เท่านั้น** — state ทุกตัว render เป็นล็อกเชิงบวก ("keeps the same face, hair, costume, proportions, silhouette throughout") ไม่ใช่ข้อห้าม (contracts §6 ข้อ 5 — Seedance ไม่มี negative-prompt field จริง)
5. **06 (video/i2v) ห้ามบรรยายภาพซ้ำ** — keyframe เป็น first frame แล้ว (contracts §1.5) → CONTINUITY BLOCK ฝั่งวิดีโอ = **short positive identity lock 1 บรรทัด** ระบุชื่อตัวละคร + อ้าง start frame (เช่น "Fon keeps the same face, hairstyle, outfit, body proportions and silhouette as the start frame throughout" — สอดคล้องกับ anchor แต่**ห้ามวาง `identity_anchor_en` เต็มก้อน** เพราะตัวตนอยู่ใน pixel ของ keyframe แล้ว + budget 1,800) + state lock เฉพาะที่ต้อง "คงอยู่ระหว่างขยับ" · ตัดส่วน REFERENCES/priority declaration และ scene re-description ออกทั้งหมด (แก่นจาก storyboard workflow: ภาพบอกว่า "เป็นยังไง" แล้ว วิดีโอบอกแค่ "ขยับยังไง") · **ข้อยกเว้น:** ช็อต reference-mode (ไม่มี keyframe เป็น first frame) ใช้ anchor ย่อกลางลง video prompt ได้ เพราะไม่มี pixel identity ให้ยึด
6. **ต่อช็อต:** `prior_context.final_frame` ของช็อตก่อน = สภาพตั้งต้นของช็อตนี้ — state lock ใน block ต้อง match เฟรมนั้น

**Template ที่แอป render ลง keyframe prompt (EN — โครงตายตัว เปลี่ยนเฉพาะค่า · เลข Image = ตามลำดับจองข้อ 2 · ช็อตหลายตัวละคร: render บรรทัด REFERENCES + ก้อน IDENTITY + ก้อน STATE LOCKS **ซ้ำต่อ char ทุกตัวในเฟรม** · ฝั่ง video prompt ใช้ฉบับย่อตามข้อ 5 — short lock + state locks เท่านั้น):**

```
=== CONTINUITY BLOCK (auto-rendered from ledger_slice — do not hand-edit) ===

REFERENCES:
- Use Image {n} as {name_en} identity reference ({sheet_asset}). Image {n}
  controls face and identity.                        ← ซ้ำต่อ char ทุกตัวในเฟรม
- Use Image {n} as {name_en} costume reference. Image {n} controls costume
  geometry only.                                     ← เฉพาะ char ที่มี costume ref
- Use Image {n} as the {prop_key} prop reference. Image {n} controls the prop's
  shape and surface detail only.                     ← เฉพาะ prop/pet ที่มี ref_asset
- Use Image {n} as the environment and lighting reference ({plate_asset}).
- {priority declaration อ้างเลข slot จริง, e.g. "The identity from Image 1 takes
  priority over all other references. The outfit from Image 3 replaces the
  outfit in Image 2. The environment from Image 4 replaces the background."}

IDENTITY (verbatim):                                 ← ซ้ำต่อ char ทุกตัวในเฟรม
{identity_anchor_en}

STATE LOCKS (valid: {valid_range}):                  ← ซ้ำต่อ char ทุกตัวในเฟรม
- Costume: {wardrobe + condition, e.g. "school uniform, top half rain-darkened,
  collar clinging to skin"}
- Hair: {e.g. "loose black hair, wet strands stuck to cheeks"}
- Wet/dry: {e.g. "hair and shoulders visibly wet since previous shot"}
- Object in hand: {e.g. "damp white envelope held in right hand at chest level"}
- Carry-over: {residual_emotion as body, e.g. "eyes red-rimmed, jaw tight"}
- Screen side / eyeline: {e.g. "stays in left third, eyes toward screen-right"}
- Posture/tension: {e.g. "shoulders hunched, jaw set, weight on back foot"}

CONTINUITY: {name_en} keeps the same face, hairstyle, costume, body proportions,
and silhouette throughout. {prop key names used exactly as registered}.
```

---

## 4) CROSS-SHOT QA HOOKS (ledger → checklist ของ endpoint 07)

Ledger คือ "ความจริง" ที่ 07 ใช้เทียบภาพ/คลิป — hooks ต่อไปนี้มาจาก tells ที่จับได้จริงใน case studies (ลำดับเช็คใหญ่ตาม contracts §5: **contact physics ก่อน** → มือ/นิ้ว → wardrobe/prop ข้ามช็อต → identity drift → text):

| tell จริง | วิธีเช็คกับ ledger |
|---|---|
| **ลายผ้า/กระดุม/ตะเข็บ re-roll ข้ามช็อต = tell อันดับต้น** (case study 2: layout ดอกบนชุดคนละแบบระหว่าง scene) | ซูมเทียบ costume geometry ทุกช็อตที่ `wardrobe` entry เดียวกัน active — เทียบกับ costume ref (slot ตาม §3 ข้อ 2) ไม่ใช่เทียบกันเองลอย ๆ |
| **prop เปลี่ยนหน้าตา/งอกของใหม่** (case study 3: หมวก plaid ธรรมดา → plaid เดียวกันงอกหูแมว) | ทุก prop ที่ขึ้นทะเบียน §2.3: เทียบกับ `canonical_desc_en` + `ref_asset` และเช็ค `holder_or_location` ว่าของอยู่ถูกที่ถูกมือ |
| **สัตว์เลี้ยง re-roll** (แมวคนละตัวใน 2 ช็อต) | สัตว์ที่โผล่เกิน 1 ช็อตต้องมี entity + ref — ถ้าไม่มีใน ledger แต่โผล่ซ้ำ = REDO หรือขึ้นทะเบียนก่อน |
| **ECU detail ต้องสม่ำเสมอทั้งเฟรม** (case study 3: ขนตาคมรายเส้นแต่ผิว/ปาก wax เรียบ — ฟุตเทจจริงผ่าน compression จะเบลอทุกอย่าง*เท่ากัน*) | ทุกช็อต CU/ECU: เช็คว่า detail level ทั่วเฟรมไล่เฉดเดียวกัน ไม่มีจุดคมผิดธรรมชาติ |
| **state ค้างหาย** (เปียกอยู่ดี ๆ แห้ง, ตาแดงหายกลางฉาก) | เทียบภาพกับทุก `state_locks` ที่ `valid_range` คลุมช็อตนี้ — ผิดข้อไหน REDO ต้องชี้ field นั้น + prompt fix (re-roll หน่วยเล็กสุด ตาม contracts §0) |
| **ฝั่งจอ/eyeline สลับ** | เทียบ `screen_side`/`eyeline` กับเฟรมจริง — 2 ตัวละครห้ามสลับฝั่ง/ห้ามข้ามแกนกลาง |

---

## 5) UPDATE & PROPAGATION — state เปลี่ยนแล้วไหลต่อยังไง

เหตุการณ์ในบทเปลี่ยนสถานะตัวละคร (เปื้อน/เปียก/บาดเจ็บ/ของหลุดมือ) → ต้องเดินตาม lifecycle นี้เท่านั้น:

1. **PLAN** — 02/04 เจอเหตุการณ์เปลี่ยน state ในบท → 02 flag `"ledger:"` ในบีต + 04 คืน `ledger_draft` (วัตถุดิบ) → **ชั้น ledger ของแอป materialize `LedgerEntry[]` `source: planned` จาก flags ของ 02 + ledger_draft ของ 04 (return contract ใน contracts §5 — ห้าม endpoint คืน `LedgerEntry[]` ตรง ๆ) แล้วบันทึกเข้า ledger** — `valid_range` เริ่มตั้งแต่ช็อตถัดจากเหตุการณ์ ปลายเปิดจนกว่าจะ CLOSE (เช่น เปียกฝน shot04 → lock มีผล `ep03_shot05 → OPEN`), `note` บันทึกเหตุการณ์ต้นเหตุ
2. **GEN** — 05/06 ของช็อตในช่วง valid_range ได้ entry นี้ใน `ledger_slice` อัตโนมัติ → state ใหม่ถูก render ลง CONTINUITY BLOCK เอง endpoint ไม่ต้องจำ
3. **VERIFY** — 07 QA ช็อตที่ state เปลี่ยนครั้งแรก: เช็คว่า pixel แสดง state ใหม่จริง (เปียกจริง แผลอยู่ตำแหน่งเดิม)
4. **COMMIT** — QA PASS แล้ว 08 อ่านจาก pixel จริง → อัป entry เป็น `source: pixel-verified` + แก้รายละเอียดให้ตรงภาพ (เช่น planned บอก "เปียก" แต่ภาพจริงเปียกแค่ครึ่งตัวบน → เขียนตามภาพ) — **ตั้งแต่จุดนี้ downstream ทั้งหมดยึด pixel-verified ไม่ใช่แผน**
5. **CLOSE** — state จบเมื่อมีเหตุการณ์ลบในบท (เปลี่ยนชุด/เช็ดตัว/ตัดข้ามเวลา/รักษาแผล): **ปิด entry เก่า** (ตัด valid_range ที่ช็อตสุดท้าย) แล้ว **เปิด entry ใหม่** — ห้ามแก้ทับของเก่า เพราะช็อตเก่าอาจถูก re-roll ทีหลังและยังต้องอ้าง state เดิมได้
6. **REDO ไม่แตะ ledger** — ถ้า QA สั่ง REDO เพราะภาพไม่ตรง ledger: ledger คือความจริง ภาพต้องตาม → แก้ที่ prompt/re-roll · จะแก้ ledger ได้กรณีเดียวคือ "เจตนากำกับเปลี่ยน" ซึ่งต้องแก้ entry `planned` ก่อนแล้วค่อย gen ใหม่
7. **Conflict rule** — `pixel-verified` ชนะ `planned` เสมอเมื่อ valid_range ทับกันบน entity เดียวกัน · scope แคบชนะ scope กว้าง (`shot` > `episode` > `series`)

---

## I/O SPEC

**ไม่ใช่ LLM endpoint** — I/O ต่อไปนี้คือสัญญาระหว่างแอปกับโมดูล ledger (ผู้เขียน = **ชั้น ledger ของแอป materialize entry `planned` จาก flags `"ledger:"` ของ 02 + `ledger_draft` ของ 04 (§5 ขั้น 1 + contracts §5) และ endpoint 08 เขียน/อัปเป็น `pixel-verified`** · ผู้อ่าน = ตัวประกอบ `PromptEnvelope`)

**Input (ตอนเขียน — จาก 08 ตาม contracts §5):** `Shot`/`Episode` ที่ `qa_status: PASS` + asset จริง (`keyframe_asset` / `vid_*`) + `ledger_slice` เดิม + `observed` — ข้อเท็จจริงจาก pixel ที่ **vision pass ของขั้น 08 สกัดจาก asset** (ดูภาพ/คลิปจริง ไม่ใช่อ่านจากบท) · กฎ: ทุก field ใน `state_locks` ของ entry `pixel-verified` ต้อง trace กลับ `observed` ได้ — field ที่ไม่ได้ observe ใหม่ให้ inherit จาก entry เดิมและระบุใน `note`
**Input (ตอนอ่าน — ตอนประกอบ envelope):** `shot_id` ปัจจุบัน → ระบบ filter `LedgerEntry` ที่ `valid_range` คลุม shot นี้ → ใส่ช่อง `ledger_slice` + ดึง `identity_blocks` (verbatim) + `ref_plan` ตาม §3

**Output format (entry ที่ 08 เขียน — JSON ตาม schema §1.6 · ค่าใน `state_locks` เป็น EN เพราะถูก render ลง prompt ตรง ๆ · `note` ไทยได้):**

ตัวอย่างย่อ 1 ชุด — ฝนตกกลาง `ep03_shot04` แล้ว QA PASS:

Input (ย่อ):
```json
{
  "shot_id": "ep03_shot04",
  "qa_status": "PASS",
  "asset": "vid_ep03_shot04.mp4",
  "observed": "ฝนตกกลางช็อต — ผม+ไหล่ฝน (char01_fon) เปียกชัด, มือขวายังถือซองจดหมายแต่ซองเริ่มยับ, ตาแดงขอบเปียก กรามเกร็ง ไหล่ห่อเกร็งจากฝน, จบช็อตอยู่ third ซ้าย มองไปทางขวาจอ"
}
```

Output:
```json
{
  "ledger_id": "led_ep03_02",
  "scope": "episode",
  "entity": "char01_fon",
  "state_locks": {
    "costume": "school uniform, top half rain-darkened, collar clinging to skin",
    "hair": "loose black hair, wet strands stuck to cheeks",
    "wet_dry": "hair and shoulders visibly wet",
    "object_in_hand": "damp wrinkled white_envelope in right hand",
    "residual_emotion": "eyes red-rimmed, jaw tight",
    "screen_side": "left third, eyeline toward screen-right",
    "posture_tension": "shoulders hunched against the rain, body held tense"
  },
  "source": "pixel-verified",
  "valid_range": "ep03_shot05 → ep03_shot09",
  "note": "เปียกฝนตั้งแต่ shot04 — ปิด lock เมื่อเข้าบ้าน scene01_home (ตัดข้ามเวลา shot10)"
}
```

---

## WORKED EXAMPLE — 1 ตัวละคร (รูปแบบตาม zhao-yu profile)

ตัวละครสมมติของ series ตัวอย่าง: `char01_fon` (ฝน) — โครงเดียวกับ Character §1.2

**Identity anchor (ก้อน verbatim — copy ท่อนนี้เข้าทุก keyframe/image prompt ห้ามแก้แม้แต่คำเดียว · video prompt ใช้ short lock ตาม §3 ข้อ 5):**

```
young Thai woman named "Fon", early 20s, round soft face, warm tan skin,
large dark brown eyes with straight black shoulder-length hair and thin
side-swept bangs, small silver stud earrings, slim build
```

- `sheet_asset`: `char01_fon_sheet.png` (named reference sheet — ป้ายชื่อ "FON" บนชีตจริง ตาม method ใน identity-lock: model ใช้ชื่อบนชีตเป็นตัวยึด) → เป็น **Image 1** ทุก prompt
- `wardrobe_default`: `"white school uniform blouse, navy pleated skirt"` — state ตั้งต้นของ ledger (contracts §1.2)
- Ledger ณ `ep03_shot06`:
  - `led_series_01` (scope series, planned, ไม่มี `valid_range` = คลุมทั้งเรื่องตาม §2): silver stud earrings ติดตัวทุกฉาก
  - `led_ep03_02` (scope episode, pixel-verified): entry เปียกฝนจากตัวอย่าง I/O ข้างบน — active เพราะ shot06 อยู่ใน `ep03_shot05 → ep03_shot09`
- ผลใน keyframe prompt ของ 05: CONTINUITY BLOCK render อัตโนมัติ = REFERENCES (Image 1 = `char01_fon_sheet.png` identity · Image 2 = costume ref ชุดนักเรียน · Image 3 = `scene02_school.png`) + identity anchor ก้อนบนแบบคำต่อคำ + state locks เปียกฝนครบ 7 ช่อง + ประโยคปิด positive lock
- ผลใน video prompt ของ 06: **short lock 1 บรรทัด** "Fon keeps the same face, hairstyle, outfit, body proportions and silhouette as the start frame throughout" (§3 ข้อ 5 — ไม่วาง anchor เต็มก้อน) + "hair and shoulders stay wet, damp white_envelope stays in her right hand" — ตัดส่วน REFERENCES/บรรยายฉากออก ไม่บรรยายภาพซ้ำ (keyframe เป็น first frame แล้ว)

---

## NOTES (ไทย — ข้อควรระวัง)

- **กฎที่ห้ามตัดถ้าจะย่อไฟล์นี้:** (1) identity anchor verbatim ห้าม paraphrase · (2) @ImageN role เดียวชัด + priority declaration · (3) `ledger_slice` เท่านั้น ห้ามส่งทั้ง ledger · (4) pixel-verified ชนะ planned · (5) ปิด entry เก่า-เปิดใหม่ ห้ามแก้ทับ · (6) positive locks เท่านั้น
- **อย่าให้ LLM "ช่วยเกลา" anchor text** — จุดตายเงียบที่สุดคือ endpoint ปลายทางเผลอ rephrase identity block ให้สละสลวย → drift ทันทีโดยไม่มี error ใด ๆ · validator ของแอป: **keyframe prompt** = เช็ค substring ตรงตัวว่า anchor เต็มก้อนอยู่ครบ · **video prompt** = เช็คแค่ว่ามี short lock line (ชื่อตัวละคร + "keeps the same face … throughout" อ้าง start frame) — ไม่บังคับ anchor เต็ม (§3 ข้อ 5)
- **CONTINUITY BLOCK กินโควตา budget** — keyframe ≤3,200 / video ≤1,800 chars (contracts §3 + margin rule ห้ามชนเพดาน) → block ต้องนับรวมใน budget เสมอ ถ้าเกิน ให้ตัดฝั่งเนื้อช็อต ห้ามตัด identity/state locks
- **prop/สัตว์คือจุดบอดของ identity lock** — identity lock คุมหน้าคนเก่ง แต่ไม่คุมลายผ้า/สัตว์/ของ → ทะเบียน prop (§2.3) ไม่ใช่ของแถม เป็นเสาหลักที่สาม
- clip <10s drift น้อยกว่า (contracts §3) — ledger ช่วยข้ามช็อต แต่ภายในช็อตยังต้องพึ่ง duration สั้น + state lock ใน prompt

> Sources: `projects/drama-app/intel-pack/00-contracts.md` · `memory/ai-video-realism-hierarchy.md` · `memory/storyboard-gpt-image-to-seedance.md` · `memory/ai-character-identity-lock.md` · `skills/seedance-2-pro-director/SKILL.md` · `memory/characters/zhao-yu.md`
