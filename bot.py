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

# AH
ah_url = "https://www.ah.nl/producten/product/wi183090/de-klok-bier"
driver.get(ah_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price__integer')))
except TimeoutException:
    print("Loading took too much time!")

ah_html = driver.page_source
ah_soup = bs(ah_html, "html.parser")
ah_integer = ah_soup.find('span', {'class':'price__integer'})
ah_fractional = ah_soup.find('span', {'class':'price__fractional'})
ah_price =  float(ah_integer.get_text() + '.' + ah_fractional.get_text())

# JUMBO
jumbo_url = "https://www.jumbo.com/product/48039BLK"
driver.get(jumbo_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jum-column-main')))
except TimeoutException:
    print("Loading took too much time!")

jumbo_html = driver.page_source
jumbo_soup = bs(jumbo_html, "html.parser")
jumbo_price = jumbo_soup.find('input', {'id':'PriceInCents_48039BLK'}).get('jum-data-price')
#<input type="hidden" value="061" name="PriceInCents_48039BLK" jum-data-price="0.61" id="PriceInCents_48039BLK">

# Hoogvliet
hoogvliet_url = "https://www.hoogvliet.com/product/de-klok-blik?tracking=searchterm:de+klok"
driver.get(hoogvliet_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price-cents')))
except TimeoutException:
    print("Loading took too much time!")

hoogvliet_html = driver.page_source
hoogvliet_soup = bs(hoogvliet_html, "html.parser")
hoogvliet_integer = hoogvliet_soup.find('span', {'class':'price-euros'})
hoogvliet_fractional = hoogvliet_soup.find('span', {'class':'price-cents'})
hoogvliet_price =  float(hoogvliet_integer.get_text() + hoogvliet_fractional.get_text())

# PLUS
plus_url = "https://www.plus.nl/product/de-klok-bier-blik-33-cl-694894"
driver.get(plus_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price-range__strikethrough')))
except TimeoutException:
    print("Loading took too much time!")

plus_html = driver.page_source
plus_soup = bs(plus_html, "html.parser")
plus_price = float(plus_soup.find('span', {'class':'price-range__strikethrough'}).get_text())
#<span class="price-range__strikethrough">0.65</span>

# DEEN
deen_url = "https://www.deen.nl/product/de-klok-bier-blik-50-cl"
driver.get(deen_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-productdetail')))
except TimeoutException:
    print("Loading took too much time!")

deen_html = driver.page_source
deen_soup = bs(deen_html, "html.parser")
deen_cents = deen_soup.find('sup', {'class':'c-price__cents'}).get_text()
deen_price = float('0.' + deen_cents)
#<sup class="c-price__cents">60</sup>

# COOP
coop_url = "https://www.coop.nl/de-klok-blik/product/8716700016358"
driver.get(coop_url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price')))
except TimeoutException:
    print("Loading took too much time!")

coop_html = driver.page_source
coop_soup = bs(coop_html, "html.parser")
coop_cents = coop_soup.find('span', {'class':'sup'}).get_text()
coop_price = float('0.' + coop_cents)

driver.close()

print('AH: ' + str(ah_price) + ' euro')
print('Jumbo: ' + str(jumbo_price) + ' euro')
print('Hoogvliet: ' + str(hoogvliet_price) + ' euro')
print('PLUS: ' + str(plus_price) + ' euro')
print('DEEN: ' + str(deen_price) + ' euro')
print('COOP: ' + str(coop_price) + ' euro')
