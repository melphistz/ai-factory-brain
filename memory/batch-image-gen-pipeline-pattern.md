---
name: batch-image-gen-pipeline-pattern
description: "Reusable engineering pattern for resumable batch image generation — JSONL queue + shared done-log dedup + parallel workers on disjoint slices + known gotchas (timeouts, worker-kill, dedup hygiene, cost-approval). Reference-for-later, not wired up (repo is prompt-first/manual-gen)."
metadata:
  node_type: memory
  type: reference
---

# Batch Image-Gen Pipeline Pattern

Source: a Claude Code skill (`ai-image-master`) shown to Mirko from a different team's environment (AI Video Skool course production pipeline, Italian team, validated in production 2026-07-07 on a 160-image batch). This is the operational/engineering half of that skill — the prompt-writing half was merged into `skills/image-prompt-writer/SKILL.md` (model-choice aesthetic A/B, one-change-at-a-time, originality boundary, Higgsfield engine params).

⚠️ **Excluded on purpose:** that source skill also included a "free GPT Image 2 via script" method that hits an internal ChatGPT-subscription-backed endpoint instead of the paid API — this violates OpenAI's ToS and got the source team's token revoked. Not reproduced, referenced, or reconstructed anywhere in this vault.

⚠️ **Not wired up.** This repo runs prompt-first/manual-gen per `/Users/working/ai-factory-brain/CLAUDE.md` — no auto `generate_*` calls until Mirko explicitly changes mode. This file is a reference pattern for *if/when* batch tooling gets built later, not something to implement now.

## The pattern

For any batch of 10+ images generated through a script/CLI (not manual one-off gen):

1. **Queue as JSONL**, one line per job: `{"src": ..., "size": ..., "prompt": ...}`. Plain-text, appendable, greppable, diffable.
2. **Shared done-log dedup**: each worker checks `cat done*.log | grep -qxF "$SRC"` before starting a job, and appends to its own `done<N>.log` after finishing. Multiple done-log files (one per worker) avoid write contention; the `grep -qxF` check across all of them is what prevents double-generation.
3. **Loop**: pull next un-done job from the queue → generate → convert to the target extension if needed (e.g. `convert x.png -quality 90 y.jpg`) → log to done-log → next.
4. **Parallelize by disjoint slices**: split the queue into N slices up front (not a shared work-stealing queue) and run one worker per slice. Simpler than a lock-based shared queue; the done-log is only there to make the whole batch resumable after a crash/interrupt, not for coordination between workers.

## Why this shape

- Resumable: kill the batch at any point, rerun the same command, already-done jobs skip via the done-log check.
- No central coordinator needed: disjoint slices mean workers never contend for the same job.
- Portable: works with any generation backend (this repo's context = Higgsfield MCP tools or manual ChatGPT/Gemini UI gen), the pattern is generation-engine-agnostic.

## Known gotchas (from the same source skill, 07-09)

- **GPT Image 2 timeout:** at quality `medium` the backend can take >180s — always pass a long timeout. If a generation call keeps failing with a timeout error, that's backend slowness, not a bug: sanity-test with quality `low` first (if that passes quickly, confirms it's just slow, not broken).
- **Killing a stuck generation worker:** killing the wrapper script does NOT kill child node processes — force-kill the actual generator process by name too, not just the wrapper.
- **Reference/asset hygiene:** when using scraped/downloaded reference images in a dataset, check for duplicates via checksum (`md5sum`) before use — e.g. the same logo repeated as image 01 in every folder is a common silent duplication bug.
- **Cost-approval rule:** any batch generation over 20 images, or any video generation, on a paid credit system → estimate the cost and get explicit confirmation before running, not after.
- **Spot-check after batch:** always spot-check 2–3 actual output files after a batch completes — never trust exit code alone as proof of success.

## Related

- [[image-prompt-suffixes-techniques]] — the prompt-writing side of batch/scale work
- `skills/image-prompt-writer/SKILL.md` — where the prompt-craft half of the source skill landed
