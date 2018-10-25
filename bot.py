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

driver.close()

print('AH: ' + str(ah_price) + ' euro')
print('Jumbo: ' + str(jumbo_price) + ' euro')
print('Hoogvliet: ' + str(hoogvliet_price) + ' euro')