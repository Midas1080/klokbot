from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

CHROMEDRIVER_PATH = '/Chromedriver/chromedriver.exe'

chrome_options = Options()  
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options) 

def getPrice(driver, url, element):
    driver.get(url)
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
    except TimeoutException:
        print("Loading took too much time!")
    html = driver.page_source
    soup = bs(html, "html.parser")
    return soup
    

# AH
ah_url = "https://www.ah.nl/producten/product/wi183090/de-klok-bier"
ah_soup = getPrice(driver, ah_url, 'price__integer')
ah_integer = ah_soup.find('span', {'class':'price__integer'})
ah_fractional = ah_soup.find('span', {'class':'price__fractional'})
ah_price =  float(ah_integer.get_text() + '.' + ah_fractional.get_text())

# JUMBO
jumbo_url = "https://www.jumbo.com/product/48039BLK"
jumbo_soup = getPrice(driver, jumbo_url, 'jum-column-main')
jumbo_price = jumbo_soup.find('input', {'id':'PriceInCents_48039BLK'}).get('jum-data-price')
#<input type="hidden" value="061" name="PriceInCents_48039BLK" jum-data-price="0.61" id="PriceInCents_48039BLK">

# Hoogvliet
hoogvliet_url = "https://www.hoogvliet.com/product/de-klok-blik?tracking=searchterm:de+klok"
hoogvliet_soup = getPrice(driver, hoogvliet_url, 'price-cents')
hoogvliet_integer = hoogvliet_soup.find('span', {'class':'price-euros'})
hoogvliet_fractional = hoogvliet_soup.find('span', {'class':'price-cents'})
hoogvliet_price =  float(hoogvliet_integer.get_text() + hoogvliet_fractional.get_text())

# PLUS
plus_url = "https://www.plus.nl/product/de-klok-bier-blik-33-cl-694894"
plus_soup = getPrice(driver, plus_url, 'price-range__strikethrough')
plus_price = float(plus_soup.find('span', {'class':'price-range__strikethrough'}).get_text())
#<span class="price-range__strikethrough">0.65</span>

# DEEN
deen_url = "https://www.deen.nl/product/de-klok-bier-blik-50-cl"
deen_soup = getPrice(driver, deen_url, 'c-price__cents')
deen_cents = deen_soup.find('sup', {'class':'c-price__cents'}).get_text()
deen_price = float('0.' + deen_cents)
#<sup class="c-price__cents">60</sup>

# COOP
coop_url = "https://www.coop.nl/de-klok-blik/product/8716700016358"
coop_soup = getPrice(driver, coop_url, 'price')
coop_cents = coop_soup.find('span', {'class':'sup'}).get_text()
coop_price = float('0.' + coop_cents)

# DIRK
dirk_url = "https://www.dirk.nl/boodschappen/dranken-sap-koffie-thee/bier/de-klok-bier/1959"
dirk_soup = getPrice(driver, dirk_url, 'product-card__price__cents')
dirk_cents = dirk_soup.find('span', {'class':'product-card__price__cents'}).get_text()
dirk_price = float('0.' + dirk_cents)

driver.close()

# print all prices
print('AH: ' + str(ah_price) + ' euro')
print('Jumbo: ' + str(jumbo_price) + ' euro')
print('Hoogvliet: ' + str(hoogvliet_price) + ' euro')
print('PLUS: ' + str(plus_price) + ' euro')
print('DEEN: ' + str(deen_price) + ' euro')
print('COOP: ' + str(coop_price) + ' euro')
print('Dirk: ' + str(dirk_price) + ' euro')
