---
name: storyboard-knowledge
description: "Storyboard fundamentals for AI video — board first render second, 3 base shots, framing, storyboard vs shot list, ขั้นตอนในระบบเรา"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 899fce53-8a28-4248-bd83-8f329db4f6f0
---

# Storyboard — ความรู้สำหรับวางแผนช็อตก่อนเจนวิดีโอ

> สรุปจากการค้นเว็บ (มิ.ย. 2026) — ใช้คู่กับ [[seedance-knowledge]] และเทมเพลต `projects/_template/03-storyboard.md`
> หลักของระบบเรา: **"Board first, render second"** — วางแผนช็อตก่อน เจนทีหลัง · workflow ทำ storyboard เป็นรูปจริงดู [[storyboard-gpt-image-to-seedance]]

## Storyboard คืออะไร / ทำไมต้องทำ
**แผนภาพของหนัง** — ลำดับเฟรมเหมือนการ์ตูนช่อง บอกว่ากล้องเห็นอะไรในแต่ละช็อต ช็อตต่อกันยังไง
**ประโยชน์:**
- บังคับให้คิด "เป็นภาพ" ตั้งแต่แรก ไม่ใช่แค่คิดเป็นพล็อต/อารมณ์
- เจอปัญหา (ช็อตขาด, มุมเป็นไปไม่ได้, ความต่อเนื่องหลุด, จังหวะเพี้ยน) **ตั้งแต่ยังแก้ฟรี** — ก่อนเสียเงิน/เวลาเจนวิดีโอ
- สื่อสารภาพในหัวให้ทีม (หรือให้ AI) เข้าใจตรงกัน

## 3 ช็อตพื้นฐานที่ต้องรู้
| ช็อต | ใช้เล่าอะไร |
|---|---|
| **Wide Shot** | สถานที่/บริบท (คนตัวเล็กในที่กว้าง) |
| **Medium Shot** | ความสัมพันธ์/แอ็กชัน (คนครึ่งตัว) |
| **Close-Up** | อารมณ์/รายละเอียด (หน้า/วัตถุ) |

## เทคนิคจัดเฟรม
- **Rule of thirds** — วางตัวแบบเยื้องกลาง
- เว้น **breathing room** รอบตัวแบบ อย่าอัดแน่นเกิน (ข้อผิดพลาดที่พบบ่อย)
- **ลูกศรบอกการเคลื่อน:** ลูกศรทึบในเฟรม = ตัวละครเดิน · ลูกศรเส้นนอกเฟรม = กล้องเคลื่อน

## Storyboard vs Shot List
- **Storyboard** = ภาพ (drawing/รูปแต่ละช็อต) — บอกองค์ประกอบ
- **Shot List** = ตาราง (metadata: มุม/เลนส์/การเคลื่อน/ความยาว) — บอกรายละเอียดทางเทคนิค
- ใช้ทั้งคู่ · สำหรับงาน AI video ตารางสำคัญกว่าเพราะแปลงเป็น prompt ตรงๆ

## ⭐ สำหรับ AI Video โดยเฉพาะ
1. **Board first, render second** — วาง storyboard ก่อน เจนทีหลัง (หัวใจของระบบเรา + ตรงกับเวิร์กโฟลว์ Daroonwan ในโพสต์ที่เจอ)
2. **แต่ละ panel = 1 decision** — angle, lens, motion, duration แยกกัน → คุมการเจนทีละช็อต = ผลนิ่ง คุมได้ แก้ง่าย
3. **ไม่ต้องวาดสวย** — stick figure หรือแค่ "คำบรรยายช็อต + มุม" ก็พอ เพราะปลายทางคือแปลงเป็น prompt ข้อความอยู่แล้ว
4. มีเครื่องมือ AI ช่วยแปลงบท→shot list อัตโนมัติ (Storyboarder.ai, Higgsfield, Studiovity) — แต่ทำมือใน Obsidian คุมละเอียดกว่า

## ขั้นตอนทำ (สำหรับระบบเรา)
```
1. เอาบทจาก 02-script.md มาแบ่งเป็นช็อต (mark beats: แอ็กชัน, สถานที่, ชุด, จุดพลิก)
2. กรอกลง 03-storyboard.md (ตาราง: # / ช็อต / แอ็กชัน / shot type / มุม / เสียง / ความยาว)
3. ระบุมุมเฉพาะช็อตสำคัญ (ดูกฎใน [[seedance-knowledge]] — ปล่อยมุมได้ ยกเว้นบีตสำคัญ)
4. ส่งต่อไป 04-prompts.md แปลงแต่ละช็อตเป็น prompt
```

## แหล่งที่มา (Sources)
- [StudioBinder — Storyboard Composition: Layout, Format, Framing](https://www.studiobinder.com/blog/storyboard-composition-techniques/)
- [Milanote — How To Make a Film Storyboard: Step-By-Step](https://milanote.com/guide/film-storyboards)
- [Bri Castellini — How To Storyboard (and How To Pick Your Shots)](https://brisownworld.medium.com/how-to-storyboard-and-how-to-pick-your-shots-bc36b38e430f)
- [Murphy — All Types of Shot in Film & Storyboard](https://murphy.inc/types-of-shots-in-film-storyboarding/)
- [M Studio — How to Make a Shot List: Templates + AI Workflow](https://mstudio.ai/blog/ai-filmmaking/how-to-make-a-shot-list)
- [Neolemon — AI Storyboard To Animation Pipeline](https://www.neolemon.com/blog/ai-storyboard-to-animation-pipeline-workflow/)
