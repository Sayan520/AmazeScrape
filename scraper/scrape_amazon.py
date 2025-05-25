import requests
import pandas as pd
from bs4 import BeautifulSoup
from config import USER_AGENTS
from scraper.utils import get_random_user_agent, add_delay

#  Function to scrape Amazon product data
def get_amazon_data(url):
    headers = {
        "User-Agent": get_random_user_agent(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page {url}, Status code: {response.status_code}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.text, "html.parser")

    product_names = []
    prices = []
    ratings = []

    for item in soup.find_all("div", {"data-component-type": "s-search-result"}):
        # Product Name
        name_tag = item.find("h2")
        name = name_tag.text.strip() if name_tag else "N/A"
        product_names.append(name)

        # Improved Price Extraction
        price = "N/A"
        price_container = item.find("span", class_="a-price")
        if price_container:
            price_whole = price_container.find("span", class_="a-price-whole")
            price_frac = price_container.find("span", class_="a-price-fraction")
            if price_whole and price_frac:
                price = f"{price_whole.text.strip()}.{price_frac.text.strip()}"
            elif price_whole:
                price = price_whole.text.strip()
        prices.append(price)

        # Rating
        rating_tag = item.find("span", class_="a-icon-alt")
        rating = rating_tag.text.strip() if rating_tag else "N/A"
        ratings.append(rating)

    return pd.DataFrame({
        "Product Name": product_names,
        "Price": prices,
        "Rating": ratings
    })

# Function to scrape multiple pages of Amazon search results
def scrape_amazon(search_term, pages):
    base_url = f"https://www.amazon.in/s?k={search_term.replace(' ', '+')}"
    all_data = pd.DataFrame()

    for page in range(1, pages + 1):
        url = f"{base_url}&page={page}"
        print(f"Scraping: {url}")
        add_delay()
        page_data = get_amazon_data(url)
        all_data = pd.concat([all_data, page_data], ignore_index=True)

    return all_data
