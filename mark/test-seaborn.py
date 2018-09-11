from bs4 import BeautifulSoup
from urllib import request


url = 'http://www.pythontab.com/html/pythonhexinbiancheng/index.html'
url_list = [url]

for i in range(2, 19):
    url_list.append('http://www.pythontab.com/html/pythonhexinbiancheng/%s.html' % i)

source_list = []  # 标题+文字
for j in url_list:
    request = request.urlopen(j)  # 打开链接
    html = request.read()   # 读取所以源码
    soup = BeautifulSoup(html, 'html.parser')  # 解析网页
    titles = soup.select('#catlist > li > a')
    links = soup.select('#catlist > li > a')
    for title, link in zip(titles, links):
        data = {
            'title': title.get_text(),
            'link': link.get('href')
        }
        source_list.append(data)



for l in source_list:
    request = request.urlopen(l['link'])
    html = request.read()
    soup = BeautifulSoup(html, 'html.parser')
    text_p = soup.select('#Article > div .content > p')
    text = []
    for t in text_p:
        text.append(t.get_text().encode('utf-8'))
        title_text = l['titles']

    with open('study/%s.txt' % title.text, 'wb') as f:
        for a in text:
            f.write(a)















