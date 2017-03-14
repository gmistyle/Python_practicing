import requests
import time
import os
import re
import urllib.request
from bs4 import BeautifulSoup

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
        soup = BeautifulSoup(resp.text, 'html.parser')#整理html
        return soup

##取得所有圖片連結
def get_articles(soup):
    articles = []
    divs = soup.find_all('div', 'PostEntry_container_245XM')#文章區塊

    for d in divs:#擷取所有文章區塊內的資訊
        push_count = d.find('div', "PostLikeCount_likeCount_2uhBH").string#愛心數
        if d.find('a'):
            href = d.find('a', 'PostEntry_entry_2rsgm')['href']#文章連結
            title = d.find('strong').string#文章標題

            articles.append({
                'title': title,
                'href': href,
                'push_count': push_count
                })
    img_urls = []
    url = []
    DCARD_URL = 'https://www.dcard.tw'
    for article in articles:#抓取原始IMG_URL
        print('Processing', article)
        soup = get_web_page(DCARD_URL + article['href'])
        links = soup.find_all('img', "GalleryImage_image_3lGzO")
        for link in links:
            if re.match(r'^https?://(i.)?(m.)?imgur.dcard.tw', link['src']):  # 判斷是否為圖片連結
                img_urls.append(link['src'])
    try:
        for img_url in img_urls:
            img_url = img_url.replace('//', '//i.')
            img_url = img_url.replace('dcard.tw', 'com')
            url.append(img_url)
    except Exception as e:
        print(e)
    return url

#爬蟲
def DCARD_crawler(website, start):
    page = get_web_page(website)
    url = get_articles(page)
    fname = start
    for u in url:
        print('download picture_' + str(fname))
        urllib.request.urlretrieve(u, os.path.join('dcard', str(fname) + '.jpg'))
        fname += 1

url = DCARD_crawler('website', 0)

#os.makedirs(foldername) #創建圖片資料夾，創在腳本所在路徑
#https://i.imgur.com/
