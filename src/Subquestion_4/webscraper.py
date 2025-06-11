import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://www.npr.org/sections/energy/?page={}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

output = []
max_pages = 50

def scrape_article(url):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.content, 'html.parser')
        time_tag = soup.find("time")
        date = time_tag.get("datetime") if time_tag else "N/A"
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        return date, text
    except Exception as e:
        return "N/A", ""

for page in range(1, max_pages + 1):
    print(f"Collecting page {page}...")
    res = requests.get(base_url.format(page), headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.find_all("article")

    for art in articles:
        a_tag = art.find("a")
        if not a_tag:
            continue
        title = a_tag.get_text(strip=True)
        url = a_tag["href"]
        if not url.startswith("http"):
            url = "https://www.npr.org" + url
        date, text = scrape_article(url)
        output.append({
            "date": date,
            "title": title,
            "url": url,
            "text": text
        })

    time.sleep(1.5)

with open("scrapping_result.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "title", "url", "text"])
    writer.writeheader()
    writer.writerows(output)

print(f"\nSaved {len(output)} articles")