from selenium import webdriver
import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://weibo.com/7407968306/profile?topnav=1&wvr=6&is_all=1')
# print(r.status_code)

driver = webdriver.Chrome('./bin/chromedriver.exe')
driver.get('https://weibo.com/u/7407968306?ssl_rnd=1607320519.9095&is_all=1')

lit = driver.find_elements_by_xpath("//*[@isfastforward='1']")
print(lit)
# isfastforward
# isforward