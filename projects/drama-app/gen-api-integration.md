# drama-app — kie.ai Gen API Integration (spec + paste-ready code)

## ▶️ WINDOWS HANDOFF — เริ่มตรงนี้ (07-29)
สเปก+โค้ดครบ ยืนยันกับ docs จริงแล้ว (image+credits 100% · เหลือ verify video/veo shape). ทำตามลำดับ:
1. เอา key: https://kie.ai/api-key → เติมเงิน → ใส่ `.env.local`: `KIE_API_KEY=...` + `GEN_ENABLED=1` (เช็ค `.gitignore` มี `.env*` แล้ว)
2. **smoke เช็ค key** (1 คำสั่ง): `curl -H "Authorization: Bearer <KEY>" https://api.kie.ai/api/v1/chat/credit` → เห็นตัวเลข balance = key ใช้ได้
3. **smoke สร้างภาพจริง 1 ครั้ง** (§8 ข้อ 2) → ยืนยัน image flow
4. ก๊อปโค้ด: `lib/gen/models.ts` `lib/gen/kie.ts` `lib/gen/jobs.ts` (§2-4) + `app/api/gen/create|status|credits/route.ts` (§5) + refactor upload-back เป็น `lib/upload.ts` (§5c)
5. verify video (veo) shape ตอนต่อ scope วิดีโอ (§8 ข้อ 3)
6. UI opt-in + cost guard (§7)
> ก่อนก๊อป: `cd D:\drama-app` → refresh PATH (คำสั่งอยู่ STATE.md §วิธีรัน) → `git pull` ก่อน (ให้ทันเครื่อง mac)

---


> **สร้าง 2026-07-29.** ที่นี่ mac แตะ `D:\drama-app` (Windows) ไม่ได้ → เอกสารนี้ = spec + โค้ดพร้อมก๊อป ไปวาง+รัน+ทดสอบบน Windows.
> **Decision reversal:** STATE เดิม (07-08) ตัดสินใจ "ไม่ต่อ gen API". พลิก 07-29 — แต่เฉพาะ **official paid API (ถูก ToS)** + **opt-in ต่อการกด (ไม่ auto, prompt-first ยัง default)**. เหตุผลที่ปฏิเสธเดิมข้อ 2 (OAuth-token hack) ไม่เกี่ยวกับ path นี้; ข้อ 1 (เสียเงินต่อการกด) แก้ด้วย cost-guard + GEN_ENABLED opt-in.

## 0. หลักการ (อย่าหลุด)
1. **prompt-first ยังเป็น default.** gen เป็นปุ่ม opt-in ข้าง prompt/character. manual upload-back เดิมยังใช้ได้เหมือนเดิม.
2. **ไม่มี auto-gen.** ต้องกดปุ่ม + confirm cost ทุกครั้ง. ไม่มี loop ยิงเอง.
3. **GEN_ENABLED=1 ถึงจะเปิด.** ถ้า flag off ทุก /api/gen/* คืน 403 — ปลอดภัย default.
4. **ผลลัพธ์ไหลเข้า upload-back เดิม** (`/api/upload-image`) → แปะ thumbnail ต่อ character/ต่อ shot. ไม่สร้าง storage แยก.

## 1. kie.ai API contract (ยืนยันจาก docs.kie.ai 07-29)
- Base: `https://api.kie.ai`
- Header: `Authorization: Bearer <KIE_API_KEY>` + `Content-Type: application/json`
- **สร้าง task (unified):** `POST /api/v1/jobs/createTask`
  ```json
  { "model": "gpt-image/1.5-text-to-image",
    "input": { "prompt": "...", "aspect_ratio": "2:3", "quality": "high" } }
  ```
  → `{ "code":200, "msg":"success", "data": { "taskId":"task_..." } }`
  200 = **สร้างสำเร็จเท่านั้น ไม่ใช่เสร็จ**
- **query (jobs):** `GET /api/v1/jobs/recordInfo?taskId=<id>` → `data.state` = `"waiting"|"success"|"fail"` · `data.resultJson` = **JSON string** → `JSON.parse` ได้ `{resultUrls:[url]}` (มีค่าเมื่อ success) · `data.failCode`/`data.failMsg` เมื่อ fail (ยืนยันจาก docs กpt-image-2 07-29)
- **Veo (dedicated, ถ้าใช้ video):** `POST /api/v1/veo/generate` + `GET /api/v1/veo/record-info?taskId=` → **คนละ shape**: `successFlag` (0/1/2/3) + `resultUrls` (string array). ⚠️ verify shape จริงตอน smoke video
- Rate limit: 20 task ใหม่ / 10 วิ (429)
- error codes: 401 auth · **402 balance ไม่พอ** · 422 validation · 429 rate · 500 server

## 2. Model map (แก้ทีหลังได้ — อยู่ไฟล์เดียว)
`lib/gen/models.ts`
```ts
// credit เป็นค่าประมาณ — verify กับ /api/v1/common/credits จริง แล้วอัปเดต
export type GenKind = "image" | "video";
export interface GenModel {
  id: string;              // ส่งเป็น body.model
  kind: GenKind;
  label: string;
  approxCredits: number;   // โชว์ก่อนกด (guard)
  endpoint: "jobs" | "veo";
  defaults: Record<string, unknown>;
}
export const GEN_MODELS: Record<string, GenModel> = {
  // input fields ยืนยันจาก playground JSON tab (expected 3): prompt / aspect_ratio / resolution
  // ⚠️ ไม่มี field "quality" — อย่าใส่. output = { resultUrls: [url] } (ตรง ไม่ nested)
  // aspect_ratio รับ "auto"|"9:16"|1:1|3:2|2:3|4:3|3:4|16:9... · resolution "1K"|"2K"|"4K"
  // ⚠️ 2K/4K ห้าม ratio 5:4,4:5,3:1,1:3,9:21 — 9:16 ปลอดภัยทุก res
  "img-gpt": {
    id: "gpt-image-2-text-to-image", kind: "image", label: "GPT Image 2 (t2i)",
    approxCredits: 6, endpoint: "jobs",
    defaults: { aspect_ratio: "9:16", resolution: "2K" },
  },
  "img2img-gpt": {
    id: "gpt-image-2-image-to-image", kind: "image", label: "GPT Image 2 (i2i)", // verify id i2i จาก market
    approxCredits: 6, endpoint: "jobs", defaults: { aspect_ratio: "9:16", resolution: "2K" },
  },
  "vid-veo": {
    id: "veo3", kind: "video", label: "Veo 3 (image→video)",
    approxCredits: 120, endpoint: "veo", defaults: { aspect_ratio: "9:16" },
  },
  // seedance ถ้ามีใน market ให้เพิ่ม endpoint:"jobs" + model id ตาม docs
};
export const isVideoModel = (k: string) => GEN_MODELS[k]?.kind === "video";
```

## 3. kie client (server-only)
`lib/gen/kie.ts`
```ts
const BASE = "https://api.kie.ai";
function key() {
  const k = process.env.KIE_API_KEY;
  if (!k) throw new GenError(503, "KIE_API_KEY ไม่ได้ตั้งค่า");
  return k;
}
export class GenError extends Error {
  constructor(public status: number, msg: string) { super(msg); }
}
async function kie(path: string, init: RequestInit) {
  const res = await fetch(BASE + path, {
    ...init,
    headers: { Authorization: `Bearer ${key()}`, "Content-Type": "application/json", ...(init.headers||{}) },
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok || (body.code && body.code !== 200)) {
    throw new GenError(res.status === 200 ? 502 : res.status, body.msg || `kie error ${res.status}`);
  }
  return body;
}
// สร้าง task → คืน taskId
export async function createTask(endpoint: "jobs"|"veo", model: string, input: Record<string, unknown>) {
  if (endpoint === "veo") {
    const b = await kie("/api/v1/veo/generate", { method:"POST", body: JSON.stringify({ model, ...input }) });
    return b.data.taskId as string;
  }
  const b = await kie("/api/v1/jobs/createTask", { method:"POST", body: JSON.stringify({ model, input }) });
  return b.data.taskId as string;
}
// query → normalize เป็น {done, failed, urls}
// ⚠️ jobs กับ veo คนละ shape:
//   jobs  → data.state ("waiting"|"success"|"fail") + data.resultJson (JSON string → {resultUrls})
//   veo   → data.successFlag (0/1/2/3) + data.resultUrls (JSON string array)
export async function queryTask(endpoint: "jobs"|"veo", taskId: string) {
  if (endpoint === "veo") {
    const b = await kie(`/api/v1/veo/record-info?taskId=${encodeURIComponent(taskId)}`, { method: "GET" });
    const d = b.data || {};
    const urls = typeof d.resultUrls === "string" ? JSON.parse(d.resultUrls || "[]") : (d.resultUrls || []);
    return { done: d.successFlag === 1, failed: d.successFlag === 2 || d.successFlag === 3, urls, raw: d };
  }
  const b = await kie(`/api/v1/jobs/recordInfo?taskId=${encodeURIComponent(taskId)}`, { method: "GET" });
  const d = b.data || {};
  const result = d.resultJson ? JSON.parse(d.resultJson) : {};
  return {
    done: d.state === "success",
    failed: d.state === "fail",
    urls: (result.resultUrls || []) as string[],
    error: d.failMsg || undefined,
    raw: d,
  };
}
// ยืนยัน docs 07-29: GET /api/v1/chat/credit → {code,msg,data:<number>} · data = credit คงเหลือ (int ตรงๆ)
export async function credits(): Promise<number> {
  const b = await kie("/api/v1/chat/credit", { method: "GET" });
  return b.data as number;
}
// bonus: /api/v1/common/download-url (POST {url}) → temp download link ถ้า static URL หมดอายุ
```

## 4. Job store (reuse pattern data/<id>.json + mutex เดิม)
`lib/gen/jobs.ts` — เก็บ job ต่อ series ในไฟล์ `data/gen/<seriesId>.json` (array). ใช้ mutex/atomic-rename แบบเดียวกับ `store.ts` v1 (กัน lost-update + Windows EPERM).
```ts
export interface GenJob {
  jobId: string; taskId: string; seriesId: string;
  kind: "image"|"video"; modelKey: string;
  target: { type:"character"|"shot"; id:string };  // เอาไปแปะ thumbnail ตอนเสร็จ
  status: "pending"|"done"|"failed"; resultUrl?: string; error?: string;
  createdAt: number;
}
// readJobs(seriesId) / appendJob() / updateJob() — copy pattern จาก store.ts (async mutex + tmp+rename)
```

## 5. Routes
### 5a. `app/api/gen/create/route.ts`
```ts
import { NextRequest, NextResponse } from "next/server";
import { GEN_MODELS } from "@/lib/gen/models";
import { createTask, GenError } from "@/lib/gen/kie";
import { appendJob } from "@/lib/gen/jobs";
export async function POST(req: NextRequest) {
  if (process.env.GEN_ENABLED !== "1")
    return NextResponse.json({ error: "การเจนถูกปิดอยู่ (ตั้ง GEN_ENABLED=1)" }, { status: 403 });
  try {
    const { seriesId, modelKey, input, target } = await req.json();
    const m = GEN_MODELS[modelKey];
    if (!m) return NextResponse.json({ error: "ไม่รู้จักโมเดล" }, { status: 422 });
    if (!seriesId || !target?.id) return NextResponse.json({ error: "ขาด seriesId/target" }, { status: 422 });
    // video ต้องมีภาพต้นทาง (image-to-video)
    if (m.kind === "video" && !input?.image_url && !input?.imageUrl)
      return NextResponse.json({ error: "video ต้องมี image_url ต้นทาง (เจนภาพก่อน)" }, { status: 422 });
    const taskId = await createTask(m.endpoint, m.id, { ...m.defaults, ...input });
    const job = await appendJob(seriesId, { taskId, kind: m.kind, modelKey, target });
    return NextResponse.json({ jobId: job.jobId, taskId, approxCredits: m.approxCredits });
  } catch (e) {
    const err = e instanceof GenError ? e : new GenError(500, "เจนล้มเหลว");
    return NextResponse.json({ error: err.message }, { status: err.status });
  }
}
```
### 5b. `app/api/gen/status/route.ts` (poll + download + แปะ thumbnail)
```ts
import { NextRequest, NextResponse } from "next/server";
import { GEN_MODELS } from "@/lib/gen/models";
import { queryTask } from "@/lib/gen/kie";
import { getJob, updateJob } from "@/lib/gen/jobs";
import { attachImageFromUrl } from "@/lib/upload"; // reuse /api/upload-image logic (ดู §5c)
export async function GET(req: NextRequest) {
  if (process.env.GEN_ENABLED !== "1")
    return NextResponse.json({ error: "การเจนถูกปิดอยู่" }, { status: 403 });
  const seriesId = req.nextUrl.searchParams.get("seriesId")!;
  const jobId = req.nextUrl.searchParams.get("jobId")!;
  const job = await getJob(seriesId, jobId);
  if (!job) return NextResponse.json({ error: "ไม่พบ job" }, { status: 404 });
  if (job.status !== "pending") return NextResponse.json(job);
  const m = GEN_MODELS[job.modelKey];
  try {
    const r = await queryTask(m.endpoint, job.taskId);
    if (r.failed) return NextResponse.json(await updateJob(seriesId, jobId, { status:"failed", error: r.error || "generation failed" }));
    if (!r.done)  return NextResponse.json({ ...job, status:"pending" }); // ยังไม่เสร็จ — client poll ต่อ
    // เสร็จ: ดาวน์โหลด result → แปะเป็น thumbnail ผ่าน upload-back เดิม
    const localUrl = await attachImageFromUrl(seriesId, job.target, r.urls[0]);
    return NextResponse.json(await updateJob(seriesId, jobId, { status:"done", resultUrl: localUrl }));
  } catch (e:any) {
    return NextResponse.json({ error: e.message || "poll error" }, { status: e.status || 502 });
  }
}
```
### 5c. reuse upload-back
UI-redesign ข้อ 1 ทำ `/api/upload-image` (รับ multipart แล้วเซฟ public/ + set thumbnail) ไว้แล้ว. Refactor logic แกนเป็น `lib/upload.ts` แล้ว export:
- `attachImageFromUrl(seriesId, target, remoteUrl)` — `fetch(remoteUrl)` → เขียนไฟล์ `public/uploads/<seriesId>/<target.id>-<ts>.png` → update series JSON (`character.thumbnail` / `shot.keyframeImage`) → คืน local path
route `/api/upload-image` เดิมเรียก helper เดียวกัน (แค่ source ต่างกัน: multipart vs URL).
### 5d. `app/api/gen/credits/route.ts` — GET → `credits()` โชว์ balance บน UI

## 6. .env.local (Windows)
```
KIE_API_KEY=xxxxx          # จาก https://kie.ai/api-key
GEN_ENABLED=1              # ปิด = ไม่ตั้ง หรือ 0
ANTHROPIC_API_KEY=...      # เดิม
LLM_MOCK=                  # เดิม (ว่าง = LLM จริง)
```
⚠️ เช็ค `.gitignore` มี `.env*` (มีอยู่แล้วจาก v1) — อย่า commit key.

## 7. UI (opt-in + cost guard)
- ที่ PromptPanel/CharacterCard เพิ่มปุ่ม **"เจนภาพนี้ (~N credit)"** — แสดง `approxCredits` จาก model map ก่อนกด
- กด → `POST /api/gen/create` → ได้ jobId → poll `GET /api/gen/status?...` ทุก 5 วิ (image) / 15 วิ (video) จน `done|failed`
- done → thumbnail เด้งขึ้น (มาจาก upload-back path เดิม)
- ปุ่มวิดีโอ disabled จนกว่า character/shot จะมีภาพ keyframe แล้ว (image→video chain)
- โชว์ balance จาก /api/gen/credits ที่ header

## 8. Smoke test (Windows, key จริง — ทำก่อนต่อ UI)
- **image shape ยืนยันแล้วจาก docs gpt-image-2 (07-29):** model `gpt-image-2-text-to-image` · input {prompt,aspect_ratio,resolution} · query `state`+`resultJson`. code ตรงแล้ว — smoke แค่กัน typo/balance
1. `curl -H "Authorization: Bearer $KEY" https://api.kie.ai/api/v1/chat/credit` → เห็น balance (ยืนยัน key ใช้ได้) ✅ path ยืนยันแล้ว
2. createTask image จริง 1 ครั้ง → recordInfo วนจน `state:"success"` → parse resultJson → เห็น url ✅
3. **verify แค่ video (veo) shape** จริง — cost สูง ยิงครั้งเดียว (i2i id `gpt-image-2-image-to-image` = ตาม pattern t2i, มั่นใจสูง)
4. ค่อยต่อ route + UI

## 9. งานเหลือ / ความเสี่ยง
- **field/endpoint + ชื่อ param ต้อง verify กับ playground JSON tab / key จริง** (docs market แต่ละ model ต่างเล็กน้อย) — §8 ก่อน hardcode. โดยเฉพาะ **model id + ชื่อ param resolution/aspect_ratio** (playground แสดงเป็น UI — ต้องเช็คว่า JSON body ใช้ key ว่าอะไร)
- ~~9:16~~ **แก้แล้ว 07-29:** playground ยืนยัน gpt-image kie รับ 9:16 แท้ + 1K/2K/4K (2K/4K เว้น 5:4/4:5/3:1/1:3/9:21 — 9:16 ปลอดภัย). ไม่ต้อง crop เอง
- poll ยาว (video 1-3 นาที) → client กัน tab ปิด / job อยู่ไฟล์แล้ว = resume ได้
- rate 20/10s → bulk ทั้งตอนต้อง throttle
