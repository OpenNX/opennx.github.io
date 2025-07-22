import json
import requests
from bs4 import BeautifulSoup

# Unicode status symbols
CHECK = "\u2713"  # ✓
CROSS = "\u274C"  # ❌ (Using the more common red cross)

# Ghostland fallback mapping (no changes here)
ghostland_status_pages = {
    "https://nx.ghostland.at": "https://status.ghostland.at/797146088",
    "https://nx-retro.ghostland.at": "https://status.ghostland.at/799726659",
    "https://nx-saves.ghostland.at": "https://status.ghostland.at/797836101"
}

# --- MODIFIED FUNCTION ---
# Function to check via Ghostland status page
def check_ghostland_status_page(status_url):
    """
    Checks the status from a Uptime Kuma-powered status page.
    This version uses a more specific and reliable CSS selector.
    """
    try:
        # Added a User-Agent header to prevent being blocked
        headers = {'User-Agent': 'Python Status Checker/1.0'}
        res = requests.get(status_url, timeout=10, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        
        # CORRECTED SELECTOR: The status pages use a div with a `data-cy` attribute,
        # and the status text is inside a nested span with the class "status".
        status_element = soup.select_one('div[data-cy="monitor-item-0"] .status')
        
        if status_element:
            # The status text on these pages is "Up" for operational.
            # We check for "up" in the lowercase text to be safe.
            status_text = status_element.text.strip().lower()
            return "up" in status_text
        
        # If the selector doesn't find anything, we print a warning and return False.
        print(f"[Ghostland Fallback Warning] Could not find the status element for {status_url}")
        return False
        
    except Exception as e:
        print(f"[Ghostland fallback error] {status_url}: {e}")
        return False

# Function to check direct HTTP access (no changes here)
def check_url_directly(url):
    """Checks if a URL is directly accessible with a 200 OK status."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"[Direct check error] {url}: {e}")
        return False

# --- MAIN SCRIPT LOGIC ---
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
    # Simplified the message to not include the URL, making it cleaner.
    status_parts.append(f"{symbol} {title}")

# --- SIMPLIFIED UPDATE ---
# Set the compact success message. Your original code set this value twice.
# This version creates a clean, newline-separated list.
data["success"] = "Open NX Shops status list:\n" + "\n".join(status_parts)

# Save the result
with open("tinfoil.json", "w", encoding="utf-8") as f:
    # Using indent=4 for better readability in the JSON file
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\nSuccessfully updated tinfoil.json with the latest shop statuses.")

