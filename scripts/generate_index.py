#!/usr/bin/env python3
"""Scan top-level sample folders and build a static GitHub Pages site in _site/.

Convention for a "sample folder": a top-level directory containing at least
one *.html file. Title/description are parsed from its design.md (first
`# ` heading and the paragraph right after it) when present, falling back
to the folder name. No manual registration needed — add a folder following
this convention and it appears on the next Pages deploy.
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
EXCLUDE_DIRS = {".git", ".github", "scripts", "_site", "node_modules"}
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp")


def parse_design_md(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    title = None
    heading_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            heading_idx = i
            raw = line[2:].strip()
            if "—" in raw:
                raw = raw.split("—", 1)[1].strip()
            raw = re.sub(r"\s*\([^)]*\)\s*$", "", raw).strip()
            title = raw or None
            break

    description = ""
    if heading_idx is not None:
        desc_lines = []
        for line in lines[heading_idx + 1:]:
            stripped = line.strip()
            if not stripped:
                if desc_lines:
                    break
                continue
            if stripped.startswith("#"):
                break
            if stripped.startswith("출처") or stripped.startswith("Source"):
                continue
            desc_lines.append(stripped)
        description = re.sub(r"\*\*(.+?)\*\*", r"\1", " ".join(desc_lines))

    return title, description


def find_samples():
    samples = []
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith(".") or entry.name in EXCLUDE_DIRS:
            continue
        html_files = sorted(entry.glob("*.html"))
        if not html_files:
            continue

        title, description = None, ""
        design_md = entry / "design.md"
        if design_md.exists():
            title, description = parse_design_md(design_md)
        if not title:
            title = entry.name.replace("-", " ").replace("_", " ").title()

        images = sorted(p for p in entry.iterdir() if p.suffix.lower() in IMAGE_SUFFIXES)

        samples.append({
            "slug": entry.name,
            "title": title,
            "description": description,
            "html": html_files[0].name,
            "thumbnail": images[0].name if images else None,
            "hasSpec": design_md.exists(),
        })

    samples.sort(key=lambda s: s["title"].lower())
    return samples


INDEX_TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>designs — 샘플 모음</title>
<style>
  :root {{
    color-scheme: light dark;
    --bg: #f7f7f8;
    --card-bg: #ffffff;
    --text: #1a1a1e;
    --muted: #6b6b76;
    --border: #e4e4e8;
    --accent: #4f46e5;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #101014;
      --card-bg: #1a1a20;
      --text: #f0f0f2;
      --muted: #9a9aa4;
      --border: #2c2c34;
      --accent: #8b7ff0;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Pretendard, Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
  }}
  header {{
    max-width: 1100px;
    margin: 0 auto;
    padding: 48px 24px 16px;
  }}
  h1 {{ margin: 0 0 8px; font-size: 28px; }}
  .sub {{ color: var(--muted); margin: 0 0 24px; }}
  #search {{
    width: 100%;
    max-width: 420px;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: var(--card-bg);
    color: var(--text);
    font-size: 15px;
  }}
  #search:focus {{ outline: 2px solid var(--accent); outline-offset: 1px; }}
  main {{ max-width: 1100px; margin: 0 auto; padding: 8px 24px 64px; }}
  #count {{ color: var(--muted); font-size: 13px; margin: 0 0 16px; }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
  }}
  .card {{
    border: 1px solid var(--border);
    border-radius: 12px;
    background: var(--card-bg);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    text-decoration: none;
    color: inherit;
    transition: transform 0.12s ease, box-shadow 0.12s ease;
  }}
  .card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  }}
  .thumb {{
    width: 100%;
    aspect-ratio: 16/10;
    object-fit: cover;
    background: var(--border);
    display: block;
  }}
  .thumb.placeholder {{
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--muted);
    font-size: 13px;
  }}
  .body {{ padding: 14px 16px 16px; }}
  .title {{ font-weight: 600; font-size: 16px; margin: 0 0 6px; }}
  .desc {{
    color: var(--muted);
    font-size: 13px;
    margin: 0;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }}
  .slug {{ color: var(--muted); font-size: 11px; margin-top: 8px; font-family: monospace; }}
  #empty {{ display: none; color: var(--muted); padding: 32px 0; text-align: center; }}
  footer {{ max-width: 1100px; margin: 0 auto; padding: 0 24px 48px; color: var(--muted); font-size: 12px; }}
</style>
</head>
<body>
<header>
  <h1>designs</h1>
  <p class="sub">UI 디자인 시안 모음 — {count}개 샘플. 폴더를 추가하면 다음 배포 때 자동으로 반영됩니다.</p>
  <input id="search" type="search" placeholder="제목, 설명, 폴더명으로 검색…" autocomplete="off">
</header>
<main>
  <p id="count"></p>
  <div class="grid" id="grid"></div>
  <p id="empty">일치하는 샘플이 없습니다.</p>
</main>
<footer>자동 생성됨 · scripts/generate_index.py</footer>
<script>
  const SAMPLES = {samples_json};

  const grid = document.getElementById('grid');
  const countEl = document.getElementById('count');
  const emptyEl = document.getElementById('empty');
  const search = document.getElementById('search');

  function card(s) {{
    const a = document.createElement('a');
    a.className = 'card';
    a.href = s.slug + '/' + s.html;

    if (s.thumbnail) {{
      const img = document.createElement('img');
      img.className = 'thumb';
      img.loading = 'lazy';
      img.src = s.slug + '/' + s.thumbnail;
      img.alt = s.title;
      a.appendChild(img);
    }} else {{
      const ph = document.createElement('div');
      ph.className = 'thumb placeholder';
      ph.textContent = '미리보기 없음';
      a.appendChild(ph);
    }}

    const body = document.createElement('div');
    body.className = 'body';
    const title = document.createElement('p');
    title.className = 'title';
    title.textContent = s.title;
    body.appendChild(title);
    if (s.description) {{
      const desc = document.createElement('p');
      desc.className = 'desc';
      desc.textContent = s.description;
      body.appendChild(desc);
    }}
    const slug = document.createElement('p');
    slug.className = 'slug';
    slug.textContent = s.slug + '/';
    body.appendChild(slug);
    a.appendChild(body);
    return a;
  }}

  function render(list) {{
    grid.innerHTML = '';
    list.forEach(s => grid.appendChild(card(s)));
    countEl.textContent = list.length + '개 표시 중 (전체 ' + SAMPLES.length + '개)';
    emptyEl.style.display = list.length ? 'none' : 'block';
  }}

  search.addEventListener('input', () => {{
    const q = search.value.trim().toLowerCase();
    if (!q) {{ render(SAMPLES); return; }}
    render(SAMPLES.filter(s =>
      s.title.toLowerCase().includes(q) ||
      s.description.toLowerCase().includes(q) ||
      s.slug.toLowerCase().includes(q)
    ));
  }});

  render(SAMPLES);
</script>
</body>
</html>
"""


def build_site():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for entry in ROOT.iterdir():
        if entry.name.startswith(".") or entry.name in EXCLUDE_DIRS:
            continue
        dest = OUT / entry.name
        if entry.is_dir():
            shutil.copytree(entry, dest)
        else:
            shutil.copy2(entry, dest)

    samples = find_samples()
    html = INDEX_TEMPLATE.format(
        count=len(samples),
        samples_json=json.dumps(samples, ensure_ascii=False),
    )
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"Generated {OUT / 'index.html'} with {len(samples)} sample(s):")
    for s in samples:
        print(f"  - {s['slug']}: {s['title']}")


if __name__ == "__main__":
    build_site()
