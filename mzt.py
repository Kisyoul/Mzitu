#-*- coding: UTF-8 -*-
import os;
from bs4 import BeautifulSoup;
import requests;
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url = 'http://www.mzitu.com/all/'
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.text,"lxml")
all_url = soup.find("div","all").find_all("a")
for url in all_url:
    rel_url = url['href']
    title = url.get_text()
    path = title
    os.makedirs(os.path.join("D:\mzitu", path))
    os.chdir("D:\mzitu\\" + path)
    img_res =  requests.get(rel_url,headers = headers)
    img_soup = BeautifulSoup(img_res.text,"lxml")
    max_span = img_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    print title
    for page in range(1, int(max_span) + 1):
        page_url = rel_url + '/' + str(page)
        image_html = requests.get(page_url,headers =headers)
        pic_soup = BeautifulSoup (image_html.text,"lxml")
        main_img_url = pic_soup.find("div","main-image").find("img").get("src")
        img = requests.get(main_img_url, headers=headers)
        f = open(str(page) + '.jpg', 'ab')
        f.write(img.content)
        f.close()

