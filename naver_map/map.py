from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

# driver 실행
# driver = webdriver.Chrome("./chromedriver", options=options)
# 옵션 적용시 브라우저가 팝업되지않고 과정을 볼수 없음.
driver = webdriver.Chrome("./chromedriver")

def call(start,via,goal):  
    driver.implicitly_wait(4)
    driver.get("https://map.naver.com/v5/directions/-/-/-/car?c=14141252.0748155,4511465.0210149,15,0,0,0,dh")
    driver.implicitly_wait(4)

    #출발지 xpath
    startbox = driver.find_element_by_xpath('//*[@id="directionStart0"]')
    #도착지 xpath
    goalbox = driver.find_element_by_xpath('//*[@id="directionGoal1"]')
    #검색버튼 xpath
    action = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[2]/button[3]')
    #경유지 버튼 xpath
    via_btn = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/directions-search/div[2]/button[2]')

    #출발지 입력
    startbox.send_keys(start)
    startbox.send_keys(Keys.ENTER)
    time.sleep(4)
    
    #경유지 팝업 & 입력
    via_btn.click()
    time.sleep(3)
    viabox = driver.find_element_by_xpath('//*[@id="directionVia1"]')
    viabox.send_keys(via)
    viabox.send_keys(Keys.ENTER)
    time.sleep(3)
    
    #도착지 입력
    goalbox.send_keys(goal)
    goalbox.send_keys(Keys.ENTER)
    time.sleep(3)

    #검색버튼.
    action.send_keys(Keys.ENTER)
    time.sleep(3)

    #검색 완료후 html 파싱
    html = driver.page_source
    html_parsing = BeautifulSoup(html,"lxml")
    #"출발 -> 경유 -> 도착"의 시간을 텍스트로 가져오기
    goal_time = html_parsing.select_one('readable-duration').get_text()

    return goal_time

if __name__ == '__main__':
    point = [] #장소 입력받을 리스트.
    index =1 #각 결과값에 매길 인덱스.
    MIN = 99999 #결과갑중 최소값 저장할 변수. 디폴트는 무조건 큰값.
    MIN_index = 0 #최소값을 가져온 인덱스 저장.

    point.append(input("첫번째 위치를 입력해주세요 : "))
    point.append(input("두번째 위치를 입력해주세요 : "))
    point.append(input("세번째 위치를 입력해주세요 : "))
    print("=============================================")
    for i in range(len(point)):
        #출발지 , 경유지 , 도착지 순서로 함수에 입력하고 result에 결과 리턴받음.
        result = call(point[i],point[(i+1)%3],point[(i+2)%3])
        print(f"{index}. {point[i]}에서 {point[(i+1)%3]}을 거쳐 {point[(i+2)%3]}까지 {result}걸립니다.")

        #result에 저장된 시간에서 숫자값만 잘라서 int 형으로 Time 변수에 저장
        if result.find('시') == -1: 
            Time = int(result[0:result.find('분')])
        else :
            if result.find('분') == -1:
                Time = int(result[0:result.find('시간')])*60
            else :
                Time = int(result[0:result.find('시간')])*60 + int(result[-3:-1])

        #Time과 MIN 비교해서 작으면 MIN에 저장 + 인덱스도 저장.
        if Time < MIN:
            MIN = Time
            MIN_index = index
        #결과값에 매길 인덱스값 증가.
        index+=1

        #====================================================
        #위의 내용에서 경유지 도착지 순서만 바꾸어 다시 계산.
        #====================================================

        result = call(point[i],point[(i+2)%3],point[(i+1)%3])
        print(f"{index}. {point[i]}에서 {point[(i+2)%3]}을 거쳐 {point[(i+1)%3]}까지 {result}걸립니다.")
        if result.find('시') == -1:
            Time = int(result[0:result.find('분')])
        else :
            if result.find('분') == -1:
                Time = int(result[0:result.find('시간')])*60
            else :
                Time = int(result[0:result.find('시간')])*60 + int(result[-3:-1])
        if Time < MIN:
            MIN = Time
            MIN_index = index
        index+=1
            
    #최소값이 들어있던 인덱스와 값 출력.
    print("=============================================")
    print(f"{MIN_index}번째가 {MIN}분으로 가장 짧습니다.")

    #크롬드라이버 종료.
    driver.quit()
