---
name: drama-app-fable-ultracode-retrospective
description: บันทึกวันสร้าง drama-app ทั้งระบบ (intel-pack + แอป + fleet audit + genre packs) ด้วย Fable 5 ultracode ในวันสุดท้ายก่อนโควต้าหมด — 2026-07-07
metadata: 
  node_type: memory
  type: project
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# สร้าง drama-app ด้วย Fable 5 ultracode — วันสุดท้ายก่อนหมดสิทธิ์ (2026-07-07)

## บริบท/แรงจูงใจ

Fable 5 กำลังจะไม่มีให้ใช้แล้ว (โควต้าหมด/เลิกใช้ถาวร) วันนี้จึงเป็นวันตัดสินใจ "รีดงานที่เป็น 'สมองแช่แข็งถาวร' (intelligence-asset) ออกมาให้ได้มากที่สุดก่อนหมดสิทธิ์" แทนที่จะปล่อยโควต้าที่เหลือทิ้งไปเฉยๆ

ต้นเรื่องมาจาก Mirko screenshot แอป `smartaihub.app` (ของคนอื่น ไม่ใช่แผนเดิมของ Mirko เอง) มาถามว่า "ทำแบบนี้ได้ไหม" — เคยมีความเข้าใจผิดในบันทึกก่อนหน้าว่าเป็นไอเดียของ Mirko เอง ซึ่งต้องแก้ให้ตรงตรงนี้: จุดเริ่มคือแอปตัวอย่างที่ไปเจอมา ไม่ใช่ไอเดียที่ Mirko คิดเองตั้งแต่ต้น

จากจุดเริ่มนั้น งานขยายเป็น 5 workflow รวด ในคืนเดียว: เขียน system-prompt "สมอง" ของแอปทั้งชุด (intel-pack) → ตัดสินใจสถาปัตยกรรมที่ค้างอยู่ → build แอปจริงเป็น Next.js → audit ยกระดับ subagent fleet ทั้งหมดที่มีอยู่ (ไหนๆ ก็มี Fable แล้ว) → ขยาย genre pack ให้แอปรองรับได้หลายแนวเรื่อง

## Timeline เหตุการณ์

อ้างอิง git log จริง (`ai-factory-brain` + `drama-app`) และ journal.jsonl จริง 5 ไฟล์ เรียงตามเวลา:

1. **21:27** `8af02e3` (ai-factory-brain, sync) — ปิดงาน **drama-intel-pack** (workflow `wf_ecd789d6-308`, 34 agent calls): เขียน `intel-pack/00-08` (9 ไฟล์ system prompts) จากความรู้ในคลังทั้งหมด รวม 10 critical + 13 minor findings ที่จับได้ระหว่าง audit/fix แต่ละไฟล์ จบด้วย **verdict: NEEDS-DECISION** เพราะเหลือข้อขัดแย้งเชิงสถาปัตยกรรม 3 จุดที่ agent ไม่กล้าตัดสินเอง (anchor เต็ม vs short-lock ใน video prompt / ใครสร้าง LedgerEntry / รูปทรง state_locks)
2. (ระหว่างนั้น) **intel-pack-decisions** (workflow `wf_da57618f-263`, 2 agent calls) — apply คำตัดสินสถาปัตยกรรม A/B/C ที่ orchestrator (Claude) ตัดสินเองจากหลักฐานใน vault (ไม่ใช่ Mirko ตัดสินโดยตรง — Mirko รับทราบผลลัพธ์หลังทำ) ลงจริง 26 จุดใน 7 ไฟล์ + agent ตรวจรับพบและแก้เศษตกค้างอีก 11 จุด → **verdict: READY** — workflow นี้รันจบก่อนที่จะเขียน STATE.md + sync ครั้งแรก ผลของมันจึงถูกรวมอยู่ใน commit `8af02e3` ด้วย (ไม่มี commit แยกของตัวเอง)
3. **22:09** `b11e033` (drama-app, scaffold) — เริ่ม **drama-app-build** (workflow `wf_26ed95df-65e`, 10 agent calls): scaffold Next.js + shared libs + prompt loader + mock mode (41 files, +9985/-0) — เริ่มด้วย Fable ultracode แต่ Mirko สั่ง pause กลางคันแล้วสลับโมเดลเป็น Opus 4.8 (effort high) *(รายละเอียดนี้มาจากบทสนทนาจริงในเซสชัน ไม่ใช่จาก git/journal facts — journal ยืนยันได้แค่ว่า agent แรก `af8a9bdb7bf9408ec` เริ่มไปแล้วไม่มี result และถูก resume ต่อโดย agent ใหม่ `acb91018d95c33715`)* — ต้องแก้ prompt scaffold ให้ agent ใหม่ resume ต่อแทนที่จะรัน `create-next-app` ซ้ำ
4. **22:27** `00a66cb` (drama-app, integrate) — API routes ครบ 7 เส้น + nav layout + mock smoke test **ผ่านทั้งไลน์ 7/7 = 200** + seed demo json
5. **22:41** `602a005` (drama-app, fix) — 2 review agent พบ 1 critical + 4 minor (lost-update race ใน store.ts / Windows rename EPERM / unescaped JSON quote ในบทพูด / error message ไม่หุ้มไทย) → fix agent แก้ครบทั้ง 5 จุด, build+smoke ผ่านซ้ำ
6. **22:45** `e3d3db1` (ai-factory-brain, sync) — อัปเดต STATE.md บันทึกความคืบหน้า
7. **22:47** `bc4553a` (ai-factory-brain, sync) — แก้ MEMORY.md ระบุสถานะ **"v1 BUILT+VERIFIED"** ที่ `D:\drama-app`
8. **23:33** `d96f8a2` (drama-app, prompts sync) — ปิดงาน **intel-pack-genres** (workflow `wf_7c524578-83c`, 11 agent calls): เขียน `09-genre-packs.md` 5 แนว (romance-drama/comedy/thriller-horror/action/family) แต่ละ pack ควบคุมงบตัวอักษร ≤4,500 chars ตาม §3 จริง (วัดได้ romance 4,479 / comedy ปรับจาก 4,501→4,487 / thriller 4,490 / action 4,428 / family 4,213) พบ 0 critical + 2 minor แก้ครบ → deploy เข้า `D:\drama-app\prompts\` จริง, build ผ่าน, smoke test POST /api/bible ไม่ส่ง genre = 200 → **verdict: READY**
9. **23:35** `5d65d55` (ai-factory-brain, fleet audit) — ปิดงาน **fleet-skills-audit** (workflow `wf_bea899ce-d6b`, 34 agent calls): audit+ยกระดับ subagent 8 ตัว (fast-worker, deep-reasoner, teardown-analyst, timeline-builder, script-hook-writer, qa-inspector, storyboard-prompter, asset-prompt-builder) + skill 3 ตัว (video-prompt-builder, seedance-2-pro-director, shotlist-builder) รวมพบ ~23 critical + ~39 minor findings ทั้งชุด (หนักสุด: storyboard-prompter ขาด identity lock/timecode/under-direct acting/hard budget/STEP 0 input-mode ไปเลย 5 เรื่องใหญ่) → agent สุดท้าย (fleet-consistency-audit) แก้ 3 จุดข้ามไฟล์ เหลือ 1 เรื่องรอตัดสินใจ (โครง `_template` เก่า) → **verdict: READY**
10. **23:39** `112c21e` (ai-factory-brain, sync, ไม่นับเป็น commit หลักของ drama-app) — บันทึกบทเรียนเรื่องกลยุทธ์เลือกโมเดล/effort ลง `feedback-model-effort-strategy.md` โดยอ้าง drama-app เป็น case study

หมายเหตุ: ลำดับเวลาข้างต้นคือลำดับที่ **commit ขึ้น git** ไม่ใช่ลำดับที่ workflow เริ่มทำงานเป๊ะ — ลำดับ workflow ที่แท้จริง (จากบทสนทนาในเซสชัน) คือ drama-intel-pack → intel-pack-decisions → (เขียน STATE.md + sync = commit `8af02e3`) → drama-app-build → ... git facts เพียงอย่างเดียว (ไม่มีการ diff ไฟล์ระดับ 03/04/06/07 ใน `8af02e3`) ไม่พอจะยืนยันลำดับนี้ได้ 100% แต่สอดคล้องกับสิ่งที่เกิดขึ้นจริงในเซสชัน

## สถาปัตยกรรม/ผลลัพธ์สุดท้าย

**intel-pack** (`D:\ai-factory-brain\projects\drama-app\intel-pack\`) — 10 ไฟล์: `00-contracts.md`, `01-story-engine.md`, `02-episode-script.md`, `03-continuity-ledger.md`, `04-character-architect.md`, `05-shot-breaker.md`, `06-keyframe-prompt.md`, `07-video-prompt.md`, `08-qa-gates.md`, `09-genre-packs.md` (genre pack เพิ่มทีหลังคืนเดียวกัน)

**drama-app** (`D:\drama-app\`) — Next.js 15 + TypeScript + Tailwind, เก็บข้อมูลเป็น JSON ต่อซีรีส์ (`data/<id>.json`), LLM ผ่าน `@anthropic-ai/sdk` (`LLM_MOCK=1` เป็น default), system prompts โหลดจาก `prompts/` (= intel-pack 9 ไฟล์ ก๊อปมา ไม่ hardcode)
- 7 page routes + 2 layout.tsx + 7 API routes = **14 route** — ตรงกับที่ STATE.md อ้าง "14 route, 20 components" พอดี ไม่มีความคลาดเคลื่อน
- verify แล้วจริง: `npm run build` ผ่าน 14 route, integrate smoke 7/7 endpoint = 200, main loop รันเซิร์ฟจริง GET 6 หน้า SSR ทุกหน้า 200
- 3 commit หลักของแอป: `b11e033` (scaffold) → `00a66cb` (integrate) → `602a005` (fix: mutex กัน race, atomic rename retry, anchor guard, sanitize ไทย, error handling)

**fleet ที่ยกระดับ** (`D:\ai-factory-brain\agents\`) — 8 agent files: opus tier (storyboard-prompter, asset-prompt-builder, script-hook-writer, deep-reasoner) + sonnet tier (qa-inspector, teardown-analyst, timeline-builder, fast-worker) ตรงกับโครง fleet-of-8 เดิมที่บันทึกไว้ พร้อม 3 skills (shotlist-builder, video-prompt-builder, seedance-2-pro-director) ที่ audit ผ่านรอบเดียวกัน

**genre packs** — 5 แนว (romance-drama baseline / comedy deadpan family / thriller-horror / action / family) deploy เข้าแอปจริงแล้วที่ commit `d96f8a2`

**Outstanding ที่ยังไม่เสร็จ** (ระบุชัดใน STATE.md): UI ยังไม่มีช่องเลือก genre และแอปยังไม่ inject `genre_pack` เข้า envelope — ไฟล์ `09-genre-packs.md` อยู่ใน `prompts/` แล้วแต่ยังไม่ถูกเรียกใช้จริง

## บทเรียนสำคัญ

**(ก) Pause กลาง workflow แล้วสลับโมเดลได้จริง ถ้าแก้ prompt ให้ resume-safe ก่อน**
ระหว่าง `drama-app-build` Mirko สั่งหยุดกลางคันแล้วเปลี่ยนจาก Fable เป็น Opus 4.8 (effort high) กลางงาน scaffold *(รายละเอียดนี้มาจากบทสนทนาจริง ไม่ใช่ข้อมูลที่ git/journal ยืนยันได้เอง)* — ทำได้จริงโดยไม่ต้องเริ่มใหม่ทั้งหมด แต่ agent แรก (`af8a9bdb7bf9408ec`) เริ่มไปแล้วไม่มี result ต้องมี agent ใหม่ (`acb91018d95c33715`) เข้ามา resume ต่อ บทเรียนที่ตกผลึก: agent/scaffold ต้องเขียน prompt ให้รองรับ "resume mode" ไว้ล่วงหน้า (เช่น เช็คว่า `create-next-app` รันไปแล้วหรือยัง ไม่รันซ้ำ) ไม่งั้นการสลับโมเดลกลางคันจะเสี่ยงพังงานที่ทำไปแล้ว

**(ข) 3-tier model strategy ที่ตกผลึกวันนี้**
จากคำถามซ้ำๆ ของ Mirko ("ใช้ max พอไหมหรือต้อง ultracode" / "opus ต้อง ultra ไหม" / "effort สูงจะเร็วกว่าไหม") ได้ข้อสรุปบันทึกไว้ที่ `feedback-model-effort-strategy.md`:
- งาน **intelligence-asset** (system prompts, skills, prompt packs, architecture/contracts) = ใช้โมเดลฉลาดสุดที่มี + ultracode + adversarial verify 2 เลนส์ (fidelity + operability) — freeze-once จ่ายแพงครั้งเดียวคุ้ม
- งาน **build/production** (โค้ด, bugfix, UI) = Opus/Sonnet ถูกกว่าและทำได้เท่ากัน เพราะ gate ด้วย build/test/skeptic check อยู่แล้ว
- **effort ≠ ความเร็ว**: high→xhigh→ultra = คิดนานขึ้น = ช้าลง+เปลืองขึ้น ไม่ใช่เร็วขึ้น — จะเร็วขึ้นต้อง**ลด** effort ไม่ใช่เพิ่ม
- ความช้าของ build workflow มาจาก subprocess (npm build / smoke test / tsc) ไม่ใช่ตัวโมเดล

**(ค) Ultracode คุ้มที่สุดกับงาน freeze-ถาวร ไม่ใช่งาน production**
drama-app เองถูกอ้างเป็น case study ตรงๆ ใน feedback file: "intel-pack freeze ด้วย Fable → Opus/Codex build แอปครอบ" — คือ ultracode ทุ่มไปกับ 3 งานที่เป็น "สมอง" (intel-pack, fleet audit, genre packs) ส่วนงาน "ตัวแอป" ที่เป็น production code ใช้ Opus/Sonnet ทำแทนได้เท่ากันโดยไม่ต้องพึ่ง Fable ที่กำลังจะหมดอายุ

**(ง) Adversarial-verify (agent ตรวจกันเอง 2 เลนส์ต่อไฟล์) จับ critical findings ได้จริงเท่าไหร่**
ตัวเลขจาก journal.jsonl จริง (นับจาก JSON โดยตรง ไม่ใช่ grep เพราะ grep รายงานต่ำกว่าจริงในบางไฟล์):
- **drama-intel-pack**: 10 critical + 13 minor จาก audit/fix รอบแรกของ intel-pack 00-08 (เช่น ไม่มีเพดานจำนวนตอน, enum shot_size ขัด contracts, ขาด style_stack verbatim rule)
- **intel-pack-decisions**: 26 จุดแก้ตาม decision + เจอเศษตกค้างเพิ่มอีก 11 จุดในรอบตรวจรับ
- **drama-app-build**: 1 critical + 4 minor (lost-update race, Windows EPERM, unescaped JSON quote, error ไม่หุ้มไทย) — ทั้งหมดถูกแก้ก่อน merge
- **fleet-skills-audit**: ~23 critical + ~39 minor รวมทั้งชุด 8 agents + 3 skills — เยอะสุดในทุก workflow เพราะเป็นการ audit ของเก่าที่สะสมมานาน
- **intel-pack-genres**: 0 critical + 2 minor (งบตัวอักษรเกิน 1 char, wording เอียงไป romance-drama) — น้อยสุดเพราะทำแบบ additive บนฐานที่ผ่าน decision แล้ว

ข้อสังเกต (ไม่ใช่สถิติที่เทียบหน่วยเดียวกันได้ทั้งหมด — intel-pack-decisions นับ "จุดแก้ตาม decision" ไม่ใช่ severity แบบ critical/minor เหมือนตัวอื่น): งานที่เขียนจากศูนย์ (intel-pack) กับงานที่ตรวจของเก่าสะสมมานาน (fleet audit) เจอ critical เยอะกว่างานที่ทำแบบ additive บนฐานที่ผ่าน verify มาแล้ว (intel-pack-genres เจอแค่ 0 critical) — สนับสนุนว่า adversarial verify มีประโยชน์มากที่สุดตอนตรวจของใหม่/ของที่ไม่เคยผ่านการตรวจแบบนี้มาก่อน

## Cost summary

ตัวเลขที่ Mirko สรุปไปแล้วจาก task notification (**ไม่ใช่ตัวเลข system-level ที่แม่นสมบูรณ์** — เป็นตัวเลขจากการรวมยอดที่แจ้งระหว่างงาน ไม่รวม token ของ main loop เอง):
- รวมประมาณ **~7.15M tokens จาก 92 agent calls** ตลอดคืนนี้ — ตัวเลข 92 นี้นับรวมทุก agent call ในเซสชัน (5 workflow หลัก + Gemini Gem 1 agent + template-fix 1 agent) ส่วนตัวเลข 91 ที่นับได้จาก journal.jsonl ของ 5 workflow หลักอย่างเดียว (34+2+10+34+11) เป็นคนละขอบเขต ไม่ใช่การคำนวณผิด
- Fable ultracode ~5.92M tokens — ใช้ในงาน intel-pack, fleet-audit, genre-packs (งาน intelligence-asset ทั้งหมด)
- Opus ~1.17M tokens — ใช้ในงาน Gemini Gem (จากวันอื่น) + build แอป (หลัง Mirko สั่งสลับโมเดลกลางคัน)
- Sonnet ~57K tokens — งาน mechanical เล็กๆ

## ลิงก์ที่เกี่ยวข้อง

[[smartaihub-drama-series]] · [[feedback-model-effort-strategy]] · [[vertical-drama-basics-dramy]] · [[claude-subagents]]
