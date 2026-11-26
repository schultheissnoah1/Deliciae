import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.scripts = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "script":
            self.scripts.append(attributes.get("src"))
        self.links.extend(attributes[key] for key in ("href", "src") if attributes.get(key))


root = Path("_site")
base = sys.argv[1].rstrip("/")
pages = {path.relative_to(root): Page(path) for path in root.rglob("*.html")}
expected = {Path(name) / "index.html" for name in ("", "services", "our-work")}
errors = [f"Missing page {path}" for path in sorted(expected - pages.keys())]

for path, page in pages.items():
    allowed_scripts = ["assets/comparisons.js"] if path == Path("index.html") else []
    if any(script not in allowed_scripts for script in page.scripts):
        errors.append(f"{path}: unexpected script")
    for reference in page.links:
        target = urlsplit(urljoin(f"{base}/{path.as_posix()}", reference))
        if target.scheme or target.netloc:
            continue
        local = unquote(target.path)
        if not local.startswith(f"{base}/"):
            errors.append(f"{path}: URL outside site base: {reference}")
            continue
        destination = Path(local[len(base) + 1:])
        if (root / destination).is_dir():
            destination /= "index.html"
        if not (root / destination).is_file():
            errors.append(f"{path}: missing target {reference}")
        elif target.fragment and destination in pages:
            if unquote(target.fragment) not in pages[destination].ids:
                errors.append(f"{path}: missing anchor {reference}")

if errors:
    sys.exit("\n".join(errors))
print(f"Checked {len(pages)} pages.")
