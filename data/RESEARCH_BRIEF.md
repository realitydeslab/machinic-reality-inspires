# Research brief (for every research agent)

Project: **Machinic Reality Inspire** — a bilingual (English / Simplified Chinese) gallery at machinic.reality.design
of the most salient **artworks, robot art, performances, films, speculative design, research prototypes and theory that
reflect on AI and machines**, made by Reality Design Lab as idea material for artists, designers, researchers and students.
The curatorial angle is **machine phenomenology**: how machines perceive, move, "feel", relate, fail and die; how humans
experience, live with, care through, grieve through, work for and are classified by machines.
Working dir: `/Users/amber/Projects/Oxford/machinic-reality-inspires`.

Read first: `data/SCHEMA.md` (JSON format, language rule) and `data/taxonomy.json` (fields / subs / machines / lenses /
kinds / collections / disciplines). Background research: `plan/categories-curatorial.md`, `plan/categories-theory.md`,
`plan/categories-embodied.md` (candidate works per category, with facts already checked).

## Inclusion rule (strict)
- IN: works whose subject is **the machine itself or our relation to it** — machine perception, machine bodies,
  machine interiority, intimacy/care, grief/afterlife, hidden labour/infrastructure, classification/power, failure;
  robot and cybernetic art from the 1940s on; critical/speculative design; landmark HCI/robotics research and theory.
- OUT: works that simply **use** AI (GAN, diffusion, LLM) to generate images, music or text without reflecting on the
  machine — "AI-generated art" as such, NFT drops, style-transfer showpieces, immersive data-painting shows.
  If in doubt, ask: *does the work make you experience or think about what the machine is / does / hides?*
- **Salience over volume.** Prefer works that are canonical (exhibited at major museums/festivals, awarded, discussed in
  the literature) or unusually sharp. Better 40 strong works than 100 average ones. For each key artist, add their
  2–6 most important machine-related works, not everything they made.
- Balance: include East Asian (Chinese, Japanese, Korean, Taiwanese), Global South, women and queer practices; the
  Chinese audience of the gallery should find Chinese-language practices well represented.

## Every work
- Bilingual text, a correct classification (`field`, `sub`, 1–3 `machines`, 1–3 `lenses`, `kind`), and as many of:
  **video** (YouTube / Vimeo / mp4, prefer the artist's or museum's upload), **images** (1–3 direct image URLs),
  **paper** (DOI / arXiv / publisher URL, with venue; for books: publisher page or DOI), `source_url` (artist or museum page).
- Aim for a visual on every artwork. Good image sources: the project page's `og:image`
  (`python3 tools/check_media.py --og <page>`), artist / museum / festival pages (Ars Electronica archive, HEK, ZKM,
  Barbican, Rhizome), Wikimedia Commons (`upload.wikimedia.org`). Avoid Instagram / Pinterest CDN links (they expire).
- Verify everything with `python3 tools/check_media.py` before writing it: videos and images (`<url>`), DOIs (`--doi`),
  arXiv ids (`--arxiv`). Keep only `"ok": true`. Check that a DOI's returned title really is the work — never guess.
- Year = year of first showing / publication. `exhibited`: 1–4 key shows / awards (free text).
- Add `collections` ids from `data/taxonomy.json` when a work was in that exhibition / won that award (only if verified).

## Writing
- `description`: 1–2 sentences, concrete: what it is and what happens (what the machine does, what the visitor experiences).
- `idea_en`: the one-line insight about machines a designer or artist should take away.
- `method`: how it works (machine, sensors, model, dataset, choreography), one sentence.
- Chinese versions natural, not word-for-word; use established Chinese titles/names where they exist (孙原 & 彭禹《没办法》).
- Plain, precise language. No hype ("groundbreaking", "revolutionary", "stunning").

## Output
- One file `data/raw/<your-batch>.json` (`"batch": "<your-batch>"`), creators + works + leads; split into
  `<your-batch>-2.json` if large.
- Creators get `disciplines` (1–2 of taxonomy.disciplines) and `name_zh` when they have a Chinese name.
- Before creating a creator, `grep -ril "<surname>" data/raw/` — parallel agents write too. If another batch has the
  creator, reuse the id (you may still add works in your scope; check the work is not already there).
  Creator ids: kebab-case of the name (`sun-yuan-peng-yu`, `lauren-lee-mccarthy`). Work id: `<first-creator-id>--<short-slug>`.
- Run `python3 tools/validate.py data/raw/<file>.json` until it prints ✓.
- `leads`: people / works you found but did not add (for the next round).
- Search: WebSearch / WebFetch and `curl`. If WebSearch fails, use curl on artist sites, Wikipedia API, Ars Electronica
  archive, YouTube/Vimeo oEmbed, Crossref, and sparingly `curl -s -A "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=<query>"`.
- Do NOT use the Chrome browser tools (shared). Scratch files: `temp/<your-batch>/` only.
- Do NOT touch files outside `data/raw/`, `data/collections/` (only if told) and `temp/<your-batch>/`.

## Report back (short)
File(s) written, number of creators and works (by field), how many have video / images / paper, notable gaps, top leads.
