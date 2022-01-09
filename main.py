import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\jbmat\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://coinmarketcap.com/sv/currencies/solana/")
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(div="priceValue "):
    name = element.find("span")

    if name not in results:
        results.append(name.text)

print(results)