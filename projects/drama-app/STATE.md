# drama-app — STATE

- **โปรเจกต์:** ระบบ web app ผลิตซีรีส์ละครแนวตั้งของเราเอง (ต้นแบบ = `memory/smartaihub-drama-series.md`)
- **โค้ดอยู่ที่:** `D:\drama-app` (git repo แยก บนเครื่อง Windows — ยังไม่มี remote, per-machine · brain repo เก็บแค่ STATE นี้ + intel-pack)
- **stage (2026-07-07): APP v1 = BUILT + VERIFIED ✅**

## v1 ทำอะไรได้ (prompt-first — ยังไม่ call gen API)
Next.js 15 + TS + Tailwind · เก็บข้อมูลเป็น JSON ต่อซีรีส์ (`data/<id>.json`) · LLM ผ่าน @anthropic-ai/sdk (`LLM_MOCK=1` เป็น default เปิดได้ทันทีไม่ต้องมี key) · system prompts โหลดจาก `prompts/` (= intel-pack 9 ไฟล์ ก๊อปมา) ไม่ hardcode
- pipeline: brief → **/api/bible** (series bible + แผนรายตอน) → **/api/script** (สคริปต์ตอน 5 ช่วง) → **/api/shots** (shot list) → **/api/characters** (การ์ด + identity-lock image prompts) → **/api/ledger** (materialize continuity — single writer) → **/api/keyframe-prompt** + **/api/video-prompt** (budget meter 3200/1800 + คัดลอก + QA checklist 2 เกท)
- 14 route, 20 components (BudgetMeter/QaChecklist/LedgerBoard/PromptPanel ฯลฯ)

## verify ที่ทำจริง (Opus + main loop double-check)
- `npm run build` ผ่าน 14 route · integrate smoke API 7/7 = 200 ตรง contracts · main loop รันเซิร์ฟจริง GET 6 หน้า SSR ทุกหน้า 200 render จริง (demo series `demo-kon-fon-ja-yut`)
- git: 3 commits (scaffold b11e033 / integrate 00a66cb / fix 602a005) working tree สะอาด
- fix รอบ review แก้ 5 (1 critical): store.ts per-series async mutex กัน lost-update · atomic rename retry (Windows EPERM) · keyframe verbatim-anchor guard (422 ถ้า anchor ไม่ครบ) · sanitize ไทยไม่ให้รั่วเข้า EN prompt · error หุ้มไทย+status

## วิธีรัน
`cd D:\drama-app` → refresh PATH (`$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine')+';'+[Environment]::GetEnvironmentVariable('Path','User')`) → `npm run dev` → เปิด localhost:3000 · ใส่ ANTHROPIC_API_KEY + set LLM_MOCK= (ว่าง) ใน .env.local เพื่อเจนจริง (default mock)

## ส่วนขยาย genre (07-07 คืนเดียวกัน — Fable ก่อนหมดสิทธิ์)
- **`intel-pack/09-genre-packs.md`** — 5 แนว: romance-drama (baseline) / comedy (deadpan family) / thriller-horror / action (กฎกันเจนพัง) / family — pack ละ 8 หัวข้อ (hook weighting / beat flavor / acting grammar / visual-lighting / director presets / cliffhanger patterns / AI pitfalls / pacing) ≤4,500 chars
- **Backward-compatible จริง (พิสูจน์แล้ว):** `SeriesBible.genre` + `PromptEnvelope.genre_pack` เป็น optional ทั้งคู่ default=romance-drama · deploy เข้า `D:\drama-app\prompts\` แล้ว (commit `d96f8a2`) build ผ่าน + smoke /api/bible แบบไม่ส่ง genre = 200 เหมือนเดิม
- **งานค้างเล็ก (Opus):** UI ยังไม่มีช่องเลือก genre + แอปยังไม่ inject genre_pack เข้า envelope (09 อยู่ใน prompts/ แล้วแต่ยังไม่ถูกเรียก) — wire ตาม spec ใน 00-contracts §1.1/§1.7

## ถัดไป (ตัวเลือก — ให้ Mirko เลือก)
1. ลองใช้จริง: เจนซีรีส์ทดสอบ 1 เรื่อง (mock ก่อน แล้วต่อ key จริง) → ดูว่า output ตรงใจไหม แก้ prompt ใน intel-pack ได้
2. ~~ต่อ gen API (kie.ai/Higgsfield) แทนคัดลอกมือ~~ — **ตัดสินใจแล้ว 07-08: อยู่ prompt-first ต่อ ไม่ต่อ gen API** (ดูเหตุผล §UI redesign ด้านล่าง)
3. polish UI / auth / deploy · push ขึ้น GitHub remote ถ้าอยากข้ามเครื่อง
- **แก้ intel-pack = ต้อง re-copy เข้า `D:\drama-app\prompts\` + rerun recheck ข้ามไฟล์**

## 🔄 UI redesign ตาม smartaihub.app reference (07-08 วางแผน · 07-10 เริ่มข้อ 1)

**✅ 07-10/11 DONE 8/8 ข้อ** (เว้นข้อ 6 = รวม STEP 8 genre×setting) — overnight autonomous chain, Sonnet build tier, sequential + build/smoke gate + commit checkpoint ต่อข้อ. drama-app commits (local, ยังไม่ push — no remote):
- `af503f5` ข้อ1 upload-back (endpoint /api/upload-image + ImageUpload + thumbnail) · `cb1d575` ข้อ3 gallery grid + detail panel · `33fe5ac` ข้อ8 success toast · `8c9c5d3` ข้อ7 แปลศัพท์เทคนิค→ไทย (เก็บใน tooltip) · `966526c` ข้อ2 sidebar ข้ามซีรีส์ · `d63a817` ข้อ4 ปุ่ม bulk video-prompt ทั้งตอน · `7cd0e64` ข้อ5 emotion chip สี+emoji · `9435a07` ข้อ9 rename Ledger→"ความต่อเนื่อง"+คำอธิบาย
- **final build ✓** 15 route (static gen 10/10) · ทุกข้อ smoke จริงผ่าน (Bash run_in_background npm start + curl)
- **บทเรียน orchestration:** (1) template verify อ่อนกับ copy/semantic task — ข้อ 7 รอบแรก drift (agent ไปทำ thumbnail แทนแปลศัพท์, verify PASS หลอกเพราะเช็คแค่ build) → main loop เช็ค diff เอง จับได้ revert+re-dispatch prompt ชัด (ย้ำ "งานแปลข้อความ ห้ามแตะรูป" + verify ต้อง grep) สำเร็จ · **ต้องเช็ค diff เองทุก copy task** (2) ข้อ 2 workflow ล้ม StructuredOutput retry cap แต่ implement เขียนไฟล์เสร็จก่อนล้ม → เช็ค build+อ่าน logic เอง = สมบูรณ์ commit ได้ ไม่ต้อง re-run (3) routine ต่อข้อ: commit checkpoint → revert data/ smoke side-effect → kill zombie server port 3000 (Get-NetTCPConnection+Stop-Process, Start-Process โดน sandbox block)
- **known minor (ทำเพิ่มทีหลัง/polish):** sidebar ยังไม่มี active-series highlight (server component) · next-start snapshot public/ ตอน boot → รูป upload runtime อาจไม่ serve จน restart (dev mode ปกติ) · ข้อ 6 genre×setting dropdown = ทำตอน STEP 8

### 🌙 AUTONOMOUS OVERNIGHT PLAN (07-10 — เดิม, ทำครบแล้ว ดูผลด้านบน)

### 🌙 AUTONOMOUS OVERNIGHT PLAN (07-10 — Mirko ไปนอน สั่งทำ UI ให้ครบแล้ว save+sync)
Mirko: "ถ้า 1 จบ รัน 2-5 แล้ว 7-9 เลย · คุม subagent ดีๆ" → main loop orchestrate เอง **sequential ทีละข้อ** (ห้ามขนาน — หลายข้อแตะไฟล์เดียว: ข้อ 1/3/8 = CharacterCard · 3/7/8 = หน้า character)
- **order (dependency-aware):** 1(รันอยู่) → 3(gallery card) → 8(toast success) → 7(ซ่อนศัพท์) → 2(sidebar) → 4(bulk video-prompt) → 5(emotion chip) → 9(rename Ledger) · **เว้น 6**
- **ต่อข้อ:** 1 workflow (scout→implement→build→fix, Sonnet+high) · รอจบ · build ผ่าน = **git commit `ui: item N ...` ใน D:/drama-app** (checkpoint) · build fail หลัง fix = `git checkout` revert เฉพาะข้อนั้น + mark skipped ในสรุป (ไม่ลามข้อถัดไป)
- **ก่อน commit ทุกครั้ง:** `git status` + เช็ค `.gitignore` มี `.env*` (กัน commit ANTHROPIC_API_KEY) · drama-app = local repo ไม่มี remote → commit only ไม่ push
- **smoke test genre×setting (Opus, รันคู่):** เสร็จ = เก็บผล 2 pack + verdict ลง `smoke-test-result.md` · **ยังไม่ deploy** (รอ Mirko approve ตอนตื่น)
- **ปิดงาน:** ครบทุกข้อ + smoke test เสร็จ → อัพเดต STATE + save+sync brain repo (git add+commit+push · ระวัง secret) → drama-app commit local
- **สรุปตอนตื่น:** ข้อไหนผ่าน/พัง/skip + smoke test verdict + วิธีทดสอบ UI + design รอ approve

**บริบท:** Mirko ส่ง screenshot หน้า UI ของ smartaihub.app (แอปคนอื่น ดู `memory/smartaihub-drama-series.md`) มาถามว่าอยากได้ layout แบบนั้น — คุยกันแล้วตกลงขอบเขต ก่อนเริ่มลงมือให้อ่าน turn การคุยเรื่องนี้ในเซสชัน 07-08 ประกอบ (มี screenshot 4 ภาพ: gallery ตัวละคร, หน้า studio ต่อช็อต, หน้าเนื้อเรื่องเต็ม)

**ตัดสินใจสำคัญ: ปฏิเสธการเจนภาพ auto ในแอป** — เคยพิจารณา "กดปุ่มแล้วเจนภาพด้วย GPT Image 2 ในตัว" แต่ตัดออกเพราะ (1) เสียเงินจริงทุกครั้งที่กด ขัดนโยบาย prompt-first/manual-gen เดิม (2) มีคนเสนอวิธี "ฟรี" โดยเอา OAuth session token ของ ChatGPT subscription (mirko.foxfunnels) ไปยิง endpoint ภายใน `chatgpt.com/backend-api/codex/responses` ตรงๆ — **ปฏิเสธไปแล้ว เพราะขัด ToS ของ OpenAI ชัดเจน + หลักฐานในสกรีนช็อตเองก็โชว์ว่าโดน revoke (401 token_revoked) แล้ว = OpenAI ตรวจจับ pattern นี้อยู่จริง ความเสี่ยงบัญชี subscription โดนแบนไม่คุ้ม** → **สรุป: อยู่ prompt-first ต่อ ไม่มีการเจนอัตโนมัติในแอปเลย ไม่ว่าทางไหน**

**แผน UI ที่ตกลงกัน เรียงตามลำดับความสำคัญ:**
1. **[ตัวปลดล็อกสำคัญสุด] "อัปโหลดรูปกลับเข้าระบบ"** — endpoint รับไฟล์ที่ Mirko เจนเองจาก Higgsfield/ChatGPT แล้วอัปโหลดกลับมาแปะเป็น thumbnail ต่อตัวละคร/ต่อช็อต — ไม่ผิดนโยบายอะไร และเป็นตัวเดียวที่ทำให้ gallery/thumbnail แบบใน reference มีความหมายจริง (ตอนนี้แอปไม่เคยโชว์รูปเลยเพราะ prompt-only) **ทำก่อนอย่างอื่นทั้งหมด**
2. Sidebar รายชื่อโปรเจกต์/ซีรีส์แบบถาวร (ตอนนี้ไม่มี nav ข้ามซีรีส์เลย)
3. รีดีไซน์การ์ดตัวละครเป็น gallery grid + panel รายละเอียดลอยด้านล่างเมื่อเลือก (แทนที่ `CharacterCard.tsx` แบบ list+`<details>` ปัจจุบัน)
4. ปุ่ม bulk "สร้างพรอมต์วิดีโอทั้งตอน" — วน `/api/video-prompt` เดิมทุกช็อตในตอน ไม่ต้องมี logic ใหม่
5. Emotion chip บนบทพูด (ข้อมูล emotion มีอยู่แล้วในระบบ แค่ยังไม่โชว์สวย)
6. **(07-09) "แนว" ในฟอร์มสร้างซีรีส์ → เปลี่ยนเป็น dropdown 5 ตัวเลือก** (romance-drama/comedy/thriller-horror/action/family) **+ ผูก backend จริง** — ตอนนี้ "แนว" เป็นแค่ text ต่อท้าย brief เฉยๆ ไม่ได้เลือก genre pack ไหนเลย ต้องทำคู่กับ wire `SeriesBible.genre` + inject `genre_pack` เข้า envelope (ของเดิมที่ค้างอยู่ข้อ 23 ด้านบน — งานเดียวกัน ทำพร้อมกัน) · "โทน" คงเป็น free-text เดิม (คำบรรยายอารมณ์ หลากหลายเกิน dropdown)
7. **(07-09, feedback จากลองใช้จริง) ซ่อนศัพท์เทคนิคจาก UI** — หน้าตัวละคร/studio โชว์คำอย่าง "04 character-architect", "P1/P2/P3", "IDENTITY_ANCHOR_EN (VERBATIM — ห้าม PARAPHRASE)", "LEDGER DRAFT (WARDROBE · SCOPE SERIES)", "entity char01_fon · materialize เป็น LedgerEntry" ตรงๆ — งงสำหรับคนไม่ใช่ dev ต้องแปลเป็นภาษาเข้าใจง่าย (เช่น "ล็อกหน้าตัวละคร", "ชุดที่ใส่", "รูปที่ 1: หน้าตรง") ศัพท์เทคนิคเก็บไว้แค่ใน tooltip/expand ถ้าจำเป็น
8. **(07-09) ปุ่ม "สร้างการ์ดตัวละคร" ไม่มี success feedback** — ทดสอบแล้ว API ทำงานถูกต้อง (POST /api/characters คืน 200 จริง) แต่กดแล้วดูเหมือนไม่มีอะไรเกิดขึ้น (โดยเฉพาะ series demo ที่ mock คืนข้อมูลเดิมซ้ำ หน้าเลยดูไม่เปลี่ยน) → เพิ่ม toast/แจ้งเตือนสำเร็จชัดเจนหลังกด ไม่ใช่แค่ router.refresh() เงียบๆ
9. **(07-09) แถบ "Ledger" ผู้ใช้ไม่เข้าใจว่าคืออะไร** — ต้อง rename เป็นภาษาที่สื่อความหมาย (เช่น "ความต่อเนื่อง" หรือ "เช็คของ/ชุด") + มีคำอธิบายสั้นในหน้าว่ามันช่วยกันหน้า/ชุด/ของเพี้ยนข้ามช็อต ไม่ใช่แค่คำว่า Ledger ลอยๆ
- **ตัดทิ้งจาก reference:** ปุ่มเจนภาพในตัว, ปุ่ม "สลับภาพ AI" — ขัด prompt-first

**Model/cost:** ตกลงแล้วว่างานนี้เป็น build/production tier (ดู `feedback-model-effort-strategy.md`) — **ใช้ Sonnet พอ ไม่ต้อง Fable/ultracode** ประเมินคร่าวๆ ~300K–600K tokens (เทียบ build v1 เต็มระบบที่ใช้ 1.02M ด้วย Opus/9 agents) แบ่งทำเป็น 2 รอบได้ถ้าอยากประหยัด: รอบแรกแค่ข้อ 1 (upload-back) ก่อน ดูผลแล้วค่อยทำข้อ 2-5

**สถานะ:** ยังไม่เริ่มทำ — Mirko ขอรอ quota/context reset ก่อน (burn ไป Fable ultracode เยอะคืนก่อนหน้า) เริ่มได้ทันทีเมื่อพร้อม ไม่ต้องวางแผนใหม่

## 🔜 PENDING: genre pack ใหม่ "revenge/vindication" (07-09 — ยังไม่เริ่ม)

**บริบท:** Mirko ถามเรื่องกระแสละคร AI ไวรัลจริง (โพสต์ขายคอร์สอ้างละคร "ผกาแก้ว x ขจรเดช" ยอดวิวหลักล้าน — ยืนยันจริงว่าไวรัล เป็นเทรนด์ "ละครคุณธรรมผลไม้/ผัก AI" ต้นตอจาก international "Fruit Love Island") คุยกันแล้วสรุปว่าโมเดลรายได้คนละแบบกับ drama-app เรา (ad-revenue-share ตาม view vs paid-unlock ของเรา) — ไม่ใช่สิ่งที่ต้องเลียนแบบ 1:1

**สิ่งที่ตกลง:** drama-app ควรทำตามสูตรที่พิสูจน์แล้วว่า convert ดีสุดในฟอร์แมตนี้ = **ขาว-ดำสุดขั้ว** (ตัวร้ายเลวสนิทไม่มีเหตุผลรองรับ, นางเอก/พระเอกถูกกระทำเกินเหตุแล้วพลิกสะใจ) แบบที่ ReelShort/DramaBox ใช้เป็นแกนหลัก (สลับตระกูลลูก/แม่เลี้ยงใจร้าย/หมั้นซ้อน/แฉแล้วเหยียบกลับ) — เช็คแล้ว `09-genre-packs.md` pack `romance-drama` ปัจจุบัน**ยังไม่ครอบคลุมพอ** (เน้นแผลรัก/ความลับ ไม่ใช่ cruelty→humiliation→triumphant reveal)

**ตัดสินใจ:** เพิ่ม **genre pack ใหม่แยกต่างหาก** `revenge-vindication` (ไม่แก้ baseline เดิม) ตามโครง 8 หัวข้อเดียวกับ pack อื่น (hook weighting / beat flavor / acting grammar / visual-lighting / director presets / cliffhanger patterns / AI-gen pitfalls / pacing)

**Model:** งานนี้เป็น **intelligence-asset (freeze ยาว)** ตาม [[feedback-model-effort-strategy]] ไม่ใช่ production — เดิมจะใช้ Fable (โมเดลฉลาดสุดตอนทำ pack ชุดแรก) แต่ **Fable ใช้ไม่ได้แล้วตอนนี้** → กฎคือ "โมเดลฉลาดสุดที่มี" ไม่ใช่ hardcode ชื่อ Fable ดังนั้นใช้ **Opus 4.8 + ultracode + verify 2 เลนส์ (fidelity + operability)** แทน · settings.json pin Opus 4.8 ไว้แล้ว (apply ตอน restart session)

**สถานะ:** ✅ **DONE (07-10)** — pack ที่ 6 `revenge-vindication` (4,366 chars ≤4,500) deploy ครบ
- **build ผ่าน ultracode Workflow** (7 agents, 0 error, ~858K tokens, Opus 4.8 inherit): Draft ×3 เลนส์ (mechanic-fidelity/ai-operability/tonal-swing) → Synthesize → Verify ×2 เลนส์ (fidelity+operability, adversarial, ทั้งคู่ PASS) → Repair (แก้ 3 minor: trace [SAH]→[CAST], เติม trope แม่เลี้ยง/สลับตัว, trim budget)
- pack แกน = cruelty→humiliation→triumphant reveal (ขาว-ดำสุดขั้ว ReelShort/DramaBox) · ครบ 8 หัวข้อ a-h ตาม template · casting idol-glam รวมนางร้าย [[feedback-drama-character-casting]] · Fincher preset สำหรับ reveal beat
- **deploy:** แปะเข้า `intel-pack/09-genre-packs.md` (ก่อน `> Sources:`, +tag [CAST] ใน footer) + enum `revenge-vindication` ใน `00-contracts.md §1.1` + สารบัญ/ตาราง §09 → copy 09+00 เข้า `D:\drama-app\prompts\` (diff identical)
- **verify:** `npm run build` ผ่าน 14 route · grep ยืนยัน 00+09 = static reference แอปยังไม่โหลด runtime (zero-touch, backward-compat สมบูรณ์) — endpoint โหลดแค่ 01/02/04/05/06/07
- **⚠️ ค้าง (งานเดียวกับ UI redesign ข้อ 6):** แอปยังไม่ inject `genre_pack` เข้า envelope → pack ทั้ง 6 อยู่ใน prompts/ แต่ยังไม่ถูกเรียกจริง · ต้อง wire ตอนทำ UI redesign
- teardown validation ชั้น 3 = section ล่าง (จะเสริม/ทับด้วยข้อมูลจริงจาก bilibili.tv ทีหลัง)

## 🔜 PENDING: teardown ละคร revenge จริง → validate/เสริม pack (07-10 — รอ Mirko ส่งคลิป)

**บริบท:** Mirko ถาม "วิธีการเล่า" ใน 09-genre-packs มาจากไหน — ตอบตรง: pack แบ่ง 3 ชั้นความแข็ง (1) โครงกระดูก 5 ช่วง+hook 4 ประเภท = hard source `vertical-drama-basics-dramy` (Dramy.ai) · (2) craft การเจน = hard source `seedance-knowledge` (validated จากเจนจริง) · (3) **"วิธีเล่าเฉพาะแนว" (เช่น revenge = cruelty→humiliation→triumphant reveal) = informed synthesis** จาก LLM dramatic-convention (archetype Monte Cristo/Cinderella-flip) + market observation (ReelShort/DramaBox/ผกาแก้ว×ขจรเดช) — **ยังไม่ผ่าน systematic teardown เชิงประจักษ์** (ต่างจาก `ads-50-teardown` ที่แกะโฆษณาจริง 50 ตัว) = gap ที่ยอมรับ

**แผน teardown 3 เฟส (model/effort ตัดสินแล้วตาม [[feedback-model-effort-strategy]]):**
| เฟส | งาน | โมเดล/effort | ใครทำ |
|---|---|---|---|
| 1. เตรียมของ | contact sheet (ffmpeg 5×6) + transcript (whisper ASR) | ไม่มี LLM = script ล้วน (`_batch.py` มีอยู่) | ผม |
| 2. teardown per-clip ×8-15 | สกัด hook/beat/cliffhanger ต่อคลิป | **Sonnet + high** (fan-out ขนาน, `teardown-analyst`) | ผม |
| 3. synthesis → สูตรกลาง → feed เข้า pack | รวม pattern ข้ามคลิป เป็นสูตร revenge เชิงประจักษ์ | **Opus 4.8 + xhigh + ultracode verify 2 เลนส์** | ผม (dispatch) |

**หลัก:** effort สูง=ช้าลงไม่เร็ว → เฟส 2 ใช้ high พอ, เร่งด้วย parallel · เผา Opus แค่เฟส 3 จุดเดียว (asset freeze), ที่เหลือ Sonnet = คุ้มสุด · contact sheet=ภาพ ตัวแกะต้องมี vision (Sonnet มี)

**Tooling setup (07-10 — เตรียมเฟส 1, ยังไม่เสร็จ):**
- ✅ **yt-dlp ติดตั้งแล้ว** (v2026.07.04) — เรียกผ่าน `python -m yt_dlp` (ไม่อยู่ใน bash PATH ตรงๆ) · เครื่องมี python 3.10 + node v24
- ❌ **ffmpeg ยังไม่ติดตั้ง** — ต้องทำก่อน download (bilibili แยก video/audio stream ต้อง merge) + ก่อน contact sheet เฟส 1 · ทางง่ายสุด = `pip install imageio-ffmpeg` (ได้ binary bundled, ไม่ต้อง winget/PATH) หรือ winget install ffmpeg
- ✅ **แหล่ง = bilibili.tv (international, /th/) ยืนยันโหลดได้จริง** — probe URL ตัวอย่าง `https://www.bilibili.tv/th/video/4800046393334784` ผ่าน BiliIntl extractor: ไม่ติด login, ไม่ติด geo, ได้ถึง **720×1280 (720P 9:16 แนวตั้ง)** ตรง format · ต่างจาก bilibili.com จีน (ตัวนั้น geo-block บาง OGV) — .tv เป็น global platform มี sub ไทย เหมาะกว่า
- ⚠️ python 3.10 = yt-dlp เตือน deprecated (ยังใช้ได้) — ควรอัพ 3.11+ อนาคต
- **ค้าง:** ติดตั้ง ffmpeg + test download 1 คลิปเต็ม (merge จริง res ไหน) — ทำตอนเริ่ม teardown จริง

**ต้องการจาก Mirko:** คลิปละคร revenge จริง 8-15 ตัว (ReelShort/DramaBox free eps / viral compilation YouTube-TikTok / ผกาแก้ว×ขจรเดช) — โหลด mp4 ไว้ `Desktop/Ads/` แล้วบอก path หรือส่ง link · ไม่ต้อง 50 (revenge สูตรตายตัว 10 เรื่องเห็นโครงซ้ำ)

**ข้อจำกัด:** ReelShort/DramaBox มี paywall → ผมดึงจาก app เองไม่ได้ · ฟรีจริง = viral compilation + ตอนแรกปลดฟรี · ละครไทย YouTube/TikTok โหลดง่ายกว่า

**สถานะ:** ยังไม่เริ่ม — Mirko "เอาทีละส่วน" ขอเซฟเข้าแผนก่อน · pack synthesis (ด้านบน) พอสำหรับตอนนี้ teardown เสริมทีหลังตอนมีคลิป (ทับ/เสริมชั้น 3 ของ pack ด้วยข้อมูลจริง)
- **07-10 scope ตัดสิน:** teardown แกะเฉพาะ **ลำดับการเล่า** (structural beats+timing, world-agnostic) — Mirko: "แนว=แค่ style เปลี่ยนได้ โฟกัสลำดับการเล่า" · 17 links = proven winners (ยอดวิวหลายแสน bilibili) แกะได้ทุกเรื่องไม่ต้องกรอง flavor · ราย link+กลุ่ม = `teardown-sources.md`

## 🔜 DECISION PENDING: แยกสถาปัตยกรรม genre × setting (07-10 — Mirko ชี้, รอ commit)

**Mirko ยืนยัน concept:** "comedy ใช้ setting ไหนก็ได้ คนรวย/คนจน/แฟนตาซี/ย้อนยุค ขอแค่เป็น genre comedy" = **แนวเล่า กับ โลก เป็น 2 มิติอิสระ**
- **แกน 1 = genre/แนวเล่า** (comedy/revenge/romance/thriller/action/family) → hook weighting · beat flavor · acting grammar · cliffhanger · pacing = *วิธีเล่า* (world-agnostic)
- **แกน 2 = setting/โลก** (สมจริง/คนรวย/คนจน/แฟนตาซี/ย้อนยุค) → visual & lighting · prop · ชื่อ/บริบท · casting flavor = *ฉาก* (genre-agnostic)
- แอป: 2 dropdown (แนว × โลก) → inject 2 pack ประกบ · ข้อดี = 6 แนว × N โลก = combination เยอะโดยเขียนแค่ 6+N ไม่ใช่ 6×N

**กระทบระบบปัจจุบัน:** genre pack ทั้ง 6 (รวม revenge ที่เพิ่งทำ) **ผูก flavor ไว้ในตัว** (revenge=modern rich-family, comedy=deadpan family) — ถ้า commit ต้อง refactor: แยกส่วน d) VISUAL&LIGHTING + e) DIRECTOR PRESETS (+ prop/casting) ออกเป็น "setting pack" · ส่วน a/b/c/f/h (hook/beat/acting/cliffhanger/pacing) คงเป็น genre pack · โครงที่ทำมาไม่เสีย แค่จัดใหม่ (บาง pitfalls ก้ำกึ่งต้องคิดละเอียดตอนทำ)
- งานนี้ = intelligence-asset (สถาปัตยกรรม/สัญญากลาง refactor ข้ามหลายไฟล์) → ตาม [[feedback-model-effort-strategy]] = **โมเดลฉลาดสุด+ultracode+verify** (scope ใหญ่ ข้าม 6 pack + contracts §1.1/§1.7 + UI) ไม่ใช่ additive เล็ก
- ต่อยอด UI redesign ข้อ 6 (เดิมจะทำ genre dropdown อย่างเดียว — ตอนนี้เป็น genre × setting 2 dropdown)

**สถานะ:** ✅ **DESIGN DONE (07-10)** — doc เต็ม = `projects/drama-app/genre-setting-design.md` (44KB) · dispatch ผ่าน ultracode workflow (8 agents, ~719K tokens, Opus 4.8): Analyze (section-ownership matrix) → Design ×3 มุม → Synthesize → Verify ×2 เลนส์ (เจอ 5 blocking) → Plan (แก้ blocking ครบใน migration steps)
- **สถาปัตยกรรม:** 6 แนว × 9 โลก = 54 คู่ เขียนแค่ 15 ก้อน · genre ถือ "วิธีเล่า" (09 ผอมลง) · setting ถือ "ฉาก" (ไฟล์ใหม่ 10) · แอป 2 dropdown → inject setting→genre
- **กลไกแก้ปมสำคัญ:** (1) hook = "genre นิยามช่อง (slot) / setting ทาผิว (skin)" กันภาพเซ็นเนเจอร์หาย (2) conflict = บันได 4 ขั้น (HARD > GENRE@function > SETTING@fixture > plot-device) + ทุกโลกต้องมี "หลอดแข็ง/ไม่สวย" ≥1 ให้ genre function เกาะ (3) tie-break จริงมาจาก lint (genre=0 ชื่อหลอด) + LLM ไม่ใช่ inject order
- **9 โลก:** 6 carve จากเดิม (real-urban/home/minimal/dim/gritty/high-society = default ของ 6 แนว) + 3 ใหม่ (rural-poor/fantasy 2-register/period)
- **migration 9 STEP** (0 audit §6 → 6 acceptance test → 7 net-new → 8 wire) · effort: STEP 2/3/6/7 = Opus+ultracode (จุด asset) · STEP 8 wire = Sonnet · ประเมิน ~1.2-1.8M แบ่ง 2 รอบได้
- **✅ Mirko approve + ตอบ (07-10):** เริ่มแบบ **smoke-test 1 โลกก่อน** (high-society) · ย้อนยุค = **จีนวังหลวง xianxia** (ทำตอน STEP 7) · ค่าอื่นใช้ตาม design แนะ (fantasy 2-register, lint gate, ลุคทางเบา 01/02, สมจริงซอย 5)
- **✅ SMOKE TEST PASS (07-10):** ผลเต็ม = `projects/drama-app/smoke-test-result.md` · carve revenge → genre[revenge]ผอม (4,476ch, lint zero-fixture ✅) + setting[high-society] (3,070ch) · **verify PASS ทั้ง 2 เลนส์** (fidelity: ของไม่หาย+humiliation เย็น/สถาบัน · operability: lint/budget/backward-compat) · repaired 1 รอบ · **สถาปัตยกรรมพิสูจน์แล้วว่าเวิร์ก** — คู่นี้เป็น template ให้ carve คู่อื่น · **ยังไม่ deploy รอ Mirko approve** ตอนตื่น → ถ้า OK ทำ migration เต็ม STEP 1-8 (รวม period=xianxia)
