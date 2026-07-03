#!/bin/bash
# One-shot sync: run at session start AND end.  ./sync.sh
set -e
cd "$(dirname "$0")"
git pull --rebase --autostash
git add -A
git commit -m "sync $(date +%Y-%m-%d_%H%M) @$(hostname -s)" 2>/dev/null || echo "nothing new to commit"
git push
echo "SYNCED."
