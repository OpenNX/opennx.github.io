import json
import requests
from bs4 import BeautifulSoup

# Unicode status symbols
CHECK = "\u2713"  # ✓
CROSS = "\u2715"  # ✕ (Reverted to the original unicode character as requested)

# Ghostland fallback mapping (no changes here)
ghostland_status_pages = {
    "https://nx.ghostland.at": "https://status.ghostland.at/797146088",
    "https://nx-retro.ghostland.at": "https://status.ghostland.at/799726659",
    "https://nx-saves.ghostland.at": "https://status.ghostland.at/797836101"
}

# --- REVISED FUNCTION ---
# Function to check via Ghostland status page by looking for the specific CSS class
def check_ghostland_status_page(status_url):
    """
    Checks the status from a Uptime Kuma-powered status page.
    This version checks for the presence of the 'uk-text-primary' CSS class,
    which is associated with the "Up" status text, as requested.
    """
    try:
        headers = {'User-Agent': 'Python Status Checker/1.2'}
        res = requests.get(status_url, timeout=15, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Find the element with the class 'uk-text-primary'.
        # This class is used when the service is operational ("Up").
        status_element = soup.select_one(".uk-text-primary")

        # If the element exists and its text is "Up", the service is online.
        if status_element and "Up" in status_element.text:
            return True
        
        return False

    except Exception as e:
        print(f"[Ghostland fallback error] {status_url}: {e}")
        return False

# Function to check direct HTTP access (no changes here)
def check_url_directly(url):
    """Checks if a URL is directly accessible with a 200 OK status."""
    try:
        # Added a user agent here as well for consistency
        headers = {'User-Agent': 'Python Status Checker/1.2'}
        response = requests.get(url, timeout=10, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"[Direct check error] {url}: {e}")
        return False

# --- MAIN SCRIPT LOGIC (no changes from here) ---
# Load JSON
try:
    with open("tinfoil.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: tinfoil.json not found. Please ensure the file is in the same directory.")
    exit()

# Build compact success message
status_parts = []

print("Checking shop statuses...")
for shop in data.get("locations", []):
    url = shop.get("url")
    title = shop.get("title")

    if not url or not title:
        continue # Skip entries that are missing a URL or title

    is_online = False # Default to offline
    if url in ghostland_status_pages:
        print(f"-> Checking {title} via status page...")
        is_online = check_ghostland_status_page(ghostland_status_pages[url])
    else:
        print(f"-> Checking {title} directly...")
        is_online = check_url_directly(url)

    symbol = CHECK if is_online else CROSS
    status_parts.append(f"{symbol} {title}")

# Set the compact success message
data["success"] = "Open NX Shops status list:\n" + "\n".join(status_parts)

# Save the result
with open("tinfoil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\nSuccessfully updated tinfoil.json with the latest shop statuses.")
