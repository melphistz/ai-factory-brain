#!/usr/bin/env python3
"""Search the local prompt index (derived from the MeiGen library on the
external volume — see index-meta.json for freshness).

  python3 search.py lavender fashion          # AND terms, ranked
  python3 search.py -n 5 -f macro water       # top 5, full text
  python3 search.py -s seedance camera        # filter source: meigen|youmind|seedance
"""
import json, sys, os, re

def main():
    args = sys.argv[1:]
    n, full, src = 10, False, None
    if "-n" in args: i = args.index("-n"); n = int(args[i+1]); del args[i:i+2]
    if "-f" in args: args.remove("-f"); full = True
    if "-s" in args: i = args.index("-s"); src = args[i+1]; del args[i:i+2]
    terms = [t.lower() for t in args]
    if not terms:
        print(__doc__); return
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt-index.jsonl")
    hits = []
    for line in open(path, encoding="utf-8"):
        it = json.loads(line)
        if src and it.get("src") != src: continue
        text = (it.get("text") or it.get("prompt") or "")
        low = text.lower()
        if all(t in low for t in terms):
            score = sum(low.count(t) for t in terms) + min(it.get("likes", 0), 50) * 0.2
            hits.append((score, it, text))
    hits.sort(key=lambda h: -h[0])
    print(f"{len(hits)} hits" + (f" (src={src})" if src else ""))
    for score, it, text in hits[:n]:
        cats = ",".join(it.get("categories") or ([it.get("category")] if it.get("category") else []))
        head = f"--- [{it.get('src')}] {it.get('model','?')} · {cats} · likes={it.get('likes',0)} · {it.get('id','')[:40]}"
        print(head)
        print(text if full else re.sub(r"\s+", " ", text)[:280])
    if len(hits) > n:
        print(f"... {len(hits)-n} more (use -n)")

if __name__ == "__main__":
    main()
