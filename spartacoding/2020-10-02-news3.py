from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook


wb = Workbook()
ws1 = wb.active
ws1.title = "articles_crawl" #시트제목
ws1.append(["신문사", "제목", "url"])

driver = webdriver.Chrome('chromedriver.exe')
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"
driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req,'html.parser')

articles2 = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul>li')

for arti in articles2:
    title = arti.select_one('dl > dt > a').text
    url = arti.select_one('dl > dt > a')['href']
    comp = arti.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
    ws1.append([comp,title,url])


driver.quit()
wb.save(filename='articles.xlsx')