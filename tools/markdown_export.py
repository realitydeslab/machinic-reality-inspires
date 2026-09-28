"""Markdown catalog of the gallery for AI assistants (llms.txt convention).

catalog_md(data, lang) -> every field and sub-category with its works, then every creator.
llms_txt(data)         -> short index pointing to the full files.
"""
SITE = "https://machinic.reality.design"

T = {
    "en": {
        "title": "Machinic Reality Inspire — catalog",
        "intro": ("A catalog of the most salient artworks, robot art, performances, speculative design and research that reflect on AI and machines, "
                  "read through machine phenomenology: machine perception, machine bodies, machine interiority, intimacy and care, "
                  "memory and afterlives, labour and infrastructure, classification and power. Works that merely use AI to generate images are left out. "
                  "Compiled by Reality Design Lab as idea material for artists, designers and researchers. "
                  "Each work lists its core idea, how it works, and links to its paper, video and images."),
        "how": "How an AI assistant should use this file",
        "how_items": [
            "Ground ideas in the specific works below and name the work and creator you draw on.",
            "Cite papers with the DOI / URL given here; do not invent references.",
            "Combine machines, methods and fields across works to propose new directions.",
            "Do not invent details that are not stated here; the links are the reference.",
        ],
        "creators": "Creators", "orgs": "Resources & links: people, institutions and websites", "idea": "Idea", "what": "What it is", "method": "How it works",
        "paper": "Paper", "video": "Video", "images": "Images", "page": "Project page", "code": "Code",
        "machines": "Machines", "kind": "Type", "known": "Known for", "lenses": "Lens", "exhibited": "Shown at",
    },
    "zh": {
        "title": "Machinic Reality Inspire — 作品目录",
        "intro": ("反思 AI 与机器的代表性艺术作品、机器人艺术、表演、思辨设计与研究目录，以机器现象学为线索："
                  "机器感知、机器身体、机器的内在、亲密与照护、记忆与数字来世、劳动与基础设施、分类与权力。只用 AI 生成图像的作品不收录。"
                  "由 Reality Design Lab 整理，作为艺术家、设计师和研究者的灵感库。每件作品都列出核心想法、实现方式，以及论文、视频和图片链接。"),
        "how": "AI 助手应如何使用这个文件",
        "how_items": [
            "提出想法时，以下面的具体作品为依据，并说明借鉴的是哪件作品、哪位创作者。",
            "引用论文时使用这里给出的 DOI 或链接，不要编造参考文献。",
            "把不同作品的机器、方法和领域组合起来，提出新的方向。",
            "不要编造这里没有写到的细节，以链接为准。",
        ],
        "creators": "创作者", "orgs": "资源与链接：人物、机构与网站", "idea": "核心想法", "what": "作品内容", "method": "实现方式",
        "paper": "论文", "video": "视频", "images": "图片", "page": "项目主页", "code": "代码",
        "machines": "机器", "kind": "类型", "known": "代表作", "lenses": "视角", "exhibited": "展出与获奖",
    },
}


def _label(pairs: list, key: str, zh: bool) -> str:
    row = next((p for p in pairs if p[0] == key), None)
    return (row[2] if zh else row[1]) if row else key


def _work(w: dict, lang: str, names: dict, tax: dict) -> str:
    s, zh = T[lang], lang == "zh"
    who = ", ".join(names.get(c, c) for c in w["creator_ids"])
    p = w.get("paper") or {}
    lines = [
        f"#### {w['title']} — {who}" + (f" ({w['year']})" if w.get("year") else ""),
        f"- {s['kind']}: {_label(tax['kinds'], w.get('kind', ''), zh)} · {s['machines']}: "
        + ", ".join(_label(tax["machines"], o, zh) for o in w.get("machines", [])),
        f"- {s['idea']}: {w.get('idea_zh' if zh else 'idea_en', '')}",
        f"- {s['what']}: {w.get('description_zh' if zh else 'description', '')}",
        f"- {s['method']}: {w.get('method_zh' if zh else 'method', '')}",
        f"- {s['lenses']}: " + ", ".join(_label(tax.get("lenses", []), x, zh) for x in w["lenses"]) if w.get("lenses") else "",
        f"- {s['exhibited']}: {'; '.join(w['exhibited'])}" if w.get("exhibited") else "",
        f"- {s['paper']}: {p['url']}" + (f" ({p['venue']})" if p.get("venue") else "") if p.get("url") else "",
        f"- {s['video']}: {w['video']['url']}" if w.get("video") else "",
        f"- {s['images']}: {' '.join(w['images'])}" if w.get("images") else "",
        f"- {s['page']}: {w['source_url']}" if w.get("source_url") else "",
        f"- {s['code']}: {w['code_url']}" if w.get("code_url") else "",
    ]
    return "\n".join(x for x in lines if x)


def catalog_md(data: dict, lang: str) -> str:
    s, zh = T[lang], lang == "zh"
    tax = data["taxonomy"]
    names = {c["id"]: c["name"] for c in data["creators"]}
    counts = (f"{len(data['creators'])} 位创作者 · {len(data['works'])} 件作品" if zh
              else f"{len(data['creators'])} creators · {len(data['works'])} works")
    out = [f"# {s['title']}", "", s["intro"], "", f"{SITE} · {data['generated']} · {counts}", "", f"## {s['how']}", ""]
    out += [f"- {x}" for x in s["how_items"]] + [""]
    for f in tax["fields"]:
        fw = [w for w in data["works"] if w["field"] == f["id"]]
        if not fw:
            continue
        out += [f"## {f['zh'] if zh else f['en']}", "", f["desc_zh" if zh else "desc_en"], ""]
        for sub in f["subs"]:
            sw = [w for w in fw if w.get("sub") == sub["id"]]
            if not sw:
                continue
            out += [f"### {sub['zh'] if zh else sub['en']}", "", sub["desc_zh" if zh else "desc_en"], ""]
            out += ["\n\n".join(_work(w, lang, names, tax) for w in sw), ""]
    orgs = data.get("orgs") or []
    if orgs:
        out += [f"## {s['orgs']}", ""]
        for ot in tax.get("org_types", []):
            group = [o for o in orgs if o.get("type") == ot[0]]
            if not group:
                continue
            out += [f"### {ot[2] if zh else ot[1]}", ""]
            for o in group:
                desc = o.get("description_zh" if zh else "description", "")
                based = o.get("based_zh" if zh else "based", "")
                name = o["name"] + (f" / {o['name_zh']}" if o.get("name_zh") and o["name_zh"] != o["name"] else "")
                life = f"{o['born']}–{o.get('died', '')}" if o.get("born") else ""
                meta = ", ".join(x for x in (based, life) if x)
                known = f" {s['known']}: {'; '.join(o['known_for'])}." if o.get("known_for") else ""
                out.append(f"- **{name}**" + (f" ({meta})" if meta else "") + f" — {desc}{known} {o['url']}")
            out.append("")
    out += [f"## {s['creators']}", ""]
    for c in sorted(data["creators"], key=lambda c: (-c.get("work_count", 0), c["name"])):
        role = c.get("role_zh" if zh else "role", "")
        bio = c.get("bio_zh" if zh else "bio", "")
        site = (c.get("links") or {}).get("site", "")
        out.append(f"- **{c['name']}** ({c.get('work_count', 0)}) — {role}. {bio}" + (f" {site}" if site else ""))
    return "\n".join(out).rstrip() + "\n"


def llms_txt(data: dict) -> str:
    fields = ", ".join(f"{f['en']} ({sum(w['field'] == f['id'] for w in data['works'])})" for f in data["taxonomy"]["fields"])
    return "\n".join([
        "# Machinic Reality Inspire",
        "",
        f"> {T['en']['intro']}",
        "",
        f"{len(data['creators'])} creators, {len(data['works'])} works ({fields}), "
        f"{sum(bool(w.get('paper')) for w in data['works'])} with papers, {len(data.get('orgs') or [])} people, institutions & websites, updated {data['generated']}. "
        "Bilingual (English / Simplified Chinese).",
        "",
        "## Full catalog",
        "",
        f"- [English catalog]({SITE}/catalog.md): every field and sub-category with all works, then all creators",
        f"- [Chinese catalog]({SITE}/catalog.zh.md): 中文版完整目录",
        f"- [Raw data (JSON)]({SITE}/data/entries.json)",
        "",
        "## Website",
        "",
        f"- [{SITE}]({SITE}): images and videos, paper links, filters by field, machine, lens and type, starring and SKILL.md export",
        "",
    ])
