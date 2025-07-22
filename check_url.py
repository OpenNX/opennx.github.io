import json
import requests
from bs4 import BeautifulSoup

# Load the tinfoil.json file
with open("tinfoil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

status_lines = []

# Map Ghostland shops to their status page URLs
ghostland_status_pages = {
    "https://nx.ghostland.at": "https://status.ghostland.at/797146088",
    "https://nx-retro.ghostland.at": "https://status.ghostland.at/799726659",
    "https://nx-saves.ghostland.at": "https://status.ghostland.at/797836101"
}

def check_ghostland_status_page(status_url):
    try:
        response = requests.get(status_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        container = soup.select_one(".component-status")
        if container and "Operational" in container.get_text():
            return True
    except Exception:
        pass
    return False

def check_shop(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and "maintenance" not in response.text.lower():
            return True
    except Exception:
        pass
    return False

for shop in data.get("locations", []):
    url = shop["url"]
    title = shop["title"]

    is_up = False

    if url in ghostland_status_pages:
        # Fallback: use the Ghostland status page
        is_up = check_ghostland_status_page(ghostland_status_pages[url])
    else:
        # Standard method
        is_up = check_shop(url)

    symbol = "✅" if is_up else "❌"
    status_lines.append(f"{symbol} {title} ({url})")

# Add the summary to the success field
data["success"] = "Shop status list:\n" + "\n".join(status_lines)

# Write updated content back to tinfoil.json
with open("tinfoil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
