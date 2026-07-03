---
name: exa-mcp-setup
description: Exa MCP server installed for searching Reddit/X/web (free tier) — how it was set up
metadata: 
  node_type: memory
  type: reference
  originSessionId: af118af7-09a7-486a-9296-4356febc322f
---

# Exa MCP — search Reddit / X / web (free tier)

ตั้งเพื่อค้น Reddit + X + เว็บ (Reddit บล็อก Anthropic crawler ตรงๆ ทั้ง WebSearch+WebFetch → ต้องผ่าน Exa). เกี่ยวกับ [[ai-influencer-image-prompt]] (ค้นความเห็นจริงเรื่องโมเดลภาพ).

## ติดตั้งแล้ว (มิ.ย. 2026)
- transport: HTTP remote (ไม่ต้องลง process เครื่อง)
- คำสั่งที่ใช้:
```
claude mcp add --transport http exa "https://mcp.exa.ai/mcp?exaApiKey=<KEY>"
```
- key เก็บใน `/Users/working/.claude.json` (project scope) แบบ plaintext — อย่า commit ไฟล์นี้
- สมัคร key ฟรีที่ https://dashboard.exa.ai/api-keys (free tier มี credit, ไม่ผูกบัตร)

## ✅ ใช้ได้ทันทีผ่าน curl (ไม่ต้อง restart!)
key ใช้กับ REST API ตรงได้เลย — เร็วกว่ารอ MCP โหลด:
```
curl -s -X POST 'https://api.exa.ai/search' \
  -H 'x-api-key: <KEY>' -H 'Content-Type: application/json' \
  -d '{"query":"...","type":"auto","numResults":8,"contents":{"highlights":true}}'
```
- `type`: auto (default) / fast / instant / deep / deep-reasoning
- `contents`: highlights (token-ประหยัด) / text.maxCharacters / summary
- `includeDomains`/`excludeDomains` (ไม่ใช่ includeUrls)
- structured: ใส่ `outputSchema` (ทุก type) → ได้ JSON + grounding citations
- canonical doc: https://docs.exa.ai/reference/search-api-guide-for-coding-agents

## ⭐ อ่าน X/Twitter ฟรี (ถ้ารู้ลิงก์) — Twitter syndication API
public, ไม่ต้อง login/auth/key. ใช้กับ tweet ที่มี url/id อยู่แล้ว:
```
curl -s "https://cdn.syndication.twimg.com/tweet-result?id=<STATUS_ID>&token=a"
```
STATUS_ID = เลขท้าย url (`x.com/user/status/<STATUS_ID>`). คืน JSON:
- `.text` (display, อาจตัดที่ media link) · `.note_tweet.text` (long tweet เต็ม) · `.user.name/.screen_name`
- `.mediaDetails[]` → photo (`.media_url_https`) / video (`.video_info.variants[-1].url` = .mp4 โหลดได้)
- `.favorite_count`

parse เร็ว:
```
curl -s "https://cdn.syndication.twimg.com/tweet-result?id=<ID>&token=a" \
| python3 -c "import sys,json;d=json.load(sys.stdin);n=d.get('note_tweet');print((n.get('text') if n else None) or d.get('text'))"
```
**ข้อจำกัด:** อ่านได้เฉพาะ tweet ที่**รู้ลิงก์** (ค้นหา X ไม่ได้) · ทีละ tweet · thread/reply ต้องรู้ id แต่ละอัน · token ใส่อะไรก็ได้

### ⭐ ดีกว่า: สคริปต์ `read_x.py` (fallback chain)
`/Users/working/.claude/scripts/read_x.py` — stdlib ล้วน ไม่ต้อง install. ลอง 3 ชั้น:
**FxTwitter → Syndication → oEmbed** (FxTwitter ดีสุด: text เต็ม + note_tweet ยาว + stats + media .mp4)
```
python3 /Users/working/.claude/scripts/read_x.py "<url|id>" [--json]
```
- recover text เต็มที่ syndication curl ตัด (เช่น conclusion + prompt ในโพสต์ทดสอบ storyboard)
- FxTwitter endpoint: `https://api.fxtwitter.com/status/<id>` (JSON สะอาด ใช้ตรงก็ได้)

## ⭐ exa `web_fetch_exa` ทะลุ Cloudflare ได้ (crack เว็บ bot-blocked)
เว็บที่ curl+WebFetch โดน **403 "Just a moment" (CF JS challenge)** → `mcp__exa__web_fetch_exa` render ผ่านได้ (เจอกับ meigen.ai ก.ค. 2026).
- แต่ **เห็นแค่ SSR shell** ถ้า content เป็น client-fetch (เช่น prompt body โหลดทีหลัง) → exa ได้ nav/related แต่ไม่ได้ตัว data
- **บทเรียน:** ก่อนสู้ CF ให้หา data source ที่เปิดอยู่ก่อน — เว็บ prompt-gallery มักมี **open-source dataset / GitHub repo / MCP server / npm package** (meigen → [[meigen-prompt-dataset]] ดึง JSON ตรงจาก GitHub raw ไม่ต้องแตะเว็บเลย)
- ลำดับเจาะเว็บ: `curl` (เร็ว) → ถ้า 403/JS → หา API/RSC ใน HTML → หา open dataset/repo → สุดท้าย `exa web_fetch_exa`

## ⚠️ ข้อจำกัดที่เจอจริง (ทดสอบ มิ.ย. 2026)
- **Reddit + X/Twitter เข้าไม่ได้บน Exa** → `SOURCE_NOT_AVAILABLE` (licensing ปิด crawler). includeDomains `reddit.com`/`x.com` = error
  - แปลว่า **ฟรีล้วน ค้น Reddit/X ตรงๆ ไม่ได้** ไม่ว่าทางไหน (WebSearch/WebFetch ก็โดน Reddit บล็อก)
  - X ตัวเดียวที่เข้าได้ = X official API จ่าย ~$200/mo
  - ทางอ้อม: ค้น general web → เจอบล็อกที่ quote reddit/x มาให้
- general web ใช้ได้ดีมาก (เจอ benchmark, comparison)
- **MCP tool (ไม่ใช่ curl) เพิ่มกลาง session → ต้อง restart** ก่อน exa tools โหลดใน ToolSearch
- free tier มี quota — หมดต้อง upgrade

## หลัง restart ใช้ยังไง
- exa มี tool ค้นเว็บ + ดึงเนื้อหา (web_search_exa ฯลฯ) — เรียกผ่าน ToolSearch `select:` ก่อน
- ค้น Reddit: ใส่ `reddit.com` หรือ subreddit ในคำค้น / domain filter
- งานค้าง: เทียบ Nano Banana vs GPT Image 2 vs FLUX (practical usage จริงจาก Reddit/X) → อัปเดต [[ai-influencer-image-prompt]]

## ถอน/แก้
```
claude mcp remove exa
claude mcp list   # เช็คสถานะ
```
