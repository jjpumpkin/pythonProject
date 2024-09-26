import os
import requests
import csv
from bs4 import BeautifulSoup


with open('./movie.csv', 'r', encoding="utf-8") as f:

    url = "http://m.cine21.com"
    reader = csv.reader(f,delimiter="|")
    data = list(reader)
    for row in data:
        print(row)
        detail_url = url + row[3]
        print(detail_url)
        res = requests.get(detail_url)
        soup = BeautifulSoup(res.content, "html.parser")
        print(soup.prettify())
        # 각 영화이름으로 csv파일을 만들고
        # '평론가 이름|평점|관람평' 을 저장하세요
