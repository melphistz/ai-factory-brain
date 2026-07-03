---
name: log-updates-to-obsidian
description: "Standing rule — log every new thing / update to the Obsidian memory vault, each time"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

Whenever something new is created, learned, changed, or updated in the work, record it in the Obsidian memory vault (`~/.claude/projects/-Users-working/memory/`) — every time, not just when asked.

**Why:** Mirko treats the memory dir as an Obsidian vault (wikilinks, graph). He won't remember details later and relies on the vault as the single durable knowledge base across sessions.

**How to apply:**
- New durable fact / skill / reference / decision → write/update a memory file (right `type`), add a `[[wikilink]]` to related notes, add a one-line pointer in MEMORY.md.
- Prefer updating an existing note over making a duplicate.
- Volatile live task-state stays in its project file (e.g. FF_factory/SESSION_STATE.md) but surface it in the vault via symlink so it shows in Obsidian — don't duplicate.
- Keep vault = distilled durable knowledge; project folders = live working docs.
