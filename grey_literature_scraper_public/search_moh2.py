import requests
import csv
import time
import pandas as pd
from urllib.parse import urlparse
from datetime import datetime

# --- CONFIG ---
API_KEY = "API_KEY"  # Replace with your actual API key
SEARCH_ENGINE_ID = "SEARCH_ID"  # Your Custom Search Engine ID
INPUT_FILE = "data/moh_urls.csv"
OUTPUT_FILE = "moh_search_results.csv"
QUERY = "maternal antimicrobial resistance"  # Update or swap for broader terms

# --- TIMESTAMP FOR THIS RUN ---
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- LOAD INPUT DATA ---
df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")
df.columns = df.columns.str.strip().str.replace('\ufeff', '')  # Clean headers
print("Detected columns:", df.columns.tolist())

# --- SETUP OUTPUT ---
fieldnames = ["Country", "MoH URL", "Search URL", "Title", "Snippet", "Page Link", "Timestamp"]
total_results = 0

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # --- LOOP THROUGH EACH COUNTRY ---
    for _, row in df.iterrows():
        country = row["Country"]
        url = row["URL"]

        if pd.isna(url) or url.lower() == "not available":
            print(f"Skipping {country}: No MoH URL.")
            continue

        domain = urlparse(url).netloc
        if not domain:
            print(f"Skipping {country}: Invalid URL.")
            continue

        search_query = f"site:{domain} {QUERY}"
        params = {
            "key": API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": search_query,
            "num": 10
        }

        try:
            print(f"\nSearching {country} ({domain})...")
            response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
            data = response.json()

            if "error" in data:
                print(f"API error for {country}: {data['error']['message']}")
                continue

            if "items" in data:
                for item in data["items"]:
                    writer.writerow({
                        "Country": country,
                        "MoH URL": url,
                        "Search URL": search_query,
                        "Title": item.get("title", "N/A"),
                        "Snippet": item.get("snippet", "N/A"),
                        "Page Link": item.get("link", "N/A"),
                        "Timestamp": timestamp
                    })
                    total_results += 1
                print(f"✔ Results found for {country}")
            else:
                print(f"✘ No results for {country}")

        except Exception as e:
            print(f"Error for {country}: {str(e)}")

        time.sleep(1)  # Avoid rate limits

# --- SUMMARY ---
print(f"\n✅ All done! {total_results} search results saved to {OUTPUT_FILE}")
