import json
import requests
from bs4 import BeautifulSoup

# Keywords to determine shop status
WORKING_KEYWORDS = ["shop", "eshop", "tinfoil", "store", "eshopdb"]
MAINTENANCE_KEYWORDS = ["maintenance", "offline", "not available", "update in progress"]

# Ghostland fallback status pages
GHOSTLAND_STATUS_IDS = {
    "nx.ghostland.at": "797146088",
    "nx-retro.ghostland.at": "799726659",
    "nx-saves.ghostland.at": "797836101"
}

def check_ghostland_status(shop_id):
    try:
        url = f"https://status.ghostland.at/{shop_id}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text.lower(), 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        if "all systems operational" in text or "no incidents reported" in text:
            return "✅"
        if "under maintenance" in text or "partial outage" in text:
            return "⚠️"
        if "major outage" in text:
            return "❌"
        return "⚠️"
    except:
        return "⚠️"

def check_shop_status(url):
    try:
        full_url = f"https://{url}"
        response = requests.get(full_url, timeout=15)
        response.raise_for_status()

        content = response.text.lower()
        soup = BeautifulSoup(content, 'html.parser')
        visible_text = soup.get_text(separator=' ', strip=True).lower()

        if any(w in visible_text for w in WORKING_KEYWORDS):
            if any(w in visible_text for w in MAINTENANCE_KEYWORDS):
                return "⚠️"
            return "✅"
        elif any(w in visible_text for w in MAINTENANCE_KEYWORDS):
            return "❌"

        # No match, use fallback for ghostland
        if url in GHOSTLAND_STATUS_IDS:
            return check_ghostland_status(GHOSTLAND_STATUS_IDS[url])
        return "⚠️"
    except:
        if url in GHOSTLAND_STATUS_IDS:
            return check_ghostland_status(GHOSTLAND_STATUS_IDS[url])
        return "❌"

# Load JSON
with open("tinfoil.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build per-shop results
status_lines = []

for shop in data.get("shops", []):
    url = shop.get("url")
    if not url:
        continue
    status = check_shop_status(url)
    status_lines.append(f"{status} {url}")

# Set summary result
data["success"] = "\n".join(status_lines)

# Save updated file
with open("tinfoil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
