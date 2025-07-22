import json
import re
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
# Function to check via Ghostland status page by parsing embedded JSON
def check_ghostland_status_page(status_url):
    """
    Checks the status from a Uptime Kuma-powered status page.
    This definitive version finds the <script> tag containing the monitor data,
    extracts the JSON object using regex, and reads the status directly.
    This is more reliable as it doesn't depend on CSS or JavaScript rendering.
    """
    try:
        headers = {'User-Agent': 'Python Status Checker/1.3'}
        res = requests.get(status_url, timeout=15, headers=headers)
        res.raise_for_status()

        # The page data is stored in a <script> tag as a JavaScript object.
        # We use a regular expression to find and extract this entire object.
        match = re.search(r"window\.kuma\s*=\s*({.*?});", res.text)
        
        if match:
            # Extract the JSON data string from the regex match
            json_data_str = match.group(1)
            # Parse the extracted string into a Python dictionary
            status_data = json.loads(json_data_str)
            
            # The status for the first monitor on the page is in monitorList[0].
            # In Uptime Kuma, the status value for "Up" is the integer 1.
            monitor_status = status_data.get("monitorList", [{}])[0].get("status")
            return monitor_status == 1

        # If we get here, the expected script data was not found on the page.
        print(f"[Ghostland Fallback Warning] Could not find monitor data for {status_url}")
        return False

    except Exception as e:
        print(f"[Ghostland fallback error] {status_url}: {e}")
        return False

# Function to check direct HTTP access (no changes here)
def check_url_directly(url):
    """Checks if a URL is directly accessible with a 200 OK status."""
    try:
        # Added a user agent here as well for consistency
        headers = {'User-Agent': 'Python Status Checker/1.3'}
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
