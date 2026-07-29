---
name: factory-audit
description: Score the health of the ai-factory-brain repo itself (not a video/ad project) and produce a scored report. Use whenever the user asks to audit, health-check, or lint the brain/vault/memory system — trigger on phrasings like "/factory-audit", "audit the brain", "check ai-factory-brain health", "how healthy is the vault", "lint the memory", "find stale memory", "is the fleet/skills up to date", "check sync status", or "find orphan files/links in the vault". Runs two check groups: an AIS-OS-style 4-dimension score (Context/Connections/Capabilities/Cadence) with leverage-ranked fixes, and a Karpathy-style wiki Lint (orphan links, orphan files, contradictions, missing back-links, plus skill/agent description quality — trigger on "lint skill descriptions", "check skill triggers", "do my skills fire right", "any skills doing too much"). Do NOT use for auditing a specific ad/video project's quality (that's qa-inspector or teardown-analyst) — this skill audits the knowledge system itself.
---

# Factory Audit

You are auditing `ai-factory-brain` — the repo, not any single ad/video project inside it. Your job is to actually walk the live repo with Read/Bash/Grep and produce a scored, evidence-backed report. Never guess or summarize from memory of a previous audit — every number and finding must trace to a file you read or a command you ran in this run.

This skill is a runbook, not the report. Follow the steps below in order, then produce the output using the template at the end.

## When to use

Trigger on `/factory-audit` or natural requests to check the brain/vault/memory's health, freshness, sync status, or internal consistency. Do NOT use this for judging the quality of an ad/video project's copy, prompts, or footage — that is `qa-inspector` or `teardown-analyst`. Do NOT use it to just read one memory file for content — that's normal memory lookup, not an audit.

## Scope decision (do this first)

Ask yourself: does the user want a **full audit** (both check groups, full report) or a **quick check** (one thing, e.g. "just check sync status" or "any orphan links?")? If the request names a single check, run only that step and skip the rest — don't force the full report on a narrow question. If ambiguous or the user says "audit the brain" with no qualifier, run the **full audit**.

---

## Step 1 — Read the ground truth

Read in this order, every time, full audit or not:

1. `/Users/working/ai-factory-brain/CLAUDE.md` — the schema: what memory/agents/skills/projects mean and the rules that govern them.
2. `/Users/working/ai-factory-brain/memory/MEMORY.md` — the index. Note every section, every listed file, and the exact one-line status text for each entry (this is your source of "what the system currently believes is true").
3. `/Users/working/ai-factory-brain/memory/claude-subagents.md` — fleet roster + the date of the last full audit (currently 07-07 — but re-read, don't assume the date is still current).
4. `/Users/working/ai-factory-brain/memory/seedance-2-pro-director-skill.md` and `/Users/working/ai-factory-brain/memory/shotlist-builder-skill.md` — records of which skills have been through a real audit and when.
5. Directory listings: `ls agents/`, `ls skills/`, `ls memory/`, `ls memory/characters/` (or equivalent) at repo root — the actual inventory of what exists on disk, independent of what any memory file claims.

Do not skip step 5 — memory files describe the system, but only the filesystem proves it. Contradictions between what a memory file claims and what's actually on disk are exactly what this audit is for.

---

## Step 2 — AIS-OS-style scoring (4 dimensions, 0–100 each)

Score each dimension independently. Start at 100, subtract points for concrete findings (cite the file/command for each deduction — no vibes-based scoring). Use this rubric as the default point values; adjust ±5 if a finding is clearly bigger or smaller than the typical case, and say why.

**Context** (is the knowledge complete, current, and where it should be?)
- Active-project entry in MEMORY.md not updated in a long time relative to its own stated cadence (e.g. "ACTIVE" project untouched >2 weeks with no note explaining the pause): −10 each
- File referenced in MEMORY.md that doesn't exist on disk, or vice versa (see Step 4 lint): −10 each
- Frontmatter/status text inside a file contradicts another file or the filesystem (see Step 4 contradictions): −10 each

**Connections** (is the wikilink graph sound?)
- Orphan `[[wikilink]]` (target file doesn't exist): −5 each
- File with zero inbound links from anywhere else in memory/ (isolated node, not a Rule/Session-State entry which are allowed to stand alone): −5 each
- Missing back-link where two files are clearly about the same topic/project and only one links to the other: −3 each

**Capabilities** (are the fleet + skills real, current, and known-good?)
- Agent in `agents/` with no audit record anywhere in memory/: −15 each
- Skill in `skills/` with no audit record anywhere in memory/: −15 each
- Skill or agent directory that exists on disk but is untracked in git (built but never synced/committed): −10 each
- Skill/agent documented in a memory file as "not built yet" / "PENDING" while it actually exists fully-built on disk (stale memory about your own capabilities): −15 each

**Cadence** (does maintenance actually happen on a rhythm, not just when Mirko opens a session?)
- Zero automation/scheduled process found anywhere in tools/ or CLAUDE.md (this is close to a permanent baseline finding for this repo — don't repeat-penalize it every run once already known, but do report it): −15 flat if true
- "Session State (volatile — archive when done)" entries in MEMORY.md marked DONE/CLOSED but still sitting in that section instead of archived: −5 each
- Uncommitted changes sitting in the repo for longer than the length of the current session (i.e., clearly left over from a previous session, not work-in-progress from right now): −10
- Unpushed commits (local ahead of remote, if a remote is configured): −5

Report each dimension as `score/100` with a bullet list of every deduction applied (finding → points).

---

## Step 3 — Leverage ranking (not just a gap list)

For every deduction you applied in Step 2, compute:

**leverage = points lost × impact multiplier**

Impact multiplier:
- **3** — actively blocks or risks corrupting a currently-ACTIVE project, or means Claude could act on false information right now (e.g. a skill memory says "not built" but it exists — next session might rebuild it from scratch, or skip using it).
- **2** — slows future work or causes repeated small friction (e.g. broken wikilink a session will hit while researching, unaudited skill that might behave unpredictably).
- **1** — cosmetic/organizational only, no near-term consequence (e.g. one missing back-link between two rarely-visited reference files).

List every finding sorted by leverage descending. This ranking — not the raw dimension scores — is what tells Mirko what to fix first. Ties break toward whichever finding is cheaper to fix (quick wins first).

---

## Step 4 — Karpathy-style Lint (wiki health)

Run these as literal commands against the repo (adjust path if not already there: `/Users/working/ai-factory-brain`). Use Bash — don't eyeball this by reading files one at a time, the repo is too large.

**4a. Orphan wikilinks** — link targets with no real file:
```
cd /Users/working/ai-factory-brain/memory && grep -rno '\[\[[^]]*\]\]' . | sort -u
```
For each unique target (strip `[[`/`]]`, and for `[[path|label]]` aliases use the `path` part before `|`), **also strip a trailing `.md` if the target already has one** (some aliases write the extension inline, e.g. `[[vertical-drama-basics-dramy.md|vertical-drama-basics-dramy]]`) — then check `[ -f "$target.md" ]`. Skipping the strip step produces a false-positive orphan on any alias that already includes `.md`. Anything still missing after that is a real orphan link — **except** literal `[[wikilink]]` used as a syntax example inside prose (e.g. a rules file explaining the `[[wikilink]]` convention itself) — read the surrounding line to tell the difference before flagging it as broken.

**4b. Orphan files** — files that exist but aren't in MEMORY.md's index:
```
cd /Users/working/ai-factory-brain/memory && for f in $(find . -maxdepth 2 -name '*.md' ! -name MEMORY.md | sed 's|^\./||;s|\.md$||'); do
  grep -q "($f)\|($f.md)\|\[\[$f\]\]\|\[\[$(basename "$f")\]\]" MEMORY.md || echo "ORPHAN: $f"
done
```
Anything printed is a file with no index entry — dead weight or a logged-and-forgotten update.

**4c. Contradictions** — two files (or a file vs. MEMORY.md, or a file vs. the filesystem) claiming conflicting status about the same thing. This has no single command — actively look for it:
- For every "PENDING" / "ยังไม่เริ่ม" / "not built" / "TODO" claim you see in a memory file, check whether the thing it's talking about (a skill dir, an agent file, a feature) actually exists on disk already. This is the highest-value contradiction pattern in this repo.
- For every "DONE" / "COMPLETE" / "BUILT+VERIFIED" claim, spot-check that the artifact it refers to actually exists where claimed.
- Two MEMORY.md entries — in the same section or different sections (e.g. one under Active Projects, another under Skills & Workflows or Tools & Setup) — pointing at the same file or describing the same underlying thing with different status words also count. Check this directly: `grep -n "<filename>" memory/MEMORY.md` for any file that appears twice.

**4d. Missing back-links** — heuristic, not exact:
- From the wikilink dump in 4a, look for A→B links where B's file, read or grepped, never links back to A despite being about the closely related content (same project, same skill, direct feedback-to-subject relationship). Flag the clearest 3-5 cases only — this is a heuristic nudge, not an exhaustive grammar check.

**4e. Skill/agent description quality** — the `description` frontmatter is the interface the router matches against, so a vague or overloaded one makes the wrong skill fire (or the right one never fire). This lint is grounded in the Agent Skills whitepaper (Kaggle/Google, 2026) — see [[agent-skills-whitepaper]]. Dump every description first:
```
cd /Users/working/ai-factory-brain && for f in skills/*/SKILL.md agents/*.md; do
  echo "=== $f ==="; awk '/^name:/{n=$0} /^description:/{d=$0} /^---/{c++; if(c==2){print n; print d; exit}}' "$f"
done
```
Then flag each of these patterns (cite the file for every finding):

- **Missing "when"** — a description that says *what* the skill does but never *when* to use it (no trigger phrases / example user requests). The router needs both. Whitepaper rule: "descriptions are the interface — spend more time here than the body." Flag any description with no concrete trigger examples.
- **Doing too much ("one skill, one job")** — a description whose *what* clause joins two unrelated jobs with "and" (e.g. "writes ad copy **and** builds shotlists"). Related sub-steps of one workflow are fine; two jobs that would trigger on totally different requests are a split signal. Flag it and name the suggested split.
- **Trigger collision (co-load ambiguity)** — the highest-value check here. Compare trigger phrases/keywords across ALL skills + agents. Two entries whose triggers overlap enough that the router could pick the wrong one on the same request = a collision. This is exactly the failure that forces a manual `[[skills-cheatsheet]]` "force-pick" table — so cross-check findings against that file: every collision the cheatsheet already disambiguates confirms a real overlap that should ideally be fixed in the descriptions themselves (add explicit "NOT for X (use Y)" boundary lines), not just papered over by the cheatsheet.
- **Over-length / capitalized shouting** — description over ~1024 chars, or leaning on ALL-CAPS "ALWAYS DO X" imperatives (the whitepaper notes models tend to ignore those; deterministic musts belong in `scripts/`, not shouted in prose). Flag as a minor cleanup.

Scoring: a missing-"when" or a trigger collision on a skill used in an ACTIVE project is a **Capabilities** deduction (−10 each, impact ×2–3 — a mis-fire wastes a whole dispatch). "Doing too much" and over-length are −5 cosmetic (impact ×1) unless they cause a real collision.

---

## Step 5 — Sync status

```
cd /Users/working/ai-factory-brain && git status --short
git log -1 --format='%h %cd %s' --date=short
```
Report: any uncommitted files (path + whether tracked/untracked), and how stale the last commit is relative to today's date (see `currentDate` in context). Untracked new skill/agent/memory files are a Capabilities/Cadence finding (Step 2), not just a footnote.

---

## Output format

Always answer with this structure, filled with real findings from this run (never a template with placeholders left in):

```
## Score summary
Context: X/100
Connections: X/100
Capabilities: X/100
Cadence: X/100
Overall: X/100 (average)

[one bullet per deduction under each dimension, with the finding + points]

## Leverage ranking
1. [finding] — points lost X × impact Y = leverage Z — [one-line fix]
2. ...
(sorted descending, only real findings — no filler rows)

## Lint findings
### Orphan wikilinks
...
### Orphan files
...
### Contradictions
...
### Missing back-links
...
### Skill/agent description quality
(missing-"when", doing-too-much, trigger collisions, over-length — cite file; note collisions the skills-cheatsheet already works around)

## Sync status
...

## Recommended next actions
(top 3-5 items pulled straight from the leverage ranking, phrased as concrete next steps)
```

If a quick check was requested instead of a full audit (see Scope decision), skip the sections that don't apply and answer only the relevant one(s) — don't pad a narrow question with an empty full-report skeleton.

---

## Ground rules

- Every score deduction and every lint finding must be traceable to something you actually read or a command you actually ran in this session — no recalling a "typical" state of the repo from training data or a previous conversation.
- Don't double-penalize the same root cause in two dimensions without saying so explicitly (e.g. an untracked-but-built skill is both a Capabilities finding and a Cadence/sync finding — it's fine to count it in both, but say it's the same underlying issue).
- This skill never edits files, never commits, never runs `git push`, and never triggers any generation tool — it only reads and reports. If the user then asks you to fix a finding (archive a session-state entry, add a back-link, commit), that's a separate follow-up action, not part of the audit itself.
- Keep the report evidence-dense and short on commentary — file paths, line references, and point math, not prose about how healthy the vault "feels."
