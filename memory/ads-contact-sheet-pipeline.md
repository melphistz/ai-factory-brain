---
name: ads-contact-sheet-pipeline
description: Pipeline that turns competitor video ads into contact sheets + transcripts for hook/body/cta teardown
metadata: 
  node_type: memory
  type: project
  originSessionId: cfc954fe-9092-4711-a327-ebd0eb31b1f4
---

Competitor AI-video-ad swipe analysis. Source ads in `/Users/working/Desktop/Ads/videos/` (50 numbered .mp4, AI-video-creator course ads).

Pipeline script: `/Users/working/Desktop/Ads/videos/_batch.py`. Per clip produces:
- `sheets/<name>.jpg` — dense contact sheet, 30 frames, 5x6 grid, scale 240w (`ffmpeg fps=30/dur,tile=5x6`). Replaced an earlier too-sparse 3x4/12-frame version — user said 12 frames missed key moments, wants denser.
- `txt/<name>.txt` — transcript w/ timestamps `[start-end] text`, via mlx-whisper model `mlx-community/whisper-large-v3-turbo`. Clips w/o audio stream get `[NO AUDIO]` (e.g. clip 26).

Script is idempotent-ish: always regenerates sheets, skips transcript if txt already exists. Re-run after adding new clips: `cd <dir> && python3 _batch.py`.

Deps already installed: `mlx-whisper` (pip), model cached. ffmpeg at /opt/homebrew/bin. No ImageMagick on this machine — tiling done via ffmpeg, not montage.

Next step (separate session): read sheets + txt per clip together, extract hook/body/cta. See [[ugc-ad-structure]].
