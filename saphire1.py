import json
from playwright.sync_api import sync_playwright
import requests
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def extract_price():
    os.makedirs("images", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://pk.sapphireonline.pk/", wait_until="networkidle")

        products = page.locator(
            "//div[@class='product-tile']"
        )
        
        all_products = []
        count = products.count()
        img_no = 1
        for i in range(count):
            
            if img_no > 8:
                break

            product = products.nth(i)
            img = product.locator("xpath=.//img[contains(@class,'tile-image')]")
            src = img.get_attribute("data-src")

            if not src:
                continue

            print("Downloading:", src)

            img_data = requests.get(src, headers=HEADERS).content
            with open(f"images/image_{i+1}.jpg", "wb") as f:
                f.write(img_data)
            img_no +=1    

            name_locator = product.locator("xpath=.//div[contains(@class,'pdp-link')]")
            try:
                name_locator.wait_for(state="visible", timeout=100000)
                pd_names = name_locator.inner_text().strip()
            except:
                pd_names = "Empty"

            price_locator = product.locator("xpath=.//span[contains(@class,'value cc-price')]")
            try:
                price_locator.wait_for(state="visible", timeout=100000)
                pd_prices = price_locator.inner_text().strip()
            except:
                pd_prices = "Empty"

            all_products.append({
                "name" : pd_names,
                "price" : pd_prices
            })
        
        with open("product.json", "a", encoding="utf-8")as f:
            json.dump(all_products, f, indent=4, ensure_ascii = False)
            
        browser.close()

extract_price() 

'''def shop_now():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://pk.sapphireonline.pk/", timeout=60000)

        page.get_by_role("link").get_by_text("SHOP NOW").nth(0).click()
        page.wait_for_timeout(3000)
               
        last_height = 0

        while True:
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(10000)
            
            new_height = page.evaluate('document.body.scrollHeight')
            if new_height == last_height: 
                break 
            last_height = new_height     
        
        products = page.locator("xpath=//div[@class='product-tile']")
        total = products.count()
        all_products = []
        for i in range( total):
            product = products.nth(i)
            img = product.locator("xpath=.//img[contains(@class,'tile-image lazyload plp-tile-image')]")   
            src = img.get_attribute("data-src") 
            
            if not src:
                continue
            print("Downloading:", src)
            
            img_data = requests.get(src, headers=HEADERS).content
            with open(f"images/shop_now{i+1}.jpg", "wb") as f:
                f.write(img_data)

            name_locator = product.locator("xpath=.//div[contains(@class, 'tile-body')]//div[contains(@class, 'pdp-link')]/a")
            try:
                name_locator.wait_for(state="visible",timeout=10000)    
                pd_names = name_locator.inner_text().strip()
            except:
                pd_names = "empty"    

            price_locator = product.locator("xpath=.//span[contains(@class,'sales') and contains(@class,'d-inline-block')]//span[contains(@class,'value')]") 
            try:
                price_locator.wait_for(state="visible", timeout=10000)
                pd_prices = price_locator.inner_text().strip()       
            except:
                pd_prices = "Empty"

            all_products.append({
                "name" : pd_names,
                "price" : pd_prices
            })

        with open("product.json", "a", encoding="utf-8")as f:
            json.dump(all_products, f, indent=4, ensure_ascii= False)        
    
        browser.close()
    
shop_now()'''