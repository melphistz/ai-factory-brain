# smoke-test-result — สถาปัตยกรรม genre×setting (คู่ revenge × high-society)

> ทดสอบ 07-10 · ultracode workflow 4 agents · **ยังไม่ deploy — รอ Mirko approve**
> พิสูจน์: แยก revenge เดิม → genre[revenge]ผอม + setting[high-society] แล้วประกบกลับ (setting→genre) ได้ flavor เดิมครบ + genre = 0 ชื่อหลอด (lint ผ่าน)

## ผล verify (adversarial 2 เลนส์)
- **fidelity (ของไม่หาย):** PASS
  - [minor] (setting S5 — venue registry) Original revenge a/b humiliation venue set included "ทิ้งกลางพิธี" (abandoned/jilted at a ceremony/wedding). S5 slot `status-contradiction` venue list = black-tie gala / ballroom / luxury banquet / penthouse party — no wedding/ceremony term. The public-humiliation FUNCTION fully survives (genre b hook + S5 gala), but the specific ceremony/jilting instance reconstructs only loosely (a gala is not a ceremony). This is the only original prop/venue noun that narrows in the recombined envelope.
    → fix: Add one venue term to S5's "งานหรู" list, e.g. `wedding ceremony / high-society betrothal / engagement gala`, so the jilted-at-ceremony image is fully recoverable. Pure additive to setting; genre stays untouched.
- **operability (lint/budget/backward-compat):** PASS
  - [minor] (completeness / reconstruction (e-preset token parity)) The token 'low-key' from the original cold-power-reveal preset ('David Fincher style, low-key locked-off camera, cold desaturated, single-hue tint') is not literally reproduced in either half. 'locked-off' survives in genre e); 'David Fincher style, cold desaturated, single-hue tint' survives in S4; but the word 'low-key' itself appears nowhere in the composed envelope.
    → fix: Semantically it is already covered (genre d) 'deep falloff / เด่นออกจากพื้นมืด' + S4 vindication 'rich deep shadow' = low-key lighting), so no functional loss. For exact parity, optionally add 'low-key' to S4 reveal/flip grade keywords.
  - [minor] (backward-compat (genre-alone readability)) When the thin genre pack is read standalone (no setting attached), section-pointers 'ผิว=S5', 'ผิว=S6', 'หลอด=S2', 'สีพื้น=S1' dangle with no target. It does not crash or break the pipeline (the generic '[plot-device: กลไกพลิกสถานะ]' and inline slot description are self-describing, and the true no-inject baseline contract is untouched), and per design-doc §11 case (ข) the app always auto-fills default_setting=high-society for revenge, so this configuration never occurs at runtime.
    → fix: No change required for the smoke test. If genre-only use is ever exposed in the app, keep the pointers human-readable (already are) so a lone-genre read still yields a coherent revenge flavor at the function level.
- repaired: True · genre=4476ch (≤4,500) · setting=3070ch (≤3,500)

## carve notes
SMOKE TEST ผ่านทุกเกต. genre=4476 (≤4500) · setting=3003 (≤3500). self-lint genre: EN fixture/material/palette leak = 0 (fluorescent/tungsten/marble/glass/sheen/golden/desaturated/single-hue = ไม่มี). คำ "หลอด/วัสดุ/สีพื้น" ที่โผล่ใน genre เป็น guard/cross-ref ล้วน (เช่น "ศูนย์ชื่อหลอด", "หลอด=S2", "ผิววัสดุที่แตก=S7") ไม่ได้ระบุหลอด/วัสดุตัวจริง → gate ผ่าน.

เก็บที่ GENRE (วิธีเล่า): a) ตารางน้ำหนัก+ตรรกะ+engine · แถว visual-hook เปลี่ยนเป็นประกาศ slot `status-contradiction` (พันธุ์ B ผิว=S5) + โน้ตว่า revenge ไม่มีพันธุ์ A · b) 5 บีต+หน้าที่ plot-device (ชื่อ prop → [plot-device·ผิว=S6]) · c) verbatim · d) LIGHTING FUNCTION ล้วน (humiliation=harsh/flat/unflattering/cold-toned/top-down → reveal=flip warm side-key+rim+falloff · status-flip=light-flip) — 0 ชื่อหลอด · e) CAMERA/MOVEMENT + กฎ 🟢🔴 (static/locked-off, low-angle push, crowd OOF) · f) ปมค้าง 4 แบบ (prop→[plot-device]) · g) เฉพาะ acting/timing (two-body impact, gore-ban, overact) · h) verbatim.

โยน SETTING S1–S7 (โลก): S1 base grade (sheen/marble-glass/warm-cool/grain) · S2 หลอด/วัสดุ/สะท้อน + **มี harsh fluorescent ≥1** (ทางเดินหลังบ้าน/ครัวโรงแรม/ลานจอด — ให้ humiliation-key เกาะ ตาม design ข้อ4 ทางออก A) + tungsten อุ่น (reveal) · S3 หน้า idol-glam+realism (house-style) · S4 world-look + Fincher cold-desaturated grade + golden vindication palette · S5 slot skin (ชุดโทรม=เครื่องแบบพนักงาน / งานหรู=gala) · S6 ผิว plot-device (นามบัตร CEO/พินัยกรรม/ตราตระกูล/DNA) + text-glyph guard + ทะเบียนชื่อ · S7 crowd blur + หน้าสลับฝั่งจอ + วัสดุแตก(glass/wine/paper).

จุดตัดเส้นแบ่ง (ไม่ตก/ไม่ซ้ำ 2 แกน): (1) casting แยก — หน้า house-style→S3 แต่ RULE "ตัวร้ายห้ามหน้าน่าเกลียด"→genre (ตาม design S3 note) · (2) อุณหภูมิแสง warm/cool/cold-toned = genre FUNCTION (ตัวอย่าง design เองใช้ "พลิกอุ่น") แต่คำ palette (sheen/desaturated/golden)→S1/S4 · (3) Fincher = ชื่อผู้กำกับ "ที่ให้ลุค" → อยู่ S4 เท่านั้น; genre e เก็บแค่พฤติกรรมกล้อง (locked-off/precise) + กฎ 🟢🔴 ทั่วไป → ประกบแล้วได้ preset cold-power-reveal ครบ · (4) text-glyph guard วางที่ S6 เพราะ "prop เป็น text-bearing หรือไม่" ขึ้นกับโลก · (5) gore-ban คงที่ genre (violence engine) แต่ skin วัสดุแตก→S7 · (6) backer-figure genericize เป็น "ผู้หนุนตัวจริง (อำนาจเหนือกว่า)" — "พ่อจริง/บอร์ด" เป็นแค่ instance โลก instantiate เอง (S6 มี boardroom/บริษัท), หน้าที่ปมครบ.

หัวใจ smoke test (humiliation ยังเย็น/สถาบัน): genre "harsh flat cold-toned top-down wash" + S2 "overhead fluorescent tubes, top-down cold unflattering" ประกบ → institutional cold humiliation ✓. reveal: genre "warm side-key+rim+falloff" + S2 "warm tungsten sconces" → พลิกอุ่นขอบสว่าง ✓.

verify programmatic: c) ACTING + h) PACING byte-verbatim vs original = MATCH · reconstruction (ทุก fixture/prop/look เดิมของ d/e/f/g) หาเจอใน setting∪genre = MISSING 0.

---

## (A) genre pack `revenge` ผอม — แกน "วิธีเล่า" (ไป 09)

### GENRE: revenge — แก้แค้น/พลิกสะใจ (ผอม · แกน "วิธีเล่า")
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / §6 · genre ถือ "วิธีเล่า" · โลก = setting pack ประกบ (setting ก่อน → genre ทับ) · **ศูนย์ชื่อหลอด/วัสดุ/สีพื้น = lint gate** · trace [DRM][GEM][DIR][CAST]

#### a) HOOK WEIGHTING
| hook [DRM] | weight | เหตุผล |
|---|---|---|
| emotional | สูง | โกรธ/เจ็บแทนทันที (ตบ/สาดน้ำ/ทิ้งต่อหน้าคนดู [DRM]) — อัดอั้นก่อน จึงสะใจตอน payoff |
| conflict | สูง | ดูถูก/เผชิญหน้า [DRM] = white-black polarity — อยากเห็น "จะพลิกกลับยังไง" |
| curiosity | กลาง | ตัวตนจริงที่ซ่อน (secret CEO/ทายาท/สลับตัวแต่เกิด) = ปมรอเฉลยตอน status-flip |
| visual | ต่ำ | hook slot `status-contradiction` — ภาพขัดสถานะเปิดเรื่อง (ผิว=S5) เก็บ flip เป็น payoff |

engine = cruelty→humiliation→triumphant reveal (ขาว-ดำสุดขั้ว, ตัวร้ายเลวไร้ backstory) · weight = bias ไม่ใช่ข้อห้าม [DRM]
- **hook slot**: revenge เรียก slot `status-contradiction` (พันธุ์ B ขัดสถานะสังคม §3) → S5 ทาผิว "ชุดโทรม/งานหรู" · revenge ไม่มี hook พันธุ์ A

#### b) BEAT FLAVOR (โครง+ลำดับ 5 ช่วง [DRM] ห้ามแตะ)
- hook: humiliation สาธารณะจบใน 1 เฟรม — สาดน้ำ/ตบ/ทิ้งต่อหน้าคนดู (venue+ฝูงชน = ผิว S5)
- setup: ปูสถานะต่ำ + ตัวร้ายเลวเชิงความสัมพันธ์ (แม่เลี้ยง/แม่สามี/คู่แข่ง) · ซ่อน "ตัวตนจริง" ใน [plot-device: กลไกพลิกสถานะ · ผิว=S6] = ระเบิดเวลา
- conflict: humiliation escalation — ดูถูกซ้ำ คนดูมากขึ้น เดิมพันสูงขึ้น · ยิ่งกด = ยิ่งเพิ่ม payoff
- twist: triumphant status-flip reveal — เผยตัวตนจริง อำนาจพลิกขั้วในเฟรมเดียว (ต่ำสุด→สูงสุด)
- cliffhanger: ค้างตรงตัวร้ายเพิ่งเริ่มรู้ / การเหยียบกลับที่เพิ่งเริ่ม ยังไม่ land

#### c) ACTING GRAMMAR (variant ของ under-direct [GEM ACTING])
ลายเซ็น = 2 register: humiliation = "กลั้น" ไม่โต้กลับ → reveal = "นิ่งเย็นทวงคืน" ไม่ตะโกน — composure ไม่ overact · ตัวร้าย ยะโสเย็น ห้ามสั่ง "evil/sneer"
- humiliation cue EN: `jaw clenches, eyes drop, one hard swallow, chin stays level, no open sob`
- reveal cue EN (deadpan hold ก่อนพลิก [GEM]): `still a beat, chin lifts, cool gaze, a faint mouth-corner curl`
- villain: `slow up-down glance, chin raised` → realize `smug grin drains, face goes still`

#### d) LIGHTING FUNCTION (คำหน้าที่แสงล้วน — 0 ชื่อหลอด/วัสดุ/สีพื้น · หลอด=S2 สีพื้น=S1)
- casting RULE [CAST]: polarity มาจากการกระทำ ไม่ใช่หน้าตา → ตัวร้ายห้ามหน้าน่าเกลียด (house-style หน้า = S3)
- แสง = ตัว flip สถานะตามบีต · ห้ามคำอารมณ์ ("cruel lighting" = ผิด)
- **humiliation key** = harsh, flat, unflattering, cold-toned, top-down wash — กดจากบน แบน หน้าหมดสง่า (drains dignity)
- **reveal key** = flip: low warm side-key + strong rim + deep falloff — พลิกอุ่น ขอบสว่าง เด่นออกจากพื้นมืด
- **status-flip**: twist สลับ humiliation→reveal key ในซีนเดียว (warm-cool contrast = แกน)

#### e) CAMERA & MOVEMENT GRAMMAR (+ กฎใส่ชื่อผู้กำกับ · palette/ลุค/ชื่อที่ให้ลุค = S4)
- กฎ 🟢/🔴 [DIR]: ชื่อผู้กำกับใส่ได้เฉพาะ 🟢 + keywords คุม · 🔴 = keywords-only ห้ามใส่ชื่อ · **ชื่อที่ให้ "ลุค/เกรดสี" = S4**
- humiliation/escalation: static / locked-off — กล้องนิ่งมองเหยื่อถูกกด (ไม่ช่วยเหลือ)
- reveal/flip beat: locked-off, precise, still — นิ่งให้ composure เป็นตัวเล่น (คู่ reveal grade S4)
- vindication beat: slow low-angle push toward hero + crowd out-of-focus (hero isolate)

#### f) CLIFFHANGER PATTERNS (chain rule N→N+1 ของ 01 ยังบังคับทุกแพตเทิร์น)
1. **ตัวร้ายเพิ่งเริ่มรู้** — เยาะ→ตระหนก · เฟรม: รอยยิ้มยะโสค้างครึ่ง ตาเบิก
2. **reveal ครึ่งใบ** — ตัวตน/หลักฐานเผยแค่เสี้ยว · เฟรม: มือรับ [plot-device·ผิว=S6] ค้าง
3. **คนอำนาจกว่าเข้าเฟรม** — ผู้หนุนตัวจริง (อำนาจเหนือกว่า) ยืนหลังเหยื่อ · เฟรม: เงากลุ่มคนที่ทางเข้า
4. **ไพ่ยังไม่เปิด** — "รู้ไหมว่าฉันคือ…" ถูกตัด / [plot-device·หลักฐาน] ยังไม่เปิด · เฟรม: นิ้วกดค้าง

#### g) AI-GEN PITFALLS เฉพาะการแสดง/จังหวะ (ไม่ทวน pitfalls กลาง · เรื่องคน/วัสดุ/crowd = S7)
- ตบ/ผลัก/สาดน้ำ/ปาของ/ฉีกเอกสาร = two-body impact → 02 ใส่ prod_note_th ให้ shot-breaker แตก "ก่อนแตะ"+"หลังแตะ" คนละช็อต [GEM]
- ห้าม gore/เลือด (โมเดลพัง+platform) → ผลเป็นร่องรอยบนร่าง แทนโชว์เลือด (ผิววัสดุที่แตก = S7)
- "evil/smug/triumphant" ตรงๆ → overact การ์ตูน [GEM] → cue c) + `underplayed, controlled menace, natural`

#### h) PACING (steps {4,5,6,8,10,12,15}s เท่านั้น [§3] · Σduration=target_sec + beat thickness เดิมบังคับ)
จังหวะ: อัดอั้นยาว → พลิกคม → สะใจ (contrast = impact [GEM])
hook ~10–15% (5–6s humiliation) · setup ~20% (6–8s ปู+หยอดปม) · conflict ~30% (6–8s cruelty สะสม) · twist ~20% (10–12s flip + composure c) + villain realize, ขึ้น 15s ได้) · cliffhanger ~10–15% (4–5s ค้างสีหน้าตัวร้าย)

---

## (B) setting pack `high-society` — แกน "โลก" (ไฟล์ใหม่ 10)

### SETTING: high-society — โลกไฮโซ/คนรวยยุคใหม่ (default ของ genre revenge)
> flavor layer เท่านั้น — ห้าม override schema §1 / budget §3 / หลักการร่วม §6 ของ 00-contracts · แกน setting ถือ "โลก" (สี/หลอด/วัสดุ/หน้าตา/ของ/ชื่อ) · ประกบ genre: inject setting ก่อน (BASE) → genre ทับ (MODULATION) · trace: [GEM]=seedance-knowledge · [DIR]=director-styles-knowledge · [CAST]=feedback-drama-character-casting

**S1 — สีพื้น + อารมณ์** (base grade · ครึ่ง base ของ d เดิม)
high-gloss luxury sheen · cold marble-and-glass palette · warm-cool contrast · fine film grain · โทนโลก = มั่งคั่ง เย็นชา สง่าจนกดคนที่ต่ำกว่า · reflective surface = complexity ฟรี [GEM]

**S2 — หลอด · วัสดุ · พื้นสะท้อน** (physical ล้วน)
- fixtures อุ่น/สวย (ให้ reveal-key เกาะ): low warm tungsten sconces, crystal chandelier spill, warm practical table lamps — จ่าย side-key/rim/falloff ได้
- **fixtures แข็ง/ไม่สวย ≥1 (บังคับ ข้อ 4 · ให้ humiliation-key เกาะ):** bare overhead fluorescent tubes ในทางเดินหลังบ้าน / ครัวโรงแรม / ลานจอดใต้ดิน — top-down, cold, unflattering
- materials: polished marble floor, floor-to-ceiling glass, mirror-panel walls, gilded metal trim
- reflective: marble sheen, dark glass, mirror = ภาพสะท้อนซ้อน (complexity ฟรี)

**S3 — หน้านักแสดงประจำโลก** (house-style เท่านั้น)
idol-glam beauty tier ทุกตัว (พระเอก/นางเอก/นางร้าย) — เครื่องหน้าคม, glam makeup, well-groomed, luxury wardrobe · **คง realism** (ผิวมีดีเทลรูขุมขน ไม่พลาสติก) [CAST] · NB: กฎ "ตัวร้ายห้ามหน้าน่าเกลียด" = ของ genre (ที่นี่จ่ายแค่ beauty tier)

**S4 — palette + ชื่อผู้กำกับที่ให้ลุค** (ครึ่ง look ของ e เดิม)
- world look (keywords-only, สาย 🔴 ห้ามใส่ชื่อ): high-gloss drama-series look, luxury interior, dramatic key+rim, DramaBox flagship-tier
- reveal/flip grade (🟢 ใส่ชื่อได้ + keywords คุมเสมอ): David Fincher style, low-key, cold desaturated, single-hue tint
- vindication palette: warm golden backlight, rich deep shadow (คู่ genre camera low-angle push + crowd OOF)

**S5 — พจนานุกรม "ขัดสถานะ" (slot-keyed · ตอบเฉพาะ slot ที่ genre เรียก)**
- slot `status-contradiction` (revenge เรียก): "ชุดโทรม" = เครื่องแบบคนรับใช้/พนักงาน หรือเสื้อผ้าเรียบเก่า · "งานหรู" = black-tie gala, ballroom, luxury banquet, penthouse party, wedding ceremony / engagement gala → ภาพ = คนชุดพนักงานยืนกลางแขก VIP งานกาลา (หรือถูกทิ้งกลางพิธี)

**S6 — ผิวของ plot-device + ทะเบียนชื่อ (slot-keyed)**
- ผิว [plot-device: กลไกพลิกสถานะ]: นามบัตร CEO · พินัยกรรม/เอกสารมรดก · ตราตระกูล/แหวนตระกูล · ผลตรวจ DNA สายเลือด (ปมสลับตัว) · โฉนด/ใบหุ้น
- **text-glyph guard** (prop เป็น text-bearing): reveal ผ่าน reaction + insert keyframe ภาพนิ่ง ตัวอักษรไม่ขยับ [GEM]
- name/venue registry: สกุลไฮโซ (ตระกูล…) · บริษัท/กรุ๊ป · venue = gala hall, penthouse, boardroom, hotel lobby, ballroom

**S7 — pitfalls เรื่องคน/วัสดุ**
- crowd = หลายหน้า deform → blur crowd, ล็อกตัวหลัก 2–3 [GEM]
- เหยื่อ/ตัวร้ายห้ามสลับฝั่งจอ → ล็อก eyeline/screen-side เข้า ledger
- วัสดุที่แตก/เสียหายแทนเลือด (ให้ genre gore-ban เกาะ): glass shatter, spilled wine, torn paper
- gilded/reflective props เปลี่ยนรูปข้ามช็อต → ล็อกเข้า ledger

---

## ถ้า Mirko approve → migration เต็ม (design doc STEP 1-8)
- STEP 1-6: carve 6 แนวเดิม + 6 โลก anchor (real-urban/home/minimal/dim/gritty/high-society) + acceptance test ทั้ง 6 แนว
- STEP 7: เขียน 3 โลกใหม่ (rural-poor / fantasy 2-register / **period=จีนวังหลวง xianxia ตาม Mirko เลือก**)
- STEP 8: wire 2 dropdown (แนว×โลก) + lint gate + contracts §1.1/§1.7/§3/§5/§6 + deploy prompts/
- pattern คู่นี้ (revenge×high-society) = template ให้ carve คู่อื่นตาม
