from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.pythontab.com/html/pythonhexinbiancheng/index.html'
url_list = [url]

for i in range(2, 19):
    url_list.append('http://www.pythontab.com/html/pythonhexinbiancheng/%s.html' % i)
# print(url_list)

source_list = []  # 标题+文字
for j in url_list:
    request = urllib.request.urlopen(j)  # 打开链接
    html = request.read()  # 读取所有源码
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')  # 解析网页
    titles = soup.select('#catlist > li > a')  # 查找.css选择器, id=catlist
    # print(titles)   # 标题
    links = soup.select('#catlist > li > a')
    # print(links)  # 文章链接
    for title, link in zip(titles, links):
        data = {
            'title': title.get_text(),  # 获取标题
            'link': link.get('href')  # 超链接
        }
        source_list.append(data)
        # print(source_list)

for l in source_list:
    request = urllib.request.urlopen(l['link'])
    html = request.read()
    soup = BeautifulSoup(html, 'html.parser')
    text_p = soup.select('#Article > div.content > p')
    text = []
    for t in text_p:
        text.append(t.get_text().encode('utf-8'))
        # print(text)
        title_text = l['title']
    # print(title_text)
    with open('study/%s.txt' % title_text, 'wb') as f:
        for a in text:
            f.write(a)
