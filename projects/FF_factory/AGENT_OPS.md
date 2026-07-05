# FF Factory — Agent Ops Playbook (2026-07-05)

> คู่มือ orchestration ของ factory: ใครทำอะไร โมเดลไหน เกทอยู่ตรงไหน
> อ่านคู่กับ `SESSION_STATE.md` (สถานะปัจจุบัน) + memory `ai-ugc-ad-factory-workflow` (สถาปัตยกรรมที่ล็อก) + memory `claude-subagents` (นโยบายโมเดล)

## กติกาเหล็ก

1. **Fable = orchestrate ใน main loop เท่านั้น** — ห้ามเป็น subagent (นโยบาย Mirko 2026-07-03)
2. **ห้าม generate/เผาเครดิตจนกว่า Mirko สั่ง "generate" ชัด ๆ** ต่อครั้ง (image เคย pre-approve ตามคำขอ · video/audio ไม่เคย) — คนที่ยิง generate_* ได้มีคนเดียวคือ main loop; subagent ทุกตัวมีกฎ no-credits ฝังในตัวแล้ว
3. **Subagent ส่งออก text เท่านั้น** (copy / prompt / verdict) → orchestrator เป็นคนเซฟไฟล์ + ยิง gen
4. **แก้งาน = re-roll หน่วยที่พังหน่วยเดียว** (หัวใจของระบบโมดูลาร์) — qa-inspector ต้องระบุหน่วยเล็กสุดเสมอ ห้าม re-run ทั้ง batch

## Fleet (ครบ 6 ตัว — `agents/` ใน brain repo, junction เข้า `~/.claude/agents` ทั้งสองเครื่อง)

| ความยาก | งาน | agent | model | สร้าง |
|---|---|---|---|---|
| 1 | storyboard → prompt คู่ (ภาพ+วิดีโอ) + continuity | **storyboard-prompter** | opus | 07-03 (แก้ path ข้ามเครื่อง 07-05) |
| 2 | copy ไทย / hook bank / SPINE script | **script-hook-writer** | opus | 07-05 |
| 3 | debug pipeline / architecture / trade-off | **deep-reasoner** | opus | 07-03 |
| 4 | QA 2 เกท (checklist + ffmpeg + ssim) | **qa-inspector** | sonnet | 07-05 |
| 5 | teardown คู่แข่ง + feedback loop ผลแอด | **teardown-analyst** | sonnet | 07-05 |
| 6 | mechanical (สคริปต์/rename/format ตาม spec) | **fast-worker** | sonnet | 07-03 |

## Pipeline → ผู้รับผิดชอบ

| stage | งาน | ผู้ทำ | หมายเหตุ |
|---|---|---|---|
| 0 Intake | brief จาก Mirko → job folder + manifest | Fable (main) | สร้าง `jobs/<id>/manifest.json` |
| 1 Concept+Copy | concept matrix + BODY + hook bank | **script-hook-writer** | ถ้ามี ads อ้างอิง/ผลแอดใหม่ ให้ **teardown-analyst** ป้อน insight ก่อน |
| — | **Gate 0**: Mirko อนุมัติ script | Mirko | ก่อน gen ทุกอย่าง |
| 2/3 Art direction | avatar/keyframe + video prompt ต่อ shot, identity lock | **storyboard-prompter** | fan out ต่อ concept ได้ · single-shot เนี้ยบพิเศษ → skill `seedance-2-pro-director` ใน main loop |
| 4 Voice | TTS ไทย 1 track ต่อเนื่อง (architecture B) | Fable + Higgsfield `generate_audio` | **ก่อน** motion เสมอ (lip-sync ตาม VO จริง) |
| — | gen keyframes | Fable + `generate_image` | ต้องมีคำสั่ง generate |
| — | **Gate 1**: ตรวจ keyframe ก่อนจ่ายค่า animate | **qa-inspector** | identity/wardrobe/composition/label |
| 5 Motion | animate + lip-sync (Seedance 2.0 หลัก / Wan 2.7 สำรอง) | Fable + `generate_video` | ต้องมีคำสั่ง generate |
| — | **Gate 2**: lip-sync + seam + drift | **qa-inspector** | fan out ต่อคลิป |
| 6 Assembly | concat `hook[i]+body[c]+cta[c]` + J-cut | deterministic script (ffmpeg) | **fast-worker** เขียน/แก้สคริปต์ตาม spec — ไม่ใช้ LLM ตอนรันจริง |
| 7 Caption/Render | whisper word-timing → Remotion | deterministic (mac) | ห้าม LLM แต่งเวลา caption เอง |
| 8 Feedback | CTR/CPA → kill/scale + อัป hook tier | **teardown-analyst** | ปิด loop กลับเข้า stage 1 |
| ∞ Debug | ปัญหาสถาปัตยกรรม/บั๊กลึก | **deep-reasoner** | read-only, ส่ง recommendation กลับ |

## Fan-out patterns (ยิงขนานใน message เดียว)

- hooks × **storyboard-prompter** (ต่อ concept) · clips × **qa-inspector** (ต่อคลิป) · ads × **teardown-analyst** (ต่อ batch)
- batch ใหญ่ระดับ matrix 8×3 (v2) → Workflow script fan-out — ต้องให้ Mirko สั่ง "use a workflow" ก่อน

## Data contracts (ต่อ job)

```
projects/FF_factory/jobs/<job_id>/
  manifest.json      # status ต่อ stage: pending/running/done/failed → resume ได้
  concepts.json      # จาก script-hook-writer (Fable แปลง output → JSON)
  renderjobs.json    # matrix concepts × hooks
  timeline_<v>.json  # feed Remotion
```
- ไฟล์ text/JSON = อยู่ใน repo (sync ข้ามเครื่อง) · ไฟล์หนัก (png/mp4/wav) = per-machine (mac: `~/Desktop/Ads/FF_factory/` · Windows: `D:\Claude\90-Assets\`) — manifest เก็บ path + เครื่อง
- อ้างรูปข้ามเครื่องผ่าน Higgsfield media library (cloud) เมื่อทำได้

## เครื่องไหนทำอะไร

- **mac mini**: canonical FF_factory assets · Remotion · whisper caption timing · contact-sheet pipeline (`_batch.py`)
- **Windows**: ทุก creative stage (copy/prompt/QA บนไฟล์ที่ sync) + gen ผ่าน Higgsfield MCP (media library อยู่ cloud) · ยังไม่มี node/whisper → assembly+caption ทำบน mac ไปก่อน

## Roadmap (ไม่ big-bang)

- **v0 PoC (ตอนนี้)**: 1 body + hook#1 (meta-reveal) + hook#3 (cost-anchor) → TTS → animate → concat J-cut → qa-inspector ตรวจ 2 physical risks (lip-sync, seam) · avatar พร้อมแล้ว = FF-CORE-01 "Ploy" · **บล็อกที่คำสั่ง generate + อนุมัติ script จาก Mirko เท่านั้น**
- **v1**: manifest schema จริง + Gate 1 เข้า flow ทุก job + สคริปต์ concat มาตรฐาน (fast-worker เขียนครั้งเดียวใช้ตลอด)
- **v2**: matrix runner 8×3 — Workflow fan-out (สั่ง gen เป็นชุดหลังอนุมัติครั้งเดียวต่อ batch) + Gate 2 ขนานอัตโนมัติ
- **v3**: feedback loop จริง — teardown-analyst อ่านผลแอด → matrix รอบถัดไป

## เศรษฐศาสตร์ที่ห้ามลืม

8 concepts × 3 hooks ≠ 24 คลิปเต็ม → **8 BODY หนัก + 24 HOOK สั้น + concat ฟรี** ≈ ประหยัด 50-60% และ body เหมือนกัน 100% ทุก variant · ตัวแปรที่ชี้ขาด = 3 วินาทีแรก จึง test ที่ hook เป็นหลัก
