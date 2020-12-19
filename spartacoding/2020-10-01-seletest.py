from bs4 import BeautifulSoup
from selenium import webdriver
import dload
import time

driver = webdriver.Chrome('chromedriver.exe') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%ED%95%9C%EA%B3%A0%EC%9D%80")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

#imgList > div:nth-child(1) > a > img
thumbnails = soup.select("#imgList > div > a > img")

i=10
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src,f'images_hw/{i}.jpg')
    i += 1
    # print(src)

driver.quit() # 끝나면 닫아주기