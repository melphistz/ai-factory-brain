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

## 🔜 PENDING: UI redesign ตาม smartaihub.app reference (07-08 — รอ Mirko reset quota ก่อนเริ่ม)

**บริบท:** Mirko ส่ง screenshot หน้า UI ของ smartaihub.app (แอปคนอื่น ดู `memory/smartaihub-drama-series.md`) มาถามว่าอยากได้ layout แบบนั้น — คุยกันแล้วตกลงขอบเขต ก่อนเริ่มลงมือให้อ่าน turn การคุยเรื่องนี้ในเซสชัน 07-08 ประกอบ (มี screenshot 4 ภาพ: gallery ตัวละคร, หน้า studio ต่อช็อต, หน้าเนื้อเรื่องเต็ม)

**ตัดสินใจสำคัญ: ปฏิเสธการเจนภาพ auto ในแอป** — เคยพิจารณา "กดปุ่มแล้วเจนภาพด้วย GPT Image 2 ในตัว" แต่ตัดออกเพราะ (1) เสียเงินจริงทุกครั้งที่กด ขัดนโยบาย prompt-first/manual-gen เดิม (2) มีคนเสนอวิธี "ฟรี" โดยเอา OAuth session token ของ ChatGPT subscription (mirko.foxfunnels) ไปยิง endpoint ภายใน `chatgpt.com/backend-api/codex/responses` ตรงๆ — **ปฏิเสธไปแล้ว เพราะขัด ToS ของ OpenAI ชัดเจน + หลักฐานในสกรีนช็อตเองก็โชว์ว่าโดน revoke (401 token_revoked) แล้ว = OpenAI ตรวจจับ pattern นี้อยู่จริง ความเสี่ยงบัญชี subscription โดนแบนไม่คุ้ม** → **สรุป: อยู่ prompt-first ต่อ ไม่มีการเจนอัตโนมัติในแอปเลย ไม่ว่าทางไหน**

**แผน UI ที่ตกลงกัน เรียงตามลำดับความสำคัญ:**
1. **[ตัวปลดล็อกสำคัญสุด] "อัปโหลดรูปกลับเข้าระบบ"** — endpoint รับไฟล์ที่ Mirko เจนเองจาก Higgsfield/ChatGPT แล้วอัปโหลดกลับมาแปะเป็น thumbnail ต่อตัวละคร/ต่อช็อต — ไม่ผิดนโยบายอะไร และเป็นตัวเดียวที่ทำให้ gallery/thumbnail แบบใน reference มีความหมายจริง (ตอนนี้แอปไม่เคยโชว์รูปเลยเพราะ prompt-only) **ทำก่อนอย่างอื่นทั้งหมด**
2. Sidebar รายชื่อโปรเจกต์/ซีรีส์แบบถาวร (ตอนนี้ไม่มี nav ข้ามซีรีส์เลย)
3. รีดีไซน์การ์ดตัวละครเป็น gallery grid + panel รายละเอียดลอยด้านล่างเมื่อเลือก (แทนที่ `CharacterCard.tsx` แบบ list+`<details>` ปัจจุบัน)
4. ปุ่ม bulk "สร้างพรอมต์วิดีโอทั้งตอน" — วน `/api/video-prompt` เดิมทุกช็อตในตอน ไม่ต้องมี logic ใหม่
5. Emotion chip บนบทพูด (ข้อมูล emotion มีอยู่แล้วในระบบ แค่ยังไม่โชว์สวย)
6. **(07-09) "แนว" ในฟอร์มสร้างซีรีส์ → เปลี่ยนเป็น dropdown 5 ตัวเลือก** (romance-drama/comedy/thriller-horror/action/family) **+ ผูก backend จริง** — ตอนนี้ "แนว" เป็นแค่ text ต่อท้าย brief เฉยๆ ไม่ได้เลือก genre pack ไหนเลย ต้องทำคู่กับ wire `SeriesBible.genre` + inject `genre_pack` เข้า envelope (ของเดิมที่ค้างอยู่ข้อ 23 ด้านบน — งานเดียวกัน ทำพร้อมกัน) · "โทน" คงเป็น free-text เดิม (คำบรรยายอารมณ์ หลากหลายเกิน dropdown)
- **ตัดทิ้งจาก reference:** ปุ่มเจนภาพในตัว, ปุ่ม "สลับภาพ AI" — ขัด prompt-first

**Model/cost:** ตกลงแล้วว่างานนี้เป็น build/production tier (ดู `feedback-model-effort-strategy.md`) — **ใช้ Sonnet พอ ไม่ต้อง Fable/ultracode** ประเมินคร่าวๆ ~300K–600K tokens (เทียบ build v1 เต็มระบบที่ใช้ 1.02M ด้วย Opus/9 agents) แบ่งทำเป็น 2 รอบได้ถ้าอยากประหยัด: รอบแรกแค่ข้อ 1 (upload-back) ก่อน ดูผลแล้วค่อยทำข้อ 2-5

**สถานะ:** ยังไม่เริ่มทำ — Mirko ขอรอ quota/context reset ก่อน (burn ไป Fable ultracode เยอะคืนก่อนหน้า) เริ่มได้ทันทีเมื่อพร้อม ไม่ต้องวางแผนใหม่

## 🔜 PENDING: genre pack ใหม่ "revenge/vindication" (07-09 — ยังไม่เริ่ม)

**บริบท:** Mirko ถามเรื่องกระแสละคร AI ไวรัลจริง (โพสต์ขายคอร์สอ้างละคร "ผกาแก้ว x ขจรเดช" ยอดวิวหลักล้าน — ยืนยันจริงว่าไวรัล เป็นเทรนด์ "ละครคุณธรรมผลไม้/ผัก AI" ต้นตอจาก international "Fruit Love Island") คุยกันแล้วสรุปว่าโมเดลรายได้คนละแบบกับ drama-app เรา (ad-revenue-share ตาม view vs paid-unlock ของเรา) — ไม่ใช่สิ่งที่ต้องเลียนแบบ 1:1

**สิ่งที่ตกลง:** drama-app ควรทำตามสูตรที่พิสูจน์แล้วว่า convert ดีสุดในฟอร์แมตนี้ = **ขาว-ดำสุดขั้ว** (ตัวร้ายเลวสนิทไม่มีเหตุผลรองรับ, นางเอก/พระเอกถูกกระทำเกินเหตุแล้วพลิกสะใจ) แบบที่ ReelShort/DramaBox ใช้เป็นแกนหลัก (สลับตระกูลลูก/แม่เลี้ยงใจร้าย/หมั้นซ้อน/แฉแล้วเหยียบกลับ) — เช็คแล้ว `09-genre-packs.md` pack `romance-drama` ปัจจุบัน**ยังไม่ครอบคลุมพอ** (เน้นแผลรัก/ความลับ ไม่ใช่ cruelty→humiliation→triumphant reveal)

**ตัดสินใจ:** เพิ่ม **genre pack ใหม่แยกต่างหาก** `revenge-vindication` (ไม่แก้ baseline เดิม) ตามโครง 8 หัวข้อเดียวกับ pack อื่น (hook weighting / beat flavor / acting grammar / visual-lighting / director presets / cliffhanger patterns / AI-gen pitfalls / pacing)

**Model:** งานนี้เป็น **intelligence-asset (freeze ยาว)** ตาม [[feedback-model-effort-strategy]] ไม่ใช่ production — เดิมจะใช้ Fable (โมเดลฉลาดสุดตอนทำ pack ชุดแรก) แต่ **Fable ใช้ไม่ได้แล้วตอนนี้** → กฎคือ "โมเดลฉลาดสุดที่มี" ไม่ใช่ hardcode ชื่อ Fable ดังนั้นใช้ **Opus 4.8 + ultracode + verify 2 เลนส์ (fidelity + operability)** แทน · settings.json pin Opus 4.8 ไว้แล้ว (apply ตอน restart session)

**สถานะ:** ยังไม่เริ่ม — Mirko ขอ "เอาเข้าแผนก่อน" รอสั่งเริ่มเอง เมื่อเริ่ม: restart/สลับ `/model` → Opus 4.8 → dispatch ออกแบบ pack ผ่าน ultracode (ห้าม main loop เขียนเอง ตาม CLAUDE.md) → เสร็จแล้ว deploy เข้า `D:\drama-app\prompts\` เหมือน pack ชุดแรก + rerun smoke
