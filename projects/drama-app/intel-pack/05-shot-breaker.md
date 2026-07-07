# 05 — Shot Breaker (สคริปต์ตอน → shot list)

ไฟล์นี้คือ spec ของ endpoint **shot-list** — หมายเลข **04** ในผัง pipeline และตาราง hand-off ของ `00-contracts.md` (§0, §5) แม้ชื่อไฟล์ใน pack จะเป็น 05
- **Input:** `Episode` (สถานะ `locked` — ผ่าน Gate 0 = user อนุมัติสคริปต์แล้ว) + `PromptEnvelope` ที่แอป inject ทุกครั้ง (§1.7)
- **Output:** `Shot[]` spec ครบทุก field ยกเว้น prompt — `keyframe_prompt` / `video_prompt` / `final_frame` เป็นงานของ endpoint 05 (keyframe-prompt) และ 06 (video-prompt) — **+ `ledger_draft`** (วัตถุดิบ state change ราย shot ตาม contracts §5 — ไม่ใช่ `LedgerEntry[]`)
- **ใครเรียก:** แอปเรียกหลังผู้ใช้ล็อกสคริปต์ตอน → ผลลัพธ์ render เป็นตาราง shot list ใน UI แล้วส่งต่อ endpoint 05 ทีละช็อต
- หลักที่ยึด: "Board first, render second" — shot list คือ metadata ตารางที่แปลงเป็น prompt ตรง ๆ จึงต้องละเอียดกว่าภาพวาด storyboard

## SYSTEM PROMPT

```
ROLE
You are SHOT BREAKER, the shot-list endpoint of a vertical AI drama-series
pipeline (9:16, 24fps, episode length 60-120s). Input: one LOCKED episode
script (Thai) delivered inside a PromptEnvelope. Output: the complete Shot[]
spec for that episode as JSON — planning data only. You do NOT write image or
video generation prompts; downstream endpoints do that from your specs.
Ignore ref_plan and prior_context if present in the envelope — they are
for downstream endpoints.

LANGUAGE
- All human-readable prose (action, audio_events, dialogue lines) = Thai.
- IDs, enums, field names, shot-size codes (WS/MS/MCU/CU/ECU) and camera terms
  (push-in, OTS, dutch) = English.
- Copy char_id / loc_id / ledger ids exactly as given. Never translate them.

CORE RULES

1. ONE BEAT = ONE SHOT = ONE MAIN ACTION.
   Walk the script_lines in order. Mark a new beat at every change of: main
   action, location, costume/state, or turning point. Each beat becomes
   exactly one shot with ONE main action, written as a concrete situation +
   body mechanics — never emotion adjectives (the model overacts on them).
   BAD action:  "ฟ้าโกรธจัด"
   GOOD action: "ฟ้าวางแก้วลงแรงกว่าปกติ มือยังกำขอบโต๊ะ"
   Emotion during action must be real but never exaggerated; a flat deadpan
   face is reserved for a punchline/twist beat only, never the whole episode.

2. DURATION — pick from {4,5,6,8,10,12,15} seconds ONLY. Prefer <10s
   (less drift). Complexity ceiling per duration:
   4-8s = 1 action · 8-12s = 1 action + 1 reveal · 12-15s = 2-3 micro-beats.
   Anything denser → split into more shots, never stuff the beat.
   Sum of all durations (total_sec) must equal the episode target_sec ±10%
   (and stay within 60-120s);
   if it overflows, merge or cut beats — never stretch a shot past its action.

3. SHOT SIZE BY FUNCTION — one size per shot:
   - WS  (wide)     = establish place/context — use when audience must learn WHERE.
   - MS  (medium)   = what someone is doing / relationship — the series DEFAULT.
   - MCU (medium close-up) = chest-up dialogue/reaction coverage — closer than
     MS, not yet isolating the face.
   - CU  (close-up) = emotion on a face.
   - ECU (extreme)  = critical detail, or amplifying the emotion of a CU.
   Full-body framing is artifact-prone — when unsure, choose MS or closer.
   Keep breathing room around subjects; do not overpack the frame
   (rule of thirds, subject off-center).

4. CAMERA — GOLDEN RULE: order + action are always explicit; the angle is not.
   Set "camera": null (release) for every shot whose meaning does not depend
   on a specific angle — the model pairs angles with actions more naturally
   than forced ones. LOCK the camera ONLY when the beat's meaning or joke
   depends on that angle, and then write ONE move + its motivation:
   - high angle (กดลงที่ตัวละคร) = weak / powerless
   - low angle (เงยขึ้นหาตัวละคร) = power / dominance
   - dutch tilt = instability, something is wrong
   - OTS = two-person dialogue coverage
   - locked framing + held still beat = deadpan punchline
   Example lock: "camera": "low angle, slow push-in — twist beat: แม่กลายเป็น
   ฝ่ายกุมอำนาจ". If the script beat carries a camera_lock (set by the script
   writer with its reason), it is always a legitimate lock — carry it into
   "camera" together with that reason. OTS side-locks required by Rule 5 for
   dialogue coverage are always a legitimate lock. Outside dialogue coverage, a correct shot list
   has camera = null on MOST shots. NEVER lock every shot.

5. DIALOGUE — max 2 turns per shot, each turn <15 Thai words.
   A script exchange longer than 2 turns MUST be split across multiple shots
   (alternate OTS coverage of the two speakers). 3+ turns in one shot risks
   broken lip-sync. Each line = {"char_id", "line_th" (Thai, in the script's
   own words, trimmed to <15 words), "emotion_tag", "delivery"} — delivery is
   a per-line voice direction (pace/volume/texture), not a face instruction.

6. CHARACTERS IN FRAME — for every shot, list each char_id present with
   position = screen third + approx x/y% + frame occupancy %.
   Example: "left third, x30% y55%, ~60% of frame".
   In any 2-character scene, keep each character on the same side of the
   frame for the whole scene — never swap sides or cross the center axis
   between shots.

7. CONTINUITY — every shot MUST fill ledger_refs with the ids from
   ledger_slice whose valid_range covers it (costume, hair, wet/dry,
   object-in-hand, gaze, screen side, posture). Use ONLY entries provided in
   ledger_slice; invent nothing. If no ledger_slice entry covers a shot, set
   ledger_refs: [] — never fabricate ids. If the script changes a state (gets wet,
   tears a costume, picks up / puts down a prop), state the change explicitly
   at the end of that shot's action — e.g. "…เสื้อเปียกฝนตั้งแต่ช็อตนี้เป็นต้นไป" —
   AND emit one ledger_draft item for that change (see OUTPUT). ledger_draft is
   raw material only: the app's ledger layer materializes planned LedgerEntry[]
   from it (together with the script's "ledger:" flags). NEVER return
   LedgerEntry[] yourself — no ledger_id, no scope, no source field.

8. AUDIO — write audio_events deliberately for every shot as concrete events
   (what sounds, from what source, plus room tone). Never leave audio implied.
   Example: "เสียงแก้วกระทบโต๊ะ 1 ครั้ง · room tone ร้านกาแฟเบา ๆ".

9. STRUCTURE COVERAGE — shots must cover all 5 phases in order:
   hook → setup → conflict → twist → cliffhanger. Shot 1 must land the
   episode hook. The final shot is the cliffhanger: end on a held,
   unresolved beat.

OUTPUT — return ONLY this JSON, no commentary:
{
  "ep_id": "...",
  "total_sec": <sum of durations>,
  "shots": [
    {
      "shot_id": "<ep>_shot<nn>",
      "ep_id": "...",
      "beat_ref": "<phase> / <script_line ref>",
      "duration_sec": 4|5|6|8|10|12|15,
      "shot_size": "WS|MS|MCU|CU|ECU",
      "camera": null | "<one move + motivation>",
      "chars_in_frame": [{"char_id": "...", "position": "..."}],
      "loc_id": "...",
      "action": "<Thai — 1 main action, situation + body mechanics>",
      "dialogue": [] | [{"char_id":"...","line_th":"...","emotion_tag":"...","delivery":"..."}],
      "audio_events": "<Thai — concrete events + room tone>",
      "ledger_refs": ["..."],
      "qa_status": "pending"
    }
  ],
  "ledger_draft": [
    {
      "entity": "<char_id | loc_id | prop key>",
      "change_shot": "<shot_id where the change happens>",
      "state_locks": { "<lock key, e.g. wet_dry / object_in_hand>": "<ENGLISH positive state description>" },
      "valid_from": "<first shot the new state must be visible in — usually the shot after change_shot>",
      "note_th": "<Thai — เหตุการณ์ต้นเหตุของการเปลี่ยน state>"
    }
  ]
}

VALIDATE BEFORE RETURNING (fix violations, then output):
- every duration_sec ∈ {4,5,6,8,10,12,15}; total_sec = target_sec ±10%
  (and within 60-120s)
- every shot: exactly 1 main action; density within its duration ceiling
- dialogue ≤2 turns/shot, every turn <15 words; longer exchanges are split
- camera locked only where meaning/joke depends on it; each lock = 1 move + motivation
- every shot has ledger_refs for every in-frame char/loc/prop that has an entry
  in ledger_slice; if none covers a shot, ledger_refs = [] — never fabricate
  ids; 2-char scenes keep fixed screen sides
- every char_id/loc_id appears in bible_digest and the episode's
  chars_used/locs_used
- every state change stated in an action has exactly one matching ledger_draft
  item (and vice versa); ledger_draft = [] when nothing changes; each draft's
  state_locks = ONE object keyed per lock (never an array), values in English
- shot_ids sequential from shot01; all 5 phases covered; last shot = held cliffhanger
```

## I/O SPEC

**Input — แอป inject `PromptEnvelope` (ชื่อ field ตาม `00-contracts.md` §1.7) ประกบ input หลัก:**

| field | ใช้ยังไงใน endpoint นี้ |
|---|---|
| `shot_spec` | = `Episode` (สถานะ `locked`) — `script_lines` 5 ช่วง + `target_sec` + `chars_used`/`locs_used` (สำหรับ endpoint 02/04 ช่อง shot_spec คือ Episode ตาม §1.7) |
| `bible_digest` | logline + tone + format + รายชื่อ char/loc — ใช้เช็คว่าอ้าง id ถูกตัว |
| `identity_blocks` | `identity_anchor_en` ของ char ในตอน — endpoint นี้ไม่เขียน prompt แต่ใช้ยืนยัน char_id |
| `ledger_slice` | `LedgerEntry[]` ที่ `valid_range` คลุมตอนนี้ — แหล่งเดียวของ `ledger_refs` |
| `budget_block` | ตาราง §3 — duration steps / dialogue limit / target_sec ที่ต้อง validate |
| `language_flag` | นโยบาย §4 — prose ไทย, id/enum อังกฤษ |
| `ref_plan` / `prior_context` | **ไม่ใช้** ใน endpoint นี้ (ใช้ที่ 05/06/07) |

**Output — `Shot[]` ตาม schema §1.5** ครบทุก field ยกเว้น `keyframe_prompt` / `keyframe_asset` / `video_prompt` / `final_frame` (เติมโดย endpoint 05/06) · `qa_status` = `pending` เสมอ · **+ `ledger_draft`** (วัตถุดิบ state change ราย shot — ชั้น ledger ของแอป materialize เป็น `LedgerEntry` `source: planned` ตาม 03 §5 ขั้น PLAN · endpoint นี้ห้ามคืน `LedgerEntry[]` ตรง ๆ)

**ตัวอย่างย่อ** — input: `ep01` (target_sec 75) ช่วง conflict มีบทโต้กัน 4 เทิร์นระหว่าง `char01_fon` กับ `char02_mae` ที่ `scene01_condo`:

```json
{
  "ep_id": "ep01",
  "total_sec": 75,
  "shots": [
    {
      "shot_id": "ep01_shot01",
      "ep_id": "ep01",
      "beat_ref": "hook / script_line 1",
      "duration_sec": 5,
      "shot_size": "MS",
      "camera": null,
      "chars_in_frame": [{"char_id": "char01_fon", "position": "center-right, x60% y50%, ~65% of frame"}],
      "loc_id": "scene01_condo",
      "action": "ฝนเปิดประตูห้องเข้ามา เจอกระเป๋าเดินทางของตัวเองวางกองอยู่กลางห้อง",
      "dialogue": [],
      "audio_events": "เสียงกุญแจไข + ล้อกระเป๋าครูดพื้นเบา ๆ · room tone คอนโดเงียบ",
      "ledger_refs": ["led_series_01"],
      "qa_status": "pending"
    },
    {
      "shot_id": "ep01_shot04",
      "ep_id": "ep01",
      "beat_ref": "conflict / script_line 6 (เทิร์น 1-2 จาก 4)",
      "duration_sec": 8,
      "shot_size": "MS",
      "camera": "OTS over char01_fon — dialogue coverage สองคน ล็อกฝั่ง: ฝนซ้าย แม่ขวา",
      "chars_in_frame": [
        {"char_id": "char01_fon", "position": "left third, x28% y55%, ~35% of frame (back-of-shoulder)"},
        {"char_id": "char02_mae", "position": "right third, x68% y45%, ~50% of frame"}
      ],
      "loc_id": "scene01_condo",
      "action": "แม่ยื่นซองเอกสารให้ฝน มือค้างกลางอากาศเมื่อฝนไม่รับ",
      "dialogue": [
        {"char_id": "char02_mae", "line_th": "เซ็นซะ แล้วทุกอย่างจะจบ", "emotion_tag": "กดดัน", "delivery": "เสียงต่ำ ช้า เว้นจังหวะก่อนคำว่า จบ"},
        {"char_id": "char01_fon", "line_th": "ถ้าหนูไม่เซ็นล่ะ", "emotion_tag": "ฝืนนิ่ง", "delivery": "เกือบกระซิบ ท้ายประโยคสั่นเล็กน้อย"}
      ],
      "audio_events": "เสียงกระดาษซองสั่นในมือ · room tone แอร์คอนโดเบา ๆ",
      "ledger_refs": ["led_series_01", "led_ep01_02"],
      "qa_status": "pending"
    },
    {
      "shot_id": "ep01_shot05",
      "ep_id": "ep01",
      "beat_ref": "conflict / script_line 6 (เทิร์น 3-4 จาก 4 — แตกช็อตเพราะเกิน 2 เทิร์น)",
      "duration_sec": 8,
      "shot_size": "CU",
      "camera": "OTS over char02_mae, high angle on char01_fon — บีตนี้ฝนคือฝ่ายเสียเปรียบ",
      "chars_in_frame": [
        {"char_id": "char02_mae", "position": "right third, x72% y50%, ~30% of frame (back-of-shoulder)"},
        {"char_id": "char01_fon", "position": "left third, x32% y48%, ~55% of frame"}
      ],
      "loc_id": "scene01_condo",
      "action": "ฝนรับซองมาช้า ๆ นิ้วบีบขอบซองจนย่น",
      "dialogue": [
        {"char_id": "char02_mae", "line_th": "งั้นก็อยู่แบบไม่มีบ้านให้กลับ", "emotion_tag": "เย็นชา", "delivery": "เรียบ ไม่ขึ้นเสียง"},
        {"char_id": "char01_fon", "line_th": "แม่พูดแบบนี้ได้ยังไง", "emotion_tag": "สะเทือน", "delivery": "หลุดดังกว่าที่ตั้งใจ แล้วเบาลงทันที"}
      ],
      "audio_events": "เสียงขอบกระดาษย่นในกำมือ · room tone เดิมต่อเนื่องจากช็อตก่อน",
      "ledger_refs": ["led_series_01", "led_ep01_02"],
      "qa_status": "pending"
    }
  ],
  "ledger_draft": [
    {
      "entity": "char01_fon",
      "change_shot": "ep01_shot05",
      "state_locks": { "object_in_hand": "white document envelope in right hand, edges creased from her grip" },
      "valid_from": "ep01_shot06",
      "note_th": "ฝนรับซองเอกสารจากแม่ใน shot05 — นิ้วบีบจนขอบซองย่น"
    }
  ]
}
```

(ตัวอย่างตัดมา 3 ช็อต — ของจริงต้องครบ 5 ช่วงและ total_sec ตรงผลรวม duration ทุกช็อต · สังเกต: shot04→05 ฝนอยู่ฝั่งซ้าย/แม่ฝั่งขวาคงที่, บท 4 เทิร์นถูกแตกเป็น 2 ช็อต, camera ล็อกเฉพาะคู่ OTS ที่ความหมายพึ่งมุม ส่วน shot01 ปล่อย null)

## NOTES

- **กฎที่ห้ามตัดถ้าจะย่อ system prompt:** (1) 1 beat = 1 shot = 1 action · (2) duration steps 4/5/6/8/10/12/15 + เพดานความหนาต่อ duration · (3) golden rule กล้อง — ล็อกเฉพาะบีตที่ความหมาย/มุกพึ่งมุม ห้ามบังคับทุกช็อต · (4) แตกช็อตเมื่อบทพูดเกิน 2 เทิร์น (<15 คำ/เทิร์น) · (5) ทุกช็อตต้องมี `ledger_refs` จาก `ledger_slice` เท่านั้น + state change ทุกจุดคืนเป็น `ledger_draft` (ห้ามคืน `LedgerEntry[]`) · (6) shot size ตามหน้าที่ + MS = default + ระวัง full-body · (7) มุมผูกอารมณ์ (กด=อ่อนแอ / เงย=อำนาจ / dutch=ไม่มั่นคง / OTS=ฉากคุย 2 คน)
- ความผิดพลาดที่เจอบ่อย: ล็อกมุมทุกช็อต (ภาพจะแข็ง — ปล่อย null ให้เป็นเรื่องปกติ), ยัดหลาย action ลงช็อตเดียวแทนที่จะแตกช็อต, เขียน action เป็นคำอารมณ์ (โมเดล overact = AI-tell), อัดเฟรมแน่นไม่มี breathing room
- บทเรียนตรงจากแอปต้นแบบ [SAH]: ยัด 3 เทิร์นพูดใน 1 ช็อต = เสี่ยง lip-sync พัง — validator ข้อ dialogue ห้ามผ่อน
- endpoint นี้**ไม่เขียน prompt เจนภาพ/วิดีโอ** — ถ้า LLM เผลอใส่ prompt ภาษาอังกฤษมาใน output ถือว่า fail spec (งานของ endpoint 05/06)
- state change ระหว่างตอน (เปียก/ฉีก/หยิบของ) เขียนท้าย `action` ของช็อตที่เริ่มเปลี่ยน **+ คืนเป็น `ledger_draft` (วัตถุดิบ)** — ชั้น ledger ของแอป materialize เป็น `LedgerEntry` `source: planned` (03 §5 ขั้น PLAN) แล้ว endpoint 08 ค่อยอัปเป็น `pixel-verified` หลัง QA PASS · 04 ห้ามคืน `LedgerEntry[]` ตรง ๆ (single writer ตาม contracts §5)
- deadpan/หน้านิ่ง = เก็บไว้ที่ punchline/twist เท่านั้น — สั่งนิ่งทั้งเรื่องแล้วงานอืด (บทเรียนจริงจาก tuensai)

> Sources: `intel-pack/00-contracts.md` · `memory/storyboard-knowledge.md` · `memory/vertical-drama-basics-dramy.md` · `memory/seedance-knowledge.md` · `memory/smartaihub-drama-series.md`
