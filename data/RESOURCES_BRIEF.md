# Resources & Links brief (for every resources research agent)

The gallery at machinic.reality.design has a **Resources & Links** tab: the key PEOPLE of machinic / robot / critical AI
art (artists & designers, theorists & researchers, curators & critics, engineers & roboticists) and the INSTITUTIONS &
WEBSITES where the field happens (museums & art centres, festivals & exhibition series, awards, labs & research centres,
residencies & programmes, archives & databases, journals/books/podcasts/newsletters, networks & nonprofits).
Working dir: `/Users/amber/Projects/HoloKit/HoloKit2/machinic-inspire`.

Read first: `data/SCHEMA.md` → section **Resource**, `data/taxonomy.json` → `org_types`, `org_themes`, `fields`,
and `data/RESEARCH_BRIEF.md` → inclusion rule (reflection on machines, not AI-generated imagery).
Candidate names: `plan/categories-*.md` (leads sections).

## Goal: complete for the key figures, selective beyond them
- People: everyone a well-read curator would expect in a canon of machinic / robot / critical AI art, from the
  cybernetic pioneers (Grey Walter, Pask, Schöffer, Ihnatowicz, Paik) to today, including East Asian, Global South,
  women and queer practitioners; plus the theorists, curators and roboticists that shaped the field.
- Institutions & websites: every museum, festival, award, lab, residency, archive, publication and network that is a
  real reference point for this field (not every media-art venue in the world). Snowball through their "partners",
  "links", "network", "jury", "alumni" pages; directories and awesome-lists are gold (record `found_via`).
- One record per person / institution. Big institutions only as the relevant unit (e.g. "Ars Electronica Futurelab").
- `url` must load (`python3 tools/check_media.py --og <url>` also returns image candidates for `image`).
  People: personal or studio site; if none, Wikipedia. Add Wikipedia / gallery / interview in `links` (0–4).
- Bilingual `description` / `description_zh` (1–2 concrete sentences: who / what, and why it matters for machines).
  `name_zh` for people and institutions with a Chinese name. `known_for`: 2–4 key works or books for people.
- `creator_id`: if the person / org exists as a creator in the works data (`grep -ril "<name>" data/raw/`), put its id.
- `image`: prefer a representative photo (og:image) over a tiny logo; skip if none passes check_media.

## Output
- Your file only: `data/orgs/<your-batch>.json` (`{"batch": "...", "orgs": [...]}`); split into -2, -3 if large.
- Ids: people `person--<kebab-name>`, institutions `<kebab-name>`.
- Before adding, grep `data/orgs/*.json` for the name/url — parallel agents write too; do not duplicate.
- Validate: `python3 tools/validate_orgs.py data/orgs/<file>.json` until ✓.
- Search: WebSearch / WebFetch, curl, Wikipedia API; sparingly `curl -s -A "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=<query>"`.
- No Chrome browser tools. Scratch: `temp/res-<your-batch>/`.

## Report back (short)
File(s), number of records by type and theme, directories harvested, notable gaps, leads.
