from serpapi import GoogleSearch

# 🔑 Put your SerpAPI key here
SERPAPI_KEY = "SERP_KEY"

def fetch_ctf_writeups(year):
    query = f"CTF writeup {year} site:ctftime.org"
    
    search = GoogleSearch({
        "q": query,
        "hl": "en",
        "gl": "us",
        "num": 10,
        "api_key": SERPAPI_KEY
    })
    
    results = search.get_dict()
    
    if "organic_results" not in results:
        print("[!] No results found.")
        return []
    
    writeups = []
    for res in results["organic_results"]:
        title = res.get("title", "No Title")
        link = res.get("link", "")
        if "ctftime.org" in link:
            writeups.append((title, link))
    
    return writeups[:10]

if __name__ == "__main__":
    year = input("Enter the CTF year (e.g., 2025, 2024, 2023): ")
    
    print(f"[*] Searching for top CTF writeups in {year}...\n")
    writeups = fetch_ctf_writeups(year)
    
    print(f"\n=== Top {len(writeups)} CTF Writeups for {year} ===\n")
    for idx, (title, link) in enumerate(writeups, 1):
        print(f"{idx}. {title}\n   {link}")
