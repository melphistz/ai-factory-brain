---
name: veo-google-flow-knowledge
description: "Veo / Google Flow knowledge — talking-head UGC \"Universal Master Prompt\" (exhaustive bracketed lock tags from a reference image → Thai-speaking avatar). SEPARATE model from our Seedance pipeline."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20a72bde-5cc0-43ba-90da-e06fffdbe0d2
---

Knowledge for **Veo (Google Flow)** — a DIFFERENT video model from FF factory's [[seedance-knowledge]] pipeline (Higgsfield/Seedance 2.0 + Wan). Not our current tool; kept for reference / if we ever A/B Veo. The identity-lock idea overlaps [[seedance-2-pro-director-skill]] (positive locks) + [[ai-character-identity-lock]] + [[seedance-ugc-repository]] — the tag structure is adaptable to Seedance.

Source: "สำนัก AI by Preecha Thongon" (FB aihubbypreecha), Google Doc "แบบที่1 ไม่มีสินค้า / Universal Master Prompt Level 1 (no product)".

## Net-new rules worth stealing (even for Seedance)
- **VO pacing: finish speaking within 5–6s of an 8s clip** (leave tail so it doesn't get cut).
- **Thai speech block**: tone `confident / energetic / engaging`, medium-fast, natural Thai conversational rhythm, perfect Thai lip sync, natural mouth movement + blinking; avoid `sleepy / monotone / robotic`.
- **"The final frame must match the first frame"** — explicit temporal-lock cue.
- Approach = exhaustive **bracketed positive-lock tags** from one reference image (talking-head UGC). Generic quality tags at the end (`Ultra realistic, Photorealistic, High detail`) are weak/AI-tell for stills per [[ai-influencer-image-prompt]] — fine-ish for video, but prefer specific realism levers.

## Full template (Veo / Google Flow — build a person/model image first, upload as reference, then paste)
```
Use the uploaded reference image as the single source of truth.
[CHARACTER_LOCK]
Maintain 100% consistency of: facial structure, face proportions, eye shape, eyebrow shape, nose shape, lips shape, skin texture, hairstyle, hair color, age appearance, ethnicity.
Do not redesign, beautify, stylize, or alter identity. The character must remain visually identical to the reference image throughout the entire video.
[BODY_LOCK]
Preserve: body shape, body proportions, posture, shoulder width, arm proportions, hand characteristics. No body morphing. No character replacement. No identity drift.
[OUTFIT_LOCK]
Preserve exactly: clothing, colors, fabrics, accessories, uniforms, jewelry, bags, hats, shoes. Do not change wardrobe. No outfit replacement. No color changes. No accessory changes.
[ENVIRONMENT_LOCK]
Preserve the original environment from the reference image. Maintain: location, architecture, furniture, objects, background elements, lighting sources. Do not redesign the environment.
[ATMOSPHERE_LOCK]
Maintain identical: lighting, shadows, reflections, color grading, mood, atmosphere. Preserve the visual feeling of the original image.
[IDENTITY_PERSISTENCE]
Maintain the exact same person throughout the entire video. No identity drift. No face morphing. No facial reconstruction. No age changes. No hairstyle changes. The final frame must match the first frame.
[FRAME_CONSISTENCY]
Maintain frame-to-frame consistency. No sudden changes in: face, clothing, hairstyle, body proportions, accessories, environment. Every frame must match the previous frame.
[TEMPORAL_LOCK]
Maintain temporal consistency throughout the entire video. The character must remain unchanged from beginning to end. No visual drift. No character regeneration. No outfit replacement.
[CAMERA_LOCK]
Camera: realistic, cinematic, natural perspective, stable framing, smooth movement. No fisheye. No distortion. No sudden zooms.
[ACTION]
The character speaks directly to the camera. Stable posture. Minimal movement. Natural body language. Maintain eye contact. Friendly confident expression.
[SPEECH]
The character speaks naturally in Thai. "ใส่บทพูดของเราตรงนี้"
Speaking pace: medium-fast. Clear pronunciation. Natural Thai conversational rhythm.
Voice tone: confident, energetic, engaging. Avoid: sleepy tone, monotone voice, robotic delivery.
Perfect Thai lip sync. Natural mouth movement. Natural facial expressions. Natural blinking. Finish speaking within the first 5-6 seconds.
[QUALITY]
Ultra realistic. Photorealistic. Natural skin texture. Professional cinematography. Stable identity. Stable facial consistency. Stable outfit consistency. Stable environment consistency. High detail. 8-second video.
```
> Doc says "Level 1 / no product / no product-holding" → มี Level อื่น (มีสินค้า/ถือสินค้า) ที่ยังไม่ได้เก็บ.
