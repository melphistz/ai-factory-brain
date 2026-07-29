---
name: agent-skills-whitepaper
description: REFERENCE — Kaggle/Google "Agent Skills" whitepaper (May 2026) — how to write, eval, version, and compose Agent Skills; the craft standard behind our whole skills/ library
metadata:
  type: reference
---

# Agent Skills Whitepaper (Kaggle/Google, May 2026)

62-page whitepaper. Authors: Tanvi Singhal, Gabriela Hernandez Larios, Debanshu Das, Lavi Nigam, Smitha Kolan (curated Shubham Saboo). Open spec at **agentskills.io** / github.com/agentskills/agentskills. Google official repo: github.com/google/skills (Cloud Next 2026).

**Source:** https://www.kaggle.com/whitepaper-agent-skills · good summary: https://explainx.ai/blog/kaggle-agent-skills-whitepaper-guide-2026

## What a Skill is
Folder with `SKILL.md` (required: `name` + `description` frontmatter) + optional `scripts/` `references/` `assets/`. Exactly the format our `skills/` already uses. **Progressive disclosure**, 3 levels:
- L1 metadata (name+description) — loaded EVERY turn (~50–100 tok/skill)
- L2 body (full SKILL.md) — loaded only when skill triggers (keep < 500 lines / ~5000 tok)
- L3 bundled files — loaded only when body references/runs them (zero token cost until touched)

## Why Skills (4 friction points they solve)
1. **Context rot** — dumping all instructions in one prompt degrades the LLM. Skills load on demand.
2. **Procedural memory** — LLMs have episodic (what happened) + semantic (facts) but lacked "how to do it step-by-step." Skill = first credible procedural-memory primitive (the day-one runbook).
3. **Multi-agent overload** — instead of deploying many sub-agents, use 1 general agent + a library of skills. (Multi-agent still wins for genuine parallelism, different security postures, adversarial checks, heterogeneous models.)
4. **Portability** — a markdown folder runs on any agent with filesystem access (Claude Code / Codex / Cursor / ADK). No vendor lock-in.

## The 5 rules (cheatsheet)
1. **One skill, one job** — if the description needs "and" for two unrelated jobs, split it.
2. **Descriptions are the interface** — spend more time on `description` than on the body; it's what the router matches. Must say WHAT + WHEN (trigger phrases).
3. **Skills are dependencies** — version, pin, PR-review, test them.
4. **Right team owns right skill** — domain expert writes it, not a central AI bottleneck.
5. **Runtime is interchangeable** — portability is the value.

## Eval (the part we were missing)
"A skill without a test is a hope." 4 failure modes: **trigger** (wrong/no fire), **execution** (fires but wrong output), **token budget** (bloated body → context rot when co-loaded), **regression** (new skill breaks routing for old ones).
- **Never eval a skill in isolation** — production co-loads 5–15 skills; a body that passes alone can fail in the library.
- Tiered gates: Read-only → 90% trigger accuracy · Draft-only → 20+ golden cases · Action-allowed (irreversible) → adversarial + human sign-off.

## Composition & meta-skills
- DAG orchestration via a file bus (not LLM context as a database) — matches our prompt-first, save-every-output-to-job-file rule.
- Shift deterministic logic into testable `scripts/`; capitalized "ALWAYS DO X" in prose gets ignored by models ("context debt").
- Meta-skills: harvest successful traces → draft new skills. Agent-written skills always enter at DRAFT tier + human review first. Don't start meta-skills on an empty library.
- Skills vs the rest: MCP = connect to systems · Skill = teach the workflow to use them · AGENTS.md/CLAUDE.md = always-on conventions + router · RAG = library.

## What we did with it (07-29)
Wired the eval lessons into our own audit: added **Step 4e — skill/agent description-quality lint** to the `[[factory-self-audit-skill-plan|factory-audit]]` skill (missing-"when", one-skill-one-job "and"-split, trigger collision vs [[skills-cheatsheet]], over-length/ALL-CAPS shouting). See [[rule-use-installed-skills]] for our force-use rule and [[skills-cheatsheet]] for the manual force-pick table that a trigger-collision lint should eventually make unnecessary.
