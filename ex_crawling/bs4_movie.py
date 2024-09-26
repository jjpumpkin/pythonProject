import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os
image_path ="./img"
if not os.path.exists(image_path):
    os.mkdir(image_path)
url ="http://m.cine21.com/movie/boxoffice/history"
res =requests.get(url)
soup = BeautifulSoup(res.content,"html.parser")
div = soup.select_one('.lst_ranking_area')
# 상세정보 url
# 영화 제목
# 관객수
# 평점 정보
print("=" *60)
# print(detail, title, score, rating)
lis = div.find_all('li')
arr =[]
for li in lis:

    detail_url =li.select_one('.title a')['href']
    title =li.select_one('.title a').text
    score =li.select_one('.sub_info').text
    rating =li.select_one('.num').text
    print(detail_url, title, score, rating)
    print("=" * 100)
    arr.append([title,score, rating, detail_url])
print(arr)
import csv
with open("movie.csv", 'a', encoding="utf-8", newline='') as f:
    write = csv.writer(f, delimiter="|")
    write.writerows(arr)




