---
name: joey-skills-v2-nov2026
description: "Joey's 5-skill v2 pack (blog Nov 2026): Shotcaller v2 / Castkit v1 / Scenecraft v1 / Motiondojo v1 / story-bible — INSTALLED house-patched 2026-11-11, v1 archived; techniques + audit verdicts + what was patched + unverified list"
metadata:
  node_type: memory
  type: reference
  originSessionId: da198558-bb0f-47e0-bfa8-41092563b0aa
  modified: 2026-11-11T01:38:09.816Z
---

# Joey Skills v2 (blog อัปเดต 2026-11-06/09) — ✅ INSTALLED 2026-11-11 (house-patched)

**สถานะ:** `shotcaller-v2` · `castkit-v1` · `scenecraft-v1` · `motiondojo-v1` อยู่ใน `skills/` แล้ว — ทุกตัวมี section `## HOUSE OVERRIDES (ai-factory-brain, 2026-11)` ต้นไฟล์ (patch list ด้านล่าง = ที่ apply ไปแล้ว) · ของเก่า `cinema-director` / `character-builder` / `banana-pro-director-30` + `shotcaller-v1` (ดิบ ไม่ patch, เข้ามาจากเครื่อง MELPHIST 11-07) ย้ายไป `skills-archive/joey-v1-2026-08/` (ไม่โหลดแล้ว) · story-bible-builder ใช้ของเราต่อ (แก้ชื่อ ref → shotcaller-v2/castkit-v1) · ไฟล์ดิบ Joey ยังอยู่ที่ Desktop

ที่มา: https://higgsfield.ai/@joeysnoisygroup/blogs/all-my-claude-skills-for-better-prompting (หน้าเป็น JS → content จริงอยู่ที่ `contentUrl` .bin บน cdn.higgsfield.ai = Yjs/Lexical doc, decode ด้วย `yjs`; zip links อยู่ใน .bin)
ไฟล์ทั้งหมด + blog text: `~/Desktop/Joey Skills v2 (2026-11)/`
ต่อยอดจาก [[joey-cinema-skills-pack]] (v1 ที่เรา patch 08-03) · routing อยู่ [[skills-cheatsheet]]

## Rename map
| v2 | แทน | verdict (audit 3 deep-reasoner 11-11) |
|---|---|---|
| `shotcaller-v2` | `cinema-director` | REPLACE + port patch (ด้านล่าง) · ต้องลบ cinema-director (v1-detect ของมันหาชื่อ "Shotcaller v1" ไม่เจอ → แย่งงานกันเงียบๆ) |
| `castkit-v1` | `character-builder` | REPLACE + port HOUSE OVERRIDES |
| `scenecraft-v1` | banana-pro Mode 3 | REPLACE → `banana-pro-director-30` retire ทั้งตัว (ไม่มีอะไร unique หาย นอกจาก override block) |
| `motiondojo-v1` | — ใหม่ (Higgsfield Genjutsu motion transfer) | INSTALL หลัง patch |
| `story-bible-builder` | ตัวเดิม | KEEP ของเรา — diff ทั้งหมด = patch ของเราเอง, ไม่มีอะไรใหม่ |

Pipeline ของ Joey: build world (bible) → lock cast (Castkit) → set scene (Scenecraft) → make it move (Shotcaller / Motiondojo)

## เทคนิคที่ใช้ได้เลย (แม้ไม่ติดตั้ง)

**Seedance 2.0 vs 2.5**: 2.0 = 9 refs/15s · 2.5 = 50 refs/30s, สีดีกว่า แต่มัก gen background music ติดมา → ล้างด้วย moises.ai. 16–30s: anchor ref ตัวเดียวเรียกทุก beat + restate lens lock ต้นทุก beat + restate geometry map เมื่อ staging reset. "Near-duplicate references still average faces."

**Shotcaller dialogue system** (ได้มากสุด): THE SCRIPT block = verbatim เท่านั้น ("No delivery notes here — delivery inside this block leaks into the spoken words") · ONE MOUTH SPEAKS AT A TIME · คนฟังเขียน `says nothing in this beat:` · ช่วงเงียบเติม ambience ที่ระบุชื่อ · **"No mouth mechanics for generated speech"** (ทำให้ overarticulate/robotic) · brow matched to line = acting lever ที่คุ้มสุด
**Video character ref sheet**: คลิป 2 panel (outfit montage + close-up พูด pangram) → `Voice: exactly the voice heard in the reference.` · "The reference owns the voice; the line owns the moment." ⚠️ voice-lock ยังไม่ verify
**Extension**: continuity paragraph อยู่ที่สองเสมอ, ระบุ final frame, hold แตกภายใน ¼ วิแรก, ต่อทีละอัน
**Lipsync**: track ใส่เป็น video บนจอดำ ตัดเป็นวินาทีเต็ม + ต้องมีเนื้อร้องท่อนนั้นจริง
**Physics chain**: mass → contact → deformation → rebound → lag → shadow (ตรง [[ai-video-realism-hierarchy]])
**Elements-first tags**: ใช้ Element handle ที่เห็นใน UI ก่อน, `@image1`/`@video1` เป็น fallback

**Castkit**: render fork photoreal/animated (3 look: graphic realism / stylized 3D / 2D hand-drawn) + style lock วางซ้ำต้นทุก close · แปลง photoreal→animated: "face, bone structure, proportions... stay identical, and only the rendering changes" · **Orientation lock**: "flat frontal view regardless of how the figure stands in the reference: no three-quarter turn… no contrapposto" · **Neckline test** เลือกวิธีตัดหัว: มีช่องคอจริง → ghost mannequin (ระบุ collar) / ไม่มี → clean neck cut · lock แบบมีเวอร์ชัน (`lock-02-red-hair`) · ข้ามขั้นไม่ได้ (face→outfit→sheet)

**Scenecraft**: plate A (environment, default) / B (people-in-scene = first frame ได้) / C (coverage: master ก่อน แนบทุกมุม, เขียน light ใหม่ตาม vantage) / D (edit: `[Target] / [Change] / [Protected]`) · prose 5 ย่อหน้า · overlay line `NO ON-SCREEN TEXT: ...` ย่อหน้า 2 · atmosphere = density gradient ข้าม plane ไม่ใช่ fog/rays · "Low macro, high micro" contrast · ทุกสีต้องมี source ในเฟรม · Seedream 5.0 Pro: HEX + ชื่อสี, in-world text ใส่ quote + ระบุภาษา

**Motiondojo** (Genjutsu): 3 form — Body Copy / Camera Copy / Body Copy New Camera · วิดีโอ motion ไม่ tag ใน prompt, ref อื่นเป็น `<<<image_N>>>` · scope sentence: "The attached motion transfer video controls body movement only — its camera is ignored completely..." · mouth lock: "HARD LOCK: nobody in this video speaks, sings, mouths or forms a single word..." · role ตามตำแหน่งเริ่ม (LEFT/RIGHT) "never swap" · ให้แต่ละคน movement quality ต่างกัน "The silhouettes never match at the same moment" · population block นับหัวคน · physics เขียนใหม่ตามพื้นผิวใหม่

## Patch list (APPLIED 11-11 — ตัวดิบไม่มี house override 08-03 เลย)
- **ทุกตัว**: description ใส่ "Do NOT use for…" (Scenecraft/Castkit แย่ง image-prompt-writer/podcast; Shotcaller เขียน "any Seedance prompt"; Motiondojo แย่ง Kling motion_control)
- **Shotcaller**: BUDGET GATE ≤1,800 chars (boilerplate บังคับเองก็ ~2,222 แล้ว, ตัวอย่างของ Joey 11k) · house philosophy (1–2 คนตัด geometry map/lens per shot) · Thai: ท้ายคำ บ/ป/พ/ม = ปิดปากค้าง ไม่มี pop (A/B ที่ 480p ก่อน) · Thai pacing นับพยางค์ + จบพูดใน 5–6s/8s · LANGUAGE block ไทย · คืน Family B phone/BTS (มี dangling ref L84) · คืน five-fingers + brand-naming rule · CRITICAL cap 5 สำหรับ 2 คนพูด · bible path → `projects/<slug>/00-bible.md` · ข้ามคำถาม version/Elements ถ้า STATE.md บอกแล้ว
- **Castkit**: port HOUSE OVERRIDES (character-builder L22-28) + age+nationality บังคับ · iris clause มีเงื่อนไข (ตาไทยสีเข้ม) · GPT-2 = Higgsfield ไม่ใช่ GPT Image 2, ตัด credit upsell · DramaBox bridge [[drama-dramabox-tier-portrait-recipe]] · flat-lay → [[outfit-swap-wichcraft-prompt]] · bug L354 (Station 3→2), L491 (grain ≠ leak)
- **Scenecraft**: age+nationality · ratio/`@img` OK นอก Higgsfield · no-teeth เฉพาะ plate · Thai block [[thai-localization-image-prompts]] (ป้ายไทย gen แบบไม่มีตัวอักษร แล้วใส่ใน post) · 9:16 ใช้ spherical แทน anamorphic default
- **Motiondojo**: budget gate (เป้า 900–1,300 คำ แต่ตัวอย่างเอง 11k chars; limit จริงของ Genjutsu ยังไม่รู้) · Thai: exact words + เสียงจากวิดีโอเป็น audio เดียว · match-the-mouth ต้องมี audio rule · camera default gentle/heavy handheld (violent เฉพาะสั่ง) · เพิ่ม hand/prop contact · population optional (ตลาด/ถนนไทยต้องมีคน) · pronoun กลาง

## Backport เข้า house
- ✅ neckline test + orientation lock → [[outfit-swap-wichcraft-prompt]] Variant B (ชุดพยาบาลมีปก = ghost mannequin)

## ยังไม่ verify
Element tag vs `@image1` บน Higgsfield · voice lock จาก video ref · audio-as-video · Thai unreleased seal · char cap Seedance 2.5 · limit prompt Genjutsu · [[seedance-knowledge]] L27 (2,000 ทั้งสอง host) ขัดกับ budget gate (kie.ai 20,000) — เคลียร์ก่อน port gate
