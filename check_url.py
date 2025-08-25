import json
import requests
from bs4 import BeautifulSoup

# Suppress warnings from insecure requests, as we will disable SSL verification.
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# --- CONFIGURATION ---

# The source URL to fetch the master list of shops from.
SOURCE_URL = "https://opennx.github.io/tinfoil.json"

# Ghostland shops mapping to their "/up" check URLs
GHOSTLAND_SHOPS = {
    "nx.ghostland.at": "https://nx.ghostland.at/up",
    "nx-retro.ghostland.at": "https://nx.ghostland.at/up",
    "nx-saves.ghostland.at": "https://nx.ghostland.at/up"
}

# --- DATA FETCHING ---

def fetch_shop_list():
    """
    Fetches the master list of shops from the source JSON URL.
    Returns the entire data structure.
    """
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
    """
    Ghostland shops return plain 'ok' on their /up endpoint when operational.
    """
    try:
        headers = {'User-Agent': 'Python Status Checker/2.4'}
        response = requests.get(status_url, timeout=10, headers=headers, verify=False)
        response.raise_for_status()

        content = response.text.strip().lower()
        if content == "ok":
            return f"Online"
        else:
            return f"Offline (resp: {content})"

    except requests.exceptions.RequestException as e:
        print(f"[Ghostland check error] {status_url}: {e}")
        return f"(Check failed)"

def check_generic_url(url):
    """
    Performs a comprehensive check on a generic URL.
    This function now expects a full URL including the scheme.
    """
    try:
        response = requests.get(url, timeout=10, stream=True, verify=False)
        
        if response.status_code != 200:
            return f"Offline ({response.status_code})"

        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            return f"Invalid content"

        content = response.raw.read(200000, decode_content=True).decode('utf-8', 'ignore').lower()
        
        soup = BeautifulSoup(content, "html.parser")
        title_text = soup.title.string.strip().lower() if soup.title else ""
        
        if "maintenance" in title_text:
            return f"Under maintenance"

        broken_indicators = ["default web page", "site not found", "502 bad gateway", "error 403"]
        if any(bad in content for bad in broken_indicators):
            return f"Error/Placeholder"

        working_indicators = [".nsp", ".xci", "tinfoil", ".nsz", "eshop", "shop", "switch"]
        if any(good in content for good in working_indicators):
            return f"Online"

        if len(content.strip()) < 300:
            return f"Possibly blank"

        return f"Online"

    except requests.exceptions.RequestException as e:
        print(f"    - Error connecting to {url}: {e}")
        return f"Connection failed"

# --- MAIN SCRIPT LOGIC ---
def main():
    """
    Main function to fetch the remote shop list, check each one,
    and update the local tinfoil.json file.
    """
    master_data = fetch_shop_list()
    if not master_data:
        return

    status_parts = []
    print("\nChecking individual shop statuses...")

    for shop in master_data.get("locations", []):
        full_url = shop.get("url")
        title = shop.get("title")

        if not full_url or not title:
            continue

        print(f"-> Checking '{title}' ({full_url})...")
    
        matched_ghost_host = None
        for host in GHOSTLAND_SHOPS:
            if host in full_url:
                matched_ghost_host = host
                break

        if matched_ghost_host:
            status = check_ghostland_status(GHOSTLAND_SHOPS[matched_ghost_host])
        else:
            status = check_generic_url(full_url)
        
        print(f"   - Status: {status}")
        status_parts.append(f"{title}:  {status}")

    master_data["success"] = "Open NX Shops status list:\n\n" + "\n".join(status_parts) + "\n\nStar on GitHub:\nhttps://github.com/OpenNX/opennx.github.io" 

    try:
        with open("tinfoil.json", "w", encoding="utf-8") as f:
            json.dump(master_data, f, ensure_ascii=False, indent=4)
        print("\nSuccessfully updated local tinfoil.json with the latest shop list and statuses.")
    except IOError as e:
        print(f"\nError: Could not write to tinfoil.json: {e}")

if __name__ == "__main__":
    main()
