# Factory — Agent Ops Playbook v2 (2026-07-05) — PROMPT-FIRST / MANUAL GEN

> **โหมดปัจจุบัน (ทดลอง):** Claude = สมองคิด prompt + QA + timeline · **Mirko เจนเองทุกภาพ/วิดีโอ (manual)** · ไม่ยิง MCP generate ใด ๆ ทั้งสิ้น
> **Ploy reset เป็น 0** — ตัวละครเริ่มใหม่ต่อโปรเจกต์ผ่าน prompt kit ไม่ผูก avatar เดิม
> **ถ้า flow นี้ผ่านค่อยต่อยอด** (automation/matrix/MCP gen จอดไว้ท้ายไฟล์)
> อ่านคู่กับ memory `ai-ugc-ad-factory-workflow` (สถาปัตยกรรม+โมดูล) + `claude-subagents` (นโยบายโมเดล)

## กติกาเหล็ก

1. **Main loop = orchestrate เท่านั้น ไม่ว่าจะเป็นโมเดลไหน** (เขียนแผนนี้สมัย Fable — ต่อไป main จะเป็น Opus ก็ใช้กติกาเดิม): ห้ามเขียน copy/prompt/QA เองใน main, dispatch ตาม PROTOCOL ข้างล่าง · โมเดล main ห้ามใช้เป็น subagent
2. **ไม่มีการยิง generate/เผาเครดิตจาก Claude เลยในโหมดนี้** — การเจนทั้งหมดเป็นของ Mirko (manual) · subagent ทุกตัวมีกฎ no-credits ฝังแล้ว
3. **Subagent ส่งออก text เท่านั้น** → orchestrator เซฟลงไฟล์ job ทันทีทั้งดุ้น แล้วค่อยสรุปสั้นให้ Mirko
4. **แก้งาน = re-roll หน่วยเล็กสุด** — QA ต้องชี้หน่วย + prompt ที่ต้องแก้เสมอ · อยากแก้งาน agent → dispatch กลับ agent เดิมพร้อม feedback

## Flow หลัก (ขั้นของ Mirko → ผู้รับผิดชอบ) — ภาพ storyboard ก่อน แล้วค่อยวิดีโอ

| ขั้น | งาน | ผู้ทำ | output |
|---|---|---|---|
| **1. Intake** | รับ brief หรือ storyboard → ตั้งโฟลเดอร์โปรเจกต์ | Fable (main) | job folder + โครงโมดูล |
| 1.5 Copy (เฉพาะงาน ad) | โมดูล copy: HOOK bank / BODY (problem·mech·demo·proof) / CTA | **script-hook-writer** (opus) | script ต่อโมดูล + visual direction |
| **2A. Prompt kit — ตัวละคร+ฉาก** | prompt ตัวละคร (portrait + character sheet) · prompt ฉาก (clean plate) · แผน storyboard (รายการเฟรม) · **GEN ORDER + ชื่อไฟล์** | **asset-prompt-builder** (opus, Phase A) | KIT A copy-paste ได้ทันที |
| **3A. Manual gen** | เจน character → ทำ character sheet → เจนฉาก → **โยนภาพกลับมา** | **Mirko** | char sheet + scene plates |
| 3A.5 QA (แนะนำ) | เช็ค identity sheet/ฉาก ก่อนลงทุนเขียน storyboard ทั้งชุด | **qa-inspector** (sonnet) | PASS/REDO + prompt fix |
| **2B. Storyboard prompts** | อ่านภาพจริง → continuity ledger จาก pixel จริง → **prompt เฟรม storyboard ต่อโมดูล/ช็อต** (composite: char×scene, @Image slot map, เฟรม = first-frame ของวิดีโอ) | **asset-prompt-builder** (opus, Phase B) | storyboard frame prompts |
| **3B. Manual gen** | เจนเฟรม storyboard ครบชุด → โยนกลับมา | **Mirko** | เฟรม storyboard จริง |
| 3B.5 QA (แนะนำ) | เช็คเฟรม: identity/continuity/composition/text | **qa-inspector** (sonnet) | PASS/REDO ต่อเฟรม |
| **4. Video prompts** | เฟรมจริง = first frame → video prompt ต่อช็อต + continuity ข้ามโมดูล | **storyboard-prompter** (opus) | video prompt พร้อมเจน |
| 4.5 Manual gen video | เจนวิดีโอต่อโมดูล | **Mirko** | ไฟล์คลิป |
| 4.6 QA คลิป (แนะนำ) | lip-sync/physics/seam/drift | **qa-inspector** (sonnet) | PASS/REDO ต่อคลิป |
| **5. Timeline** | JSON timing ครอบโมดูล (J-cut, captions, fx markers) → Remotion/Hyperframe/ตัดมือ | **timeline-builder** (sonnet) | timeline.json + cue sheet |

เสริมนอก flow: **teardown-analyst** (sonnet) ป้อน pattern ก่อนขั้น 1.5 / อ่านผลแอดหลังปล่อย · **deep-reasoner** (opus) debug สถาปัตยกรรม · **fast-worker** (sonnet) งาน mechanical

## จุดที่คนกับ Claude สลับมือกัน (hand-off)

```
brief ─▶ KIT A (char+ฉาก) ─▶ [Mirko gen] ─▶ ตัวละคร/ฉากจริง ─▶ STORYBOARD PROMPTS ─▶ [Mirko gen]
      ─▶ เฟรมจริง ─▶ VIDEO PROMPTS ─▶ [Mirko gen] ─▶ คลิป ─▶ TIMELINE ─▶ Mirko ตัดต่อ
```
- ทำไม storyboard ภาพก่อนวิดีโอ: prompt composite เขียนหลังเห็นตัวละครจริง = ledger ตรง pixel · เห็นทั้งเรื่องเป็นภาพนิ่งก่อนจ่ายค่าเจนวิดีโอ · แก้ภาพนิ่งถูกกว่า re-roll วิดีโอ (board first, render second)
- ทุกครั้งที่โยนภาพ/คลิปกลับมา: วางไฟล์แล้วบอกว่าไฟล์ไหน = asset id ไหน (ตาม naming ใน GEN ORDER) — Claude จับคู่ต่อให้เอง
- ชื่อไฟล์ตาม ASSET MAP (`char01_fon_sheet.png`, `scene02_school.png`, `sb_HOOK_01.png`)

## Fleet (8 ตัว — `agents/` ใน brain repo, junction ทั้งสองเครื่อง)

| ความยาก | งาน | agent | model |
|---|---|---|---|
| 1 | storyboard/ภาพจริง → video prompt + continuity | storyboard-prompter | opus |
| 2 | 2 เฟส: A=prompt char/scene + gen order · B=storyboard frame prompts จากภาพจริง | asset-prompt-builder | opus |
| 3 | copy ไทย / hook bank / SPINE | script-hook-writer | opus |
| 4 | debug pipeline / architecture | deep-reasoner | opus |
| 5 | QA 2 เกท (ภาพ/คลิป, ดู pixel จริง) | qa-inspector | sonnet |
| 6 | teardown คู่แข่ง + feedback ผลแอด | teardown-analyst | sonnet |
| 7 | timeline JSON (Remotion/Hyperframe) | timeline-builder | sonnet |
| 8 | mechanical ตาม spec | fast-worker | sonnet |

Fan-out ได้ใน message เดียว: concepts × asset-prompt-builder · ภาพ/คลิป × qa-inspector · ช็อต × storyboard-prompter

## โครงไฟล์ต่อ job

```
projects/<campaign or FF_factory/jobs/<id>>/
  STATE.md                  # สถานะล่าสุด + ขั้นถัดไป + ของที่ล็อกแล้ว (อัปเดตทุกจบขั้น — จุด resume)
  01-brief.md               # brief + โมดูลที่ล็อก (frontmatter จาก onboarding)
  02-script.md              # จาก script-hook-writer (งาน ad)
  03a-promptkit.md          # Phase A: char/scene prompts + GEN ORDER + แผน storyboard
  03b-storyboard-prompts.md # Phase B: เฟรม storyboard prompts (หลัง char/ฉากจริงกลับมา)
  04-video-prompts.md       # จาก storyboard-prompter (หลังเฟรมจริงกลับมา)
  05-timeline.json          # จาก timeline-builder (+ cue sheet ใน 05-cuesheet.md — ตาม PROTOCOL ข้อ 10)
  assets/                   # ภาพเล็ก (char sheet, เฟรม storyboard) — เข้า git ข้ามเครื่อง
```
ไฟล์หนัก (คลิป/ภาพชุดใหญ่) per-machine: mac `~/Desktop/Ads/...` · Windows `D:\Claude\90-Assets\`

## โมดูลมาตรฐาน (tag ใช้ทั้ง kit → timeline)

`HOOK` (×n สลับได้) · `BODY.PROBLEM` · `BODY.MECH` · `BODY.DEMO` · `BODY.PROOF` · `CTA` — งานหนัง/MV ใช้เลขช็อตแทน · กฎเดิมคงอยู่: BODY ใช้ร่วมทุก hook, hook ≠ body เชิงภาพ (intentional cut), J-cut ที่รอยต่อ

## ORCHESTRATION PROTOCOL — บทสั่งงานต่อขั้น (main loop ทุกโมเดล copy ไปใช้ได้เลย)

**ขั้น 0 — ONBOARDING (บังคับ เมื่อ Mirko บอก "งานใหม่"/"โปรเจกต์ใหม่"):**
- ถามกลับชุดเดียว 4 ข้อ: **(1) ชื่อโปรเจกต์ (2) ประเภทงาน: ad หรือ หนัง/MV (3) video ratio (4) ความยาวเป้าหมาย (วินาที)** — งาน ad ถามเพิ่ม: จำนวน hook (default 3)
- **สร้างโฟลเดอร์แยกทันที** (ห้ามเริ่มงานใด ๆ โดยไม่มีโฟลเดอร์):
  - ad → ก๊อป `jobs/_template/` → `jobs/<slug>/` · หนัง/MV → ก๊อป `projects/_template/` → `projects/<slug>/` (slug = ชื่อสั้น kebab-case อังกฤษ/ทับศัพท์)
- เติมคำตอบลง frontmatter `01-brief.md` (job/aspect/target_sec/hooks/created) + อัปเดต `STATE.md` (stage: brief)
- คุยเก็บ brief ที่เหลือ (สินค้า/ข้อเสนอ, กลุ่มเป้าหมาย, สไตล์, ข้อห้าม) เติมลง `01-brief.md` แล้วค่อยเดินขั้น 2

**กฎแยกโปรเจกต์ (กันงง):** ทุกไฟล์ของโปรเจกต์ — script, prompt kit, verdicts, timeline, `assets/` — อยู่ในโฟลเดอร์ตัวเอง**เท่านั้น** ห้ามปนข้ามโปรเจกต์/ห้ามวางที่ root · **จบขั้นไหนอัปเดต `STATE.md` ทันที** (stage + ขั้นถัดไป + สิ่งที่ล็อกแล้ว) · เปิด session มาทำต่อ → อ่าน `STATE.md` ของโปรเจกต์นั้นก่อนเสมอ

**หลัง onboarding (งาน ad):**
2. dispatch **script-hook-writer**: *"อ่าน `<job>/01-brief.md` แล้วเขียน copy เต็มตาม output contract: CONCEPT / BODY (line-by-line + วินาที + visual beat) / HOOK BANK <n> ตัวพร้อม tier / CTA / FLAGS — campaign: <ชื่อ>"* → เซฟลง `02-script.md` → **Gate 0: ให้ Mirko อนุมัติ script ก่อน**
3. dispatch **asset-prompt-builder**: *"PHASE A. อ่าน `<job>/01-brief.md` + `02-script.md`. aspect <x>, สไตล์ <y>. ทำ ASSET MAP + GEN ORDER + prompt ตัวละคร (portrait+sheet) + prompt ฉาก + แผน storyboard"* → เซฟลง `03a-promptkit.md` → ส่ง GEN ORDER ให้ Mirko ไปเจน
   (งานหนัง/MV: ข้ามข้อ 2, dispatch Phase A จาก brief/storyboard ตรง ๆ)

**เมื่อ Mirko โยนภาพตัวละคร/ฉากกลับมา:**
4. ย้ายไฟล์เข้า `<job>/assets/` ตั้งชื่อตาม ASSET MAP (Mirko บอกว่าไฟล์ไหนคือ asset ไหน)
5. dispatch **qa-inspector**: *"Gate 1 เช็คภาพใน `<job>/assets/`: <รายชื่อไฟล์> เทียบ prompt ใน `03a-promptkit.md` — identity sheet ใช้ล็อกหน้าได้ไหม, ฉากตรง spec ไหม"* → REDO = ส่ง prompt แก้กลับ Mirko · PASS = ข้อ 6
6. dispatch **asset-prompt-builder**: *"PHASE B. ภาพจริง: <path=asset id ทุกคู่>. อ่าน `01/02/03a` แล้วทำ CONTINUITY LEDGER จาก pixel จริง + STORYBOARD FRAME PROMPTS ทุกโมดูล + GEN ORDER"* → เซฟลง `03b-storyboard-prompts.md` → Mirko ไปเจนเฟรม

**เมื่อเฟรม storyboard กลับมา:**
7. เก็บเข้า `assets/` (ชื่อ `sb_<module>_<nn>.png`) → dispatch **qa-inspector** (Gate 1 รอบเฟรม: identity/continuity/composition/text)
8. dispatch **storyboard-prompter**: *"storyboard = เฟรมจริงใน `<job>/assets/sb_*.png` (เรียงตาม `03b`), continuity ledger ใน `03b`, ความยาวต่อช็อตใน `02`/brief. ทำ VIDEO PROMPT ต่อช็อต + FINAL FRAME + QA hooks"* → เซฟลง `04-video-prompts.md` → Mirko ไปเจนวิดีโอ

**เมื่อคลิปกลับมา:**
9. dispatch **qa-inspector**: *"Gate 2 คลิปใน <paths>: lip-sync (ถ้ามีพูด), contact physics, drift, รอยต่อ hook↔body ตามกฎ J-cut"* → REDO ต่อคลิปที่พังเท่านั้น
10. dispatch **timeline-builder**: *"คลิป: <path=module ทุกคู่>, target <sec>, aspect <x>. ทำ CUE SHEET + TIMELINE JSON + CHECKS"* → เซฟ JSON ลง `05-timeline.json`, cue sheet ลง `05-cuesheet.md` → ส่งให้ Mirko ตัดต่อ (Remotion/Hyperframe/มือ)

**ทุกขั้น:** เซฟ output agent ทั้งดุ้นก่อนสรุป · fan-out ได้เมื่องานอิสระกัน (หลาย concept/หลายคลิป = ยิงใน message เดียว) · sync ขึ้น git อัตโนมัติ (hooks) — mac รัน `./sync.sh` เอง

## เกณฑ์ตัดสิน "flow ผ่าน" (ประเมินหลัง dry run จบ 1 job)

1. GEN ORDER ทำตามได้จนจบโดยไม่ต้องถามเพิ่ม (prompt พร้อมใช้จริง)
2. เฟรม storyboard identity/wardrobe นิ่งทั้งชุด — QA รอบแรกผ่าน ≥ ~80% ของเฟรม
3. video prompt ใช้เจนได้โดยแก้เล็กน้อยหรือไม่แก้เลย
4. timeline.json/cue sheet เอาไปตัดได้จริงโดยไม่ต้องรื้อ
→ **ผ่านทั้ง 4 = เปิดหัวข้อ 🅿️ ต่อยอดได้** · ข้อไหนไม่ผ่าน → dispatch deep-reasoner วิเคราะห์ root cause แล้วแก้ playbook/agent ก่อน ห้ามฝืนต่อยอด

## 🅿️ จอดไว้ (ต่อยอดเมื่อ flow ผ่าน)

- MCP auto-gen (Higgsfield) แทน manual ขั้น 3/4.5 — สถาปัตยกรรมเดิมใน memory ใช้ได้ทันที (TTS ก่อน motion, Gate 1 ก่อน animate)
- matrix runner 8×3 (Workflow fan-out) · manifest.json resumable · feedback loop v3 · Remotion render อัตโนมัติบน mac
