# Machinic Reality Inspire

**https://machinic.reality.design**

What is it like to be a machine? A bilingual (English / 中文) gallery of the most salient **artworks, robot art, performances, films, speculative design, research prototypes and theory that reflect on AI and machines**, read through **machine phenomenology**: how machines perceive, move, "feel", care, fail and die, and how we live with, work for, grieve through and are classified by them. Works that merely use AI to generate images are left out. Built by [Reality Design Lab](https://reality.design) as idea material for artists, designers, researchers and students; a sibling of [More than Human Inspire](https://more-than-human.reality.design) and [Reality Design Inspire](https://inspire.reality.design).

## What's inside

- **Atlas**: the ten fields and their sub-categories at a glance, the twelve lenses, and collections.
- **Ten field views**, each grouped by sub-category:
  - Machine Perception: seeing machines & operational images, listening machines & voice, datasets & labels, faces & biometrics, adversarial seeing & evasion.
  - Machine Bodies & Behaviour: cybernetic creatures, artificial life & collectives, industrial arms & choreography, androids & the uncanny, robotic sculpture, misbehaving machines, soft & "living" machines.
  - Machine Interiority: machine affect, dreams & latent space, artificial minds & agency, machine umwelt, machine-to-machine worlds, machine time.
  - Intimacy, Care & Companionship: smart home & humans as algorithms, companion robots, care & parenting machines, love & attachment, chatbots.
  - Memory, Death & Afterlives: griefbots, algorithmic kin, machine death, voice & likeness, sacred & ritual machines.
  - Labour & Infrastructure: ghost work, automation & the worker's body, planetary materials, military AI.
  - Classification, Power & Justice: bias & the coded gaze, surveillance & prediction, counter-datasets, feminist, decolonial & Indigenous AI.
  - Co-performance & Hybrid Bodies: cyborgs & prostheses, telepresence, dance, theatre, music, co-drawing.
  - Speculative & Critical Design: speculative robots, counter-devices, AI futures & worldbuilding, machines as design material.
  - Theory & Foundations: cybernetics & early AI, machine phenomenology, critical AI studies, robotics & HRI, art & media theory.
- **All works**: filter by field, machine (robot arm, android, vision system, chatbot, dataset, infrastructure…), lens (machine seeing, embodiment, intimacy & care, grief & afterlife, hidden labour, classification, failure…), type, collection and era; full-text search.
- **Collections**: landmark exhibitions (Cybernetic Serendipity, AI: More than Human, Uncanny Valley, Training Humans…), awards (Prix Ars Electronica, VIDA, S+T+ARTS…) and archives (the Machine Vision database).
- **Resources & Links**: the key artists, theorists, curators and engineers of the field, and the museums, festivals, awards, labs, archives, journals and networks where it happens.
- **Papers**, **Creators**, **Starred** (export as `SKILL.md`, `README.md` or a reading list with DOIs).

## For AI assistants

- [`llms.txt`](llms.txt): index
- [`catalog.md`](catalog.md) / [`catalog.zh.md`](catalog.zh.md): full catalog in English / Chinese
- [`data/entries.json`](data/entries.json): raw data

## Maintain it with AI

Open this folder in [Claude Code](https://claude.com/claude-code) and run:

```text
/add-work Lauren Lee McCarthy
/add-work https://www.jiabaoli.org/aimom
/add-work https://doi.org/10.1145/3313831.3376301
```

`/add-work` (in [`.claude/commands/`](.claude/commands/)) researches the artist, work or paper, adds every salient machine-related work in both languages with verified video / image / paper links, rebuilds and publishes. The inclusion rule and research rules are in [`data/RESEARCH_BRIEF.md`](data/RESEARCH_BRIEF.md), the data format in [`data/SCHEMA.md`](data/SCHEMA.md), the Resources tab brief in [`data/RESOURCES_BRIEF.md`](data/RESOURCES_BRIEF.md).

| Script | Purpose |
|---|---|
| `python3 tools/check_media.py <url>…` / `--doi` / `--arxiv` / `--og <page>` | Check videos, images, DOIs and arXiv ids; list image candidates on a page |
| `python3 tools/validate.py data/raw/<file>.json` (or `--all`) | Check a batch: bilingual fields, taxonomy ids (field, sub, machines, lenses), duplicates |
| `python3 tools/validate_orgs.py --all` | Check the Resources & Links records |
| `python3 tools/build_data.py [--recheck]` | Merge batches, verify every link, write `data/entries.*`, catalogs and `llms.txt` |
| `python3 tools/audit_titles.py` | List same-title works across batches (possible duplicates) |
| `tools/publish.sh "<message>"` | Validate all, rebuild, refuse on errors or unexpected removals, commit and push |

## Run locally

```bash
./serve.sh   # rebuilds data/ and serves http://localhost:8932
```

## Data layout

| Path | Contents |
|---|---|
| `data/taxonomy.json` | Fields and sub-categories, machines, lenses, work types, collections, disciplines, resource types |
| `data/raw/*.json` | Research batches: creators, works, leads |
| `data/orgs/*.json` | Resources & Links: people, institutions, websites |
| `data/collections/*.json` | Extra members of a collection (lists of work ids); `defs/` adds collections |
| `data/lens/*.json`, `data/discipline/*.json` | Optional re-classification passes (override lenses / disciplines) |
| `data/entries.json`, `data/entries.js` | Built dataset used by the site |
| `data/media_cache.json`, `data/dropped.json` | Link-check results; dead links and DOI/title mismatches |
| `data/leads.json` | People and works found but not yet researched |

## Credits

Images and videos are linked from the artists, museums, labs and publishers and remain theirs. To suggest a correction or an addition, please open an issue.

---

# Machinic Reality Inspire（中文）

**https://machinic.reality.design**

成为一台机器，是什么感觉？这是一个中英双语作品库，收录**反思 AI 与机器**的代表性艺术作品、机器人艺术、表演、影像、思辨设计、研究原型与理论，以**机器现象学**为线索：机器如何感知、行动、“感受”、照护、失败与死去，我们又如何与机器共处、为机器劳动、借机器哀悼、被机器分类。只用 AI 生成图像的作品不收录。由 [Reality Design Lab](https://reality.design) 整理，是 [More than Human Inspire](https://more-than-human.reality.design) 与 [Reality Design Inspire](https://inspire.reality.design) 的姊妹站。

- **总览**：十个领域及其子类、十二种视角与各个合集。
- **十个领域页**：机器感知；机器身体与行为；机器的内在；亲密、照护与陪伴；记忆、死亡与数字来世；劳动与基础设施；分类、权力与正义；人机共演与混成身体；思辨与批判设计；理论与奠基。
- **全部作品**：按领域、机器、视角、类型、合集和年代筛选，支持全文搜索。
- **合集**：标志性展览、奖项与档案库。
- **资源与链接**：这个领域的关键艺术家、理论家、策展人与工程师，以及美术馆、艺术节、奖项、实验室、档案、期刊与网络。
- **论文**、**创作者**、**收藏**（可导出 `SKILL.md`、`README.md` 或附 DOI 的阅读清单）。

在 Claude Code 中打开本仓库，输入 `/add-work <名字、作品链接或 DOI>` 即可让 AI 调研并添加新作品。本地运行：`./serve.sh`。

图片与视频版权归原作者、美术馆、实验室和出版方所有。如需更正或补充，欢迎提交 issue。
