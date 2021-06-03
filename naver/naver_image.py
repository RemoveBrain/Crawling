import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

#홈페이지 뜨기전에 기다려주기.(3초이내 뜨면 알아서진행됨..?)
driver.implicitly_wait(3)
driver.get("https://www.naver.com")

from bs4 import BeautifulSoup

html = driver.page_source
html_parsing = BeautifulSoup(html,"lxml")

#프로그래스바
from tqdm import tqdm

keyword = "블랙핑크"

print("접속중")

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC"
driver.get(url)

imgs = driver.find_elements_by_css_selector("img._image")
#print(imgs)

result = []
for img in imgs:
    if "http" in img.get_attribute('src'):
        result.append(img.get_attribute('src'))  
#print(result)

driver.close()
print("수집완료")

#OS
import os

if not os.path.isdir(f"./{keyword}"):
    os.mkdir(f"./{keyword}")
else:
    print("폴더 존재")
    
print("크롤링한 사진을 폴더에 저장")

from urllib.request import urlretrieve

for idx, link in tqdm(enumerate(result)):
    start = link.rfind('.')
    end = link.rfind('&')
    filetype = link[start:end]
    
    urlretrieve(link, f"./{keyword}/{keyword}{idx}{filetype}")
    
print("이미지 크롤링 완료")
