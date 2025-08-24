# ctftime-writeups.py

A Python script that fetches **top CTF writeups** for a given year from the site 'ctftime.org' using the **SerpAPI Google Search API**.  
It also logs activity into a `ctf_writeups_log.txt` file for debugging and tracking. Make sure to creeate thath before hand.

---
# ctf-accross-web-writeup.py
A python script that fetches top 20 CTF writeups for a given year accross the web using the **SerpAPI Google Search API**.  


## 🔧 Requirements

Before running the script, make sure you have:

- **Python 3.8+** installed
- A **SerpAPI API key** (free tier available)

Install required Python libraries:

```bash
pip install requests
```
🔑 Setup SerpAPI API Key
	1.	Go to SerpAPI.
	2.	Create a free account.
	3.	Copy your API Key from your dashboard.
	4.	Replace the placeholder inside the script:
 📂 Logging Setup

This script automatically creates a log file named ctf_writeups_log.txt in the same directory.
It tracks each step (searching, fetching results, errors, etc.).
Example log entries:
```text
2025-08-24 05:15:23,421 - INFO - Searching for: CTF writeup 2024
2025-08-24 05:15:23,965 - INFO - Found 10 results for 2024
```
▶️ How to Run
	1.	Clone or download this repo/script.
	2.	Open a terminal in the folder.
	3.	Run: 
 ```python
python3 ctftime-writeups.py
python3 ctf-accross-web-writeup.py
```
  4.	Enter the year when prompted, for example:
```text
Enter the CTF year (e.g., 2025, 2024, 2023): 2024
```
📜 Example Output:
```text
[*] Searching for top CTF writeups in 2024...

=== Top 10 CTF Writeups for 2024 ===

1. KalmarCTF 2024 Writeups
   https://ctftime.org/event/2227/tasks/
2. DEF CON Quals 2024 Writeups
   https://ctftime.org/writeup/39151
3. Google CTF 2024 Official Writeups
   https://google.com/ctf-writeups-2024
...
