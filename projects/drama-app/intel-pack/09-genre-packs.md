# 09 — GENRE PACKS (แกน "วิธีเล่า" · static reference)

ไฟล์นี้**ไม่ใช่ endpoint** — static reference (ตาราง §5 แถว 09 ของ `00-contracts.md`) · **สถาปัตยกรรม 2 แกน (07-11):** genre = "วิธีเล่า" (จังหวะ/hook/beat/cliffhanger/pacing) world-agnostic · **โลก/ฉาก = setting pack ไฟล์ `10-setting-packs.md`** · แอปเลือก genre × setting แล้ว inject **setting ก่อน (BASE) → genre ทับ (MODULATION)** เข้า endpoint 01/02
**lint gate:** genre pack = **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น** (มีแต่คำหน้าที่แสง — หลอดจริงอยู่ setting S2) · budget ต่อ pack ≤4,500 chars (§3) · flavor-layer เท่านั้น (ห้าม override schema §1/§6)
**backward-compat:** ไม่ส่ง genre = ไม่ inject = pipeline เดิม · ค่านอก enum = `romance-drama` · **wire logic (2 dropdown + inject order) = STEP 8 ของ migration (ดู genre-setting-design.md)**

## สารบัญ (แนว × โลก default)

| `genre` (enum §1.1) | pack | default setting |
|---|---|---|
| `romance-drama` (default) | รักดราม่า | `real-urban` |
| `comedy` | ตลก | `real-minimal` |
| `thriller-horror` | ระทึกขวัญ/สยอง | `real-dim` |
| `action` | แอ็กชัน | `real-gritty` |
| `family` | ครอบครัว/อบอุ่น | `real-home` |
| `revenge-vindication` | แก้แค้น/พลิกสะใจ | `high-society` |

ทุก genre pack ใช้ template: a) HOOK WEIGHTING · b) BEAT FLAVOR · c) ACTING GRAMMAR · d) LIGHTING FUNCTION · e) CAMERA & MOVEMENT · f) CLIFFHANGER · g) AI-GEN PITFALLS · h) PACING


### GENRE: romance-drama — รักดราม่า (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / §6 · genre ถือ "วิธีเล่า" · โลก = setting pack ประกบ (setting ก่อน → genre ทับ) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM][GEM][DIR]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | สงสาร/เจ็บแทนทันที (โดนตบ/ถูกไล่ออกจากบ้าน [DRM]) สาย "MV ปวดตับ" [mv-dir] |
| curiosity | สูง | ความลับความสัมพันธ์/ข้อความแปลก = เครื่องยนต์หลัก ("ทำไมเจ้าบ่าวหนี") |
| conflict | กลาง | เผชิญหน้า/รักต้องห้ามได้ แต่ต้องมีชั้นอารมณ์ ไม่ใช่แค่ปะทะ |
| visual | ต่ำ | อุบัติเหตุไม่ใช่ลายเซ็น — เฉพาะ "ภาพขัดสถานการณ์" (เจ้าสาวเต็มยศยืนคนเดียว) |

weight = bias ให้ 01 ไม่ใช่ข้อห้าม — [DRM] "หลัง hook ต้องพาไปหาคำตอบจริง" ยังบังคับ
- **hook slot**: romance = พันธุ์ A (ขัดความสัมพันธ์ §3) — ภาพเปิดเซ็นเนเจอร์อยู่ในก้อนนี้ (เจ้าสาวเต็มยศยืนคนเดียว/ถูกทิ้ง) → **ไม่เรียก slot** · `status-contradiction` โลกเตรียมให้แนวอื่น (S5)

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วงห้ามแตะ [DRM])
- hook: เปิดที่ "แผลความสัมพันธ์" ภาพเดียว — ถูกทิ้ง (พันธุ์ A) / [plot-device·ผิว=S6] (ข้อความไม่ควรทัก)
- setup: ปูสัมพันธ์ผ่าน [plot-device·ผิว=S6] (ของเก็บความหมาย)
- conflict: ความจริงโผล่บางส่วน — [plot-device·ผิว=S6] ครึ่งจอ / ได้ยินครึ่งประโยค · ขัดแย้งเงียบผ่านระยะห่างในเฟรม
- twist: [plot-device·ผิว=S6] ชิ้นเดิมเปลี่ยนความหมาย — ที่เข้าใจผิดมาตลอด
- cliffhanger: ค้างที่ prop/สายตา — มือค้างกลางอากาศ, [plot-device·ผิว=S6] (ข้อความเด้ง) ยังไม่กดอ่าน

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
อารมณ์จริงระหว่างแอ็กชันเสมอ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว = อารมณ์ "กลั้น" ไต่เป็น micro-beats ต่อ timecode (0-3/3-7/7-11/11-15) ด้วยกล้ามเนื้อจริง [GEM worked example]: inner brow lift + draw together, lower-lid tighten, throat swallow, chin tremble, breath catch, tear spill, slow blink
- physical cue EN: `white-knuckle grip on the ring, breath catch` · `faint closed-lip smile, barely there` · `chin tremble, lips stay pressed, no open mouth`
- deadpan: เฉพาะ punchline/twist beat — อ่านข้อความจบ `her face goes still and blank, a long held beat` แล้วค่อยปล่อย micro-beat ถัดไป

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- แสง = ขับ "ความอบอุ่นที่มีระยะห่าง" ตามบีต · ห้ามคำอารมณ์ ("sad lighting"=ผิด)
- **intimacy/setup**: soft warm key from one side, gentle wrap, low contrast
- **longing/conflict**: warm key on subject + cool counter-light from behind (= ระยะห่างทางใจ)
- **twist/cliffhanger**: ไม่ flip อำนาจ (ต่างจากแก้แค้น) — คงนุ่ม/อุ่น, falloff บีบโฟกัสที่หน้า/มือ/prop
- reflective = complexity ฟรี (ผิวจริง = โลก S2)

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่เฉพาะ 🟢 + keywords คุม · 🔴 = keywords-only · **ชื่อที่ให้ "ลุค/เกรดสี" = S4**
- intimacy/setup: slow, still, intimate close-up
- longing/conflict: handheld, subtle drift, hold the gap in frame
- twist: hold framing, minimal push-in (ห้าม "very slow push-in" ลอย → reframe เกิน ดู g)
- cliffhanger: locked hold on prop/hand/eyeline
- step-printing blur / clean still composition = movement grammar (ลุค/เกรด = S4)

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **ของค้างมือ** — [plot-device·ผิว=S6] เฉลยครึ่งแล้วถูกเก็บ · เฟรม: เห็นชื่อบนของ มือค้างที่กระเป๋า
2. **ข้อความค้างจอ** — [plot-device·ผิว=S6] เด้งยังไม่กดอ่าน · เฟรม: จอสว่างในมือเกร็ง (text-glyph=S6)
3. **คนที่สามเข้าเฟรม** — คนไม่ควรอยู่โผล่ · เฟรม: รองเท้า/เงาที่ธรณีประตู
4. **คำพูดครึ่งประโยค** — สารภาพถูกตัดกลางคำ · เฟรม: ปากเผยอ ตาอีกฝ่ายเบิกค้าง

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ (ไม่ทวน pitfalls กลาง · เรื่องคน/วัสดุ/text-prop = S6/S7)
- กอด/จับมือ/เช็ดน้ำตาให้กัน = two-body impact → แตก "ก่อนแตะ"+"หลังแตะ" คนละช็อต (เอื้อม→cut→กอดค้างจากหลัง) 02 prod_note_th [GEM]
- น้ำตา: สั่ง "cry" ตรง = open-sob เว่อร์ → micro-beats c) + `lips stay pressed, no open mouth` [GEM]
- ยิ้มเศร้า: ยิ้มแรงเกิน → `faint closed-lip smile, barely there` [GEM]
- อารมณ์ยาว: "very slow push-in" → reframe เกิน → `hold framing, minimal push-in` [GEM]

#### h) PACING (ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3])
hook ~10-15% (ช็อต 5-6s คม) · setup ~20% (6-8s) · conflict ~30% (8-10s รับ dialogue) · twist ~20% (10-12s — emotional-arc shot ที่ใช้ micro-beats จาก c) ขึ้น 15s ได้ [GEM worked example 15s]) · cliffhanger ~10-15% (4-5s ค้างภาพ)
bias นี้ห้ามชน Σduration = target_sec และ beat thickness เดิม [§3]

### GENRE: comedy — ตลก (deadpan visual comedy) (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override §1/§3/§6 · genre = วิธีเล่า ประกบ setting (setting→genre) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM][GEM][DIR]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| visual | สูง | slot `situational-incongruity` — ภาพขัดสถานการณ์ (ผิว=S5) มุกเปิด อ่านจบ 1 เฟรม |
| curiosity | กลาง | ครึ่งข้อมูลแล้วเฉลย = setup→punchline ของมุก |
| conflict | กลาง | ขัดแย้งจิ๋วประจำวัน + จริงจังเกินเหตุ = เชื้อ absurd |
| emotional | ต่ำ | สงสาร/เจ็บแทน = ดราม่า ใช้เมื่อเป็น "เอาใจช่วยแบบขำ" |

engine = จริงจังเกินเหตุ (=เชื้อมุก) → อุปสรรค physical/สถานการณ์ บานปลาย → deadpan payoff เดียว · weight = bias ไม่ใช่ข้อห้าม [DRM]
- **hook slot**: comedy เรียก `situational-incongruity` (พันธุ์ B §3) → S5 ทาผิว "แต่ง/ตัวไม่เข้ากับที่" · ไม่มีพันธุ์ A

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: ภาพขัดสถานการณ์อ่านจบใน 1 เฟรม — ยังไม่ต้องขำ แค่ "อะไรวะ" (ผิว "ไม่เข้ากับที่" = S5)
- setup: ตั้งเป้าเล็ก ๆ แบบจริงจังเกินเหตุ (ความจริงจัง=เชื้อมุก) · ซ่อน visual gag ใน deep staging ได้
- conflict: อุปสรรค physical ซ้ำ/บานปลาย ทุ่มสุดตัวอารมณ์จริงเต็ม — ตลกจากร่างกาย/สถานการณ์ ไม่ใช่สีหน้า [DIR Keaton]
- twist: จุดเฉลยมุก = deadpan moment เดียวของตอน (EN cue = c punchline) [GEM]
- cliffhanger: ความซวยรอบใหม่โผล่ในเฟรมก่อนตัวละครเห็น / punchline เปิดคำถามใหม่

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
- ระหว่างแอ็กชัน = อารมณ์จริงเต็ม (รีบจริง หอบจริง ตกใจจริง — จริงแต่ไม่เว่อร์การ์ตูน) · ห้ามหน้านิ่งตลอดเรื่อง = อืดไม่มีชีวิต [GEM]
- ลายเซ็น: หายใจถี่ตอนทุ่มแอ็กชัน → ไหล่ตกช้า+ถอนหายใจยาวครั้งเดียวตอนเฉลย — ความตัดกัน "ทุ่มเต็ม→นิ่ง" คือมุก
- physical cue EN: `genuine reactions — startled, flustered, out of breath — real but never exaggerated` · punchline: `her face goes still and blank, a long held beat, then a small sigh`
- deadpan ใช้เฉพาะ punchline/twist beat [GEM]

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- แสง = รับ tableau นิ่งตลอดบีต — staging เล่นมุก แสงห้ามดราม่า · ห้ามคำอารมณ์ ("quirky lighting"=ผิด)
- **base** = flat, even, ambient fill, cool-neutral wash — แบนเสมอกัน ไม่มี key เด่น ไม่มีเงาปั้นหน้า (un-modeled)
- **punchline beat** = แสง flat เดิม ไม่พลิก — comedy หน่วงดราม่าแสงไว้ มุก land ในเฟรมแบนสว่างนิ่ง (no flip)

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่เฉพาะ 🟢 + keywords คุม · 🔴 = keywords-only ห้ามใส่ชื่อ · ตระกูล deadpan (Keaton/Tati/Andersson/Kitano) = 🔴 data น้อย · **ชื่อที่ให้ "ลุค/เกรดสี" = S4**
- framing: locked static tableau, observational wide, deep staging, single long take, planimetric front-on symmetry
- movement/timing: long static hold → slow observational drift on non-burst beats → sudden quick burst → settle (fast-slow [DIR Kitano])

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับ)
1. ซวยใหม่โผล่ก่อนตัวเห็น — คนดูเห็นภัยก่อนตัวละคร · ค้าง: ถอนหายใจโล่ง หลังเฟรมมี [prop=S6] กำลังจะล้ม
2. เฉลยครึ่งเดียว — punchline เปิดคำถามใหม่ · ค้าง: มือหยิบ [prop=S6] ผิดชิ้นค้างกลางอากาศ
3. หน้านิ่งค้างเฟรม — deadpan hold ยาวเป็นตัวค้างเอง · ค้าง: นิ่งมอง [prop=S6] ชิ้นเดียวกลางเฟรมว่าง
4. แผนใหม่ที่แย่กว่าเดิม — คนดูรู้ว่าจะพัง · ค้าง: มือวาง [prop=S6 อุปกรณ์ใหม่] ลงโต๊ะ

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ/กล้อง (ไม่ทวน pitfalls กลาง · เรื่องคน/วัสดุ/ฉาก = S7)
- มุกกายภาพ (สะดุด/ล้ม/ชน) = movement ซับซ้อน เสี่ยง deform → 02 prod_note_th แตกช็อต ตัดข้าม impact (เห็นก่อน/ผลหลัง) [GEM]
- "funny face / comedic expression" → overact → สถานการณ์+กล้ามเนื้อ + `Underplayed, restrained, natural performance` [GEM]
- deadpan hold ยาว = หน้า drift → hold ช็อตสั้น 4–6s + `holds a still beat` + final_frame cue ชัด [GEM]
- wide observational [DIR Tati] แต่ default=medium [DRM] → วาง gag ใน mid-ground medium-wide หรือแตก insert
- burst เร็ว: ห้าม "fast" ลอย ๆ → physics `sudden quick burst, settling sharp` [GEM]
- มุกพึ่งมุมกล้อง = ล็อกมุมเฉพาะบีตนั้น (`CUT to` ตอนเฉลย) นอกนั้นปล่อย GOLDEN RULE [GEM]

#### h) PACING (ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมบังคับ)
จังหวะแนว = fast-slow [DIR Kitano]: ช็อตแอ็กชันสั้น สลับ hold นิ่ง
- hook ~10%: 4–6s ช็อตเดียว
- setup ~20%: 6–10s
- conflict ~40%: ช็อต 4–6s ต่อกันหลายช็อต (ยิ่งซวยยิ่งถี่)
- twist ~20%: 8–10s — action เฉลย + deadpan hold ท้ายช็อต
- cliffhanger ~10%: 4–6s ช็อตเดียว จบเฟรมค้าง

### GENRE: thriller-horror — ระทึกขวัญ/สยอง (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / §6 · genre ถือ "วิธีเล่า" · โลก = setting pack ประกบ (setting ก่อน → genre ทับ) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM]/[GEM]/[DIR]

#### a) HOOK WEIGHTING
weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์เดิม "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" ยังบังคับ [DRM]
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| curiosity | สูง | ข้อมูลบางส่วน+ไม่เฉลย = เครื่องยนต์ dread — เปิดด้วยความลับแล้วทั้งเรื่องไล่หาคำตอบ |
| conflict | สูง | เผชิญหน้า/กล่าวหา = แรงกดดันที่บีบขึ้นเรื่อยๆ — ใครโกหก ใครรอด |
| visual | กลาง | ภาพขัดสถานการณ์เปิดได้ แต่เผาความกลัวเร็ว — เก็บภาพช็อกไว้เป็น payoff |
| emotional | ต่ำ | สงสาร/เจ็บแทนเป็นรสดราม่า — ใช้เป็นชั้นรอง (ผูกใจกับเหยื่อ) ไม่ใช่ตัวเปิด |
- **hook slot**: thriller = ภาพ **พันธุ์ A** (ordinary frame, one wrong detail — ขัดการรับรู้ §3) → genre เก็บภาพในบีต b · ไม่เรียก slot · skin "ของผิดที่"=S6

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: เฟรมปกติที่มี "สิ่งผิดที่" 1 จุด (ordinary frame, one wrong detail) — ไม่ใช่ภาพช็อกเต็มเฟรม
- setup: กิจวัตรที่เริ่มเอียง — เงียบผิดปกติ ช็อตนิ่งยาว (near-silent room tone, long static hold)
- conflict: ตัวละครเดินเข้าหาความจริง — พื้นที่แคบลง แสงน้อยลง (narrowing space, receding light)
- twist: เฉลยที่เปลี่ยนความหมายภาพก่อนหน้า (recontextualizes an earlier frame) — ตัดสั้นหลัง build ช้า
- cliffhanger: ค้างที่ภาพ "เห็นแล้วแต่ยังไม่เข้าใจ" หรือ presence โผล่ในเฟรม

#### c) ACTING GRAMMAR
variant ของ under-direct [GEM ACTING]: ความกลัว = แช่แข็ง ไม่ใช่กรีดร้อง — อารมณ์จริงระหว่างแอ็กชัน (สะดุ้งจริง เหนื่อยจริง) แค่ไม่เว่อร์ ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง
- ลายเซ็นแนว: หายใจตื้นแล้วค้าง · กลืนน้ำลายช้า · ไหล่/กรามเกร็งครึ่งวินาที · หันช้ากว่าปกติ · กะพริบช้า
- physical cue EN: "her breath catches and goes shallow" · "shoulders tense, jaw tightens for half a second" [GEM] · "a slow swallow, eyes fixed, a long held beat"
- deadpan: เฉพาะ twist beat — ผู้คุกคามหน้านิ่งสงบตอนเฉลย ตัดกับเหยื่อที่สั่น (ห้ามใช้ก่อนหน้านั้น)

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 mood/สีพื้น=S1)
- แสง = หน้าที่ตามบีต · ห้ามคำอารมณ์ ("eerie/moody lighting" = ผิด)
- setup: even ordinary light — ธรรมดาก่อน ไม่ประกาศภัยด้วยแสง
- conflict: **receding light** — แสงถอยหนี บีบพื้นที่แคบลง
- isolation key: single hard directional source, sharp pool, hard falloff — ซ่อนผู้คุกคาม
- reflection tells threat: เงา/รีเฟลกชันเล่าผู้คุกคามแทนโชว์ตัว (พื้นสะท้อน=S2)
- NB มืด=falloff → S2/S7

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่ได้เฉพาะ 🟢 + keywords คุมเสมอ · 🔴 = keywords-only ห้ามใส่ชื่อ · **ชื่อที่ให้ "ลุค/เกรดสี" = S4**
- dread hold: static / locked-off precise camera — นิ่ง ให้ long static hold เล่น
- corridor dread: one-point perspective, dead-center vanishing point, wide lens (24mm), symmetrical framing
- uncanny: slow floating/drifting camera + off-source sound cue (audio รูปธรรม §6 ข้อ 4)

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **เห็นแต่ไม่เข้าใจ** — ค้างวัตถุที่ยังไม่เฉลย · เฟรม: "ของผิดที่" (ผิว=S6)
2. **presence ในรีเฟลกชัน** — สิ่งที่ไม่ควรอยู่โผล่ในพื้นสะท้อนหลังตัว (พื้นสะท้อน=S2) · เฟรม: เงาร่างที่สอง
3. **เสียงผิดที่** — ภาพค้างตัวหยุดหันช้าๆ + audio event รูปธรรม (เสียงเคาะจากห้องที่ควรว่าง) §6 ข้อ 4
4. **threshold** — ค้างที่ทางผ่านแง้ม/แสงลอดใต้ช่อง มือแตะค้าง (threshold·ผิว=S6)

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ (ไม่ทวน pitfalls กลาง · เรื่องหลอด/วัสดุ/มืด = S2/S7)
- คำกลัวตรงๆ ("terrified, screams") → overact AI-tell [GEM ACTING] → physical cue (c) + "underplayed, restrained, natural performance"
- jump scare ช็อตเดียว = fast subject+fast camera พร้อมกัน → jitter [GEM] → ให้ 02/04 แตกเป็น build shot + reveal shot (shot-breaker + prod_note_th)
- ผู้คุกคาม/ผี render เต็มตัว → เสี่ยงหลุด 3D/การ์ตูน → เผย partial (เงา สะท้อน ขอบเฟรม) + video prompt ล็อก positive "photorealistic live-action throughout" (negative tail เฉพาะ keyframe 05 — §6 ข้อ 5)

#### h) PACING (dread = build ช้า / กระชากสั้น)
ค่าจาก steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ
- hook ~10%: 4–6s กระแทกเร็ว
- setup ~25%: 8–12s/ช็อต — long static hold ยืด dread
- conflict ~35%: 6–8s/ช็อต จังหวะบีบถี่ขึ้น
- twist ~10%: 4–5s ตัดสั้นหลัง build ช้า (contrast = impact [GEM])
- cliffhanger ~20%: 8–10s ค้างเฟรมนิ่งนาน

### GENRE: action — แอ็กชัน (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / §6 · genre ถือ "วิธีเล่า" · ประกบ setting (setting→genre) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM][GEM][DIR][realism]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| visual | สูง | นิยาม visual hook = อุบัติเหตุ/ภาพอันตรายชวนตกใจ [DRM] — คือภาพเปิดธรรมชาติของแอ็กชัน |
| conflict | สูง | เปิดเผชิญหน้า/ไล่ล่า = แกนแนว — คนดูอยากรู้ใครแพ้ใครรอด [DRM] |
| curiosity | กลาง | ใช้เป็นปม "ของ/ข้อมูลที่ทุกฝ่ายไล่ล่า" ขับเรื่องได้ แต่ไม่ใช่ภาพเปิดหลัก |
| emotional | ต่ำ | ใช้เมื่อ stake = คนใกล้ตัวถูกคุกคาม — ตัวเสริม ไม่ใช่จุดแข็งแนว |

weight = bias [DRM] ไม่ใช่ข้อห้าม — เกณฑ์ "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" ยังบังคับ
- **hook slot**: visual hook = ภาพอันตราย พันธุ์ A (genre ถือความสัมพันธ์อันตราย: chase/ถูกกด/impact) · setting ทาผิว slot `danger-arena` → S5 · plot-device "ของที่ทุกฝ่ายไล่ล่า" ผิว=S6

#### b) BEAT FLAVOR
(โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ — นี่คือรสเท่านั้น)
- hook: เปิดกลางอันตรายที่เห็นครบใน 1 เฟรม (mid-chase, ถูกจับกด) — opens mid-danger (สนาม=ผิว S5)
- setup: ลมหายใจก่อนพายุ — ตั้ง stake + ผู้ไล่ล่าผ่านภาพ (ใครถืออะไร ใครขวางใคร) ไม่ใช่คำอธิบาย
- conflict: การปะทะหลัก — 1 การกระทำใหญ่ต่อบีต (breach / chase / standoff) แล้วแตกเป็นหลายช็อตตาม g)
- twist: reversal ที่เห็นเป็นภาพเดียว — ผู้ล่ากลายเป็นผู้ถูกล่า / พันธมิตรหันอาวุธกลับ
- cliffhanger: ค้างตรง impact ที่ยังไม่ land — เห็นอันตรายชัด แต่ไม่เห็นผลลัพธ์

#### c) ACTING GRAMMAR
variant ของ under-direct [GEM ACTING]: ระหว่างแอ็กชัน = อารมณ์จริงเต็ม (เหนื่อยจริง กลัวจริง) แค่ไม่เว่อร์ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว: หายใจหอบหลังออกแรง, ไหล่/กรามเกร็งก่อนปะทะ, มือสั่นค้างหลังพ้นอันตราย
- physical cues EN: "chest heaving, out of breath" · "shoulders tense, jaw tightens" [GEM] · "knuckles white around the grip"
- deadpan: เฉพาะ punchline/twist beat เท่านั้น [GEM] — เช่น one-liner นิ่งหลังรอด แล้วค่อยหอบ

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- แสง = เพิ่มน้ำหนัก/ความคมการปะทะตามบีต · ห้ามคำอารมณ์ ("sad lighting"=ผิด)
- **action/impact key** = hard, directional, single-source, sharp falloff into deep shadow
- **setup key** = flat, even, overhead fill (กลาง ๆ ให้อ่าน stake)
- **spectacle beat** = low backlight from behind, long shadows toward camera (คู่ orbit + grade S4)

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่เฉพาะ 🟢 + keywords คุม · 🔴 = keywords-only · **ชื่อที่ให้ลุค/เกรด/สภาพอากาศ = S4**
- epic-grit: deep focus, wide lens, dynamic tracking and crane movement (ชื่อ+weather=S4)
- grounded-real: handheld tension (ชื่อ+practical=S4)
- hero-spectacle: constant moving camera, low-angle hero orbit (backlight/flare=S4)

#### f) CLIFFHANGER PATTERNS
(chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. Impact ค้าง — freeze หนึ่งจังหวะก่อนถึงตัว · เฟรมค้าง: กำปั้นห่างใบหน้าหนึ่งฝ่ามือ ตาเบิกกว้าง
2. ผู้ล่าเข้าเฟรม — ตัวเอกเพิ่งคิดว่ารอด · เฟรมค้าง: เงาร่างใหม่ทาบทับตัวเอกจากด้านหลัง
3. ของหลุดมือ — [plot-device: ของที่ทุกฝ่ายไล่ล่า · ผิว=S6] ตกไปฝั่งศัตรู · เฟรมค้าง: มือศัตรูหยิบของขึ้นจากพื้น close-up
4. ทางตัน — หนีมาสุดทาง (สุดสนาม=ผิว S5) · เฟรมค้าง: ยืนขอบสุดทาง หันเจอผู้ไล่ยืนเต็มประตู

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ/กล้อง (ไม่ทวน pitfalls กลาง · เรื่องวัสดุ/ฝุ่น/สะท้อน = S7)
1. ท่าต่อสู้/movement ซับซ้อน = character deform [GEM PITFALLS] → 1 action/ช็อต 4–8s, แตก fight หลาย prompt (02 prod_note_th shot-breaker), coverage MS/CU (medium=default [DRM])
2. "fast" ลอยๆ = jitter [GEM] → บรรยาย physics แทนความเร็ว: น้ำหนักตัวกระแทก, รองเท้าไถลพื้น, ผ้า/ผมสะบัดตามแรง (secondary motion+foot contact [realism])
3. wide→close ในช็อตเดียว = morph → "rapid hyperzoom, heavy directional motion blur, keep final frame sharp" [GEM] · ยังเพี้ยน = แตก 2 ช็อต + cut
4. fast camera + fast subject + ฉากซับซ้อนพร้อมกัน = ห้าม [GEM] → เร็วทีละชั้น: กล้องนิ่ง-ตัวเร็ว / กล้อง track-ตัวคุมจังหวะ
5. impact ไร้น้ำหนัก (floaty) → เขียน weight+impact ทุกจุดปะทะ [realism] (วัสดุกระเด็น ฝุ่น/เศษ=S7)

#### h) PACING
(ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ)
- hook ~10–15%: ช็อต 4–6s กระแทกทันที
- setup ~20%: ช็อต 8–10s ให้คนดูหายใจ + อ่าน stake
- conflict ~35–40%: หลายช็อตสั้น 4–8s (1 action/ช็อต) — ห้ามยัดฉากปะทะลงช็อตยาวช็อตเดียว
- twist ~15%: 6–8s ให้ reversal อ่านชัด
- cliffhanger ~10–15%: 4–6s จบที่เฟรมค้างคม

### GENRE: family — ครอบครัว/อบอุ่น (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / §6 · genre ถือ "วิธีเล่า" · โลก = setting pack ประกบ (setting ก่อน → genre ทับ) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM][GEM][DIR][CAST]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | ลายเซ็นแนว: ทำให้ "รู้สึก" ทันทีแบบ warm restrained (คิดถึง/เอ็นดู/เจ็บแทนเงียบ ๆ) ไม่ใช่ดราม่าตบตี |
| curiosity | กลาง | ความลับข้ามรุ่นทำงานดี (จดหมายเก่า/รูปในลิ้นชัก — ผิว=S6) แต่ต้องอุ่น ไม่หลอน |
| visual | กลาง | hook พันธุ์ A (ขัดความสัมพันธ์) — ภาพขัดสถานการณ์ในบ้าน (โต๊ะจัดครบแต่เก้าอี้ว่าง 1 ตัว / จานเกินมา 1 ใบ) |
| conflict | ต่ำ | เผชิญหน้าแรงขัดโทนอบอุ่น — เก็บความขัดแย้งเล็กไว้ช่วง conflict แทนการเปิดเรื่อง |

weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์ [DRM] "เรื่องหลัง hook ต้องพาไปหาคำตอบของ hook จริง" ยังบังคับทุกตัว
- **hook slot**: family ใช้ hook **พันธุ์ A (ขัดความสัมพันธ์ §3)** — ภาพเปิด "one warm frame, one missing element" เก็บไว้ในก้อน genre (ความหมายจากความสัมพันธ์ ไม่ใช่โลก) · family ไม่เรียก slot พันธุ์ B → S5 ว่าง

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: ภาพอบอุ่นที่มีรอยแหว่ง 1 จุด — one warm frame, one missing element (an empty chair, an extra plate) [พันธุ์ A เก็บใน genre]
- setup: กิจวัตรในบ้านเล่าความสัมพันธ์ผ่านมือ+ของ — domestic routine, hands passing objects (ผิวของ = S6)
- conflict: ขัดแย้งเล็กในบ้าน/ข้ามรุ่น เสียงไม่ขึ้น — short clipped sentences, a door closed gently, not slammed
- twist: ของชิ้นเล็กเปลี่ยนความหมายทั้งเรื่อง — [plot-device·ผิว=S6] a kept object quietly revealed
- cliffhanger: คืนดีครึ่งทางแล้วค้างไว้ — a reconciling gesture offered, not yet answered

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
อารมณ์จริงระหว่างแอ็กชันเสมอ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว = อารมณ์ไหลลงมือ/ไหล่/ลมหายใจช้า มากกว่าหน้าและน้ำเสียง
physical cues: "hands pause mid-fold, then resume slower" · "shoulders soften, one slow exhale through the nose" · "lips part to speak, then close, a small swallow"
deadpan ใช้เฉพาะ punchline/twist beat (หน้านิ่ง+ทิ้งเฟรมตอนเฉลย) เท่านั้น [GEM ACTING]

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- แสง = ตัวโอบอารมณ์อบอุ่นตามบีต · ห้ามคำอารมณ์ ("cozy sad lighting" = ผิด)
- **base key** = soft warm enveloping key + gentle low-contrast fill, soft falloff — โอบหน้า ไม่กระด้าง
- **hook (missing-element)** = warm frame with one cool/negative pocket marking the empty seat — จุดว่างเย็น 1 จุดชี้รอยแหว่ง
- **twist (kept-object reveal)** = a small warm accent lifts the revealed keepsake out of soft ground
- casting RULE [CAST]: หน้าอบอุ่นสมจริง มีร่องรอยวัย — house-style+ช่วงวัย = S3

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่ได้เฉพาะ 🟢 + keywords คุม · 🔴 = keywords-only ห้ามใส่ชื่อ · **ชื่อที่ให้ "ลุค/เกรดสี" = S4**
- base movement: gentle sweeping single camera move + warm ensemble staging, overlapping natural blocking
- reveal/emotion beat: awe close-up + eye trace — ตามสายตา ค้างใกล้ให้ของ/สีหน้าเล่น
- conflict beat: still, restrained framing — นิ่ง ไม่ไล่ตาม ปล่อยระยะห่างในเฟรมเล่าความห่าง

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **มือยื่นค้าง** — gesture คืนดีถูกยื่นแต่ยังไม่ถูกรับ · เฟรมค้าง: [prop·ผิว=S6] ถูกวางตรงหน้า อีกคนยังไม่เงยหน้า
2. **ของที่เพิ่งเข้าใจ** — [plot-device·ผิว=S6] เดิมถูกเผยความหมายใหม่ · เฟรมค้าง: close-up ของเก่าโผล่ครึ่งใบจากที่เก็บ
3. **ประตูแง้ม** — คนกลับมา/กำลังจะไป ค้างที่ธรณีประตู · เฟรมค้าง: เงายืนในประตูแง้ม แสงอุ่นลอดด้านหลัง
4. **คำที่ยังไม่ได้พูด** — ประโยคสำคัญถูกตัดก่อนคำตอบ · เฟรมค้าง: ปากเผยอค้าง อีกคนเพิ่งหันมา

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ (ไม่ทวน pitfalls กลาง · เรื่องคน/วัสดุ/ยุค = S7)
- ฉากกอด/ป้อนข้าว (two-body overlap) → shot-breaker: แตกบีตเป็น approach → hands close-up → faces หลังสัมผัส [GEM] · 02 ใส่ prod_note_th
- NB: age-drift ข้ามรุ่น / จาน-อาหารเปลี่ยนเอง / golden-hour ต่อเนื่อง = คน/วัสดุ/แหล่งแสงจริง → setting S7

#### h) PACING (steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ)
- สัดส่วนเวลา 5 ช่วงโดยประมาณ: hook 10% · setup 25% · conflict 30% · twist 15% · cliffhanger 20%
- duration bias: hook 5–6s (ดึงอารมณ์โดยไม่กระชาก) · setup 8–10s (อยู่กับ routine ได้นาน) · conflict 6–8s/shot · twist 4–6s (เฉลยเงียบสั้นคม) · cliffhanger 6–8s (hold ท่าค้าง)

### GENRE: revenge-vindication — แก้แค้น/พลิกสะใจ (ผอม)
> flavor เท่านั้น — ห้าม override §1/§3/§6 · genre="วิธีเล่า" · ประกบ setting→genre · **0 ชื่อหลอด/วัสดุ/สีพื้น=lint gate** · trace [DRM][GEM][DIR][CAST][TD teardown]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | อัดอั้น→สะใจตอน payoff |
| conflict | สูง | white-black polarity |
| curiosity | กลาง | ตัวตนซ่อน=ปมรอ status-flip |
| visual | ต่ำ | ภาพขัดสถานะเปิด, เก็บ flip เป็น payoff (slot=ล่าง) |

engine [TD] = **audience-ahead/dramatic irony** — คนดูรู้ความลับ/ปลายทางก่อนตัวละคร → humiliation ทนดูได้+รอสะใจ · ขาว-ดำสุดขั้ว ตัวร้ายเลวไร้ backstory · weight=bias [DRM]
- **hook slot** `status-contradiction` (พันธุ์ B ขัดสถานะสังคม §3) → S5 ทาผิว "ชุดโทรม/งานหรู" · ไม่มีพันธุ์ A
- **stack 2-3 hook/นาทีแรก** [TD] resolve premise เร็ว · เปิด (=คนดูรู้ก่อน): cold-open โชว์พลัง / flash-forward จุดจบ / news+ภาพขัดสถานะ

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: humiliation สาธารณะจบใน 1 เฟรม — สาดน้ำ/ตบ/ทิ้งต่อหน้าคนดู (venue+ฝูงชน=ผิว S5) · audience-ahead ตาม a
- setup: สถานะต่ำ + ตัวร้ายเลวเชิงสัมพันธ์ (แม่เลี้ยง/แม่สามี/คู่แข่ง) · ซ่อน "ตัวตนจริง" ใน [plot-device: กลไกพลิกสถานะ·ผิว=S6] = ระเบิดเวลา
- conflict: **กดก่อนพลิก** [TD] humiliation stack หลายครั้งก่อน payoff แรก — ห้ามชนะหลังโดนครั้งแรก (ยิ่งกด=ยิ่งเพิ่ม payoff)
- twist: status-flip reveal **แต่ undercut ตั้งใจ** [TD] mid-win downgrade (รู้บางตัว/"ถูกใช้") กันสะใจเร็ว → full payoff = **cascading 3-4 sub-reveal** · **ลงโทษ 2 โหมด**: สะท้อนเหยียบคืน (ดราม่า) vs legal/institutional
- cliffhanger: ตัวร้ายเพิ่งรู้/เหยียบกลับยังไม่ land · **arc จบ = seed hook ใหม่ทันที** [TD] (ตัว/ภัยใหม่=continuation)

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
2 register: humiliation "กลั้น" ไม่โต้กลับ → reveal "นิ่งเย็นทวงคืน" ไม่ตะโกน · ตัวร้ายเย็นชา ห้ามสั่ง "evil/sneer"
- humiliation cue EN: `jaw clenches, eyes drop, one hard swallow, chin stays level, no open sob`
- reveal cue EN (deadpan hold [GEM]): `still a beat, chin lifts, cool gaze, faint mouth-corner curl`
- villain: `slow up-down glance, chin raised` → realize `smug grin drains, face goes still`

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- casting RULE [CAST]: polarity มาจากการกระทำ ไม่ใช่หน้าตา → ห้าม "plain/ugly villain" (house-style หน้า=S3)
- แสง = ตัว flip สถานะตามบีต · ห้ามคำอารมณ์ ("cruel lighting" = ผิด)
- **humiliation key** = harsh, flat, unflattering, cold-toned, top-down wash (drains dignity)
- **reveal key** = flip: low warm side-key + strong rim + deep falloff (พลิกอุ่น เด่นจากพื้นมืด)
- **status-flip**: twist สลับ humiliation→reveal key ในซีนเดียว (warm-cool=แกน)

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎชื่อผู้กำกับ · ลุค/palette/ชื่อที่ให้ลุค=S4)
- กฎ 🟢/🔴 [DIR]: ใส่ชื่อผู้กำกับได้เฉพาะ 🟢 + keywords คุม · 🔴=keywords-only ห้ามชื่อ · **ชื่อที่ให้ "ลุค/เกรดสี"=S4**
- humiliation/escalation: static / locked-off — กล้องนิ่งมองเหยื่อถูกกด (ไม่ช่วยเหลือ)
- reveal/flip: locked-off, precise, still — นิ่งให้ composure เป็นตัวเล่น
- vindication: slow low-angle push toward hero + crowd out-of-focus

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับ)
> กลไก [TD]: threat/ไพ่ประกาศ → hard cut ก่อน land → payoff ซีนถัดไป · หรือ contrast-cut (โทษหนัก→ตัดฉากสุขอีกฝ่าย)
1. **ตัวร้ายเพิ่งเริ่มรู้** — เยาะ→ตระหนก · เฟรม: รอยยิ้มยะโสค้างครึ่ง ตาเบิก
2. **reveal ครึ่งใบ/ไพ่ยังไม่เปิด** — เผยเสี้ยว หรือ "รู้ไหมว่าฉันคือ…" ถูกตัด · เฟรม: นิ้วกด [plot-device·ผิว=S6] ค้าง
3. **คนอำนาจกว่าเข้าเฟรม** — ผู้หนุนตัวจริง (อำนาจเหนือกว่า) หลังเหยื่อ · เฟรม: เงากลุ่มคนที่ประตู

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ (ไม่ทวน pitfalls กลาง · คน/วัสดุ/crowd=S7)
- ตบ/ผลัก/สาดน้ำ/ปาของ/ฉีกเอกสาร = two-body impact → 02 shot-breaker แตก "ก่อนแตะ"+"หลังแตะ" [GEM]
- ห้าม gore/เลือด → ผลเป็นร่องรอยแทนโชว์เลือด (ผิววัสดุที่แตก = S7)
- "evil/smug" ตรงๆ → overact การ์ตูน [GEM] → cue c) + `underplayed, controlled menace, natural`

#### h) PACING (steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมบังคับ)
จังหวะ [TD] = **2 ระดับ**: mid-reveal snap ถี่ <60วิ (จบในฉาก ไม่มีฉากว่าง) ซ้อน **finale-tier ยืด rug-pull ตัวเดียว** — slow-burn เฉพาะ reveal สุดท้าย (=ช้าสุด cascading) · **escalation = tier ไม่ใช่ intensity** [TD]: ยกระดับ family→สถาบัน→อำนาจใหญ่ ทันทีที่ tier เดิมเก็บ
สัดส่วน: hook 10–15%/5–6s · setup 20%/6–8s · conflict 30%/6–8s · twist 20%/10–12s (reveal ท้าย≤15s) · cliffhanger 10–15%/4–5s

> Sources: `intel-pack/00-contracts.md` · `intel-pack/10-setting-packs.md` · `memory/vertical-drama-basics-dramy.md` · `memory/seedance-knowledge.md` · `memory/director-styles-knowledge.md` · `memory/mv-directors-knowledge.md` · `memory/ai-video-realism-hierarchy.md` · `memory/feedback-drama-character-casting.md` · `projects/drama-app/teardown-results.md`
