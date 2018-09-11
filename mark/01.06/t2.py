from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
print(soup.prettify())

print('~~~~~~~~~~~')
print(1, soup.title)
print(2, soup.title.name)
print(3, soup.title.string)
print(4, soup.title.parent.name)
print(5, soup.p)
print(6, soup.p['class'])
print(7, soup.a)
print(8, soup.find_all('a'))
print(9, soup.find(id='link3'))


for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())
