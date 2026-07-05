---
name: ai-ugc-ad-factory-workflow
description: "Modular AI UGC video-ad factory — multi-agent pipeline, hook-swap variations, design decisions locked"
metadata: 
  node_type: memory
  type: project
  originSessionId: edd72312-26b5-4aa5-9630-01041bcb5217
---

⚠️ **HARD RULE — no generation without explicit go.** Do NOT call any Higgsfield generate_* / preflight (get_cost) / models_explore-that-spends or otherwise touch credits until Mirko explicitly says generate. Image gen earlier WAS pre-approved per request; video/audio gen is NOT — confirm each time. When Mirko says "เตรียมตัว/prep only", stay in planning: scripts, schema, file org, no API spend. Higgsfield balance as of 2026-06-30: 435 credits (plan: plus).

ACTIVE project (started 2026-06-30): build a "video factory" workflow to mass-produce AI UGC ad videos for **Fox-Funnels** (FF), Mirko's video-marketing agency. Position edge: FF sells **DFY** (done-for-you — "we make 10 ad videos in 48hr, no crew") vs competitors' DIY (e.g. AI Video Bootcamp's $9 course). DFY = stronger for Thai SME. Reference competitor teardown: [[ads-50-teardown-ai-video-bootcamp]].

## Core money-saving principle (do NOT lose this)
8 concepts × 3 hooks ≠ render 24 full videos. Render **modular**:
- BODY+CTA = gen ONCE per concept = 8 heavy renders
- HOOK (0-3s) = gen per variant = 24 short/cheap renders
- assemble `hook[i] + body[c] + cta[c]` via ffmpeg concat = free
- heavy cost ≈ 8 long + 24 short instead of 24 full → ~50-60% saving + 100% body consistency

## Architecture locked (after 4 design rounds)
- **Data backbone**: 1 job = 1 folder + `manifest.json` flowing through every stage (status field → resumable, parallelizable, rerun only edited stage). 3 JSON contracts: `concepts.json` → `renderjobs.json` (matrix concepts×hooks) → `timeline<video>.json` (feeds Remotion directly).
- **LLM agents touch only 4 creative steps**: (1) Strategist, (2+3 merged) Art-Director w/ identity lock, (8) QA. Everything else = deterministic scripts. Fewer agents = cheaper/stabler/resumable.
- **Stage order**: 0 Intake → 1 Concept Strategist → 2/3 Avatar+Keyframe (one art-director agent, identity lock sheet reused all clips) → **Voice (TTS) BEFORE Motion** → Motion (Seedance/Veo lip-sync) → Assembly/timeline (deterministic, NOT LLM) → Remotion render → QA.

## Audio/lip-sync decision: chose (B) over (A)
- (A) Seedance native audio per clip — REJECTED (voice drifts between blocks, can't hide visual cut).
- (B) **TTS / 1 continuous VO track + per-block lip-sync + intentional hard-cuts** — CHOSEN.
- Voice consistency lock: same voice_id + TTS params + loudness-normalize whole job → "sounds like one take".

## The 2 physical risks that kill the system (orchestration is the easy part)
1. **lip-sync quality** (stage Motion)
2. **hook↔body seam** — AI gen of separate clips drifts (avatar/light/outfit/bg) → visible cut = looks cheap AI. Mitigate:
   - last-frame of body = first-frame of hook (img→video chain)
   - **J-cut / L-cut**: audio crosses the clip boundary (body VO enters ~0.3-0.5s before body visual) — audio track INDEPENDENT of clip boundary in Remotion timeline
   - **"intentional cut" not "seamless"**: design hook as a DIFFERENT shot-type/angle/location/B-roll from body → hard cut reads as normal, not continuity break. Make it a constraint in stage 1-2, not luck.

## Captions
Word-level timing must be EXTRACTED from real VO via whisper (mlx_whisper large-v3-turbo) → fed to Remotion. NOT authored ahead by an LLM. Captions = word-by-word big center text (genre standard).
- **Remotion = the factory captioner** (deterministic from JSON, scriptable). CapCut OK for a quick PoC only — never bake into the system (manual = unscalable).

## QA = 2 gates, not 1
- **pre-motion gate** (after keyframe): check identity/keyframe BEFORE paying for animate
- **post-render gate**: check lip-sync/caption/identity on contact-sheet keyframes → pass/redo

## Feedback loop (makes it a system, not a dumb press)
Ad results (CTR/CPA) → back into stage 1 → double-down winning hooks, kill losers. Without this you mass-produce untested creative.

## Build order (no big-bang)
- v0 (now): manual glue, prove on **1 body + 2 hooks** (not 1 clip — need ≥2 variants sharing a body to actually test the seam). De-risk lip-sync + seam first.
- v1: manifest schema + auto stages 1,(2+3),6,7 + pre-motion gate
- v2: matrix runner 8×3 parallel + post-render QA agent
- v3: feedback loop from ad results

## Tooling stack
Nano Banana Pro / GPT Image 2 (Thai AI presenter + identity lock, see [[ai-character-identity-lock]], [[ai-influencer-image-prompt]]) → Seedance 2.0 / Veo (animate + lip-sync, see [[seedance-ugc-repository]], [[seedance-knowledge]]) → Remotion (caption/super/CTA card render) → whisper (caption timing). Higgsfield + Seedance MCP for generation (costs credits — confirm with Mirko before spending).

## Fox-Funnels current ad (baseline creative)
File: `~/Desktop/Ads/Fox-Funnels - Video Marketing Agency_*/`. 3 files = 1 creative (identical transcript, aspect variants). Thai AI presenter, talking-head selfie. Structure: hook(problem "แอดยิงแล้วเงียบ?") → agitate (Meta hungry for video, 1 clip dies fast, ad cost rising) → offer (FF makes 10 AI ad videos Commercial+UGC in 48hr, no crew) → meta-reveal ("this clip = all FF AI, not filmed") → CTA "ทักแชต". Gaps vs playbook: meta-reveal buried at 26s (test moving to front), no social proof, no risk reversal/price anchor, only 1 hook so far.

## FF Modular Ad Bank v1 — SPINE + 10 Thai hooks
SPINE locked (problem→mechanism→proof→CTA "ทักแชต"), swap only HOOK 0-3s + presenter. Saved draft: `knowledge/ff_ai_ads_modular_bank_v1.md`.
Hook tiers (my ranking):
- **Tier S (test first)**: #1 meta-reveal "คลิปนี้ไม่ถ่ายจริงสักวิ" (FF's unfair edge — ad IS the demo); #2 "แอดยิงแล้วเงียบ" (proven baseline); #3 "ค่าจ้างทีมถ่าย 1 คลิป = ค่าแอดเกือบเดือน" (cost-anchor).
- **Tier A**: #6 competitor-FOMO, #9 meta-honest, #5 direct-offer.
- **Tier C cut/rework**: #7 "ไม่ต้องออกหน้าเอง" (wrong avatar — creator pain not SME); #10 "กลัว AI ดูปลอม?" (defensive open plants doubt — never open defending).
- Rule: each hook needs a DISTINCT visual (not 10 identical talking heads).

## Next action (where we paused)
PoC = 1 body + hook#1 + hook#3 → concat J-cut → inspect seam. Blocked on: (1) Mirko confirm spend credits, (2) avatar — provide Thai presenter ref or gen new + identity-lock sheet.

## ⚡ OPERATING MODE v2 (2026-07-05) — PROMPT-FIRST / MANUAL GEN

Mirko pivot: **ลืม Ploy ไปก่อน (reset 0)** · **ไม่ยิง MCP gen เลย** — Claude คิด prompt เป็นหลัก Mirko เจนเอง manual แล้วเอาภาพ/คลิปกลับมาให้ Claude ต่อ · ถ้า flow นี้ OK ค่อยต่อยอด (automation/matrix จอดไว้)

Flow (storyboard ภาพก่อนวิดีโอ — Mirko เลือก 2026-07-05): (1) intake brief/storyboard → (2A) **asset-prompt-builder Phase A** — prompt char portrait+sheet / scene plate + GEN ORDER + แผน storyboard → (3A) Mirko เจน char/ฉาก **โยนกลับ** → (3A.5) qa-inspector เช็ค → (2B) **asset-prompt-builder Phase B** — อ่านภาพจริง ทำ continuity ledger จาก pixel แล้วเขียน **storyboard frame prompts** ต่อโมดูล/ช็อต (@Image map, เฟรม = first-frame วิดีโอ) → (3B) Mirko เจนเฟรม โยนกลับ → (4) **storyboard-prompter** video prompt จากเฟรมจริง → (4.5) Mirko เจนวิดีโอ → (5) **timeline-builder** timeline.json (J-cut/captions/fx) สำหรับ Remotion/Hyperframe/ตัดมือ · เหตุผล board-first: ledger ตรงภาพจริง + เห็นทั้งเรื่องก่อนจ่ายค่าวิดีโอ + แก้ภาพนิ่งถูกกว่า

Playbook เต็ม: `projects/FF_factory/AGENT_OPS.md` · โมดูล tag: HOOK / BODY.PROBLEM / BODY.MECH / BODY.DEMO / BODY.PROOF / CTA — กฎ modular เดิมคงอยู่ทั้งหมด (BODY ร่วมทุก hook, hook≠body เชิงภาพ, J-cut ที่รอยต่อ)
