#========================================
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.hankookilbo.com/News/Read/A2021042715550005147?did=NS&dtype=2")
#========================================
from bs4 import BeautifulSoup

html = driver.page_source
html_parsing = BeautifulSoup(html,"lxml")

#=======================================

#===========웹페이지내 크롤링 시작

# 기사의 제목
title = html_parsing.find("h2",{"class" : "title"})
print(title.text)

# 기사의 내용
contents = html_parsing.find_all("p",{"class" : "editor-p"})

print("기사내용 :")
for content in contents:
    try :
        print(content.text)
        print()
    except :
        print("error")
    
#기자의 이름 + 이메일
reporter_name = html_parsing.find("div",{"class":"writer"})
print(reporter_name.text)
        

# 기사의 이미지
image_all = html_parsing.find_all("div",{"class" :"editor-img-box"})
# print(image_all)
# for image in image_all:
#     image_result = image.find("img")["src"]    
#     print(image_result)
    
idx = 1
for image in image_all:
    image_result = image.find("img")["src"]
    print(str(idx) + "번째 이미지 : ",image_result)
    idx += 1
    print()
    
                                    

driver.close() # 크롤링끝나면 자동으로 브라우저 닫기.
