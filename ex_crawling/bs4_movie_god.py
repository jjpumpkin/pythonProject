import csv
from idlelib.iomenu import encoding

import requests
from bs4 import BeautifulSoup
import re

from ex_crawling.bs4_movie import detail_url

# csv 파일 읽기
url = "http://m.cine21.com"
with open("./data/movie.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="|")
    data = list(reader)

    arr = []

    for row in data:
        detail_url = url + row[3]
        res = requests.get(detail_url)
        title = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', row[0])

        soup = BeautifulSoup(res.content, "html.parser")
        div = soup.select_one('.review_writer')
        lis = div.find_all('li')

        with open("./data/" + title + ".csv", 'a', encoding="utf-8", newline='') as f:
            for li in lis:
                name = li.select_one('.name a').text
                num = li.select_one('.num').text
                review_txt = li.select_one('.review_txt').text
                arr.append([name, num, review_txt])

            write = csv.writer(f, delimiter="|")
            write.writerows(arr)
            arr = []
