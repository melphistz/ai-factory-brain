# Memory Index

One line per memory, grouped by section. Add new entries under the matching section, newest on top within it. Volatile session-state lives in project files — symlink in, don't duplicate.

## Rules

- [Address User Politely](feedback-address-user-politely.md) — FEEDBACK (07-15): เรียก user = "คุณ/เรา" เสมอ · **ห้ามใช้มึง/กู/คำหยาบเด็ดขาด** แม้ pordee mode (pordee ตัดแค่ particle ไม่แตะสรรพนาม) · เคยเผลอหลายรอบจน user สั่งลบพฤติกรรม
- [Use Installed Skills](rule-use-installed-skills.md) — RULE (Mirko 07-14): งานที่มี skill/agent ตรง → **ต้องเรียกใช้ ห้ามเขียนสดใน main** (build+audit ไป token เยอะแล้ว) · ยกเว้นแก้เล็กกลาง iteration สด · เช็ค [[skills-cheatsheet]] ตอนเริ่ม task
- [Search Prompt-Index First](rule-search-prompt-index-first.md) — RULE: ก่อนเขียน image/video prompt ใหม่ → ค้น `~/ai-factory-brain/tools/prompt-index/` (8.7k prompts, internal ไม่ติด FDA, `search.py term1 term2`) หา reference ก่อนเสมอ · sync.py export ให้อัตโนมัติ
- [Model/Effort Strategy](feedback-model-effort-strategy.md) — FEEDBACK: intelligence-asset (freeze ยาว) = โมเดลฉลาดสุด+ultracode+verify 2 เลนส์ · build/production = Opus/Sonnet+high ถูกกว่าทำได้เท่ากัน · effort สูง=ช้าลงไม่ใช่เร็ว · build ช้าเพราะ subprocess ไม่ใช่โมเดล
- [Always Full Prompt](feedback-always-full-prompt.md) — FEEDBACK: คุยเรื่อง prompt สร้างภาพ/วิดีโอ = จบด้วย full paste-ready prompt เสมอ ทุกครั้ง (อธิบายที่เพิ่มได้ แต่ต้องมี full)
- [Drama Character Casting Feedback](feedback-drama-character-casting.md) — FEEDBACK: ตัวละคร drama ทุกตัว (เอก+นางร้าย) ต้องสวย/หล่อหมด แต่ไม่ over ต้องสมจริง · validated recipe → [[drama-dramabox-tier-portrait-recipe]]
- [Storyboard Narrative Not Flat](feedback-storyboard-narrative-not-flat.md) — FEEDBACK: storyboard/ซีน ต้องคิดเป็น flow หนัง (มุมกล้อง/reveal/movement/jump/arc) ทุก panel dynamic + สลับ framing · ห้ามยืนโพสตรงๆ สุ่มๆ แบนๆ · ref = อ่านเป็น template ของ FLOW ไม่ใช่แค่ mood (จาก vid04 ตีกลับ 3 รอบ)
- [Thai Lyric Craft Feedback](feedback-thai-lyric-craft.md) — FEEDBACK: เนื้อเพลง/กวีไทยต้องวางสัมผัส (นอก+ใน) ตั้งแต่ร่างแรก + โชว์ rhyme map · หลักอยู่ thai-lyric-writing
- [Vault Structure](vault-structure.md) — reorg 2026-07-03: 9-section index + entry rule, rename log (ai-influencer-image-prompt), backup location
- [Log Updates to Obsidian](log-updates-to-obsidian.md) — RULE: record every new thing/update in the vault, each time

## Active Projects

- [Drama App (ของเราเอง)](smartaihub-drama-series.md) — ระบบซีรีส์แนวตั้งเอง (ต้นแบบ = case study ในลิงก์) · **07-07: v1 BUILT+VERIFIED + genre packs 5 แนว** · **07-08: ตัดสินใจอยู่ prompt-first ต่อ (ปฏิเสธ auto-gen ผ่าน token trick — ขัด OpenAI ToS)** + วางแผน UI redesign แล้ว (upload-รูปกลับ→sidebar→gallery card→bulk button→emotion chip, Sonnet พอ ~300-600K tokens) **PENDING รอ Mirko reset quota** · **07-10: genre pack `revenge-vindication` DONE** (pack ที่ 6, ขาว-ดำสุดขั้ว ReelShort/DramaBox, ultracode workflow 7 agents + verify 2 เลนส์, 4,366 chars deploy เข้า prompts/ — ยังไม่ wire inject รอ UI redesign) · **teardown validation ชั้น 3 batch-1 DONE 07-11** (3 เรื่อง bilibili.tv → converged 7 pattern → fed revenge pack empirical `eedb5f4` · เหลือ batch-2 n=7 optional รอ overnight run) · **07-11: UI redesign 8/8 DONE** (overnight autonomous Sonnet chain) + **genre×setting 2-axis ทำครบ+wire แล้ว** (autonomous full run): teardown 3 ละคร→revenge empirical · migration A carve 6 genre (09-slim, 0 fixture) + 6 setting · B +3 โลก (rural-poor/fantasy celestial+gothic/xianxia = 10 โลก) · C wire แอปจริง (contracts enum + packs.ts loader + inject 01/02 setting→genre + BriefForm 2 dropdown + lint:packs) **build+lint+smoke PASS** · genre="วิธีเล่า" × setting="โลก" อิสระ, backward-compat (ไม่เลือก=pipeline เดิม) · brain pushed, drama-app local commit `732c032` — รายละเอียดเต็ม = `projects/drama-app/STATE.md` · retrospective คืนสร้าง v1 = [[drama-app-fable-ultracode-retrospective]]
- [แค่วันนี้ (Just Today MV)](kae-wan-nee-project.md) — MV รักสองสาว+อุกกาบาตวันสุดท้าย · Guadagnino×Malick×Melancholia · เพลง Suno สไตล์ fellow fellow · ไฟล์เต็ม projects/kae-wan-nee/ · status: shotlist ล็อก, next = gen เพลง + character sheet
- [ตื่นสาย (Sunday School Comedy)](tuensai-project.md) — หนังสั้น deadpan แนวเต๋อ (จาก Windows vault): รีบไปโรงเรียน→วันอาทิตย์ · ไฟล์เต็ม projects/tuensai/ · status: รอผลเจน V3 + ค้างเซฟ prompt 30s
- [Story Ideas — แนวเต๋อ นวพล](story-ideas-nawapol.md) — idea bank 10 เรื่อง ภาพล้วนไม่มีบทพูด สำหรับตั้งโปรเจกต์ถัดไป (ก๊อป projects/_template)
- [AI UGC Ad Factory Workflow](ai-ugc-ad-factory-workflow.md) — ACTIVE · **MODE v2 (07-05): prompt-first/manual-gen** (Ploy reset, no MCP gen, flow 5 ขั้นใน AGENT_OPS.md, ถ้า OK ค่อยต่อยอด) · โครงเดิม: 8 concept × 3 hook hook-swap
- [FF Factory — Live Session State](FF_SESSION_STATE.md) — symlink → Desktop/Ads/FF_factory/SESSION_STATE.md (volatile task-state, edit at source)
- [Neezplus (client ad)](../projects/neezplus/STATE.md) — **ACTIVE** โฆษณาอาหารแมว NEEZ+ 12 คลิป (SB01–08 อาหาร + SB09–12 ทราย + SB13–20 showcase) · 07-10: presenter kit+sheet approved (QA Gate1 ผ่าน), **SB01 kit เสร็จ (green screen, GPT Image 2 + Veo lip-sync)** → Mirko gen ได้เลย · รอ client sign-off บท scene 6 + tag [รีวิวเพียบ] · next = prompt SB02–08 · ทุกอย่างใน `projects/neezplus/` (STATE.md เป็น source of truth)
- [Valenshield Dokkaew Styling (vid04)](valenshield-dokkaew-styling-vid04.md) — **ACTIVE (เดียวที่เหลือ)** camp 4 = magic-wardrobe styling montage (clone UNIQLO Workday Styling), 3 ลุค, 20s 9:16, **ไม่มี VO**, สี=ลาเวนเดอร์, **ฉากโทนขาว**. mechanic = POV เปิดตู้(ชุดอยู่บ้าน)→ว้าว→ปัด/จิ้มเลือก→**jump-cut เปลี่ยนชุด**→โพส dynamic. char sheet 3 ลุค+storyboard v4 DONE · **07-13: fix ปก L2/L3 gen ซ้ำกัน** (collar discrimination: ปลายชี้ลง vs เชิดขึ้น) · next = regen storyboard 1-3 + ห้องขาว + casual sheet → stills → Seedance. ⚠️ ของลอย/jump = AE/CapCut ไม่ใช่ Seedance
- [Valenshield vid01-03 — DONE](valenshield-nurse-ad-project.md) — ✅ ปิดหมด 07-10: vid01 editorial HERO ([[valenshield-nurse-ad-project]]) · vid02 macro ASMR ([[valenshield-macro-asmr-ad]]) · vid03 walking-pad TIFU ([[valenshield-walkingpad-tifu-vid03]]). เก็บ prompt/บทเรียนไว้ reuse

## Session State (volatile — archive when done)

(empty — nothing currently in-flight; ดู Archived ด้านล่างสำหรับของที่ปิดแล้ว)

## Archived (resolved — kept for reference, not action items)

- [Gemini Gem — ARCHIVED](gemini-gem-seedance-director.md) — เดิมทำไว้แจก เลิกแจกแล้ว (07-14) ไม่เคยติดตั้งใช้ · Instructions + [knowledge pack](gemini-gem-seedance-knowledge-pack.md) ยังอยู่ครบถ้าจะฟื้น
- [YouMind Scrape — DONE](youmind-scrape-session-state.md) — DONE 3 ก.ค.: merged youmind→galleries (img 6877, video 363). optional leftover: 44 img fail + youmind video undercount
- [MeiGen Library — DONE](meigen-library-session-state.md) — CLOSED, sync ongoing periodically: 07-13 +592→**7,420** prompts (gallery 8,259 cards). FDA needs re-toggle EVERY reboot (confirmed macOS external-volume TCC bug, not MDM)

## Seedance / Video Prompting

- [Vertical Drama Basics (Dramy.ai)](vertical-drama-basics-dramy.md) — โครงละครแนวตั้ง: ตอน 5 ช่วง Hook/Setup/Conflict/Twist/**Cliffhanger บังคับ**, Hook 4 ประเภท+เกณฑ์เลือก, ไอเดีย AI-friendly (ตัวละคร≤3/สถานที่≤2/30-60วิ) · Dramy.ai = ผู้เล่นไทย niche เดียวกับ smartaihub
- [Storyboard Knowledge](storyboard-knowledge.md) — storyboard พื้นฐานสำหรับ AI video: board first render second, 3 ช็อตพื้นฐาน, จัดเฟรม, storyboard vs shot list (จาก Windows vault)
- [AI Video Realism Hierarchy](ai-video-realism-hierarchy.md) — motion/แสง/กล้อง = ตัวคูณ realism, skin detail = แค่ gate; QA ข้อ 1 = contact physics (มือแตะของ) + case study MV ไทย AI
- [Seedance Marco Freestyle Method](seedance-marco-freestyle-method.md) — ⭐ ORIGINAL ([@MarcoBorinEdit](https://x.com/MarcoBorinEdit/status/2068075513206174081)): **set the RULES not the SHOTS** — shot-by-shot ละเอียด = "the AI tell" (ช้า แข็ง) · ปล่อยให้โมเดล freestyle มุม + `Rare camera angles.` = คำปลดล็อก · 2 รูป + 6 บรรทัด + 1 gen · template เต็ม
- [Seedance Knowledge](seedance-knowledge.md) — how to write Seedance 2.0 video prompts: formula/camera/host specs + กฎทองมุมกล้อง (ลำดับบอก/มุมปล่อย) + under-direct acting (merged Windows vault 2026-07-05)
- [Seedance Prompt Repository](seedance-prompt-repository.md) — real Seedance 2.0 prompt examples + reusable style stacks
- [Seedance UGC Repository](seedance-ugc-repository.md) — Seedance 2.0 prompts for realistic UGC talking-head ads (don't look AI)
- [Storyboard GPT Image 2 → Seedance](storyboard-gpt-image-to-seedance.md) — make storyboard/keyframes in GPT Image 2, animate in Seedance 2.0
- [UGC Storyboard Sheet Template](ugc-storyboard-sheet-template.md) — production-ready 3-part@10s UGC storyboard layout that actually feeds Seedance (+ 4 fix-before-use rules)
- [Veo / Google Flow Knowledge](veo-google-flow-knowledge.md) — SEPARATE model (not Seedance): talking-head UGC master lock-tag template + Thai speech/VO-pacing rules
- [Director Styles Knowledge](director-styles-knowledge.md) — famous film director visual styles + prompt keywords (Wong Kar-wai, Nolan, Kubrick...) + สาย deadpan comedy (Keaton/Tati/Andersson/Kitano…) + เกณฑ์ว่าใส่ชื่อผู้กำกับใน prompt ได้ผลเมื่อไหร่
- [MV Directors Knowledge](mv-directors-knowledge.md) — drama/storytelling MV directors (intl + Thai) as style refs

## Music & Lyrics

- [Thai Lyric Writing](thai-lyric-writing.md) — หลักแต่งเนื้อเพลงไทย: สัมผัสนอก/ใน, 6 ประเภทสัมผัส+สเกลเสถียร, rhyme scheme aabb/abab, วรรณยุกต์ vs เมโลดี้, กฎ "ความหมายชนะสัมผัส" + สไตล์ fellow fellow

## Image Generation & Character

- [Thai Localization — Image Prompts](thai-localization-image-prompts.md) — กฎทำภาพ AI คนไทย/ฉากไทยให้อ่านออกว่าจริง (ไม่ postcard-fake): subject/setting specifics, standard adaptation phrase (ยิงตรง Thai subject/location ทับ prompt เดิม, validated 112 prompts), text-glyph verify rule, culture · wired เข้า `image-prompt-writer` skill (trigger note)
- [Zhao Yu (趙宇) — Character Profile](characters/zhao-yu.md) — Korean idol, pink Y2K theme; identity spec + 4 gen prompts (portrait/turnaround/expression sheet/TREND ICON cover) ล็อกหน้าข้ามภาพ · +07-06 **realistic RAW-UGC variant** (cherryhikiko-style: bright flat phone selfie + matte skin, sexy-tasteful preset + ceiling)
- [Cute-Face Charm Recipe](cute-face-charm-recipe.md) — แก้ realism ผ่านแต่หน้าไม่น่ารัก: Korean dong-an/aegyo-sal geometry block + full cherryhikiko cute-UGC prompt (หน้าสั้นกลม/ตากลมโตยิ้มเสี้ยว/จมูกเล็กมน)
- [K-pop Idol Visual Prompt](kpop-idol-visual-prompt.md) — realistic 20yo K-pop female "visual" beauty portrait recipe + แปลง superlative (สวยจนลืมหายใจ) → concrete features (glass skin/almond eyes/magnetic gaze)
- [AI Influencer Image Prompt](ai-influencer-image-prompt.md) — generate very realistic AI influencer/virtual-model images (don't look AI)
- [Wichcraft Prompt — Outfit Swap](outfit-swap-wichcraft-prompt.md) — เปลี่ยนเสื้อผ้า multi-ref: `@img1`=นางแบบ/identity + `@img2`=เสื้อ + `@img3`=button override + `@img4`=ท่อนล่าง + `@img5`=fit photo · **3 variant:** A=ภาพเดี่ยว 9:16 (7 บล็อก) · B=3-panel sheet (headless-front / rear+หัว / portrait) · **C=✅ VALIDATED 07-16 re-clothe 2-panel sheet เดิมเป็น anchor → หน้าไม่เพี้ยนข้าม 3+ ชุด (Dokkeaw nurse)** · หัวใจ = แยก img1/img2 เด็ดขาด+ปลดชุดเดิม + "translate flat-lay→worn naturally" + item-by-item + button "METAL not fabric" + "THE ONE CHANGE" สำหรับ override เดี่ยว (แขน/ปก) + flat catalogue lighting · close-up-dominant anchor = หน้าแรง · คู่ [[char-sheet-2panel-identity-garment]]
- [Char Sheet — 2-Panel (identity + faceless garment)](char-sheet-2panel-identity-garment.md) — ฟอร์แมต char sheet สาย fashion/lookbook: ซ้าย = beauty close-up (identity + ดีเทลปกคอ) · ขวา = full-body **front+back หน้าถูก mask เทา** (garment/fit ล้วน) · paste-ready prompt · **เสริม ไม่แทน** 4-view เดิม · **⚠️ VERDICT 07-15 (deep-research):** 16:9 ไม่ผิดแต่ sub-optimal — โมเดลย่อ ref เป็น patch grid เพดานคงที่ + ถ่วงทั้งเฟรมเท่ากัน (ไม่ face-aware) → หน้าเล็ก=signal อ่อน · ดีกว่า = anchor แนวตั้ง/close-up-dominant + แยกหน้ากับชุดเป็น 2 ภาพ · ตัวเลข "หน้า 30-50%/≥1024px" = REFUTE หมด · grey-mask low-risk
- [AI Character Identity Lock](ai-character-identity-lock.md) — keep same face across many images/scenes (named reference sheet, GPT Image 2)
- [DramaBox-Tier Portrait Recipe](drama-dramabox-tier-portrait-recipe.md) — 07-09 validated paste-ready drama character prompt template (idol glam makeup + dramatic key/rim light + sharp catchlights = the tier-clinching diff), tested on throwaway test char "Fon" not a locked character
- [AI Asset Library Workflow](ai-asset-library-workflow.md) — 07-09 from tutorial video: 3 asset categories (character/scene/prop)+color board, face-3-angle+9:16, scene 9-square grid+floor plan, prop turnaround, color hex-naming · demo footage also confirms [[feedback-drama-character-casting]]
- [Image Prompt Suffixes & Techniques](image-prompt-suffixes-techniques.md) — TVC white-tone suffix, pose-transfer, character-swap, upscale prompts, storyboard tool (from ZenityX)
- [AI Platform Content Limits](ai-platform-content-limits.md) — revealing/suggestive clothing limits (GPT Image/Nano Banana/Seedance): allowed vs blocked

## Prompt Libraries

- [Batch Image-Gen Pipeline Pattern](batch-image-gen-pipeline-pattern.md) — reusable resumable-batch pattern (JSONL queue + shared done-log dedup + parallel workers on disjoint slices) + known gotchas (timeouts, worker-kill, dedup hygiene, cost-approval), from AI Video Skool team's skill (07-09); reference-for-later, repo still prompt-first/manual-gen · prompt-craft half merged into `image-prompt-writer` skill (aesthetic A/B, one-change-at-a-time, originality rule, Higgsfield engine params, identity anchor kit, Real-Reference method, camera-angle vocab)
- [MeiGen Prompt Dataset](meigen-prompt-dataset.md) — FULL 7,420 prompts via open /api/search → gallery.html (external) + **text index บน internal `tools/prompt-index/` ค้นได้เสมอ** ([[rule-search-prompt-index-first]]); +1,446 curated; ad formulas
- [MeiGen Top Prompts](meigen-top-prompts.md) — full copy-paste text of top brand-ad/product/editorial/food prompts (Act as + PHASE formula, JSON identity-lock, [BRAND NAME] vars)
- [YouMind Prompt Pack](youmind-prompt-pack.md) — 8 full copy-paste GPT Image 2 prompts (editorial/UGC/product/food) + {argument} template + 10 restyle presets
- [YouMind GPT Image 2 Prompt Library](youmind-gpt-image-prompt-library.md) — filterable prompt gallery; use Photography×Influencer/Model / Product / Storyboard filters (skills subsite = academic, skip)

## Ad Knowledge & Research

- [SmartAIHub Drama App — Case Study](smartaihub-drama-series.md) — แอปของคนอื่น (ไม่ใช่ของเรา): drama-series แนวตั้งครบวงจร คิดเรื่อง→ตัวละคร→shot prompt→เจนผ่าน API · เก็บเป็น feature spec + จุดอ่อนที่เห็น · verdict 07-07: เราสร้างแบบนี้ได้ (คลัง = intelligence layer พร้อมแล้ว)
- [UGC Ad Structure](ugc-ad-structure.md) — UGC ad anatomy (hook/body/CTA) + worked teardowns of real AI UGC ads
- [Ads 50 Teardown — AI Video Bootcamp](ads-50-teardown-ai-video-bootcamp.md) — 50 competitor ad teardown: 4-beat skeleton, hook formulas, the modular hook-swap scale mechanic
- [Ads Contact-Sheet Pipeline](ads-contact-sheet-pipeline.md) — competitor ad teardown: _batch.py → sheets/ (30-frame 5x6) + txt/ transcripts in Desktop/Ads/videos

## Skills & Workflows

- [Watch Skill (claude-video)](watch-skill-claude-video.md) — INSTALLED `watch:watch` จาก repo bradautomates/claude-video: ให้ Claude ดูวิดีโอ (yt-dlp+ffmpeg+Whisper). detail modes (transcript/efficient50/balanced100/token-burner) · frame budget ตามความยาว · dedup ≤2.0 brightness · flags `--start/--end`/`--timestamps`/`--max-frames`/`--no-whisper` · ~197 tok/frame · ใช้ teardown ad คู่แข่งเร็ว คู่ [[ads-contact-sheet-pipeline]]
- [Factory Audit Skill](factory-self-audit-skill-plan.md) — DONE 07-09: `/factory-audit` scores brain health (Context/Connections/Capabilities/Cadence + leverage ranking) + wiki-lint (orphan links/files, contradictions, missing back-links) — trial-run verified against live repo, found real findings first run
- [Image Prompt Writer Skill](skill-candidates-image-lyrics.md) — DONE 07-09: ad-hoc single-image prompt skill (GPT Image 2/Nano Banana), pairs with asset-prompt-builder subagent (production pipeline) · **audited 07-09 (fleet-audit-style): 0 critical, 4 minor fixed** (anatomy positive-companion, restyle/pose-transfer sub-section, Seedream 4.5 in model table, hand-off boundary vs asset-prompt-builder)
- [Thai Lyric Writer Skill](skill-candidates-image-lyrics.md) — DONE 07-09: enforces mandatory 3-phase rhyme-map discipline (plan→draft→show map), can't skip · **audited 07-09: 1 critical fixed** (scope creep — dropped false "Thai poetry" claim, source is song-lyric-only) **+ 3 minor** (Phase 3 drift-check, outer-rhyme mandatory wording, worked example)
- [Skills Cheat Sheet](skills-cheatsheet.md) — which installed skill runs for which ad task + how to force-pick / auto-allocate
- [Seedance 2 Pro Director Skill](seedance-2-pro-director-skill.md) — INSTALLED skill (~/.claude/skills): elite single-shot Seedance prompt director (formula + char-anchor + frame-coords + QA); companion = shotlist-builder · Fable audit ยกระดับ 07-07 (+11 findings: golden rule/under-direct fix/input modes/budget 1,800)
- [Shotlist Builder Skill](shotlist-builder-skill.md) — INSTALLED skill: stateful 4-phase screenplay→shotlist HTML w/ Chinese Seedance prompts; cinematic-film lane; Claude Code-ready (Fable audit 07-07)
- [Video Prompt Builder Framework](video-prompt-builder-framework.md) — 4-section structure for planning whole Seedance ads (skill in ~/.claude/skills/) · audited 07-09 (fleet-audit-style): 0 critical, 1 minor fixed (reference file missing ENERGY ARC header)
- [Higgsfield 3-Step AI Ad Workflow](higgsfield-3step-ai-ad-workflow.md) — CINEMATIC-COMMERCIAL (not UGC): 2 Higgsfield Seedance 2.0 tutorials (headphones + football/robot) — asset→shotlist→scene + layout-map/erase-face/style-prefix/beat-ramp/physics-weight tricks
- [Higgsfield Marketing Studio Workflow](higgsfield-marketing-studio-workflow.md) — MS auto ad generator (beauty-brand demo): UGC + Hyper Motion + TV Spot in one tool + 5 luxury location prompts

## Tools & Setup

- [AI Factory Brain Sync](ai-factory-brain-sync.md) — git repo ~/ai-factory-brain: vault/agents/skills ตัวจริง + symlink กลับ; sync ด้วย ./sync.sh ต้น-ท้าย session; Windows junction map (รวม D--Claude → repo memory)
- [Legacy Vault D:\Claude](legacy-vault-d-claude.md) — vault เก่าบน Windows เกษียณ 2026-07-05: เหลือ 90-Assets (ไฟล์หนัก) + _archive · ความรู้ตัวจริงอยู่ repo
- [Grok Media Saver — Project](grok-media-saver-project.md) — extension โหลดรูป Grok Imagine ที่ D:\Downloads (Windows), v6.1.1 ใช้ได้จริง · เครื่อง Windows มี Node v24 แล้ว (07-07, refresh PATH ก่อนใช้)
- [Grok Media Saver — Knowledge](grok-media-saver-knowledge.md) — คู่มือใช้งาน + ความรู้เชิงลึก extension (ย้ายจาก vault เก่า)
- [Claude Subagents](claude-subagents.md) — MODEL POLICY: main=orchestrate เท่านั้น · **fleet 9** (opus: storyboard-prompter/asset-prompt-builder/script-hook-writer/deep-reasoner · sonnet: qa-inspector/teardown-analyst/timeline-builder/fast-worker/**kondomarie**) · playbook = FF_factory/AGENT_OPS.md · fleet ผ่าน Fable audit 07-07 (+kondomarie 07-09) · **skills 6 ตัวมี audit record ครบ** (3× 07-07, 3× 07-09) · kondomarie cloud routine รันเองทุกวันที่ 1+16
- [Exa MCP Setup](exa-mcp-setup.md) — Exa search via curl/MCP (free); Reddit+X unavailable, general web works; read_x.py for single tweets
- [Claude Plugins Installed](claude-plugins-installed.md) — 07-08: `pordee@pordee` จาก marketplace `kerlos/pordee` (GitHub) — ติดตั้งแล้ว ยังไม่ได้สำรวจว่าทำอะไร
