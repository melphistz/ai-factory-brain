# Memory Index

One line per memory, grouped by section. Add new entries under the matching section, newest on top within it. Volatile session-state lives in project files — symlink in, don't duplicate. Keep lines SHORT (hook only); full detail lives in the topic file.

## Rules

- [Address User Politely](feedback-address-user-politely.md) — FEEDBACK (07-15): เรียก user = "คุณ/เรา" · **ห้ามมึง/กู/คำหยาบ** แม้ pordee (pordee ตัดแค่ particle)
- [Use Installed Skills](rule-use-installed-skills.md) — RULE: งานที่มี skill/agent ตรง → ต้องเรียกใช้ ห้ามเขียนสดใน main (ยกเว้นแก้เล็ก) · เช็ค [[skills-cheatsheet]]
- [Search Prompt-Index First](rule-search-prompt-index-first.md) — RULE: ก่อนเขียน prompt ภาพ/วิดีโอ → ค้น `~/ai-factory-brain/tools/prompt-index/` (`search.py term1 term2`) ก่อน
- [Model/Effort Strategy](feedback-model-effort-strategy.md) — FEEDBACK: intelligence-asset = ฉลาดสุด+ultracode+verify 2 เลนส์ · build/production = Opus/Sonnet+high · effort สูง=ช้าลง
- [Always Full Prompt](feedback-always-full-prompt.md) — FEEDBACK: คุยเรื่อง prompt ภาพ/วิดีโอ = จบด้วย full paste-ready prompt เสมอทุกครั้ง
- [Drama Character Casting](feedback-drama-character-casting.md) — FEEDBACK: ตัวละคร drama ทุกตัวต้องสวย/หล่อ แต่สมจริงไม่ over · recipe → [[drama-dramabox-tier-portrait-recipe]]
- [Storyboard Narrative Not Flat](feedback-storyboard-narrative-not-flat.md) — FEEDBACK: storyboard คิดเป็น flow หนัง (มุม/reveal/movement/arc) ทุก panel dynamic · ห้ามแบน
- [Thai Lyric Craft](feedback-thai-lyric-craft.md) — FEEDBACK: เนื้อเพลงไทยวางสัมผัส (นอก+ใน) ตั้งแต่ร่างแรก + โชว์ rhyme map · หลัก = [[thai-lyric-writing]]
- [Vault Structure](vault-structure.md) — reorg 07-03: 9-section index + entry rule, rename log, backup location
- [Log Updates to Obsidian](log-updates-to-obsidian.md) — RULE: record every new thing/update in the vault, each time

## Active Projects

- [SEC Car Transport](sec-car-transport-project.md) — **NEW 07-23** งานลูกค้า AGV valet parking robot VMR-CR5300GAW2 (จับล้อยกลอย, split-modular, Laser SLAM, 3000kg). DONE = เอกสารคำอธิบาย 7 ขั้น + 16 loading frames. ไฟล์ที่ `/Volumes/WONYOUNG/SEC Car Transport/`
- [Drama App (ของเราเอง)](smartaihub-drama-series.md) — ระบบซีรีส์แนวตั้งเอง · v1 BUILT+VERIFIED · prompt-first (ปฏิเสธ auto-gen ขัด ToS) · UI redesign 8/8 DONE + genre×setting 2-axis wire แล้ว (build+lint+smoke PASS, commit `732c032`) · **detail เต็ม = `projects/drama-app/STATE.md`** · retrospective = [[drama-app-fable-ultracode-retrospective]]
- [แค่วันนี้ (Just Today MV)](kae-wan-nee-project.md) — MV รักสองสาว+อุกกาบาต · Guadagnino×Malick×Melancholia · projects/kae-wan-nee/ · next = gen เพลง + character sheet
- [ตื่นสาย (Sunday School Comedy)](tuensai-project.md) — หนังสั้น deadpan แนวเต๋อ · projects/tuensai/ · next = ผลเจน V3 + ค้างเซฟ prompt 30s
- [Story Ideas — แนวเต๋อ นวพล](story-ideas-nawapol.md) — idea bank 10 เรื่อง ภาพล้วนไม่มีบทพูด สำหรับโปรเจกต์ถัดไป
- [AI UGC Ad Factory Workflow](ai-ugc-ad-factory-workflow.md) — ACTIVE · MODE v2 prompt-first/manual-gen (flow 5 ขั้นใน AGENT_OPS.md) · 8 concept × 3 hook
- [FF Factory — Live Session State](FF_SESSION_STATE.md) — symlink → Desktop/Ads/FF_factory/SESSION_STATE.md (volatile, edit at source)
- [Neezplus (client ad)](../projects/neezplus/STATE.md) — **ACTIVE** โฆษณาอาหารแมว NEEZ+ 12 คลิป · SB01 kit เสร็จ (green screen, GPT Image 2 + Veo) · next = prompt SB02–08 · STATE.md = source of truth
- [Valenshield vid01-04 — DONE](valenshield-nurse-ad-project.md) — ✅ ปิดครบ: vid01-03 (07-10) + vid04 styling montage (07-29) · [[valenshield-nurse-ad-project]] · [[valenshield-macro-asmr-ad]] · [[valenshield-walkingpad-tifu-vid03]] · [[valenshield-dokkaew-styling-vid04]]

## Session State (volatile — archive when done)

(empty)

## Archived (resolved — reference only)

- [Gemini Gem — ARCHIVED](gemini-gem-seedance-director.md) — เลิกแจก 07-14 · Instructions + [knowledge pack](gemini-gem-seedance-knowledge-pack.md) ยังอยู่ถ้าจะฟื้น
- [YouMind Scrape — DONE](youmind-scrape-session-state.md) — DONE 07-03: merged youmind→galleries (img 6877, video 363)
- [MeiGen Library — DONE](meigen-library-session-state.md) — 07-30 +1,209→8,629 prompts (index 9,985) · FDA re-toggle EVERY reboot (macOS external-volume TCC bug)

## Seedance / Video Prompting

- [Vertical Drama Basics (Dramy.ai)](vertical-drama-basics-dramy.md) — ตอน 5 ช่วง Hook/Setup/Conflict/Twist/Cliffhanger บังคับ · Hook 4 ประเภท · AI-friendly (ตัวละคร≤3/สถานที่≤2/30-60วิ)
- [Storyboard Knowledge](storyboard-knowledge.md) — พื้นฐาน AI video: board first render second, 3 ช็อตพื้นฐาน, storyboard vs shot list
- [AI Video Realism Hierarchy](ai-video-realism-hierarchy.md) — motion/แสง/กล้อง = ตัวคูณ realism · QA ข้อ 1 = contact physics (มือแตะของ)
- [Seedance Marco Freestyle](seedance-marco-freestyle-method.md) — ⭐ set the RULES not the SHOTS · shot-by-shot = "the AI tell" · `Rare camera angles.` = คำปลดล็อก
- [Seedance Knowledge](seedance-knowledge.md) — เขียน Seedance 2.0: formula/camera/host + กฎทองมุมกล้อง + under-direct acting
- [Seedance Prompt Repository](seedance-prompt-repository.md) — real Seedance 2.0 prompt examples + reusable style stacks
- [Seedance UGC Repository](seedance-ugc-repository.md) — Seedance 2.0 prompts for realistic UGC talking-head (don't look AI)
- [Storyboard GPT Image 2 → Seedance](storyboard-gpt-image-to-seedance.md) — keyframes ใน GPT Image 2, animate ใน Seedance 2.0
- [UGC Storyboard Sheet Template](ugc-storyboard-sheet-template.md) — 3-part@10s UGC storyboard layout ที่ feed Seedance ได้ (+4 fix rules)
- [Veo / Google Flow](veo-google-flow-knowledge.md) — SEPARATE model: talking-head UGC lock-tag template + Thai speech/VO-pacing
- [Director Styles](director-styles-knowledge.md) — film director visual styles + keywords (Wong Kar-wai/Nolan/Kubrick + deadpan Keaton/Tati/Andersson)
- [MV Directors](mv-directors-knowledge.md) — drama/storytelling MV directors (intl + Thai) as style refs

## Music & Lyrics

- [Thai Lyric Writing](thai-lyric-writing.md) — สัมผัสนอก/ใน, 6 ประเภท, rhyme scheme aabb/abab, กฎ "ความหมายชนะสัมผัส" + สไตล์ fellow fellow

## Image Generation & Character

- [Thai Localization — Image Prompts](thai-localization-image-prompts.md) — กฎทำภาพคนไทย/ฉากไทยให้อ่านออกว่าจริง · adaptation phrase (validated 112) · wired เข้า image-prompt-writer
- [Zhao Yu (趙宇)](characters/zhao-yu.md) — Korean idol pink Y2K · identity + 4 gen prompts ล็อกหน้า · +07-06 realistic RAW-UGC variant (cherryhikiko-style)
- [Cute-Face Charm Recipe](cute-face-charm-recipe.md) — Korean dong-an/aegyo-sal geometry block + full cherryhikiko cute-UGC prompt
- [K-pop Idol Visual Prompt](kpop-idol-visual-prompt.md) — 20yo K-pop "visual" beauty portrait · superlative→concrete features (glass skin/almond eyes)
- [AI Influencer Image Prompt](ai-influencer-image-prompt.md) — realistic AI influencer/virtual-model (don't look AI)
- [Wichcraft — Outfit Swap](outfit-swap-wichcraft-prompt.md) — เปลี่ยนเสื้อผ้า multi-ref (@img1 identity + @img2 เสื้อ...) · 3 variant (A เดี่ยว/B 3-panel/**C ✅ VALIDATED 07-16 re-clothe 2-panel anchor**) · หัวใจ = แยก img1/img2 + flat-lay→worn + button METAL · คู่ [[char-sheet-2panel-identity-garment]]
- [Char Sheet — 2-Panel](char-sheet-2panel-identity-garment.md) — char sheet fashion: ซ้าย beauty close-up + ขวา full-body หน้า mask เทา (garment ล้วน) · ⚠️ VERDICT 07-15: anchor แนวตั้ง/close-up ดีกว่า 16:9 · แยกหน้ากับชุด 2 ภาพ
- [AI Character Identity Lock](ai-character-identity-lock.md) — keep same face across images/scenes (named reference sheet)
- [DramaBox-Tier Portrait](drama-dramabox-tier-portrait-recipe.md) — 07-09 validated drama char template (idol glam + dramatic key/rim + sharp catchlights)
- [AI Asset Library Workflow](ai-asset-library-workflow.md) — 3 asset categories (char/scene/prop)+color board · face-3-angle+9:16, scene 9-grid+floor plan
- [Image Prompt Suffixes & Techniques](image-prompt-suffixes-techniques.md) — TVC white-tone suffix, pose-transfer, char-swap, upscale, storyboard tool
- [AI Platform Content Limits](ai-platform-content-limits.md) — revealing/suggestive clothing limits (GPT Image/Nano Banana/Seedance)

## Prompt Libraries

- [Batch Image-Gen Pipeline Pattern](batch-image-gen-pipeline-pattern.md) — resumable-batch (JSONL queue + done-log dedup + parallel workers) + gotchas · prompt-craft half merged เข้า image-prompt-writer
- [MeiGen Prompt Dataset](meigen-prompt-dataset.md) — 8,629 prompts via /api/search → gallery + text index บน internal tools/prompt-index/ ([[rule-search-prompt-index-first]])
- [MeiGen Top Prompts](meigen-top-prompts.md) — full text top brand-ad/product/editorial/food (Act as + PHASE, JSON identity-lock, [BRAND] vars)
- [YouMind Prompt Pack](youmind-prompt-pack.md) — 8 full GPT Image 2 prompts + {argument} template + 10 restyle presets
- [YouMind GPT Image 2 Library](youmind-gpt-image-prompt-library.md) — filterable gallery; Photography×Influencer/Product/Storyboard filters

## Ad Knowledge & Research

- [SmartAIHub Drama App — Case Study](smartaihub-drama-series.md) — แอปคนอื่น: drama-series ครบวงจร · feature spec + จุดอ่อน · verdict 07-07: เราสร้างได้
- [UGC Ad Structure](ugc-ad-structure.md) — UGC ad anatomy (hook/body/CTA) + teardowns
- [Ads 50 Teardown](ads-50-teardown-ai-video-bootcamp.md) — 50 competitor ad: 4-beat skeleton, hook formulas, modular hook-swap
- [Ads Contact-Sheet Pipeline](ads-contact-sheet-pipeline.md) — teardown: _batch.py → sheets/ (30-frame 5x6) + txt/ transcripts

## Skills & Workflows

- [ZenityX Interview Workflow](zenityx-interview-scene-workflow.md) — AI podcast/interview 3 ขั้น: 4-block image (identity lock+mirror trick) → Thai talking video (Grok Imagine, ~4 ประโยค/15s) → Kling two-shot closing

- [Agent Skills Whitepaper](agent-skills-whitepaper.md) — REFERENCE (Kaggle/Google 2026): craft standard for skills · 5 rules (desc=interface, one-skill-one-job) + eval (co-load, never in isolation) · wired into [[factory-self-audit-skill-plan]] Step 4e
- [Watch Skill (claude-video)](watch-skill-claude-video.md) — INSTALLED `watch:watch` (bradautomates): ให้ Claude ดูวิดีโอ · detail modes · flags `--start/--end`/`--timestamps` · gotcha: brew upgrade yt-dlp (SABR), Groq key expiry · คู่ [[ads-contact-sheet-pipeline]]
- [Factory Audit Skill](factory-self-audit-skill-plan.md) — DONE 07-09: `/factory-audit` scores brain health + wiki-lint (orphan/contradiction/back-link) · +07-29 Step 4e desc-quality lint ([[agent-skills-whitepaper]])
- [Image Prompt Writer Skill](skill-candidates-image-lyrics.md) — DONE 07-09: ad-hoc single-image (GPT Image 2/Nano Banana) · audited: 0 critical, 4 minor fixed
- [Thai Lyric Writer Skill](skill-candidates-image-lyrics.md) — DONE 07-09: mandatory 3-phase rhyme-map · audited: 1 critical + 3 minor fixed
- [Skills Cheat Sheet](skills-cheatsheet.md) — which skill runs for which ad task + how to force-pick
- [Seedance 2 Pro Director Skill](seedance-2-pro-director-skill.md) — INSTALLED: elite single-shot Seedance director · companion = shotlist-builder · Fable audit 07-07
- [Shotlist Builder Skill](shotlist-builder-skill.md) — INSTALLED: 4-phase screenplay→shotlist HTML w/ Chinese prompts · Fable audit 07-07
- [Video Prompt Builder Framework](video-prompt-builder-framework.md) — 4-section whole-ad planning (skill in ~/.claude/skills/) · audited 07-09
- [Higgsfield 3-Step Ad Workflow](higgsfield-3step-ai-ad-workflow.md) — CINEMATIC-COMMERCIAL: asset→shotlist→scene + layout-map/erase-face/beat-ramp tricks
- [Higgsfield Marketing Studio](higgsfield-marketing-studio-workflow.md) — MS auto ad gen: UGC + Hyper Motion + TV Spot + 5 luxury location prompts

## Tools & Setup

- [AI Factory Brain Sync](ai-factory-brain-sync.md) — repo ~/ai-factory-brain: vault/agents/skills + symlink กลับ · sync ด้วย ./sync.sh ต้น-ท้าย session
- [Legacy Vault D:\Claude](legacy-vault-d-claude.md) — เกษียณ 07-05: เหลือ 90-Assets + _archive · ความรู้จริงอยู่ repo
- [Grok Media Saver — Project](grok-media-saver-project.md) — extension โหลดรูป Grok Imagine (Windows) v6.1.1 · Node v24 (refresh PATH ก่อนใช้)
- [Grok Media Saver — Knowledge](grok-media-saver-knowledge.md) — คู่มือ + ความรู้เชิงลึก extension
- [Claude Subagents](claude-subagents.md) — MODEL POLICY: main=orchestrate · fleet 9 (opus 4 + sonnet 5) · playbook = AGENT_OPS.md · kondomarie routine วันที่ 1+16
- [Exa MCP Setup](exa-mcp-setup.md) — Exa search via curl/MCP (free); general web works, Reddit+X ไม่ได้
- [Claude Plugins Installed](claude-plugins-installed.md) — 07-08: `pordee@pordee` (marketplace kerlos/pordee)
