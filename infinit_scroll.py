import json
import requests
from lxml import html

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def scraper():
    url_template = (
        "https://pk.sapphireonline.pk/on/demandware.store/"
        "Sites-Sapphire-Site/default/Search-UpdateGrid"
        "?cgid=woman&start={start}&sz=24"
    )

    all_products = []
    img_count = 1
    page = 0

    while True:
        start = page * 24
        url = url_template.format(start=start)

        print(f"Scraping page start={start}")

        response = requests.get(url, headers=HEADERS)
        dom = html.fromstring(response.text)

        names = dom.xpath(
            '//div[contains(@class,"tile-body")]'
            '//div[contains(@class,"pdp-link")]/a/text()'
        )
        prices = dom.xpath(
            '//span[contains(@class,"sales") and contains(@class,"d-inline-block")]'
            '//span[contains(@class,"value")]/text()'
        )
        images = dom.xpath(
            '//div[contains(@class,"image-container")]//img/@data-src'
        )

        names = [name.strip() for name in names if name.strip()]
        prices = [price.strip() for price in prices if price.strip()]
        images = [image.strip() for image in images if image.strip()]

        if not names:
            break

        for name, price, image in zip(names, prices, images):
            all_products.append({
                "name": name,
                "price": price,
                "image": image,
            })

            img_data = requests.get(image, headers=HEADERS).content
            with open(f"image_{img_count}.jpg", "wb") as f:
                f.write(img_data)

            img_count += 1

        page += 1

    with open("product.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    scraper()
