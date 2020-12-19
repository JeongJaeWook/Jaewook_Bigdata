from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
#print(req)
soup = BeautifulSoup(req,'html.parser')

#print(soup)

##sp_nws1 > dl > dt > a

'#main_pack > div.news.mynews.section._prs_nws > ul'
#articles = soup.select_one('#sp_nws1 > dl > dt > a')

#print(articles.text)

articles2 = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul>li')

for arti in articles2:
    title = arti.select_one('dl > dt > a').text
    url = arti.select_one('dl > dt > a')['href']
    comp = arti.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')

    # sp_nws1 > dl > dd.txt_inline > span._sp_each_source
    print(comp,title,url)



driver.quit()