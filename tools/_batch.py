import os, glob, subprocess, mlx_whisper, traceback

os.chdir('/Users/working/Desktop/Ads/videos')
os.makedirs('sheets', exist_ok=True)
os.makedirs('txt', exist_ok=True)
MODEL = 'mlx-community/whisper-large-v3-turbo'

def has_audio(f):
    out = subprocess.run(['ffprobe','-v','error','-select_streams','a',
        '-show_entries','stream=codec_type','-of','csv=p=0', f],
        capture_output=True, text=True).stdout.strip()
    return bool(out)

files = sorted(glob.glob('*.mp4'))
for i, f in enumerate(files, 1):
    base = f[:-4]
    sheet = f'sheets/{base}.jpg'
    txt = f'txt/{base}.txt'
    try:
        dur = float(subprocess.check_output(
            ['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0', f]).strip())
        # dense contact sheet: 30 frames, 5 cols x 6 rows — always regenerate
        rate = max(0.1, 30/dur)
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i', f,
            '-vf', f'fps={rate},scale=240:-1,tile=5x6','-frames:v','1', sheet], check=True)
        # transcribe (skip if no audio or already done)
        if not os.path.exists(txt):
            if has_audio(f):
                r = mlx_whisper.transcribe(f, path_or_hf_repo=MODEL)
                lines = [f"[{s['start']:.1f}-{s['end']:.1f}] {s['text'].strip()}" for s in r['segments']]
                open(txt,'w').write('\n'.join(lines))
            else:
                open(txt,'w').write('[NO AUDIO]')
        print(f'[{i}/{len(files)}] OK {base}', flush=True)
    except Exception as e:
        print(f'[{i}/{len(files)}] FAIL {base}: {e}', flush=True)
        traceback.print_exc()

print('ALL_DONE', flush=True)
