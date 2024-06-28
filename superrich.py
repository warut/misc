from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Open a new browser page
    page = browser.new_page()

    URL = "https://www.superrich1965.com/currency.php"
    page.goto(URL)
    soup = BeautifulSoup(page.content(),'html.parser')
    ssflist=(soup.find(id="ratesTable1"))
    for ss in ssflist:
        print(ss.text)
    browser.close()

