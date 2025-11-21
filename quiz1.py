import json
import requests
from bs4 import BeautifulSoup

def scrape_authors():
    
    """Scrape authors from quotes.toscrape.com and save as JSON."""
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    data = []    

    for quote in quotes:
    
        link = "https://quotes.toscrape.com" + quote.find("a")["href"]
        detail_response = requests.get(link)
        detail_soup = BeautifulSoup(detail_response.text, "html.parser")
        details = detail_soup.find_all("div", class_="author-details")

        for detail in details:
            name = detail.find("h3", class_="author-title").text.strip()
            description = detail.find(
                "div", class_="author-description").text.strip()
            
            data.append({
                "name": name,
                "description": description
            })

    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    scrape_authors()