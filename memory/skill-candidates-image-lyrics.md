---
name: skill-candidates-image-lyrics
description: "PENDING (07-08) — two candidate skills identified from scanning the brain: image-prompt-writer (mirrors seedance-2-pro-director but for character/image prompts) and thai-lyric-writer (enforces rhyme-map discipline from feedback-thai-lyric-craft)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 72a4a9da-c166-4cd1-b6d1-c921aa8e967a
---

# Candidate skills — ยังไม่ทำ (เก็บไว้เทียบกับ `/factory-audit` ที่ pending อยู่แล้ว)

## ที่มา
07-08: คุยเรื่อง skill/memory/subagent ต่างกันยังไง แล้วสแกน brain ทั้งหมดหาว่ามีความรู้ก้อนไหนสมควรแปลงเป็น skill (workflow ที่ทำซ้ำบ่อย มีขั้นตอนชัด) บ้าง นอกจากที่มีอยู่แล้ว (seedance-2-pro-director / shotlist-builder / video-prompt-builder — ทั้งหมดเป็นสาย **วิดีโอ**)

## Candidate 1: Image-prompt skill
**ช่องว่าง:** ความรู้เขียน prompt รูปมีเยอะพอในระบบแล้ว (เทียบเท่าที่ Seedance มีก่อนกลายเป็น skill) แต่ตอนนี้ถูก "แปลงเป็นความสามารถ" ในรูปแบบ **subagent** (`asset-prompt-builder`) ซึ่งใช้เฉพาะตอน dispatch งานสาย production โฆษณาเท่านั้น — **ไม่มี skill แบบ ad-hoc สำหรับพิมพ์ขอ prompt รูปสั้นๆ นอกสาย production** เหมือนที่ seedance-2-pro-director ทำให้วิดีโอ

**ไฟล์ต้นทางที่จะป้อนเข้า:** `ai-influencer-image-prompt.md` · `ai-character-identity-lock.md` (ล็อกหน้าข้ามหลายภาพ) · `cute-face-charm-recipe.md` · `kpop-idol-visual-prompt.md` · `image-prompt-suffixes-techniques.md` · `ai-platform-content-limits.md`

## Candidate 2: Thai-lyric-writing skill
**เหตุผล:** มี [[feedback-thai-lyric-craft]] บังคับกฎเข้มงวด ("ต้องวางสัมผัสนอก+ในตั้งแต่ร่างแรก + ต้องโชว์ rhyme map เสมอ") — สัญญาณชัดว่าเป็นกฎที่พลาดง่ายถ้าปล่อยให้จำเองจากไฟล์ ทำเป็น skill จะบังคับทำตามขั้นตอนทุกครั้งแบบ shotlist-builder บังคับ 4 phase ห้ามข้าม

**ไฟล์ต้นทางที่จะป้อนเข้า:** `thai-lyric-writing.md` · `feedback-thai-lyric-craft.md`

## สถานะ
ยังไม่เริ่มทำทั้งคู่ — เซฟไว้รอคิว ไม่ผูกกับ Fable/drama-app แต่ใช้ตรรกะ model/cost เดียวกับ [[factory-self-audit-skill-plan]] (skill เดียว งาน production tier ใช้ Sonnet พอ ไม่ต้อง ultracode)
