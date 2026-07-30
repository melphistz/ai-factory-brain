---
name: skill-candidates-image-lyrics
description: "DONE 07-09 — both candidate skills built: image-prompt-writer (mirrors seedance-2-pro-director but for character/image prompts) and thai-lyric-writer (enforces rhyme-map discipline from feedback-thai-lyric-craft)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# Candidate skills — ✅ ทำแล้ว (07-09)

**สถานะล่าสุด:** ทั้งคู่สร้างเสร็จแล้ว (fast-worker, Sonnet high, dispatch ขนานกัน) — `skills/image-prompt-writer/SKILL.md` (246 บรรทัด) + `skills/thai-lyric-writer/SKILL.md` (84 บรรทัด) commit เข้า repo แล้ว. งานค้าง: ยังไม่ผ่าน audit รอบเต็มแบบ fleet 07-07 (factory-audit เจอจุดนี้เป็น leverage สูงสุดอันดับ 4-5)

## ที่มา
07-08: คุยเรื่อง skill/memory/subagent ต่างกันยังไง แล้วสแกน brain ทั้งหมดหาว่ามีความรู้ก้อนไหนสมควรแปลงเป็น skill (workflow ที่ทำซ้ำบ่อย มีขั้นตอนชัด) บ้าง นอกจากที่มีอยู่แล้ว (seedance-2-pro-director / shotlist-builder / video-prompt-builder — ทั้งหมดเป็นสาย **วิดีโอ**)

## Candidate 1: Image-prompt skill
**ช่องว่าง:** ความรู้เขียน prompt รูปมีเยอะพอในระบบแล้ว (เทียบเท่าที่ Seedance มีก่อนกลายเป็น skill) แต่ตอนนี้ถูก "แปลงเป็นความสามารถ" ในรูปแบบ **subagent** (`asset-prompt-builder`) ซึ่งใช้เฉพาะตอน dispatch งานสาย production โฆษณาเท่านั้น — **ไม่มี skill แบบ ad-hoc สำหรับพิมพ์ขอ prompt รูปสั้นๆ นอกสาย production** เหมือนที่ seedance-2-pro-director ทำให้วิดีโอ

**ไฟล์ต้นทางที่จะป้อนเข้า:** `ai-influencer-image-prompt.md` · `ai-character-identity-lock.md` (ล็อกหน้าข้ามหลายภาพ) · `cute-face-charm-recipe.md` · `kpop-idol-visual-prompt.md` · `image-prompt-suffixes-techniques.md` · `ai-platform-content-limits.md`

## Candidate 2: Thai-lyric-writing skill
**เหตุผล:** มี [[feedback-thai-lyric-craft]] บังคับกฎเข้มงวด ("ต้องวางสัมผัสนอก+ในตั้งแต่ร่างแรก + ต้องโชว์ rhyme map เสมอ") — สัญญาณชัดว่าเป็นกฎที่พลาดง่ายถ้าปล่อยให้จำเองจากไฟล์ ทำเป็น skill จะบังคับทำตามขั้นตอนทุกครั้งแบบ shotlist-builder บังคับ 4 phase ห้ามข้าม

**ไฟล์ต้นทางที่จะป้อนเข้า:** `thai-lyric-writing.md` · `feedback-thai-lyric-craft.md`

## Update 07-30 — merge จาก prompt-director.skill

ประเมิน third-party skill `prompt-director.skill` (Fox AI Academy course companion, 88 บรรทัด) → **ไม่ติดตั้ง**: description กว้างเกิน (ครอบ image+video+5 โมเดล ไม่มี negative boundary) ชน trigger กับ image-prompt-writer / seedance-2-pro-director / video-prompt-builder, และส่วน video สอน 7-block shot-by-shot ซึ่งขัด [[seedance-marco-freestyle-method]] ("set the RULES not the SHOTS")

ขูด 3 ชิ้นที่ดีจริงเข้า `image-prompt-writer` แทน (333 → 364 บรรทัด):
1. **`Locked:` / `Assumed:` output block** + กฎ *write the prompt first, never interrogate first* — user เห็นว่าเราเติมอะไรให้ = รู้ว่าหมุน dial ไหนได้ ไม่ต้อง reverse-engineer prompt
2. **Iteration section** — วินิจฉัยว่า block ไหนพัง 1 บรรทัด → คืน prompt เต็ม **ห้ามคืนเศษให้แปะ** (เศษ = user re-assemble มือ แล้ว prompt พังเงียบ) + ตาราง model-typical failure 8 อาการ→counter-instruction
3. **Reference-image rule** — ref attached แล้วห้าม re-describe สิ่งที่ ref ล็อกอยู่แล้ว (words vs pixels แข่งกัน → model averaging = drift) · corollary: identity เพี้ยนทั้งที่มี ref → **ลบ** face description ไม่ใช่เพิ่ม · เข้าคู่ [[char-sheet-2panel-identity-garment]] / [[outfit-swap-wichcraft-prompt]]

description เพิ่ม trigger ตอนเอาผลเสียกลับมา ("ภาพออกมาหน้าเพี้ยน แก้ prompt ให้") · Final QA เพิ่มข้อ 8 (ref attached แต่ยังบรรยายหน้า → strip)

## สถานะ (เดิม)
ยังไม่เริ่มทำทั้งคู่ — เซฟไว้รอคิว ไม่ผูกกับ Fable/drama-app แต่ใช้ตรรกะ model/cost เดียวกับ [[factory-self-audit-skill-plan]] (skill เดียว งาน production tier ใช้ Sonnet พอ ไม่ต้อง ultracode)
