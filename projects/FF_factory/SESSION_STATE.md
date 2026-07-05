# FF AI UGC Ad Factory — Session State (2026-06-30)

> ⚠️ MIRROR COPY (synced 2026-07-03) — canonical live file = `~/Desktop/Ads/FF_factory/SESSION_STATE.md` on the mac mini.
> Edit there when working on mac; this copy is for reading on other machines. If you edit here on Windows, say so in the commit message and reconcile on mac.

โปรเจกต์: video factory ผลิต AI UGC ad ให้ Fox-Funnels (DFY agency). รายละเอียดเต็มใน memory `ai-ugc-ad-factory-workflow.md` + `ads-50-teardown-ai-video-bootcamp.md`.

## 🎬 Skills ติดตั้งแล้ว (cheat sheet = memory `skills-cheatsheet`)
- `seedance-2-pro-director` (1 shot) · `video-prompt-builder` (ทั้งคลิปจาก brief) · `shotlist-builder` (script→shotlist, patched for Claude Code)
- lane แยกแล้วกัน trigger ชน. บังคับ = พิมพ์ชื่อ skill ตรงๆ
- ref memory: `higgsfield-3step-ai-ad-workflow`, `higgsfield-marketing-studio-workflow`

## ⚠️ กติกา
- **ห้าม generate/preflight/ยิงเครดิต จนกว่า Mirko สั่งชัด** (image เคย pre-approve แล้ว / video+audio ยังไม่)
- Higgsfield balance: 435 credits (plan plus)

## Assets locked
- `FF_factory/avatar/concept1_presenter_anchor.png` — ad first-frame (selfie บ้าน + เสื้อ Fox Funnels brand, 941×1672, 9:16)
- `FF_factory/avatar/FFCORE01_Ploy_identity_sheet.png` — face-lock reference (front/3-4/profile, studio)
- หน้ายืนยันตรงกัน = **FF-CORE-01 "Ploy"** canonical presenter (คนแรก, brand face)
- (ทิ้งได้: presenter_v1.png = soul_2 มี IG chrome / presenter_gptimage2_v1.png = gen ก่อนได้ตัวจริง)

## Avatar prompt ที่ใช้ได้ (GPT Image 2 ใน Higgsfield, vault candid-real Thai)
model `gpt_image_2`, quality high, 2k, aspect 3:4. lane candid-real + Thai 6-field. negative ต้องมี `no app interface, no UI, no username overlay` (กัน soul_2/IG-chrome bug). vault: `ai-influencer-image-prompt.md` (renamed from seedance-ugc-image-prompt.md 2026-07-03)

## Script — concept 1 (cost-compare / DFY) — รออนุมัติ
SPINE ล็อก (problem→mechanism→proof→CTA "ทักแชต") สลับเฉพาะ hook 0-3s.

**BODY (~30s, render ครั้งเดียว/concept):**
> "ยุคนี้ Meta หิววิดีโอมาก คลิปเดียวพังเร็ว คนเลื่อนผ่าน ค่าแอดแพงขึ้นเรื่อยๆ — Fox Funnels ทำวิดีโอแอด AI ให้คุณ 10 ตัว ทั้ง Commercial และ UGC ใน 48 ชั่วโมง ไม่ต้องจ้างทีมถ่าย / แล้วคลิปที่ดูอยู่นี่? AI ของ Fox Funnels ทั้งหมด ไม่ได้ถ่ายจริงสักคลิป / อยากได้ 10 ตัวใน 48 ชม. ทักแชตมาเลย"

**HOOK#1 (meta-reveal):** "คลิปที่คุณกำลังดูนี่... ไม่ถ่ายจริงสักวินาที ทั้งหมดคือ AI" — visual: selfie anchor + super "100% AI ไม่มีกล้อง"
**HOOK#3 (cost-anchor):** "จ้างทีมถ่าย 1 คลิป เกือบเท่าค่าแอดทั้งเดือน รู้ตัวไหม" — visual: framing คนละแบบ (กฎ hook≠body), ถือมือถือโชว์ใบเสนอราคา

10-hook bank เต็ม + tiers อยู่ใน memory + draft `knowledge/ff_ai_ads_modular_bank_v1.md`

## Pipeline เลือกไว้ (ยังไม่รัน)
- TTS Thai VO → lip-sync animate → concat J-cut (architecture B)
- video model: **Seedance 2.0** primary (id `seedance_2_0`, identity + audio_references, 9:16, 1080p) / **Wan 2.7** (`wan2_7`) สำรอง lip-sync เฉพาะทาง
- TTS: Higgsfield generate_audio (text2speech_v2_* — ยังไม่เลือก voice ไทย)
- caption: Remotion (whisper word-timing จาก VO จริง)

## NEXT (เปิด session หน้า)
PoC = 1 body + hook#1 + hook#3 → animate → concat J-cut → ตรวจ **lip-sync quality + รอยต่อ** (2 physical risk).
แนะ staged: ยิง 1 hook สั้นก่อน (เช็ค lip-sync) → ผ่านค่อยทำ body + hook2 + concat. de-risk ก่อนเผาเครดิตเต็ม.
รอ: Mirko สั่ง generate + อนุมัติ script.

## ⚡ PIVOT 2026-07-05 (แก้จาก Windows — reconcile บน mac ด้วย)
Mirko เปลี่ยนโหมด: **prompt-first / manual gen** — ลืม Ploy ไปก่อน (reset 0), ไม่ยิง MCP gen, Claude คิด prompt เป็นหลักแล้ว Mirko เจนเอง · NEXT เดิมข้างบน**พักไว้** จนกว่า flow ใหม่จะผ่านแล้วค่อยต่อยอด · flow + fleet 8 agents อยู่ `AGENT_OPS.md` (อัปเป็น v2 แล้ว) + memory `ai-ugc-ad-factory-workflow` ท้ายไฟล์
