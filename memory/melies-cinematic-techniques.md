---
name: melies-cinematic-techniques
description: "Melies.co library 424 cinematic techniques (13 หมวด) + วิธีเขียน prompt แบบ Melies (1 เทคนิค/ช็อต, ล็อกสิ่งที่ห้ามเปลี่ยน, ห้าม failure mode) + prompt ตัวอย่าง verbatim"
metadata:
  node_type: memory
  type: reference
  originSessionId: 9841687f-2993-4fd0-b1a3-eddc42ee9580
  modified: 2026-10-02T09:52:05.866Z
---

# Melies Cinematic Techniques Library

Source: https://melies.co/cinematic-techniques (เรียน 2026-10-02)
หน้าย่อย: `/cinematic-techniques/<category-slug>/<technique-slug>` เช่น `camera-movement/dolly-zoom`, `in-camera-and-optical-effects/rack-focus`, `composition/reflections`, `lighting/silhouette`, `editing-and-transitions/match-cut`
ทุกหน้ามี: Definition · When to use / **When NOT** · Emotional effect · Film examples · **AI prompt** · Common mistakes · Related

## ⭐ วิธีเขียน prompt แบบ Melies (บทเรียนหลัก)
1. **1 ช็อต = 1 เทคนิค** เรียกชื่อตรงๆ (rack focus / dolly zoom / silhouette)
2. **ระบุความยาว + "one continuous shot"** — เช่น "One continuous six-second shot..."
3. **บอกกลไกทางกายภาพ** ไม่ใช่แค่ชื่อ — "dolly straight backward while optically zooming in at the compensating rate"
4. **ล็อกสิ่งที่ห้ามเปลี่ยน (invariants)** — "No camera move, no zoom, neither object changes position" · "Keep her head exactly the same height and centered"
5. **ห้าม failure mode ของเทคนิคนั้นโดยชื่อ** — match cut: "forbid a morph or dissolve" · silhouette: "no visible facial detail or artificial rim halo" · dolly zoom: ห้ามยืดฉากหลังแบบดิจิทัลโดยกล้องไม่เคลื่อน
6. **ระบุ edge/ระนาบ** — dirty frame: "specify which edges are occupied, forbid clean margins"
7. **เทคนิคเด่นใช้ครั้งเดียวต่อเรื่อง** — "Use it once" (dolly zoom) ใช้ซ้ำ = กลายเป็นลูกเล่น
8. รู้ **When NOT** ก่อนเลือก: ต้องการ 2 ระนาบคมพร้อมกัน → split diopter/deep focus ไม่ใช่ rack · ต้องเห็นปากพูด → ไม่ใช่ silhouette · อยากแบนภาพ → zoom ไม่ใช่ parallax

## Prompt ตัวอย่าง (verbatim จากเว็บ)
- **Dolly Zoom:** "One continuous six-second shot of a station attendant realizing a train is missing. Dolly straight backward while optically zooming in at the compensating rate. Keep her head exactly the same height and centered; the long platform behind her appears to compress." — ใช้กับ "ช่วงเวลาที่รู้ว่าพื้นใต้เท้าไม่มั่นคง"
- **Rack Focus:** "Locked composition: a brass key in sharp foreground on a desk, a woman blurred in the doorway behind it. Hold the key, then slowly rack focus to her expression as the key becomes soft. No camera move, no zoom, neither object changes position." — "slow rack = ประโยค, snap rack = หมัด"
- **Reflections:** "Reflections of [Subject] in glass, water, or chrome, observer and observed in one plane." + ระบุชนิดพื้นผิว (one-way glass/shop window/puddle/chrome) + สั่งให้เงาขยับตามหัวอย่างสมจริงทางแสง · **กฎแสง: ฝั่งที่ถูกสะท้อนต้องสว่างกว่าอีกฝั่งกระจก เงาถึงจะอ่านออก**
- **Silhouette:** "...rendered as clean dark silhouettes against a luminous pale sky. Keep their limbs and the telescope distinct. Locked wide view, gentle wind, no visible facial detail or artificial rim halo." · expose ตามพื้นหลัง · แยกแขนขา/พร็อพไม่ให้ทับกัน
- **Match Cut:** "Match cut from [Subject] to a rhyming shape or motion in another time, graphic continuity across a hard cut... Name the shared contour or vector, name what changes (place, era, scale), and forbid a morph or dissolve."
- **Dirty Frame:** "Dirty frame around [Subject], out-of-focus shoulders, glass, foliage, or crowd chewing the edges, voyeur layers." — "Dirty edges say it was stolen, crowded, or survived."
- **Parallax:** "Parallax around [Subject], near things racing, far things crawling, depth proven by relative speed." · ต้อง translate กล้อง ไม่ใช่ zoom

## Vocabulary ตามหมวด (ชื่อเทคนิค ใช้เป็นคำใน prompt)
- **Camera Movement (86):** slow/crash/rapid/yoyo zoom · dolly zoom · dolly in/out/left/right · push in/pull out · super dolly · double dolly · pan/tilt · whip pan/tilt · crane up/down/over · jib · 360 orbit · arc · dutch roll · FPV drone · aerial pullback/push in · steadicam · handheld · gimbal · SnorriCam · locked-on · slider · lazy susan · bolt cam · parallax · pass through · through object in/out · hyperlapse · conveyor · falling · wandering · car grip · road rush · static locked-off · fixed cam · head tracking · hero cam · robo arm · wiggle · camera roll
- **Framing (25):** ECU · choker · CU · MCU · medium · cowboy · full body · long · extreme long · wide · establishing · master · two/three/group shot · insert · cutaway · reaction · OTS · single · cut-ins · gesture
- **Angles (19):** eye level · high · low · bird's-eye · worm's-eye · overhead top-down · ground level · hip level · dutch · profile · three-quarter · shoulder level · POV · first-person · object POV · trunk shot · fourth wall · incline
- **Lighting (41):** three-point · key/fill/back/rim/kicker/hair/eye light · high-key · low-key · chiaroscuro · Rembrandt · butterfly · loop · split · short · broad · silhouette · motivated · practical · available · bounce · hard/soft · side · top · underlighting · cross · window · candle · neon practicals · golden hour · blue hour · dappled · gobo · volumetric · cameo · epiphany · spotlight · glam
- **Composition (32):** rule of thirds · golden ratio · central/centered · symmetry/asymmetry · leading lines · diagonal · triangular · one-point perspective · vanishing point · frame within frame · layered depth · dirty/clean frame · foreground interest · negative space · visual weight · repetition · figure-ground · tonal contrast · look space · short siding · headroom · architexture · reflections · screen in screen · tableau · void · voyeur · windows
- **Lenses (17):** 14/24/35/50/85/135/200mm · anamorphic · spherical · fisheye · tilt-shift · macro · probe lens · split diopter · vintage cine glass · telephoto compression
- **Color (19):** teal-orange · bleach bypass · monochrome · sepia · desaturation · hyper-saturation · cool blue · warm amber · filmic faded · cross process · day for night · tungsten · moonlight gel · split toning · natural grade · color shift · palette · overexposed
- **Time & Motion (21):** slow/fast motion · speed ramp · freeze frame · time-lapse · step printing · reverse · bullet time · long take · oner · motion blur · stutter · boomerang · stop motion · frozen in motion
- **In-Camera/Optical (57):** lens/anamorphic flare · halation · grain · light leak · vignette · chromatic aberration · bokeh · rack focus · shallow/deep focus · double exposure · echo print · forced perspective · slit-scan · morph · cinemagraph · diorama · scale shift · ratio switch · shadow box · particles · ฯลฯ
- **Editing (23):** match cut · graphic match · match on action · jump cut · smash/crash/flash cut · axial cut · invisible cut · dissolve · fade · iris · wipe · match motion · cross-cutting · split screen · montage · quick cuts · fragments · J/L-cut
- **Atmosphere (13):** rain · fog · mist · haze · smoke · dust motes · steam · snow · underwater · wet-down · sparks/embers · dust & sand
- **Genre Looks (27):** noir · neo-noir · German expressionism · giallo · spaghetti western · French new wave · vérité · wuxia · tech noir · southern gothic · cosmic horror · found footage · arthouse · dreamcore · magical realism · weirdcore ฯลฯ
- **Viral Looks (44):** สไตล์โซเชียล (Comic, Origami, Broken Mirror, Action Figure, 2000s Paparazzi ฯลฯ)

## ใช้กับโปรเจกต์
- [[still-warm-project]] S14 (rack focus + reflection): ตัวแม่โดนแดด / ในร้านมืด → เงาอ่านออก · เขียน prompt แบบ "Locked... rack focus from X to Y... no camera move" · S08 silhouette = ยกเว้นกฎ "no visible eyes" โดยตั้งใจ (eyeshine ข้างเดียว) · S02/S17 = dirty frame + parallax ป่าขา
- เสริม [[seedance-knowledge]] · [[seedance-marco-freestyle-method]] (Marco = ตั้งกฎ ไม่ใช่ช็อต — ใช้คนละงาน: Melies = ช็อตที่ต้องคุมเทคนิคเป๊ะ) · [[director-styles-knowledge]] · [[storyboard-knowledge]]
