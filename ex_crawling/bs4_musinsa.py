#정규 표현식 re를 써서 (re.sub(r'\D','',info
import requests
from bs4 import BeautifulSoup
import re
url="https://www.musinsa.com/mz/community-info?sort=uid&orderby=desc&p=1"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
if res.status_code ==200:
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.prettify())
    divs =soup.select('.listPost')
    for div in divs:
        # info = div.select_one('.info')
        info = div.select('.info span')
        print(re.sub(r'\D','',info[0].text))  # 숫자가 아닌 모든 것 제거
        print(re.sub(r'\D','',info[1].text))
        print(info[2].text)
        print(info[3].text)
else:
    print(res.text)