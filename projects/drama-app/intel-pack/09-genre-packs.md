# 09 — GENRE PACKS (ส่วนขยาย genre · static reference)

ไฟล์นี้**ไม่ใช่ endpoint** — เป็น static reference file ไม่มี LLM call (ตาราง §5 แถว 09 ของ `00-contracts.md`)
แอปเลือก section ตาม `SeriesBible.genre` (§1.1) แล้ว inject ทั้ง block เป็น `PromptEnvelope.genre_pack` (§1.7) ให้ endpoint 01 (series-bible) และ 02 (episode-script)
ทุก pack เป็น **flavor layer เท่านั้น** — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ contracts · budget ต่อ pack ≤4,500 chars (§3)
**ไม่ส่ง `genre` = ไม่ inject `genre_pack` = pipeline ทำงานเหมือนเดิมทุกตัวอักษร** (ค่านอก enum = ปฏิบัติเป็น `romance-drama`)

## วิธี inject

1. อ่าน `SeriesBible.genre` — ไม่มี field นี้ = จบ ไม่ inject อะไรเลย (พฤติกรรมเดิม) · มีแต่ไม่อยู่ใน enum = ปฏิบัติเป็น `romance-drama` (default §1.1)
2. ตัด block ตั้งแต่หัว `### GENRE: <genre>` ถึงก่อนหัว `### GENRE:` ถัดไป (pack สุดท้ายตัดถึงก่อน `> Sources:`) — ใช้เป็น string ล้วน ไม่แปลงรูป
3. ใส่เป็น `PromptEnvelope.genre_pack` ก่อนเรียก endpoint 01/02 — endpoint อื่นยังไม่รับ field นี้ในส่วนขยายรอบนี้

## สารบัญ

| `genre` (enum §1.1) | pack |
|---|---|
| `romance-drama` (default) | รักดราม่า (baseline) |
| `comedy` | ตลก (deadpan visual comedy) |
| `thriller-horror` | ระทึกขวัญ/สยอง |
| `action` | แอ็กชัน |
| `family` | ครอบครัว/อบอุ่น |

ทุก pack ใช้ template หัวข้อเดียวกัน: a) HOOK WEIGHTING · b) BEAT FLAVOR · c) ACTING GRAMMAR · d) VISUAL & LIGHTING GRAMMAR · e) DIRECTOR KEYWORD PRESETS · f) CLIFFHANGER PATTERNS · g) AI-GEN PITFALLS · h) PACING

### GENRE: romance-drama — รักดราม่า (baseline)
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ 00-contracts · ที่มา: [DRM]=vertical-drama-basics-dramy · [GEM]=seedance-knowledge · [director-styles] · [mv-directors]=mv-directors-knowledge

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | หัวใจของแนว — สงสาร/เจ็บแทนทันที (นางเอกโดนตบ/ถูกไล่ออกจากบ้าน = ตัวอย่างตรง [DRM]) ตรงสาย "MV ปวดตับ" ไทย [mv-directors] |
| curiosity | สูง | ความลับความสัมพันธ์/ข้อความแปลก ๆ = เครื่องยนต์หลักของแนว ("ทำไมเจ้าบ่าวหนี") |
| conflict | กลาง | เผชิญหน้า/ความสัมพันธ์ต้องห้ามใช้ได้ แต่ต้องมีชั้นอารมณ์รองรับ ไม่ใช่แค่ปะทะ |
| visual | ต่ำ | ภาพอันตราย/อุบัติเหตุไม่ใช่ลายเซ็นแนว — ใช้เฉพาะ "ภาพขัดสถานการณ์" (เจ้าสาวเต็มยศยืนคนเดียว) |

weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์ [DRM] "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" ยังบังคับทุกตัว

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วงห้ามแตะ [DRM])
- hook: เปิดที่ "แผลความสัมพันธ์" เห็นเป็นภาพเดียว — ถูกทิ้ง / แชตจากคนที่ไม่ควรทัก
- setup: ปูสัมพันธ์ผ่าน prop ใกล้ตัว — ring, chat thread, old photo, keepsake (ของ = ตัวเก็บความหมาย)
- conflict: ความจริงโผล่บางส่วน — เห็นแชตครึ่งจอ / ได้ยินครึ่งประโยค · ขัดแย้งเงียบผ่านระยะห่างในเฟรม
- twist: ของชิ้นเดิมเปลี่ยนความหมาย — จดหมาย/แหวนที่เข้าใจผิดมาตลอด
- cliffhanger: ค้างที่ prop/สายตา — มือค้างกลางอากาศ, ข้อความเด้งยังไม่กดอ่าน

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
อารมณ์จริงระหว่างแอ็กชันเสมอ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว = อารมณ์ "กลั้น" ไต่เป็น micro-beats ต่อ timecode (0-3/3-7/7-11/11-15) ด้วยกล้ามเนื้อจริง [GEM worked example]: inner brow lift + draw together, lower-lid tighten, throat swallow, chin tremble, breath catch, tear spill, slow blink
- physical cue EN: `white-knuckle grip on the ring, breath catch` · `faint closed-lip smile, barely there` · `chin tremble, lips stay pressed, no open mouth`
- deadpan: เฉพาะ punchline/twist beat — อ่านข้อความจบ `her face goes still and blank, a long held beat` แล้วค่อยปล่อย micro-beat ถัดไป

#### d) VISUAL & LIGHTING GRAMMAR
- mood = visual noun EN ล้วน [GEM]: golden haze, halation, bloom, film grain, blue-grey mist, rain-streaked glass — ต่อท้าย style_stack / style_note_th ได้
- lighting = physical เท่านั้น [GEM LIGHTING]: `single warm tungsten lamp from frame left, cool rain light through window behind` · `soft window light, late-afternoon low sun` — ห้ามคำอารมณ์ ("sad lighting" = ผิด)
- reflective surface = ความซับซ้อนฟรี [GEM]: wet pavement, rain on glass, tears catching golden hour

#### e) DIRECTOR KEYWORD PRESETS [director-styles]
- **Neon Longing** (🟢 Wong Kar-wai + keywords คุมเสมอ): `neon-lit, step-printing blur, saturated red/green, handheld, melancholic close-up`
- **Quiet Indie Ache** (keywords-only — สาย 🔴 ห้ามใส่ชื่อ): `minimalist observer, slow camera, sunlit white space, analog, Instagram framing`
- **Poetic Monochrome MV** (keywords-only [mv-directors]): `black and white, intimate, poetic, clean still composition`

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **ของค้างมือ** — prop เฉลยครึ่งเดียวแล้วถูกเก็บ · เฟรมค้าง: มุมแคบเห็นชื่อบนซองจดหมาย มือค้างที่กระเป๋า
2. **แชตค้างหน้าจอ** — ข้อความ/typing เด้งแต่ยังไม่กดอ่าน · เฟรมค้าง: จอสว่างในมือที่เกร็ง
3. **คนที่สามเข้าเฟรม** — คนที่ไม่ควรอยู่โผล่ · เฟรมค้าง: รองเท้า/เงาที่ธรณีประตู
4. **คำพูดครึ่งประโยค** — สารภาพถูกตัดกลางคำ · เฟรมค้าง: ปากเผยอ ตาอีกฝ่ายเบิกค้าง

#### g) AI-GEN PITFALLS (เฉพาะแนว — ไม่ทวน pitfalls กลาง)
- ซีนกอด/จับมือ/เช็ดน้ำตาให้กัน → แตกเป็น "ก่อนแตะ" + "แตะแล้ว" คนละช็อต (มือเอื้อม → cut → กอดค้างจากหลัง) — 02 ใส่ prod_note_th ให้ shot-breaker แตก
- น้ำตา: สั่ง "cry" ตรง ๆ = open-sob เว่อร์ → ใช้ micro-beats จาก c) + `lips stay pressed, no open mouth` [GEM tuning]
- ยิ้มเศร้า: model ยิ้มแรงเกินสั่ง → `faint closed-lip smile, barely there` [GEM tuning]
- แชต = prop หลักของแนวแต่ชนความเสี่ยง text → เล่าผ่าน reaction + insert keyframe ภาพนิ่งของจอ ไม่ให้ตัวอักษรขยับในวิดีโอ
- ซีนอารมณ์ยาว: "very slow push-in" → model reframe เกินตั้งใจ → `hold framing, minimal push-in` [GEM tuning]

#### h) PACING (ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3])
hook ~10-15% (ช็อต 5-6s คม) · setup ~20% (6-8s) · conflict ~30% (8-10s รับ dialogue) · twist ~20% (10-12s — emotional-arc shot ที่ใช้ micro-beats จาก c) ขึ้น 15s ได้ [GEM worked example 15s]) · cliffhanger ~10-15% (4-5s ค้างภาพ)
bias นี้ห้ามชน Σduration = target_sec และ beat thickness เดิม [§3]

### GENRE: comedy — ตลก (deadpan visual comedy)
> flavor layer เท่านั้น — ห้าม override §1/§3/§6 ของ 00-contracts · trace: [DRM]=vertical-drama-basics · [GEM]=seedance-knowledge · [DIR]=director-styles-knowledge

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| visual | สูง | เล่าด้วยภาพล้วน — "ภาพขัดสถานการณ์/แต่งตัวไม่เข้ากับที่" [DRM] = มุกเปิดตรง ๆ |
| curiosity | กลาง | ให้ข้อมูลครึ่งเดียวแล้วค่อยเฉลย = โครง setup→punchline ของมุก |
| conflict | กลาง | ขัดแย้งจิ๋วในชีวิตประจำวันแต่ตัวละครจริงจังเกินเหตุ = เชื้อ absurd |
| emotional | ต่ำ | สงสาร/เจ็บแทน [DRM] = โทนดราม่า — ใช้ได้เมื่อแปลงเป็น "เอาใจช่วยแบบขำ" |

weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์เดิม "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" [DRM] ยังบังคับ

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: ภาพขัดสถานการณ์อ่านจบใน 1 เฟรม — ยังไม่ต้องขำ แค่ "อะไรวะ"
- setup: ตั้งเป้าเล็ก ๆ แบบจริงจังเกินเหตุ (ความจริงจัง=เชื้อมุก) · ซ่อน visual gag ใน deep staging ได้ [DIR]
- conflict: อุปสรรค physical ซ้ำ/บานปลาย ทุ่มสุดตัวอารมณ์จริงเต็ม — ตลกจากร่างกาย/สถานการณ์ ไม่ใช่สีหน้า [DIR Keaton]
- twist: จุดเฉลยมุก = deadpan moment เดียวของตอน — `face goes still, a long held beat, a small sigh` [GEM]
- cliffhanger: ความซวยรอบใหม่โผล่ในเฟรมก่อนตัวละครเห็น / punchline เปิดคำถามใหม่

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
- ระหว่างแอ็กชัน = อารมณ์จริงเต็ม (รีบจริง หอบจริง ตกใจจริง — จริงแต่ไม่เว่อร์การ์ตูน) · ห้ามหน้านิ่งตลอดเรื่อง = อืดไม่มีชีวิต [GEM]
- ลายเซ็น: หายใจถี่ตอนทุ่มแอ็กชัน → ไหล่ตกช้า+ถอนหายใจยาวครั้งเดียวตอนเฉลย — ความตัดกัน "ทุ่มเต็ม→นิ่ง" คือมุก
- physical cue EN: `genuine reactions — startled, flustered, out of breath — real but never exaggerated` · punchline: `her face goes still and blank, a long held beat, then a small sigh`
- deadpan ใช้เฉพาะ punchline/twist beat [GEM]

#### d) VISUAL & LIGHTING GRAMMAR
- mood = visual noun EN (ต่อท้าย style_stack / style_note_th ได้): `sunlit white space, muted pale palette, locked static framing, deep staging` [DIR: เต๋อ-keywords/Andersson/Tati]
- lighting = physical เท่านั้น [GEM LIGHTING]: `soft even daylight from a large window frame-right, flat ambient fill, cool neutral color temperature` — แสงแบนรับ tableau นิ่ง · ห้ามคำอารมณ์ ("quirky lighting"=ผิด)

#### e) DIRECTOR KEYWORD PRESETS ([DIR] · ตระกูล deadpan+เต๋อ = 🔴 data น้อย → keywords-only ห้ามใส่ชื่อ)
1. `still-tableau`: locked static tableau, observational wide shot, deep staging, muted pale palette, single long take, visual gag, deadpan
2. `fast-slow`: long static take, sudden quick burst, deadpan stone face, silent physical comedy, restrained
3. `sunlit-minimal`: minimalist observer, slow camera, sunlit white space, analog, Instagram framing
- ชื่อใส่ได้เฉพาะ 🟢 + keywords คุมเสมอ — ที่ใกล้แนวนี้: `Wes Anderson: perfect symmetry, pastel palette, planimetric front-on, storybook`

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับ)
1. ซวยใหม่โผล่ก่อนตัวเห็น — คนดูเห็นภัยรอบต่อไปในเฟรมก่อนตัวละคร · ค้าง: ถอนหายใจโล่ง หลังเฟรมมีของกำลังจะล้ม
2. เฉลยครึ่งเดียว — punchline ตอนนี้เปิดคำถามใหม่ · ค้าง: มือหยิบของผิดชิ้นค้างกลางอากาศ
3. หน้านิ่งค้างเฟรม — deadpan hold ยาวผิดปกติเป็นตัวค้างเอง · ค้าง: นิ่งมองของชิ้นเดียวกลางเฟรมว่าง
4. แผนใหม่ที่แย่กว่าเดิม — เริ่มแผนถัดไปที่คนดูรู้ว่าจะพัง · ค้าง: มือวางอุปกรณ์ชิ้นใหม่ลงโต๊ะ

#### g) AI-GEN PITFALLS (เฉพาะแนว — ไม่ทวน pitfalls กลาง)
- มุกกายภาพ (สะดุด/ล้ม/ชน) = movement ซับซ้อน เสี่ยง deform [GEM] → 02 ใส่ prod_note_th ให้แตกช็อต ตัดข้ามจุด impact (เห็นก่อน/ผลหลัง)
- สั่ง "funny face / comedic expression" → overact การ์ตูน [GEM] → เขียนสถานการณ์+กล้ามเนื้อ + `Underplayed, restrained, natural performance`
- deadpan hold ยาว = หน้า drift/ขยับเอง [GEM] → hold เป็นช็อตสั้น 4–6s + `holds a still beat` + final_frame cue ชัด
- อยาก wide observational [DIR Tati] แต่ default ซีรีส์=medium [DRM] → วาง gag ใน mid-ground ของ medium-wide หรือแตก insert shot
- burst เร็ว: ห้าม "fast" ลอย ๆ [GEM] → บรรยาย physics `sudden quick burst, settling sharp`
- มุกที่พึ่งมุมกล้อง = ล็อกมุมเฉพาะบีตนั้น (`CUT to` ตอนเฉลย) นอกนั้นปล่อยตาม GOLDEN RULE [GEM]

#### h) PACING (ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมบังคับ)
จังหวะแนว = fast-slow [DIR Kitano]: ช็อตแอ็กชันสั้น สลับ hold นิ่ง
- hook ~10%: 4–6s ช็อตเดียว
- setup ~20%: 6–10s
- conflict ~40%: ช็อต 4–6s ต่อกันหลายช็อต (ยิ่งซวยยิ่งถี่)
- twist ~20%: 8–10s — action เฉลย + deadpan hold ท้ายช็อต
- cliffhanger ~10%: 4–6s ช็อตเดียว จบเฟรมค้าง

### GENRE: thriller-horror — ระทึกขวัญ/สยอง
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ 00-contracts · ทุกกฎ/คีย์เวิร์ด trace: [DRM]/[GEM]/[director-styles]

#### a) HOOK WEIGHTING
weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์เดิม "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" ยังบังคับ [DRM]
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| curiosity | สูง | ข้อมูลบางส่วน+ไม่เฉลย = เครื่องยนต์ dread — เปิดด้วยความลับแล้วทั้งเรื่องไล่หาคำตอบ |
| conflict | สูง | เผชิญหน้า/กล่าวหา = แรงกดดันที่บีบขึ้นเรื่อยๆ — ใครโกหก ใครรอด |
| visual | กลาง | ภาพขัดสถานการณ์เปิดได้ แต่เผาความกลัวเร็ว — เก็บภาพช็อกไว้เป็น payoff |
| emotional | ต่ำ | สงสาร/เจ็บแทนเป็นรสดราม่า — ใช้เป็นชั้นรอง (ผูกใจกับเหยื่อ) ไม่ใช่ตัวเปิด |

#### b) BEAT FLAVOR
(โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
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

#### d) VISUAL & LIGHTING GRAMMAR
- mood = visual noun EN ล้วน (ต่อท้าย style_stack / style_note_th ได้): deep shadow, blue-grey mist, halation, heavy film grain, single-hue cold tint, wet pavement reflection
- lighting = physical เท่านั้น [GEM LIGHTING]: source/direction/color temp — เช่น "single bare tungsten bulb overhead, sharp circular pool, hard falloff into black" — ห้ามคำอารมณ์ ("eerie/moody lighting" = ผิด)
- ความมืด+พื้นผิวสะท้อน (wet floor, dark window) = complexity ฟรี [GEM] — เงา/รีเฟลกชันเล่าผู้คุกคามแทนการโชว์ตัว

#### e) DIRECTOR KEYWORD PRESETS [director-styles]
ชื่อเฉพาะ 🟢 + คีย์เวิร์ดคุมเสมอ · data น้อย = keywords-only
- **fincher-cold** (🟢): "David Fincher style, low-key shadow, single-hue green tint, locked-off precise camera, cold desaturated"
- **kubrick-corridor** (🟢): "Kubrick one-point perspective, dead-center vanishing point, 24mm wide lens, symmetrical, cold sterile space"
- **uncanny-dread** (keywords-only ห้ามใส่ชื่อ): "surreal everyday interior, slow floating camera, deep shadow, uncanny dread, off-source sound"

#### f) CLIFFHANGER PATTERNS
(chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **เห็นแต่ไม่เข้าใจ** — ค้างวัตถุที่ความหมายยังไม่เฉลย · เฟรม: มุมแคบเห็นรองเท้าคู่ที่สองใต้ม่าน
2. **presence ในรีเฟลกชัน** — สิ่งที่ไม่ควรอยู่โผล่ในกระจก/หน้าต่างมืดหลังตัวละคร · เฟรม: เงาร่างที่สองในหน้าต่างดำ
3. **เสียงผิดที่** — ภาพค้างตัวละครหยุดหันช้าๆ + audio event รูปธรรม (เสียงเคาะจากห้องที่ควรว่าง) — เขียนเสียงตั้งใจตาม §6 ข้อ 4
4. **threshold** — ค้างที่ประตูแง้ม/แสงลอดใต้ประตู มือแตะลูกบิดค้าง

#### g) AI-GEN PITFALLS (เฉพาะแนว — ไม่ทวน pitfalls กลาง)
- คำกลัวตรงๆ ("terrified, screams") → overact AI-tell [GEM ACTING] → ใช้ physical cue จาก (c) + "underplayed, restrained, natural performance"
- เฟรมมืดสนิท → โมเดลเติม noise/detail มั่ว → ห้ามสั่ง "pitch black" — ล็อกแหล่งแสง physical 1 จุดเสมอ ให้ความมืด = falloff [GEM LIGHTING]
- jump scare ช็อตเดียว = fast subject+fast camera พร้อมกัน → jitter [GEM PITFALLS] → ให้ 02/04 แตกเป็น build shot + reveal shot (shot-breaker + prod_note_th)
- ผู้คุกคาม/ผี render เต็มตัว → เสี่ยงหลุด 3D/การ์ตูน → เผย partial (เงา สะท้อน ขอบเฟรม) + video prompt ล็อก positive "photorealistic live-action throughout" (negative tail เฉพาะ keyframe 05 — §6 ข้อ 5)

#### h) PACING (dread = build ช้า / กระชากสั้น)
ค่าจาก steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ
- hook ~10%: 4–6s กระแทกเร็ว
- setup ~25%: 8–12s/ช็อต — long static hold ยืด dread
- conflict ~35%: 6–8s/ช็อต จังหวะบีบถี่ขึ้น
- twist ~10%: 4–5s ตัดสั้นหลัง build ช้า (contrast = impact [GEM])
- cliffhanger ~20%: 8–10s ค้างเฟรมนิ่งนาน

### GENRE: action — แอ็กชัน
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ 00-contracts · ทุกกฎ/คีย์เวิร์ด trace ไฟล์ต้นทาง [DRM]/[GEM]/[director-styles]/[realism]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| visual | สูง | นิยาม visual hook = อุบัติเหตุ/ภาพอันตรายชวนตกใจ [DRM] — คือภาพเปิดธรรมชาติของแอ็กชัน |
| conflict | สูง | เปิดเผชิญหน้า/ไล่ล่า = แกนแนว — คนดูอยากรู้ใครแพ้ใครรอด [DRM] |
| curiosity | กลาง | ใช้เป็นปม "ของ/ข้อมูลที่ทุกฝ่ายไล่ล่า" ขับเรื่องได้ แต่ไม่ใช่ภาพเปิดหลัก |
| emotional | ต่ำ | ใช้เมื่อ stake = คนใกล้ตัวถูกคุกคาม — ตัวเสริม ไม่ใช่จุดแข็งแนว |

weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์เดิม "เรื่องหลัง hook ต้องพาไปหาคำตอบจริง" [DRM] ยังบังคับ

#### b) BEAT FLAVOR
(โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ — นี่คือรสเท่านั้น)
- hook: เปิดกลางอันตรายที่เห็นครบใน 1 เฟรม (mid-chase, ถูกจับกด) — opens mid-danger, no warm-up
- setup: ลมหายใจก่อนพายุ — ตั้ง stake + ผู้ไล่ล่าผ่านภาพ (ใครถืออะไร ใครขวางใคร) ไม่ใช่คำอธิบาย
- conflict: การปะทะหลัก — 1 การกระทำใหญ่ต่อบีต (breach / chase / standoff) แล้วแตกเป็นหลายช็อตตาม g)
- twist: reversal ที่เห็นเป็นภาพเดียว — ผู้ล่ากลายเป็นผู้ถูกล่า / พันธมิตรหันอาวุธกลับ
- cliffhanger: ค้างตรง impact ที่ยังไม่ land — เห็นอันตรายชัด แต่ไม่เห็นผลลัพธ์

#### c) ACTING GRAMMAR
variant ของ under-direct [GEM ACTING]: ระหว่างแอ็กชัน = อารมณ์จริงเต็ม (เหนื่อยจริง กลัวจริง) แค่ไม่เว่อร์ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว: หายใจหอบหลังออกแรง, ไหล่/กรามเกร็งก่อนปะทะ, มือสั่นค้างหลังพ้นอันตราย
- physical cues EN: "chest heaving, out of breath" · "shoulders tense, jaw tightens" [GEM] · "knuckles white around the grip"
- deadpan: เฉพาะ punchline/twist beat เท่านั้น [GEM] — เช่น one-liner นิ่งหลังรอด แล้วค่อยหอบ

#### d) VISUAL & LIGHTING GRAMMAR
- mood (visual noun EN ล้วน — ต่อท้าย style_stack / style_note_th ได้): amber dust, blue-grey mist, film grain, halation, heavy directional motion blur, wet pavement reflections [GEM] — reflective surface = ความซับซ้อนฟรี [GEM]
- lighting (physical เท่านั้น [GEM LIGHTING] — "sad lighting" = ผิด): "single hard warm tungsten source from frame left, sharp falloff into deep shadow" · "cool overcast daylight from above, flat even spill" · "low warm golden backlight from behind, long shadows toward camera"

#### e) DIRECTOR KEYWORD PRESETS
[director-styles] — ใส่ชื่อได้เฉพาะ 🟢 + ต้องมี keywords คุมเสมอ:
- "Epic Grit" (🟢 Kurosawa + keywords): deep focus, wide lens, weather as character (rain, dust, mud), dynamic tracking and crane movement
- "Grounded Real" (🟢 Nolan + keywords): practical-effects look, muted palette, naturalistic light, handheld tension, large-format scale
- "Hero Spectacle" (keywords-only): constant moving camera, low-angle hero orbit, golden hour backlight, lens flare

#### f) CLIFFHANGER PATTERNS
(chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. Impact ค้าง — freeze หนึ่งจังหวะก่อนถึงตัว · เฟรมค้าง: กำปั้นห่างใบหน้าหนึ่งฝ่ามือ ตาเบิกกว้าง
2. ผู้ล่าเข้าเฟรม — ตัวเอกเพิ่งคิดว่ารอด · เฟรมค้าง: เงาร่างใหม่ทาบทับตัวเอกจากด้านหลัง
3. ของหลุดมือ — object สำคัญ (หลักฐาน/กุญแจ/อาวุธ) ตกไปฝั่งศัตรู · เฟรมค้าง: มือศัตรูหยิบของขึ้นจากพื้น close-up
4. ทางตัน — หนีมาสุดทาง · เฟรมค้าง: ยืนขอบดาดฟ้า หันกลับมาเจอผู้ไล่ยืนเต็มประตู

#### g) AI-GEN PITFALLS
(เฉพาะแนว — ไม่ทวน pitfalls กลางของ contracts)
1. ท่าต่อสู้/movement ซับซ้อน = character deform [GEM PITFALLS] → 1 action/ช็อต 4–8s, แตก fight เป็นหลาย prompt (02 ใส่ prod_note_th shot-breaker), coverage บังคับ MS/CU (medium = default series [DRM])
2. "fast" ลอยๆ = jitter [GEM] → บรรยาย physics แทนความเร็ว: น้ำหนักตัวกระแทก, รองเท้าไถลพื้น, ผ้า/ผมสะบัดตามแรง (secondary motion + foot-ground contact [realism])
3. wide→close ในช็อตเดียว = morph → "rapid hyperzoom, heavy directional motion blur, keep final frame sharp" [GEM] · ยังเพี้ยน = แตก 2 ช็อต + cut
4. fast camera + fast subject + ฉากซับซ้อนพร้อมกัน = ห้าม [GEM] → เร็วได้ทีละชั้น: กล้องนิ่ง-ตัวเร็ว หรือกล้อง track-ตัวคุมจังหวะ
5. impact ไร้น้ำหนัก (floaty) → เขียน weight + impact + dust/debris ทุกจุดปะทะ [realism]

#### h) PACING
(ค่าจาก steps 4/5/6/8/10/12/15s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ)
- hook ~10–15%: ช็อต 4–6s กระแทกทันที
- setup ~20%: ช็อต 8–10s ให้คนดูหายใจ + อ่าน stake
- conflict ~35–40%: หลายช็อตสั้น 4–8s (1 action/ช็อต) — ห้ามยัดฉากปะทะลงช็อตยาวช็อตเดียว
- twist ~15%: 6–8s ให้ reversal อ่านชัด
- cliffhanger ~10–15%: 4–6s จบที่เฟรมค้างคม

### GENRE: family — ครอบครัว/อบอุ่น
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ 00-contracts · ไม่ inject block นี้ = pipeline เดิมทุกตัวอักษร · แหล่ง: [DRM]/[GEM]/[director-styles]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | ลายเซ็นแนว: ทำให้ "รู้สึก" ทันทีแบบ warm restrained (คิดถึง/เอ็นดู/เจ็บแทนเงียบ ๆ) ไม่ใช่ดราม่าตบตี |
| curiosity | กลาง | ความลับข้ามรุ่นทำงานดี (จดหมายเก่า/รูปในลิ้นชัก) แต่ต้องอุ่น ไม่หลอน |
| visual | กลาง | ภาพขัดสถานการณ์ในบ้านได้ผลเป็นครั้งคราว (โต๊ะจัดครบแต่เก้าอี้ว่าง 1 ตัว) |
| conflict | ต่ำ | เผชิญหน้าแรงขัดโทนอบอุ่น — เก็บความขัดแย้งเล็กไว้ช่วง conflict แทนการเปิดเรื่อง |

weight = bias ให้ endpoint 01 ไม่ใช่ข้อห้าม — เกณฑ์ [DRM] "เรื่องหลัง hook ต้องพาไปหาคำตอบของ hook จริง" ยังบังคับทุกตัว

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: ภาพอบอุ่นที่มีรอยแหว่ง 1 จุด — one warm frame, one missing element (an empty chair, an extra plate)
- setup: กิจวัตรในบ้านเล่าความสัมพันธ์ผ่านมือ+ของ — domestic routine, hands passing objects
- conflict: ขัดแย้งเล็กในบ้าน/ข้ามรุ่น เสียงไม่ขึ้น — short clipped sentences, a door closed gently, not slammed
- twist: ของชิ้นเล็กเปลี่ยนความหมายทั้งเรื่อง — a kept object quietly revealed
- cliffhanger: คืนดีครึ่งทางแล้วค้างไว้ — a reconciling gesture offered, not yet answered

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
อารมณ์จริงระหว่างแอ็กชันเสมอ — ห้ามตีความเป็นหน้านิ่งตลอดเรื่อง · ลายเซ็นแนว = อารมณ์ไหลลงมือ/ไหล่/ลมหายใจช้า มากกว่าหน้าและน้ำเสียง
physical cues: "hands pause mid-fold, then resume slower" · "shoulders soften, one slow exhale through the nose" · "lips part to speak, then close, a small swallow"
deadpan ใช้เฉพาะ punchline/twist beat (หน้านิ่ง+ทิ้งเฟรมตอนเฉลย) เท่านั้น [GEM ACTING]

#### d) VISUAL & LIGHTING GRAMMAR
mood = visual noun EN ล้วน (ต่อท้าย style_stack / style_note_th ได้): golden haze, warm window light, steam over a rice bowl, dust motes in afternoon sun, soft bloom, faded family photos
lighting = physical เท่านั้น [GEM LIGHTING]: "low warm tungsten from kitchen doorway, cool dusk spill from window behind" · "morning sun through thin curtains from frame right, warm lamp fill from left" — ห้ามคำอารมณ์ ("cozy sad lighting" = ผิด)

#### e) DIRECTOR KEYWORD PRESETS [director-styles]
- warm-coming-of-age (keywords-only — Gerwig ไม่อยู่รายชื่อ 🟢 จึงห้ามใส่ชื่อ): warm coming-of-age, overlapping natural dialogue, ensemble family scenes, muted warm grade
- lush-nature-soft (keywords-only — Miyazaki ไม่อยู่รายชื่อ 🟢): lush nature, soft palette, gentle pacing, dreamlike afternoon light
- spielberg-warm-wonder (🟢 ใส่ชื่อได้ + keywords คุมเสมอ): Spielberg-style warm light, sweeping single camera move, awe close-up, eye trace

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. มือยื่นค้าง — gesture คืนดีถูกยื่นแต่ยังไม่ถูกรับ · เฟรมค้าง: ชามข้าวถูกวางตรงหน้า อีกคนยังไม่เงยหน้า
2. ของที่เพิ่งเข้าใจ — object เดิมถูกเผยความหมายใหม่ · เฟรมค้าง: close-up รูปเก่าโผล่ครึ่งใบจากลิ้นชัก
3. ประตูแง้ม — คนกลับมา/กำลังจะไป ค้างที่ธรณีประตู · เฟรมค้าง: เงายืนในประตูแง้ม แสงอุ่นลอดด้านหลัง
4. คำที่ยังไม่ได้พูด — ประโยคสำคัญถูกตัดก่อนคำตอบ · เฟรมค้าง: ปากเผยอค้าง อีกคนเพิ่งหันมา

#### g) AI-GEN PITFALLS เฉพาะแนว (ไม่ทวน pitfalls กลางของ contracts)
- หน้าเด็ก/ผู้สูงอายุ age-drift ข้ามช็อตง่ายกว่าวัยกลาง → identity_anchor ใส่ age marker รูปธรรม (gray streak at temples, deep smile lines) + คุม medium/close · 02 ใส่ prod_note_th
- โต๊ะอาหาร: จาน/อาหาร/ตะเกียบเปลี่ยนเองระหว่างช็อต → จำกัด prop เด่นบนโต๊ะ ≤3 ชิ้น + flag "ledger:" เข้า state_locks
- ฉากกอด/ป้อนข้าว (two-body overlap) → shot-breaker: แตกบีตเป็น approach → hands close-up → faces หลังสัมผัส
- golden hour ต่อเนื่องหลายช็อต: มุมแดด drift → copy lighting_anchor เดียวกัน verbatim ทุกช็อตในซีน

#### h) PACING (steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมยังบังคับ)
- สัดส่วนเวลา 5 ช่วงโดยประมาณ: hook 10% · setup 25% · conflict 30% · twist 15% · cliffhanger 20%
- duration bias: hook 5–6s (ดึงอารมณ์โดยไม่กระชาก) · setup 8–10s (อยู่กับ routine ได้นาน) · conflict 6–8s/shot · twist 4–6s (เฉลยเงียบสั้นคม) · cliffhanger 6–8s (hold ท่าค้าง)

> Sources: `intel-pack/00-contracts.md` · `memory/vertical-drama-basics-dramy.md` · `memory/seedance-knowledge.md` · `memory/director-styles-knowledge.md` · `memory/mv-directors-knowledge.md` · `memory/ai-video-realism-hierarchy.md`
