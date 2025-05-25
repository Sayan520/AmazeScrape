from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")

driver = webdriver.Chrome(options=options)

query = "ROLEX DATEJUST"
url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}"
print(f"Loading {url}")
driver.get(url)
time.sleep(3)  # wait for page to load

items = driver.find_elements(By.CSS_SELECTOR, "li.s-item h3.s-item__title")
print(f"Found {len(items)} items:")
for i, item in enumerate(items[:5], 1):
    print(f"{i}. {item.text}")

driver.quit()
