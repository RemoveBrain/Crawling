
#네이버 메인 페이지 배너 (메일,카페,블로그 ~~ 책,웹툰) 부분 텍스트 크롤링 

import requests 
from bs4 import BeautifulSoup

url = "https://www.naver.com"

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


# class 명이 'list_nav type_fix'인 ul 태그 찾기
ul = soup.find('ul', {'class' : 'list_nav type_fix'})
ul2 = soup.find('ul', {'class' : 'list_nav NM_FAVORITE_LIST'})
# ul 태그 안에 있는 li 태그 모두 찾기
li = ul.find_all('li')
li2 = ul2.find_all('li')

for i in li:
    print(i.text) #실행 결과에 string과 비교해 놓았다.

for i in li2:
    print(i.text) #실행 결과에 string과 비교해 놓았다.
