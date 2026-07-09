---
name: smartaihub-drama-series
description: "CASE STUDY ของคนอื่น (ไม่ใช่ของ Mirko — แก้ความเข้าใจ 07-07): web app smartaihub.app ทำ drama series แนวตั้งครบวงจร เจ้าของเคลมว่าสร้างด้วย Claude/Codex · Mirko เอา screenshot มาถามว่า 'เราทำแบบนี้ได้ไหม' — ใช้เป็น feature-spec reference"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# SmartAIHub Drama Series — case study แอปของคนอื่น (เก็บ 2026-07-07)

> ⚠️ **แก้ความเข้าใจ (07-07):** ตอนแรกบันทึกผิดว่าเป็นระบบ/ทิศทางของ Mirko — จริงๆ คือ **แอปของคนอื่น** ที่ Mirko screenshot มาถามว่า "ทำได้ไหม" · แชตสีเขียวในภาพ = คำพูดของเจ้าของแอป ไม่ใช่ Mirko

## ยุทธศาสตร์ของเจ้าของแอป (จากแชตที่แนบมา — น่าเรียนแบบ)
ใช้ Claude (Fable, จนโควต้าหมด→ซื้อ API) + Codex **สร้างระบบ** แต่ไม่ใช้ทำงาน production จริง — สร้าง UI/UX ของตัวเองที่ call API ตรง "เสียเวลาวางระบบทีเดียว" · เคลมว่าระบบประกอบด้วย ~11 skills + หน้า UI จำนวนมาก

## Feature spec ที่เห็นจริงจาก screenshot (`smartaihub.app/drama-series/4`)
1. **เนื้อเรื่องเต็ม** — ระบบคิด synopsis + แผนรายตอน (เป้า 10 ตอน, beat ต่อตอน, ปิดตอนด้วย hook ค้าง)
2. **ตัวละคร** — การ์ด + role tag (ตัวเอก/แม่/ตัวร้าย/มาสคอต) + ปุ่มเจน: ภาพตัวละคร / ช็อตตัวละคร / Character Sheet เต็ม · โมเดล GPT Image 2 ผ่าน **Higgsfield MCP** · สลับภาษา EN/TH
3. **ต่อช็อต:** image prompt เฟรมเปิด (ลิมิต 3,500) → video prompt (ลิมิต 2,000 ตาม Seedance) → บทพูด + emotion tag + voice/delivery direction ต่อบรรทัด · ปุ่ม: แก้ไขภาพ(AI) / สร้าง prompt+ภาพ / หลายมุมกล้อง 3×3 / ให้ AI ปรับ (คิดเงิน)
4. มี 3 โปรเจกต์ตัวอย่างรัน (ความทรงจำในขวดแก้ว ฯลฯ)

## คุณภาพ prompt ของแอปเขา (อ่านจากช็อตจริง)
ทำตามหลักเดียวกับคลังเรา: micro-expression เป็นกล้ามเนื้อ, camera move เดียว+motivation, "Continue from the start frame" (i2v ไม่บรรยายซ้ำ), dialogue ใน quotes + จังหวะ uneven
**จุดอ่อนที่เห็น (บทเรียนถ้าเราสร้างเอง):** video prompt ชนเพดาน 1,973/2,000 ไม่เหลือ margin · ยัด 3 เทิร์นพูดใน 1 ช็อต (เกิน 2–3 beats เสี่ยง lip-sync พัง)

## ประเมินของเรา: ทำได้ไหม → ได้ (07-07)
ส่วนที่ยากจริงคือ **intelligence layer (system prompts/skills)** ซึ่งเรามีครบใน vault แล้ว ([[seedance-knowledge]] ฯลฯ — [[gemini-gem-seedance-director]] คือตัวอย่าง freeze ความรู้หนึ่งก้อน) · ชิ้นที่ต้องสร้าง: UI + DB (Supabase มี MCP) + LLM API (story/char/prompt gen) + gen API (Higgsfield/kie.ai) · ตัวยากเชิงคิด = **continuity ledger ข้ามช็อต-ข้ามตอน + QA/cost gates** (จุดตายซีรีส์ AI ตาม [[ai-video-realism-hierarchy]])

เกี่ยว: [[vertical-drama-basics-dramy.md|vertical-drama-basics-dramy]] (Dramy.ai — ผู้เล่นอีกรายใน niche เดียวกัน) · [[ai-ugc-ad-factory-workflow]] · [[drama-app-fable-ultracode-retrospective]] (คืนสร้าง drama-app v1 จริง)
