---
name: youmind-prompt-pack
description: "Full GPT Image 2 prompts extracted from YouMind (verbatim, copy-paste ready) — editorial/UGC/product lane + {argument} template + restyle presets"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1700360a-211b-4395-855f-9773306fc7ed
---

# YouMind Prompt Pack — full copy-paste prompts (GPT Image 2)

> Prompt เต็ม verbatim ที่ curl-crack มาจาก [[youmind-gpt-image-prompt-library]] (วิธีดึงอยู่ในโน้ตนั้น).
> lane เรา: editorial portrait · product ad · UGC. ทุกอันใช้ `{argument name="x" default="y"}` = จุดสลับตัวแปร.
> เกี่ยว: [[ai-character-identity-lock]] · [[ai-influencer-image-prompt]] · [[image-prompt-suffixes-techniques]] · [[ai-ugc-ad-factory-workflow]]

---

## 1. Gen-Z Editorial Portrait ⭐ (identity-lock + full negative prompt) — best template
```
Using the uploaded face image, preserve the person's facial identity with absolute accuracy (100% identity preservation), maintaining the exact face shape, bone structure, forehead, eyebrows, eyes, nose, lips, ears, jawline, hairstyle, hairline, facial hair, skin tone, complexion, age, and natural expression without beautifying or altering the individual. Create an ultra-premium Gen-Z fashion editorial portrait of the same person seated casually on a perfectly cylindrical matte {argument name="furniture color" default="purple"} ottoman, leaning slightly forward with elbows resting naturally on the thighs and hands loosely clasped together, projecting effortless confidence and modern attitude while making direct eye contact with the camera. Dress the subject in an oversized luxury monochromatic {argument name="outfit color" default="purple"} trench coat layered over a matching purple crew-neck t-shirt, relaxed-fit white trousers, premium white and purple designer sneakers, and a sophisticated stainless steel wristwatch. Place the subject inside a seamless monochromatic purple studio where both the floor and background are the same rich matte purple with a clean {argument name="aesthetic style" default="minimalist"} aesthetic and no additional props or distractions. Illuminate the scene using high-end professional fashion studio lighting with a large softbox positioned slightly above and to camera left, complemented by subtle fill lighting and gentle cinematic shadows that sculpt the face while preserving realistic skin texture and premium fabric details. Capture the image in a perfectly balanced 4:5 vertical composition with the full body and shoes visible, centered framing, shot using an 85mm medium-format portrait lens with shallow depth of field, ultra-sharp focus, hyper-realistic skin pores, luxury editorial color grading, Apple-style minimalism, Vogue campaign quality, commercial advertising photography, HDR, photorealistic 8K resolution.
Negative prompt: different person, identity change, face swap, altered facial features, beautified face, different hairstyle, incorrect facial hair, asymmetrical face, distorted anatomy, extra fingers, missing fingers, duplicate limbs, bad hands, blurry image, low quality, low resolution, cartoon, anime, CGI, illustration, plastic skin, oversmoothed skin, fisheye lens, wide-angle distortion, cluttered background, text, watermark
```

## 2. Industrial Loft / Laundromat Editorial (multi-variable + magazine text layout)
```
Create a high-end fashion magazine editorial cover shot in a minimalist cold white-gray laundromat. The scene has clean white rectangular wall tiles, dark glossy industrial laundry machines with round chrome drum doors in the background, and a black metal vertical pole dividing the composition near the left third. The subject is a {argument name="model identity" default="young Asian woman"} seated casually on a dark worn laundry bench or machine ledge, leaning slightly forward with long voluminous {argument name="hair style" default="black natural loose wavy hair"}, pale refined makeup, delicate features, and a calm detached gaze with a faint lazy, tipsy, thoughtful mood. She wears narrow black sunglasses lowered slightly as she touches the frame with one hand, an oversized crisp white button-down shirt worn open, a light blue washed denim corset-style crop top, matching high-waisted denim shorts, and sheer black tights patterned with many small black X marks. Her pose is editorial and relaxed: one arm extends down toward the washer area, legs angled diagonally across the lower frame, torso turned toward camera. Use cool desaturated tones, sharp magazine photography, soft diffused studio lighting, subtle film grain, realistic skin texture, glossy metal reflections, and a polished yet industrial mood. Add a dark navy-black vertical typography panel along the far left edge occupying about one quarter of the image, with distressed oversized off-white vertical headline text reading {argument name="cover headline" default="COOLNESS"}. Include exactly three smaller text blocks on this panel: near the upper right, vertical microcopy reading {argument name="side quote" default="STYLE ISN'T LOUD — IT JUST DOESN'T NEED TO EXPLAIN"}; near the lower left, stacked text reading "WASHED IN SILENCE. WORN ON PURPOSE."; and below it, stacked issue text reading "SS / 24 EDITORIAL SERIES" with a short thin horizontal rule. Make the layout feel like a contemporary fashion magazine cover, 3:4
```

## 3. Tennis Club — 2-subject blocking (count-lock "exactly two women")
```
Create a realistic editorial fashion photograph of two stylish young women entering or leaving a tennis club through a dark metal gate at golden hour. The foreground woman has dark brunette hair in a loose messy bun with face-framing strands, slim black oval sunglasses, small hoop earrings, a fitted black short-sleeve polo shirt with a tiny white chest logo, a white tennis mini skirt, and holds a pink tennis racket down at her side. The second woman walks just behind her, with blonde hair in a relaxed ponytail, black cat-eye sunglasses, small gold hoop earrings, a delicate necklace, a cream cable-knit tennis sweater with pink striped V-neck cuffs and hem, a white tennis skirt, and a large cream tote bag over one shoulder. Show exactly two women, both mid-stride, confident and relaxed, with warm sun rim-lighting their hair and shoulders. The setting is an upscale tennis club entrance with a partially visible dark signboard on the left, black gate posts framing the image, blurred green tennis court and trees in the background, and a luxurious late-afternoon atmosphere. Use a vertical 3:4 composition, waist-to-thigh fashion framing, shallow depth of field, natural skin texture, warm cinematic color grading, high-end lifestyle magazine photography, no readable text emphasis, no extra people, no watermark.
```

## 4. Tropical Leaf — oversized prop as sculptural backdrop
```
Fashion editorial studio portrait of a young woman with long dark wavy hair sitting centered in front of one oversized tropical palm leaf used as a sculptural fan-shaped backdrop prop. The leaf fills almost the entire frame behind her, radiating outward from behind her body with strong visible ridges, veins, deep green color, and warm directional rim lighting that highlights the texture; a soft mustard-yellow studio background is visible only around the edges. She has a relaxed confident pose with arms crossed gently over her chest, one leg crossed in the foreground, head slightly tilted, and a soft warm smile while looking directly at the camera. She wears a sleeveless floral print mini dress in pink, coral, muted green, and black tones with a black tie-neck bow detail hanging down the front. Warm golden studio lighting, natural skin tones, subtle makeup, glossy editorial fashion photography, shallow depth of field, rich tropical color palette, clean composition, vertical 4:5 crop, no text, no watermark.
```

## 5. Golden-Hour Rooftop — male lifestyle streetwear (low angle, sky 70%)
```
Create a cinematic lifestyle portrait of a stylish young man sitting casually on the edge of a modern concrete rooftop during golden hour. The camera is positioned at a low angle, emphasizing the expansive sky while making the subject appear confident and effortlessly cool. The subject sits with one knee raised and the other leg hanging naturally. One hand rests casually on the raised knee while the other relaxes near his thigh. His head is turned to the right, gazing into the distance with a calm, thoughtful expression. His face is illuminated by warm late afternoon sunlight, creating soft highlights across the cheekbones and jawline. He has naturally messy, medium-length dark brown hair with textured volume and loose strands falling across the forehead. He wears an oversized beige crewneck sweatshirt with relaxed sleeves paired with loose black trousers, creating a clean minimalist streetwear look. The background features a deep blue cloudless sky occupying nearly seventy percent of the composition. A faint airplane contrail crosses the upper left corner. On the left side, a modern concrete building with [...truncated — tail = building/skyline detail]
```

## 6. Coquette Tea Room — feminine detail-heavy (count-lock "exactly 3 items")
```
Create a realistic, high-resolution fashion portrait of a cute young woman in a romantic vintage tea room, seated at a small round marble café table. She has dark brown long hair styled in twin low pigtails with wispy bangs, soft natural makeup, and a gentle playful smile while looking slightly to the side. Pose her sitting on an ornate wooden chair with patterned upholstery, raising one hand in a small wave and holding one pigtail with the other. Dress her in a soft feminine coquette outfit: a fluffy white faux-fur jacket with oversized fuzzy cuffs, a white lace-trim camisole with a tiny pink bow, and a pale pink high-waisted mini skirt with a corset-lace front. Add a pale pink shoulder bag with a gold chain strap hanging from the chair, decorated with one small white plush bunny charm. On the table place exactly 3 visible tea-time items: a delicate floral teacup and saucer, a white porcelain teapot, and a slice of strawberry shortcake on a floral plate with a fork. The background should show an elegant shabby-chic room with warm cream walls, antique wooden furniture, a gold-framed mirror, a framed portrait, a w[...truncated]
```

## 7. Blueberry Pop-Art Poster — 90s diner food/drink ad
```
Create a bold retro pop-art poster for a Blueberry Dessert Shake.
Use a thick blueberry shake in a transparent glass with dripping syrup, whipped cream swirl, blueberries, mint leaf, and a colorful straw.
Theme: 90s retro diner poster
Colors: bright magenta, electric blue, cream, purple, hot pink
Background: halftone dots, vintage paper texture, bold geometric shapes, sticker-style cutout behind the glass
Typography: huge stacked text saying "BLUEBERRY BLAST[...truncated]
```

## 8. Restyle presets (1-line, apply to reference photo) — เร็ว/ปรับลุค
```
Cinematic Drama — Transform the reference photo into a dramatic cinematic scene with high-contrast lighting, a moody atmosphere, controlled shadows, subtle lens flare, and a polished film still finish.
Golden Hour   — Change the reference photo into a warm golden-hour image with soft sunlight, long natural shadows, gentle glow, realistic skin tones, and an inviting outdoor photography mood.
Golden Light  — Transform the reference photo with golden rim lighting, cinematic depth, a warm atmospheric glow, subtle background drama, and a polished hero-shot look.
Minimalist    — Refine the reference photo into a clean minimalist composition with neutral colors, structured framing, intentional negative space, soft diffused light, and premium editorial simplicity.
Editorial Cut — Create an editorial version of the reference photo with a stronger crop, clean subject focus, magazine-grade contrast, refined color balance, and a premium visual direction.
Neon Portrait — Use the reference photo as the main subject. Add electric neon lighting, sharp contrast, saturated blue and gold accents, clean subject separation, and a bold campaign-style finish.
Urban Poster  — Turn the reference photo into a raw urban poster with concrete textures, heavy black borders, hard shadows, crisp realism, and an unapologetic graphic composition.
Action Motion — Convert the reference photo into a dynamic action visual with subtle motion lines, hard shadows, energetic composition, crisp subject clarity, and high-impact poster energy.
Product Hero  — Upgrade the reference product photo with heroic commercial lighting, punchy geometric composition, clean high-contrast styling, realistic reflections, and a campaign-ready finish.
Surreal       — Reimagine the reference photo as a surreal fantasy scene with dreamlike colors, floating abstract details, imaginative background elements, and a cohesive magical atmosphere.
```

## หมายเหตุ
- #5/#6/#7 ปลาย prompt ถูกตัด (chunk boundary) — โครงหลักครบพอใช้; อยากเต็ม re-curl หน้า detail
- pattern ที่เห็นซ้ำ: identity-lock clause → subject+pose → outfit → environment → lighting → lens/crop → **negative prompt** (ดู [[youmind-gpt-image-prompt-library]] §pattern)
