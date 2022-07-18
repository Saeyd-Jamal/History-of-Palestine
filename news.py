import requests as req
from bs4 import BeautifulSoup

def gazaAlanFun(gazaAlan):
    page = req.get('https://gazaalan.net/') # رابط الموقع المطلوب
    data = page.content
    soup = BeautifulSoup(data,'html.parser')
    title_page = soup.find('title').text # الكلاس الخاص بالنص لكل خبر
    img = soup.find('div',{"class": "news-image"}).find_all('img')
    for img_urls in img:
        img_url = img_urls["src"]
    head_news = soup.find('div',{"class": "news-content"}).find_all('h3')
    for head_news_urls in head_news:
        a_head_news = soup.find('div',{"class": "news-content"}).find_all('a')
        for a_head_new in a_head_news:
            href_head_new = a_head_new["href"]
            text_head_new = a_head_new.text
    gazaAlan['title_page'] = title_page
    gazaAlan['imgs'] = img_url
    gazaAlan['href_head_new'] = href_head_new
    gazaAlan['text'] = text_head_new

def aljazeeraFun(aljazeera):
    page = req.get('https://www.aljazeera.net/where/palestine/') # رابط الموقع المطلوب
    data = page.content
    soup = BeautifulSoup(data,'html.parser')
    head_news = soup.find('a',{"class": "u-clickable-card__link"}).find_all('span')
    for head_new in head_news:
        text_head_new = head_new.text
    url = soup.find('a',{"class": "u-clickable-card__link"})
    href_head_new = 'https://www.aljazeera.net'+url["href"]
    title_page = soup.find('title').text # الكلاس الخاص بالنص لكل خبر
    aljazeera['title_page'] = title_page
    aljazeera['imgs'] = 'https://www.aljazeera.net/wp-content/uploads/2022/04/t555.jpg?resize=770%2C513'
    aljazeera['href_head_new'] = href_head_new
    aljazeera['text'] = text_head_new


def alwatanFun(alwatan):
    page = req.get('https://www.alwatanvoice.com/arabic/index.html') # رابط الموقع المطلوب
    data = page.content
    soup = BeautifulSoup(data,'html.parser')
    head_news = soup.find('div',{"class": "home-featured"}).find('h2')
    for head_new in head_news:
        head_new_url_s = head_new['href']
        for head_new_s in head_new:
            head_new_text = head_new_s
        head_new_url = 'https://www.alwatanvoice.com/arabic/' + head_new_url_s
    img = soup.find('img',{"class": "lazy"})
    img_url = 'https:' + img['src']
    title_page = soup.find('title').text # الكلاس الخاص بالنص لكل خبر
    alwatan['title_page'] = title_page
    alwatan['imgs'] = img_url
    alwatan['href_head_new'] = head_new_url
    alwatan['text'] = head_new_text


def maannewsFun(maannews):
    page = req.get('https://www.maannews.net/') # رابط الموقع المطلوب
    data = page.content
    soup = BeautifulSoup(data,'html.parser')
    title_page = soup.find('title').text # الكلاس الخاص بالنص لكل خبر
    box_new = soup.find('a',{"class": "featured-3__item"})
    href_head_new = box_new['href']
    img = soup.find('div',{"class": "featured-3__image"}).find_all('img')
    for img_src in img:
        img_url =  img_src['data-src']
    text_head_new = soup.find('div',{"class": "featured-3__title"}).text
    maannews['title_page'] = title_page
    maannews['imgs'] = img_url
    maannews['href_head_new'] = href_head_new
    maannews['text'] = text_head_new

def qudspressFun(qudspress):
    page = req.get('https://www.qudspress.com/') # رابط الموقع المطلوب
    data = page.content
    soup = BeautifulSoup(data,'html.parser')
    title_page = soup.find('title').text # الكلاس الخاص بالنص لكل خبر
    box_new = soup.find('div',{"class": "entry-thumb"}).find_all('a')
    for box_new_s in box_new:
        href_head_new_s = box_new_s['href']
        href_head_new = 'https://www.qudspress.com/' + href_head_new_s
        for img_url_s in box_new_s:
            img_url = img_url_s['src']
    head_new = soup.find('h4',{"class": "entry-title"}).find_all('a')
    for text_head_new_s in head_new:
        for text in text_head_new_s:
            text_head_new = text
    qudspress['title_page'] = title_page
    qudspress['imgs'] = img_url
    qudspress['href_head_new'] = href_head_new
    qudspress['text'] = text_head_new