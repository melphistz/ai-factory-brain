#!/bin/bash
# Mac setup — recreate symlinks from Claude Code dirs to this repo.
# (Already done on the mac mini 2026-07-03; use this only on a NEW mac.)
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE="$HOME/.claude"
PROJ="$CLAUDE/projects/$(pwd | sed 's/[\/:]/-/g')"   # adjust if your slug differs

for d in agents skills; do
  [ -e "$CLAUDE/$d" ] && [ ! -L "$CLAUDE/$d" ] && mv "$CLAUDE/$d" "$CLAUDE/$d.bak"
  ln -sfn "$REPO/$d" "$CLAUDE/$d"
done

mkdir -p "$PROJ"
[ -e "$PROJ/memory" ] && [ ! -L "$PROJ/memory" ] && mv "$PROJ/memory" "$PROJ/memory.bak"
ln -sfn "$REPO/memory" "$PROJ/memory"

echo "DONE:"
ls -la "$CLAUDE/agents" "$CLAUDE/skills" "$PROJ/memory"
