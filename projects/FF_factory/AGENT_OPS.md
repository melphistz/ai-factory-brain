# Factory — Agent Ops Playbook v2 (2026-07-05) — PROMPT-FIRST / MANUAL GEN

> **โหมดปัจจุบัน (ทดลอง):** Claude = สมองคิด prompt + QA + timeline · **Mirko เจนเองทุกภาพ/วิดีโอ (manual)** · ไม่ยิง MCP generate ใด ๆ ทั้งสิ้น
> **Ploy reset เป็น 0** — ตัวละครเริ่มใหม่ต่อโปรเจกต์ผ่าน prompt kit ไม่ผูก avatar เดิม
> **ถ้า flow นี้ผ่านค่อยต่อยอด** (automation/matrix/MCP gen จอดไว้ท้ายไฟล์)
> อ่านคู่กับ memory `ai-ugc-ad-factory-workflow` (สถาปัตยกรรม+โมดูล) + `claude-subagents` (นโยบายโมเดล)

## กติกาเหล็ก

1. **Fable = orchestrate ใน main loop เท่านั้น** — ห้ามเป็น subagent
2. **ไม่มีการยิง generate/เผาเครดิตจาก Claude เลยในโหมดนี้** — การเจนทั้งหมดเป็นของ Mirko (manual) · subagent ทุกตัวมีกฎ no-credits ฝังแล้ว
3. **Subagent ส่งออก text เท่านั้น** → orchestrator เซฟไฟล์เข้าโปรเจกต์
4. **แก้งาน = re-roll หน่วยเล็กสุด** — QA ต้องชี้หน่วย + prompt ที่ต้องแก้เสมอ

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
  01-brief.md               # brief + โมดูลที่ล็อก
  02-script.md              # จาก script-hook-writer (งาน ad)
  03a-promptkit.md          # Phase A: char/scene prompts + GEN ORDER + แผน storyboard
  03b-storyboard-prompts.md # Phase B: เฟรม storyboard prompts (หลัง char/ฉากจริงกลับมา)
  04-video-prompts.md       # จาก storyboard-prompter (หลังเฟรมจริงกลับมา)
  05-timeline.json          # จาก timeline-builder (+ cue sheet ใน 05-score-and-edit.md)
  assets/                   # ภาพเล็ก (char sheet, เฟรม storyboard) — เข้า git ข้ามเครื่อง
```
ไฟล์หนัก (คลิป/ภาพชุดใหญ่) per-machine: mac `~/Desktop/Ads/...` · Windows `D:\Claude\90-Assets\`

## โมดูลมาตรฐาน (tag ใช้ทั้ง kit → timeline)

`HOOK` (×n สลับได้) · `BODY.PROBLEM` · `BODY.MECH` · `BODY.DEMO` · `BODY.PROOF` · `CTA` — งานหนัง/MV ใช้เลขช็อตแทน · กฎเดิมคงอยู่: BODY ใช้ร่วมทุก hook, hook ≠ body เชิงภาพ (intentional cut), J-cut ที่รอยต่อ

## 🅿️ จอดไว้ (ต่อยอดเมื่อ flow ผ่าน)

- MCP auto-gen (Higgsfield) แทน manual ขั้น 3/4.5 — สถาปัตยกรรมเดิมใน memory ใช้ได้ทันที (TTS ก่อน motion, Gate 1 ก่อน animate)
- matrix runner 8×3 (Workflow fan-out) · manifest.json resumable · feedback loop v3 · Remotion render อัตโนมัติบน mac
