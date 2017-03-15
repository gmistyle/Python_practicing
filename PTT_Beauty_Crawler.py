import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request

#取得該網址的source code
def get_web_page(url):
    time.sleep(0.5)
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}## over 18 means you are an adult
    )
    if resp.status_code != 200:## 200means normal, not like error 404
        print('Invalid url:', resp.url)
        return None
    else:
        soup = BeautifulSoup(resp.text, 'html.parser')
        return soup

##取得該source code裡面的資訊並整理
def get_articles(soup, push):
    articles = []
    divs = soup.find_all('div', 'r-ent')
    for d in divs:#儲存所有文章的資訊
        push_count = 0
        if d.find('div', 'nrec').string:
            if d.find('div', 'nrec').string == '爆':
                push_count = 100
            else:
                try:
                    push_count = int(d.find('div', 'nrec').string)
                except ValueError: # 若轉換失敗，不做任何事，push_count 保持為 0
                    pass
        if d.find('a'):
            href = d.find('a')['href']#取得文章網址
            title = d.find('a').string#取得文章標題
            articles.append({
                'title': title,
                'href': href,
                'push_count': push_count
                })
    img_urls = []
    url = []
    title = []
    PTT_URL = 'https://www.ptt.cc'
    for article in articles:#找出所有圖片連結
        if article['push_count'] >= push:
            print('Processing', article)
            soup = get_web_page(PTT_URL + article['href'])
            links = soup.find(id='main-content').find_all('a')
            for link in links:
                if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
                    img_urls.append(link['href'])
                    title.append(article['title'])

    for img_url in img_urls:#將圖片連結改成可下載
        if img_url.split('//')[1].startswith('m.'):
            img_url = img_url.replace('//m.', '//i.')
        if not img_url.split('//')[1].startswith('i.'):
            img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
        if not img_url.endswith('.jpg'):
            img_url += '.jpg'
        url.append(img_url)
    return url, title

##儲存圖片##存成資料夾
def save(img_urls, title, start):
    for file in set(title):
        os.makedirs(file.strip())
    cnt = start
    for url, name in zip(img_urls, title):
        foldername = name.strip()
        try:
            print('download picture:'+str(cnt))
            urllib.request.urlretrieve(url, os.path.join(foldername, str(cnt)+'.jpg'))
            cnt +=1
        except:
            pass

## PTT crawler
def PTT_beauty_crawler(from_page, to_page, start_name_num, push):
    url_0 = 'https://www.ptt.cc/bbs/Beauty/index'
    url_2 = '.html'
    for number in range(from_page, to_page):
        print('# # # # # ' + 'processing page:' + str(number) + ' # # # # # ')
        URL = url_0 + str(number) + url_2  # 重複取得網址
        page = get_web_page(URL)
        url, title = get_articles(page, push)
        save(url, title, start_name_num)

PTT_beauty_crawler(2109, 2115, 0, 100)
##PTT_beauty_crawler(起始頁數, 結束頁數, 第一個檔案名稱(數字), 幾推以上)
##頁數從0到2109，(2017/3/15最後一頁為2109)
##Reference : <http://www.pycone.com/blogs/python-data-science-tutorial-1>
