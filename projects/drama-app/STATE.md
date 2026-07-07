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
2. ต่อ gen API (kie.ai/Higgsfield) แทนคัดลอกมือ — Higgsfield มี MCP อยู่แล้ว
3. polish UI / auth / deploy · push ขึ้น GitHub remote ถ้าอยากข้ามเครื่อง
- **แก้ intel-pack = ต้อง re-copy เข้า `D:\drama-app\prompts\` + rerun recheck ข้ามไฟล์**
