# Memory Index

One line per memory, grouped by section. Add new entries under the matching section, newest on top within it. Volatile session-state lives in project files — symlink in, don't duplicate.

## Rules

- [Model/Effort Strategy](feedback-model-effort-strategy.md) — FEEDBACK: intelligence-asset (freeze ยาว) = โมเดลฉลาดสุด+ultracode+verify 2 เลนส์ · build/production = Opus/Sonnet+high ถูกกว่าทำได้เท่ากัน · effort สูง=ช้าลงไม่ใช่เร็ว · build ช้าเพราะ subprocess ไม่ใช่โมเดล
- [Always Full Prompt](feedback-always-full-prompt.md) — FEEDBACK: คุยเรื่อง prompt สร้างภาพ/วิดีโอ = จบด้วย full paste-ready prompt เสมอ ทุกครั้ง (อธิบายที่เพิ่มได้ แต่ต้องมี full)
- [Drama Character Casting Feedback](feedback-drama-character-casting.md) — FEEDBACK: ตัวละคร drama ทุกตัว (เอก+นางร้าย) ต้องสวย/หล่อหมด แต่ไม่ over ต้องสมจริง · validated recipe → [[drama-dramabox-tier-portrait-recipe]]
- [Thai Lyric Craft Feedback](feedback-thai-lyric-craft.md) — FEEDBACK: เนื้อเพลง/กวีไทยต้องวางสัมผัส (นอก+ใน) ตั้งแต่ร่างแรก + โชว์ rhyme map · หลักอยู่ thai-lyric-writing
- [Vault Structure](vault-structure.md) — reorg 2026-07-03: 9-section index + entry rule, rename log (ai-influencer-image-prompt), backup location
- [Log Updates to Obsidian](log-updates-to-obsidian.md) — RULE: record every new thing/update in the vault, each time

## Active Projects

- [Drama App (ของเราเอง)](smartaihub-drama-series.md) — ระบบซีรีส์แนวตั้งเอง (ต้นแบบ = case study ในลิงก์) · **07-07: v1 BUILT+VERIFIED + genre packs 5 แนว** · **07-08: ตัดสินใจอยู่ prompt-first ต่อ (ปฏิเสธ auto-gen ผ่าน token trick — ขัด OpenAI ToS)** + วางแผน UI redesign แล้ว (upload-รูปกลับ→sidebar→gallery card→bulk button→emotion chip, Sonnet พอ ~300-600K tokens) **PENDING รอ Mirko reset quota** · **07-09: PENDING genre pack ใหม่ "revenge/vindication"** (ขาว-ดำสุดขั้วแบบ ReelShort/DramaBox, Opus 4.8+ultracode แทน Fable ที่ใช้ไม่ได้แล้ว) — รายละเอียดเต็ม = `projects/drama-app/STATE.md` · retrospective คืนสร้าง v1 = [[drama-app-fable-ultracode-retrospective]]
- [แค่วันนี้ (Just Today MV)](kae-wan-nee-project.md) — MV รักสองสาว+อุกกาบาตวันสุดท้าย · Guadagnino×Malick×Melancholia · เพลง Suno สไตล์ fellow fellow · ไฟล์เต็ม projects/kae-wan-nee/ · status: shotlist ล็อก, next = gen เพลง + character sheet
- [ตื่นสาย (Sunday School Comedy)](tuensai-project.md) — หนังสั้น deadpan แนวเต๋อ (จาก Windows vault): รีบไปโรงเรียน→วันอาทิตย์ · ไฟล์เต็ม projects/tuensai/ · status: รอผลเจน V3 + ค้างเซฟ prompt 30s
- [Story Ideas — แนวเต๋อ นวพล](story-ideas-nawapol.md) — idea bank 10 เรื่อง ภาพล้วนไม่มีบทพูด สำหรับตั้งโปรเจกต์ถัดไป (ก๊อป projects/_template)
- [AI UGC Ad Factory Workflow](ai-ugc-ad-factory-workflow.md) — ACTIVE · **MODE v2 (07-05): prompt-first/manual-gen** (Ploy reset, no MCP gen, flow 5 ขั้นใน AGENT_OPS.md, ถ้า OK ค่อยต่อยอด) · โครงเดิม: 8 concept × 3 hook hook-swap
- [FF Factory — Live Session State](FF_SESSION_STATE.md) — symlink → Desktop/Ads/FF_factory/SESSION_STATE.md (volatile task-state, edit at source)
- [Valenshield Walking-Pad TIFU (vid03)](valenshield-walkingpad-tifu-vid03.md) — ACTIVE Valenshield campaign 3 = **vid03** (เคยเรียก vid02 ผิด, แยกแล้ว 07-06): cute walking-pad + TIFU-flip (หกใส่ตัว→ผ้าสะท้อนน้ำเซฟ), 20s 9:16 new model. sheet + 9-beat keyframe grid DONE (ใน `vid03/`), next=แตก keyframe เดี่ยว→animate. Has grid direction-lock + sheet-render pipeline
- [Valenshield Macro ASMR Ad](valenshield-macro-asmr-ad.md) — ACTIVE Valenshield campaign 2: 4-clip no-person WHITE fabric macro ASMR; Clip 2 defined (water-repellent bead demo)
- [Valenshield Nurse Ad Project](valenshield-nurse-ad-project.md) — ACTIVE project (campaign 1): LAVENDER nurse-uniform HERO ad w/ model, 5 clips, Seedance pipeline

## Session State (volatile — archive when done)

(empty — nothing currently in-flight; ดู Archived ด้านล่างสำหรับของที่ปิดแล้ว)

## Archived (resolved — kept for reference, not action items)

- [YouMind Scrape — DONE](youmind-scrape-session-state.md) — DONE 3 ก.ค.: merged youmind→galleries (img 6877, video 363). optional leftover: 44 img fail + youmind video undercount
- [MeiGen Library — DONE](meigen-library-session-state.md) — CLOSED, sync ongoing periodically: 07-08 +309→6,828 prompts. FDA needs re-toggle EVERY reboot (confirmed macOS external-volume TCC bug, not MDM)

## Seedance / Video Prompting

- [Vertical Drama Basics (Dramy.ai)](vertical-drama-basics-dramy.md) — โครงละครแนวตั้ง: ตอน 5 ช่วง Hook/Setup/Conflict/Twist/**Cliffhanger บังคับ**, Hook 4 ประเภท+เกณฑ์เลือก, ไอเดีย AI-friendly (ตัวละคร≤3/สถานที่≤2/30-60วิ) · Dramy.ai = ผู้เล่นไทย niche เดียวกับ smartaihub
- [Gemini Gem — Seedance Director](gemini-gem-seedance-director.md) — Gem สำเร็จรูป "Seedance 2.0 Prompt Director" สำหรับ Gemini: Instructions EN 11.8k chars + [knowledge pack](gemini-gem-seedance-knowledge-pack.md) พร้อมอัปโหลด + วิธีติดตั้ง/ลำดับตัดถ้าเกินลิมิต (กลั่นจากคลัง Seedance ทั้งหมด 07-05)
- [Storyboard Knowledge](storyboard-knowledge.md) — storyboard พื้นฐานสำหรับ AI video: board first render second, 3 ช็อตพื้นฐาน, จัดเฟรม, storyboard vs shot list (จาก Windows vault)
- [AI Video Realism Hierarchy](ai-video-realism-hierarchy.md) — motion/แสง/กล้อง = ตัวคูณ realism, skin detail = แค่ gate; QA ข้อ 1 = contact physics (มือแตะของ) + case study MV ไทย AI
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
- [AI Character Identity Lock](ai-character-identity-lock.md) — keep same face across many images/scenes (named reference sheet, GPT Image 2)
- [DramaBox-Tier Portrait Recipe](drama-dramabox-tier-portrait-recipe.md) — 07-09 validated paste-ready drama character prompt template (idol glam makeup + dramatic key/rim light + sharp catchlights = the tier-clinching diff), tested on throwaway test char "Fon" not a locked character
- [AI Asset Library Workflow](ai-asset-library-workflow.md) — 07-09 from tutorial video: 3 asset categories (character/scene/prop)+color board, face-3-angle+9:16, scene 9-square grid+floor plan, prop turnaround, color hex-naming · demo footage also confirms [[feedback-drama-character-casting]]
- [Image Prompt Suffixes & Techniques](image-prompt-suffixes-techniques.md) — TVC white-tone suffix, pose-transfer, character-swap, upscale prompts, storyboard tool (from ZenityX)
- [AI Platform Content Limits](ai-platform-content-limits.md) — revealing/suggestive clothing limits (GPT Image/Nano Banana/Seedance): allowed vs blocked

## Prompt Libraries

- [Batch Image-Gen Pipeline Pattern](batch-image-gen-pipeline-pattern.md) — reusable resumable-batch pattern (JSONL queue + shared done-log dedup + parallel workers on disjoint slices) + known gotchas (timeouts, worker-kill, dedup hygiene, cost-approval), from AI Video Skool team's skill (07-09); reference-for-later, repo still prompt-first/manual-gen · prompt-craft half merged into `image-prompt-writer` skill (aesthetic A/B, one-change-at-a-time, originality rule, Higgsfield engine params, identity anchor kit, Real-Reference method, camera-angle vocab)
- [MeiGen Prompt Dataset](meigen-prompt-dataset.md) — FULL 6,828 prompts pulled via open /api/search (no auth, bypasses CF) → local gallery.html; +1,446 curated open-source JSON; query/filter + ad formulas
- [MeiGen Top Prompts](meigen-top-prompts.md) — full copy-paste text of top brand-ad/product/editorial/food prompts (Act as + PHASE formula, JSON identity-lock, [BRAND NAME] vars)
- [YouMind Prompt Pack](youmind-prompt-pack.md) — 8 full copy-paste GPT Image 2 prompts (editorial/UGC/product/food) + {argument} template + 10 restyle presets
- [YouMind GPT Image 2 Prompt Library](youmind-gpt-image-prompt-library.md) — filterable prompt gallery; use Photography×Influencer/Model / Product / Storyboard filters (skills subsite = academic, skip)

## Ad Knowledge & Research

- [SmartAIHub Drama App — Case Study](smartaihub-drama-series.md) — แอปของคนอื่น (ไม่ใช่ของเรา): drama-series แนวตั้งครบวงจร คิดเรื่อง→ตัวละคร→shot prompt→เจนผ่าน API · เก็บเป็น feature spec + จุดอ่อนที่เห็น · verdict 07-07: เราสร้างแบบนี้ได้ (คลัง = intelligence layer พร้อมแล้ว)
- [UGC Ad Structure](ugc-ad-structure.md) — UGC ad anatomy (hook/body/CTA) + worked teardowns of real AI UGC ads
- [Ads 50 Teardown — AI Video Bootcamp](ads-50-teardown-ai-video-bootcamp.md) — 50 competitor ad teardown: 4-beat skeleton, hook formulas, the modular hook-swap scale mechanic
- [Ads Contact-Sheet Pipeline](ads-contact-sheet-pipeline.md) — competitor ad teardown: _batch.py → sheets/ (30-frame 5x6) + txt/ transcripts in Desktop/Ads/videos

## Skills & Workflows

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
- [Claude Subagents](claude-subagents.md) — MODEL POLICY: main=orchestrate เท่านั้น · fleet 8 (opus: storyboard-prompter/asset-prompt-builder/script-hook-writer/deep-reasoner · sonnet: qa-inspector/teardown-analyst/timeline-builder/fast-worker) · playbook = FF_factory/AGENT_OPS.md · **ทั้ง fleet+3 skills ผ่าน Fable audit 07-07**
- [Exa MCP Setup](exa-mcp-setup.md) — Exa search via curl/MCP (free); Reddit+X unavailable, general web works; read_x.py for single tweets
- [Claude Plugins Installed](claude-plugins-installed.md) — 07-08: `pordee@pordee` จาก marketplace `kerlos/pordee` (GitHub) — ติดตั้งแล้ว ยังไม่ได้สำรวจว่าทำอะไร
