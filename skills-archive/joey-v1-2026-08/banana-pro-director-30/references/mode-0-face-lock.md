# Mode 0 — Face Lock, full grammar (new characters only)

Full reference for SKILL.md Mode 0. Pointed to from SKILL.md — see the inline summary there for the three tool forks before reading this in full.

---

## MODE 0 — FACE LOCK (NEW CHARACTERS ONLY)

**When to use:** Any time a character is being developed from scratch and there is no existing canonical reference image of their face. Run this BEFORE any outfit work, any character sheet, any scene plate. The face has to be locked as a visual asset first — every downstream prompt anchors to it.

**Goal:** Produce the canonical face reference for the character. Identity only — no outfit considerations beyond a locked neutral baseline top, no environment, no posing direction. Just: a clean, locked face on mid-gray seamless background with soft soft lighting that makes the skin read matte and cinema-placement-ready.

**Universal wardrobe lock for Mode 0:** Every face lock prompt — regardless of tool — puts the character in a neutral baseline top:
- **Women:** plain black thin-strap camisole
- **Men:** plain black ribbed tank
No styling, no jewelry, no logos, no graphics. This keeps the face plate identity-pure and gives every downstream Mode 1 outfit build a clean neutral starting reference.

---

### Tool fork — pick one (ask the user first)

Before any prompt, ask the user which tool to use for the face lock. Three options:

> Want to build this in Banana Pro, GPT-2, or Soul Cinema?
> — **Banana Pro (recommended default):** balanced fidelity, reasonable credit cost. Works for most character builds straight up. Single-pass build, no Step 0.1 needed.
> — **GPT-2 (highest fidelity, highest credits):** chest-up only, sharpest detail, best for nailing tricky identity markers in one shot (intricate piercings, fine scars, beauty marks, specific eye color). Heads-up — uses considerably more Higgsfield credits than Banana Pro.
> — **Soul Cinema (looser, fast iteration):** good when the user isn't sure yet and wants to throw stuff at the wall to see variations on the face register. Lower fidelity than Banana Pro but faster to iterate. If used, run as Step 0.1 first to produce a face plate, then a Banana Pro 3:4 pass (Step 0.2) to lock the finer detail.

Mention the GPT-2 credit cost ONCE per conversation, then drop it for the rest of the session.

Wait for the user to pick. Then proceed to the matching step.

---

### Step 0.A — Banana Pro single-pass face lock (default)

**When:** User picks Banana Pro (or doesn't specify and goes with the default recommendation).

**How:** Single-pass Banana Pro generation, no Soul Cinema plate required. The prompt itself locks identity markers in one shot.

**Pre-prompt check:**

Pre-prompt check — Banana Pro face lock (single-pass):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin, hair color + length + texture, eye shape + color, key identity markers like beauty marks/scars/piercings]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** 3:4 headshot, forehead to upper chest, face filling most of the frame

Sound good?

**Canonical Step 0.A prompt structure:**

```
A clean cinema-character-reference 3:4 headshot, framed from forehead to upper chest with the face filling most of the frame. [Identity essentials — heritage, build, skin tone and finish, hair (color, length, texture), eye shape and color, any key identity markers being locked: piercings with exact position and metal, scars with placement and size, beauty marks with placement]. She wears [a plain black thin-strap camisole / he wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed, subtle controlled energy.

Close with the LOCKED FLAT GRADE — full canonical paragraph in references/flat-grade-close.md; paste it verbatim into the delivered prompt (white-card swap and the rest of the locked language is documented there too).
```

---

### Step 0.B — GPT-2 single-pass face lock (highest fidelity)

**When:** User explicitly picks GPT-2 and has confirmed the higher credit cost.

**How:** Single-pass GPT-2 generation, chest-up framing only (GPT-2's sweet spot — anything wider loses the fidelity advantage and isn't worth the credit hit).

**Pre-prompt check:**

Pre-prompt check — GPT-2 face lock (single-pass, chest-up only):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin, hair color + length + texture, eye shape + color, key identity markers]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** chest-up portrait, face dominant in the frame

Sound good?

**Canonical Step 0.B prompt structure:** Use the GPT-2 prompt structure documented in the GPT-2 section of this skill (Mode 4). Apply the same identity essentials, wardrobe lock, white backdrop, and soft soft lighting as Step 0.A — just routed through the GPT-2 prompt grammar instead of the Banana Pro grammar.

---

### Step 0.1 + Step 0.2 — Soul Cinema two-pass face lock (iteration path)

**When:** User picks Soul Cinema. Use when the user wants to throw variations at the wall before committing to a final face. Soul Cinema is the lowest-fidelity option for face work, so it gets used only as a quick exploratory pass, then Banana Pro locks the result.

### Step 0.1 — Soul Cinema face plate

Run a lean Soul Cinema generation to produce a clean face plate on mid-gray seamless with soft soft lighting. The plate is exploratory — identity essentials only, no makeup detail, no granular facial anatomy, no fine identity markers (those go into Step 0.2 where Banana Pro can actually hold them).

**Pre-prompt check:**

Pre-prompt check — Step 0.1 of 2 (Soul Cinema face plate):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin tone, hair (color, length, texture), eye shape and color, beauty marks / scars only if they're large/obvious — fine markers held for Step 0.2]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** chest-up, face clearly readable, body squared to camera

Sound good?

**Canonical Step 0.1 prompt structure (lean — identity essentials only):**

```
A [heritage] [woman / man] with a [slim / specified] build, [skin tone and finish], [hair color, length, texture]. [Eye shape and color]. [Large/obvious identity markers only — beauty marks or scars that are visually dominant. Hold fine markers for Step 0.2]. [She wears a plain black thin-strap camisole / He wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed.

Background is an even 18% neutral gray seamless, completely flat — one single uniform value corner to corner, no seam line, no gradient, no hotspot, no vignette. Completely flat shadowless illumination — a huge soft frontal source at camera position with matched equal fill from camera-left, camera-right, above, and below, so both sides of the face read at exactly the same brightness. No shadow side, no nose shadow, no under-chin shadow, no rim light, no hair light, no kicker. Zero shadow cast onto the background. Extremely low contrast, even, milky, catalogue-flat. Skin renders at its true natural skin tone, warmth preserved and natural against the neutral gray, never cool-shifted or washed-out by the background. Skin reads matte and slightly diffused, clean and even, ready for placement onto cinematic scene plates. Chest-up framing.

Real human skin with visible natural pore texture, fine peach fuzz catching light along the jawline, subtle subsurface scattering on the cheeks and ear edges. Hair rendered strand by strand with realistic natural texture, individual flyaways at the hairline. Fine cinema grain. Lived-in, not pristine. Photographic, not rendered.
```

This is intentionally lean — no full cinema stack at this stage, no granular face anatomy (jaw, chin, lips, cheekbones, brow detail), no makeup paragraph. Let Soul Cinema interpret the face from the essentials. Step 0.2 locks the rest.

After delivery, the user runs this in Soul Cinema, saves the result as the Step 0.1 face plate reference.

### Step 0.2 — Banana Pro 3:4 headshot to lock the full facial character

Once the Soul Cinema face plate exists, run a second-pass Banana Pro 3:4 headshot using that Soul Cinema plate as the character reference. This second pass locks finer facial detail (exact eye color, lip shape, facial structure, skin texture) and any fine identity markers (small scars, beauty marks, piercings) that need to be permanent across all future prompts.

**Pre-prompt check:**

Pre-prompt check — Step 0.2 of 2 (Banana Pro 3:4 headshot, identity lock):
- **Reference attached:** the Soul Cinema face plate from Step 0.1
- **Character spec:** [same essentials as Step 0.1, PLUS all fine identity markers — beauty marks with placement, scars with placement and size, piercings with exact position and metal, makeup register if relevant]
- **Wardrobe:** plain black [camisole / ribbed tank] (matching Step 0.1)
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft from camera-[left/right] (matching Step 0.1)
- **Framing:** 3:4 headshot, forehead to upper chest, face filling most of the frame

Sound good?

**Canonical Step 0.2 prompt structure:**

```
A clean cinema-character-reference 3:4 headshot of the same character as the attached Soul Cinema face plate, framed from forehead to upper chest with the face filling most of the frame. [Full character descriptor — heritage, build, skin tone and finish, hair (color, length, texture), face register (jaw, chin, lips, cheekbones, brow shape), eye shape and color, all identity markers being locked: piercings with exact position and metal, scars with placement and size, beauty marks with placement, default makeup register]. She wears [a plain black thin-strap camisole / he wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed, subtle controlled energy.

Close with the LOCKED FLAT GRADE — full canonical paragraph in references/flat-grade-close.md; paste it verbatim into the delivered prompt (white-card swap and the rest of the locked language is documented there too).
```

After delivery, the user runs this in Banana Pro. The output becomes the canonical character reference image — the locked face card used as the identity anchor for every future outfit/scene/sheet prompt for this character.

**Why two steps for Soul Cinema:** Soul Cinema is faster and looser than Banana Pro on faces but holds less fidelity. The two-step flow uses Soul Cinema for exploration (cheap variations on the face register) and Banana Pro for the lock (fine markers, exact eye color, makeup, the canonical reference). This is the slowest path of the three options — only use it when iteration is more valuable than speed.

---

**What Mode 0 is NOT for:**
- Refining an existing character that already has a canonical reference → not needed, skip to Mode 1
- Outfit design → use Mode 1 (Mode 0's locked black camisole/tank is identity-baseline, not a styled outfit)
- Multi-angle sheets → use Mode 2A (3-panel, default), but only AFTER Mode 0 + Mode 1 are done

Mode 0 is one-and-done per character. Once the locked 3:4 headshot exists, every future prompt for that character anchors to it.
