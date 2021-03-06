from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time

driver = webdriver.Chrome("./chromedriver.exe")

driver.implicitly_wait(3)

driver.get("https://www.youtube.com/watch?v=MssCLewODGc")

title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
print("영상 제목 : ",title.text)

channel = driver.find_element_by_xpath('//*[@id="text"]/a')
print("채널 명 : ",channel.text)

driver.find_elements_by_xpath('//*[@id="more"]/yt-formatted-string')[0].click() #자세히 누르기

time.sleep(2)
# TimeStamp 크롤링=======================
i = 3
j = 4
time_list = []
des_list = []
while 1 :
    time_stamp = driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string/a['+str(i)+']')
    des = des = driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string/span['+str(j)+']')
    if time_stamp.text.find(':') == -1 :
        break;
    time_list.append(int(time_stamp.text[0:2])*60 + int(time_stamp.text[3:]))
    des_list.append(des.text)
    i = i+1
    j = j+1
#========================================
print("timestamp : ",time_list)
print("description : ",des_list)
