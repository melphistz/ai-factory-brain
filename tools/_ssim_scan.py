#!/usr/bin/env python3
"""Full-coverage temporal anomaly scan for AI-video detection.

Computes SSIM between every consecutive frame pair (ffmpeg), then flags:
  PASS A: hard discontinuities inside stable shots (missed cuts / glitches)
  PASS B: mid-band single-frame dips in stable shots (warp/morph candidates)
Extracts a 4-frame strip per candidate for eyeball verification.

Usage: python3 _ssim_scan.py video1.mp4 [video2.mp4 ...]
Output: /tmp/vidscan_ev/<name>_wN_tXX.Xs.jpg + console table

Interpretation notes (from 2026-07-03 session, 3 AI clips / 8.6k pairs):
- modern gen video shows ZERO frame-level flicker — expect candidates to be
  hidden cuts, fades, whip pans, close-to-lens blur. Verify by eye.
- real AI tells live at semantic level: cross-shot wardrobe/prop/animal
  consistency, ECU detail-inconsistency. See vault: ai-video-realism-hierarchy
"""
import re, sys, os, statistics, subprocess, tempfile

FPS_DEFAULT = 24.0

def ssim_series(video):
    log = tempfile.mktemp(suffix='.log')
    subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-filter_complex',
        f'[0:v]scale=320:-2,split=2[a][b];[b]trim=start_frame=1,setpts=PTS-STARTPTS[b1];[a][b1]ssim=stats_file={log}',
        '-f', 'null', '-'], check=True)
    vals = [float(m.group(1)) for line in open(log)
            if (m := re.search(r'All:([\d.]+)', line))]
    os.unlink(log)
    return vals

def fps_of(video):
    out = subprocess.run(['ffprobe', '-v', 'quiet', '-select_streams', 'v:0',
        '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', video],
        capture_output=True, text=True).stdout.strip()
    try:
        num, den = out.split('/')
        return float(num) / float(den)
    except Exception:
        return FPS_DEFAULT

def scan(video, outdir='/tmp/vidscan_ev', top=6):
    os.makedirs(outdir, exist_ok=True)
    name = os.path.basename(video)[:16]
    s = ssim_series(video)
    n = len(s)
    fps = fps_of(video)
    cuts = [k for k in range(n) if s[k] < 0.50]
    bounds = [-1] + cuts + [n]
    cands = []
    for bi in range(len(bounds) - 1):
        a, b = bounds[bi] + 1, bounds[bi + 1]
        seg = [(k, s[k]) for k in range(a, b)]
        if len(seg) < 8:
            continue
        vals = [v for _, v in seg]
        med = statistics.median(vals)
        if med < 0.95:
            continue  # unstable shot (pan/handheld) — too noisy to flag
        for k, v in seg:
            if 0.55 < v < 0.88 and all(abs(k - c) > 3 for c in cuts):
                nb = [s[j] for j in (k - 2, k - 1, k + 1, k + 2) if 0 <= j < n]
                if sum(x > med - 0.03 for x in nb) >= 2:  # neighbors normal = isolated jump
                    cands.append((med - v, k, v, med))
    cands.sort(reverse=True)
    print(f'\n== {name}: {n+1} frames, {len(cuts)} cuts, {len(cands)} candidates ==')
    for i, (sev, k, v, med) in enumerate(cands[:top]):
        t = k / fps
        print(f'  t={t:7.2f}s frame={k} ssim={v:.3f} shot_med={med:.3f}')
        out = f'{outdir}/{name}_w{i}_t{t:.1f}s.jpg'
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', video, '-vf',
            f"select='between(n\\,{k-1}\\,{k+2})',scale=-2:480,tile=4x1",
            '-vsync', '0', '-frames:v', '1', out], check=True)
    return cands

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for v in sys.argv[1:]:
        scan(v)
