html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2" /> and
<a href="http://example.com/tillie" class="sister">Tillie</a>
<a href="http://example.com/tillie" class="sister">한글</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""
# pip install bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
# 구조화되게 출력
print(soup.prettify())
a_tag= soup.a
print(a_tag.name)
print(a_tag.text)
print(a_tag['href'])     #속성명으로
print(a_tag.get('id'))   # get 함수로 해당 속성 찾음
# find: 1개만(여러개라면 첫번째 등장하는)
# find_all :모두
a_all = soup.find_all('a')
for a in a_all:
  print(a.text)
  print(a['href'])

  a_all2 = soup.find_all('a', string=True) #text가 있는 a태그만
  print(' 텍스트 포함:',len(a_all2))
  import re
  # re 정규표현식 관련 라이브러리
  a_han =soup.find_all('a',string=re.compile(r'[가-힝]')) #한글이 있는
  print('한글 포함:',len(a_han))

  # select : 다건 css 셀렉터 사용
  # select_one :한건
  link1 =soup.select_one('#link1')
  print(link1)
  cls = soup.select('.sister')
  print(cls)




