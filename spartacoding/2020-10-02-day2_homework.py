from openpyxl import Workbook
from selenium import webdriver
from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#엑셀 생성
wb = Workbook()
ws1 = wb.active
ws1.title = "crawling_articles"
ws1.append(["신문사","제목","링크","썸네일_사진"])

#크롤링
driver = webdriver.Chrome('chromedriver.exe')
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"
driver.get(url)

req = driver.page_source
soup = BeautifulSoup(req,'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul>li')

for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    somenail = article.select_one('div > a > img')["src"]
    ws1.append([comp, title, url,somenail])



wb.save(filename='articles_jw.xlsx')
driver.quit() # 끝나면 닫아주기

#이메일로 해당 엑셀파일 보내기
# 보내는 사람 정보
me = "bigdatajw@gmail.com"
my_password = "game91757603"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
emails = ['jaewook111@naver.com']

for you in emails:

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "추석검색시 나오는 기사"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "테스트용입니다."
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("articles_jw.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())
s.quit()