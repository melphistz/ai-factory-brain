# Mode 2B — 6-Panel Character Sheet, full grammar (legacy, explicit request only)

Full reference for SKILL.md Mode 2B. Pointed to from SKILL.md — see the inline note there. **Legacy, explicit request only** — starves face resolution vs the 3-panel default (Mode 2A). Never propose this format.

---

## MODE 2B — 6-PANEL CHARACTER SHEET (LEGACY, EXPLICIT REQUEST ONLY)

**Never propose this format.** It only runs when the user names it.

**When the user asks for a 6-panel, say this once, then wait:**

> Heads up — splitting into six panels cuts the pixel budget per cell, so the face panels will hold noticeably less identity detail than the 3-panel sheet's chest-up lock. The face is usually the whole point of the sheet, so the 3-panel holds up better as a downstream anchor. Happy to run the 6-panel anyway if you want it — just say go.

If the user says go, build it. Don't re-litigate, don't repeat the warning later in the session.

**When to use:** Only after a single-image base reference has been generated and approved. The 6-panel uses the locked outfit from the base and shows the same character from multiple angles in one image.

**Critical:** Never deliver six separate prompts. Always one prompt → one 16:9 image → six panels in a 3×2 grid.

**Goal:** A single multi-angle reference asset showing the same character from multiple angles, framings, and detail focuses, all generated in one frame so identity is maximally consistent across the panels.

**Canonical 6-panel layout (3×2 grid, top row left-to-right, bottom row left-to-right):**

1. **Top-left — Full body front:** straight-on neutral stance, full styling readable head-to-boots
2. **Top-center — Side profile close headshot (left side):** tight crop from collarbone up, character's left profile facing screen-right, hair detail, ear and earring detail, jaw and chin geometry readable
3. **Top-right — Full body back:** straight back view, showing hair fall, garment drape, accessory details from behind, footwear from behind
4. **Bottom-left — Side profile close headshot (right side):** tight crop from collarbone up, character's right profile facing screen-left, mirror of Panel 2 from the opposite side
5. **Bottom-center — Front face close headshot:** tight crop from collarbone up, body squared to camera, face filling the frame, eyes to camera, skin texture and facial structure readable
6. **Bottom-right — Detail shot:** ONE locked detail close-up — nails (with ring stack if relevant), key jewelry piece (necklace clasp, earring detail, signature ring), a piercing close-up, a tattoo close-up, OR a held prop (the prop fills the frame with the hand). User picks which detail at the pre-prompt check.

**Variation rule:** If the user requests a different mix of panels (e.g., back of head showing hair clip, midriff close-up showing piercing, boot detail), swap them in by name but keep the 3×2 grid and the single-prompt format. The default layout above is what gets used if the user doesn't specify.

**Frame and composition:**
- Layout: 3×2 grid, equal cells, thin clean white gutters between panels, horizontal sheet orientation
- Each panel composed within its cell as if it were its own shot — no cell should feel like a crop of a wider frame
- Background: same studio backdrop across all six cells (default mid-gray seamless, matching the base reference) for consistency. Only swap to white-across-all-six-panels if the user explicitly asks for a white sheet (see the "18% GRAY SEAMLESS + FLAT GRADE" section in SKILL.md).
- Lighting: flat and shadowless, uniform across all six cells — identity stays locked when lighting is locked
- Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI (typically 16:9 for sheets, but specified in UI not prompt)

**Canonical Mode 2 prompt structure:**

```
A 6-panel character reference sheet arranged as a 3-column by 2-row grid in a single horizontal frame, separated by thin clean white gutters between panels. Each panel shows the same single character — [full visual descriptor of the character including build, face, hair, makeup, full wardrobe head-to-toe, all accessories, jewelry, body markers, held props].

Panel 1 (top-left): Full body front — [stance description, framing, what's readable].
Panel 2 (top-center): Side profile close headshot, left side — [tight crop from collarbone up, character's left profile facing screen-right, hair and ear and jaw geometry visible].
Panel 3 (top-right): Full body back — [stance, what's visible from behind].
Panel 4 (bottom-left): Side profile close headshot, right side — [tight crop from collarbone up, character's right profile facing screen-left, mirror of Panel 2].
Panel 5 (bottom-center): Front face close headshot — [tight crop from collarbone up, body squared to camera, face filling the frame, eyes to camera].
Panel 6 (bottom-right): Detail shot — [the locked detail close-up: nails / specific jewelry piece / piercing / tattoo / held prop, filling the panel cleanly].

Close with the LOCKED FLAT GRADE — full canonical paragraph in references/flat-grade-close.md; paste it verbatim into the delivered prompt, adapted per the sheet-panel note in that file (flat value, shadowless light, and zero cast shadow stated as applying uniformly across all six panels, plus identical character identity locked across all six panels — same face, same skin, same hair, same wardrobe, same accessories, same proportions in every cell).

[Gray is the locked default — use the flat grade above. If the user explicitly asks for a white sheet, swap to "Pure white seamless studio backdrop applied uniformly across all six panels" and keep every flat/shadowless clause exactly as written. Flatness never comes off.]
```

**Critical rules for the 6-panel format:**
- One prompt, one fenced code block, one image output. Never deliver six separate prompts when the user asks for a character sheet.
- Identity description (build, face, hair, wardrobe, accessories) lives in the opening paragraph — described once, applies to all six panels.
- Each panel only describes what's *different* from the locked identity — stance, angle, framing, focus.
- Aspect ratio is set in the Higgsfield UI by the user, never written into the prompt.
- Lighting and backdrop are always uniform across all six cells.
- Every panel must include the explicit panel position label ("Panel 1 (top-left)", etc.) so Banana Pro can compose the grid correctly.
