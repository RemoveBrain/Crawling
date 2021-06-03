#========================================
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.naver.com")
#========================================
from bs4 import BeautifulSoup

html = driver.page_source
html_parsing = BeautifulSoup(html,"lxml")
# print(html_parsing)

#=======================================

#===========웹페이지내 크롤링 시작
mailtoweb = html_parsing.select(".group_nav > .list_nav.type_fix > .nav_item > .nav")
# print(mailtoweb)

for nav in mailtoweb:
    print(nav.text)
