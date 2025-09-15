import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Suppress warnings from insecure requests, as we will disable SSL verification.
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# --- CONFIGURATION ---

SOURCE_URL = "https://opennx.github.io/tinfoil.json"

# Ghostland shops mapping to their "/up" check URLs
GHOSTLAND_SHOPS = {
    "nx.ghostland.at": "https://nx.ghostland.at/up",
    "nx-retro.ghostland.at": "https://nx-retro.ghostland.at/up",
    "nx-saves.ghostland.at": "https://nx-saves.ghostland.at/up"
}

# --- DATA FETCHING ---

def fetch_shop_list():
    try:
        print(f"Fetching master shop list from {SOURCE_URL}...")
        response = requests.get(SOURCE_URL, timeout=15, verify=False)
        response.raise_for_status()
        print("Successfully fetched master list.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"FATAL: Could not fetch master shop list: {e}")
        return None
    except json.JSONDecodeError:
        print("FATAL: Failed to parse master shop list as JSON.")
        return None

# --- STATUS CHECKING FUNCTIONS ---

def check_ghostland_status(status_url):
    try:
        headers = {'User-Agent': 'Python Status Checker/2.4'}
        response = requests.get(status_url, timeout=10, headers=headers, verify=False)
        response.raise_for_status()
        content = response.text.strip().lower()
        if content == "ok":
            return "Online"
        else:
            return f"Offline (resp: {content})"
    except requests.exceptions.RequestException as e:
        print(f"[Ghostland check error] {status_url}: {e}")
        return "Check failed"

def check_generic_url(url):
    try:
        response = requests.get(url, timeout=10, stream=True, verify=False)
        
        if response.status_code != 200:
            return f"Offline ({response.status_code})"

        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            return "Invalid content"

        content = response.raw.read(200000, decode_content=True).decode('utf-8', 'ignore').lower()
        
        soup = BeautifulSoup(content, "html.parser")
        title_text = soup.title.string.strip().lower() if soup.title else ""
        
        if "maintenance" in title_text:
            return "Under maintenance"

        broken_indicators = ["default web page", "site not found", "502 bad gateway", "error 403"]
        if any(bad in content for bad in broken_indicators):
            return "Error/Placeholder"

        working_indicators = [".nsp", ".xci", "tinfoil", ".nsz", "eshop", "shop", "switch"]
        if any(good in content for good in working_indicators):
            return "Online"

        if len(content.strip()) < 300:
            return "Possibly blank"

        return "Online"

    except requests.exceptions.RequestException as e:
        print(f"    - Error connecting to {url}: {e}")
        return "Connection failed"

# --- MAIN SCRIPT LOGIC ---

def main():
    master_data = fetch_shop_list()
    if not master_data:
        return

    directories = master_data.get("directories", [])
    status_parts = []
    print("\nChecking individual shop statuses...")

    for full_url in directories:
        host = urlparse(full_url).netloc
        print(f"-> Checking '{host}' ({full_url})...")

        matched_ghost_host = None
        for ghost_host in GHOSTLAND_SHOPS:
            if ghost_host in full_url:
                matched_ghost_host = ghost_host
                break

        if matched_ghost_host:
            status = check_ghostland_status(GHOSTLAND_SHOPS[matched_ghost_host])
        else:
            status = check_generic_url(full_url)
        
        print(f"   - Status: {status}")
        status_parts.append(f"{host}:  {status}")

    master_data["success"] = "Open NX Shops status list:\n\n" + "\n".join(status_parts) + "\n\nStar on GitHub:\nhttps://github.com/OpenNX/opennx.github.io"

    try:
        with open("tinfoil.json", "w", encoding="utf-8") as f:
            json.dump(master_data, f, ensure_ascii=False, indent=4)
        print("\nSuccessfully updated local tinfoil.json with the latest shop list and statuses.")
    except IOError as e:
        print(f"\nError: Could not write to tinfoil.json: {e}")

if __name__ == "__main__":
    main()
