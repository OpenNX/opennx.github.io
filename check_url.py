import json
import requests
from bs4 import BeautifulSoup

# Load tinfoil.json
with open("tinfoil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

status_lines = []

# Ghostland status pages mapping
ghostland_status_pages = {
    "https://nx.ghostland.at": "https://status.ghostland.at/797146088",
    "https://nx-retro.ghostland.at": "https://status.ghostland.at/799726659",
    "https://nx-saves.ghostland.at": "https://status.ghostland.at/797836101"
}

def check_ghostland_status_page(status_url):
    try:
        res = requests.get(status_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        component = soup.select_one(".component-status")
        return component and "Operational" in component.text
    except Exception:
        return False

def check_url_directly(url):
    try:
        res = requests.get(url, timeout=10)
        return res.status_code == 200 and "maintenance" not in res.text.lower()
    except Exception:
        return False

# Check each shop
for shop in data.get("locations", []):
    url = shop["url"]
    title = shop["title"]

    if url in ghostland_status_pages:
        is_up = check_ghostland_status_page(ghostland_status_pages[url])
    else:
        is_up = check_url_directly(url)

    symbol = "\u2713" if is_up else "\u2717"  # ✓ or ✗
    status_lines.append(f"{symbol} {title} ({url})")

# Update success field
data["success"] = "Shop status list:\n" + "\n".join(status_lines)

# Save the result
with open("tinfoil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
