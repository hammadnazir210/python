from bs4 import BeautifulSoup
import requests
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

Quotes = soup.find_all("div", class_="quote")

data = []    

for q in Quotes:
    
    link = "https://quotes.toscrape.com" + q.find("a")["href"]

    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    detail = soup.find_all("div", class_="author-details")

    for d in detail:
        name = d.find("h3", class_="author-title").text.strip()
        description = d.find("div", class_="author-description").text.strip()

        
        data.append({
            "name": name,
            "description": description,
            "detail_page": link
        })


with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

