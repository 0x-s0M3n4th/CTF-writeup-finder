from serpapi import GoogleSearch
import datetime

# ==============================
# CONFIG
# ==============================
SERPAPI_KEY = "SERPAPI_KEY"   # 🔑 Put your key here
RESULTS_PER_QUERY = 20               # number of results to fetch per year

# ==============================
# MAIN FUNCTION
# ==============================
def get_ctf_writeups(year):
    print(f"\n[*] Running query for CTF writeups in {year}...\n")

    # Build query dynamically
    query = f"CTF writeup {year} -site:reddit.com -site:twitter.com"

    # Log query
    print(f"[>] Search Query: {query}")
    print(f"[>] Using SerpAPI key: {'*' * (len(SERPAPI_KEY) - 4) + SERPAPI_KEY[-4:]}")  # mask API key
    print(f"[>] Results requested: {RESULTS_PER_QUERY}\n")

    # Call SerpAPI
    search = GoogleSearch({
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": SERPAPI_KEY,
        "num": RESULTS_PER_QUERY
    })

    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    writeups = []
    for r in organic_results:
        title = r.get("title")
        link = r.get("link")
        snippet = r.get("snippet", "")
        if title and link:
            writeups.append((title, link, snippet))

    # Output
    if not writeups:
        print("[!] No writeups found.\n")
        return

    print(f"\n=== Top {len(writeups)} CTF Writeups for {year} ===\n")
    for i, (title, link, snippet) in enumerate(writeups, 1):
        print(f"{i}. {title}\n   {link}\n   ↳ {snippet}\n")

    # Tracking log
    with open("ctf_writeups_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.datetime.now()}] Query: {query} | Results: {len(writeups)}\n")
        for i, (title, link, _) in enumerate(writeups, 1):
            f.write(f"{i}. {title} - {link}\n")

# ==============================
# RUN SCRIPT
# ==============================
if __name__ == "__main__":
    year = input("Enter the CTF year (e.g., 2025, 2024, 2023): ").strip()
    get_ctf_writeups(year)
