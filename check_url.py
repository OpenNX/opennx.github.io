import json
import requests
from bs4 import BeautifulSoup

# Unicode status symbols
CHECK = "\u2713"  # ✓
CROSS = "\u2715"  # ✕ or "\u274C" for ❌

# Ghostland fallback mapping
ghostland_status_pages = {
    "https://nx.ghostland.at": "https://status.ghostland.at/797146088",
    "https://nx-retro.ghostland.at": "https://status.ghostland.at/799726659",
    "https://nx-saves.ghostland.at": "https://status.ghostland.at/797836101"
}

# Function to check via Ghostland status page
def check_ghostland_status_page(status_url):
    try:
        res = requests.get(status_url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        component = soup.select_one(".component-status")
        return component and "Operational" in component.text.strip()
    except Exception as e:
        print(f"[Ghostland fallback error] {status_url}: {e}")
        return False

# Function to check direct HTTP access
def check_url_directly(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"[Direct check error] {url}: {e}")
        return False

# Load JSON
with open("tinfoil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build compact success message
status_parts = []

for shop in data.get("locations", []):
    url = shop.get("url")
    title = shop.get("title")

    if url in ghostland_status_pages:
        is_online = check_ghostland_status_page(ghostland_status_pages[url])
    else:
        is_online = check_url_directly(url)

    symbol = CHECK if is_online else CROSS
    status_parts.append(f"{symbol} {title} ({url})")

# Set the compact success message
data["success"] = " | ".join(status_parts)
# Update success field
data["success"] = "Open NX Shops status list:\n" + "\n".join(status_lines)

# Save the result
with open("tinfoil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
