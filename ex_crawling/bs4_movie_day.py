import os
import requests
import csv
from bs4 import BeautifulSoup


with open('./movie.csv', 'r', encoding="utf-8") as f:
    url = "http://m.cine21.com"
    reader = csv.reader(f, delimiter="|")
    data = list(reader)

    for row in data:
        movie_url = url + row[0]
        movie_title = row[1]
        print(movie_url)
        print(f"영화 제목: {movie_title}")

        # 파일 이름에서 특수 문자를 제거하여 유효한 파일 이름으로 변환
        safe_movie_title = "".join(c for c in movie_title if c.isalnum() or c in (" ", "_", "-")).strip()

        res = requests.get(movie_url)
        soup = BeautifulSoup(res.content, "html.parser")

        div = soup.select_one('.review_writer_area')
        if div:
            lis = div.find_all('li')

            with open(f"./{safe_movie_title}.csv", 'w', encoding="utf-8", newline='') as f:
                writer = csv.writer(f, delimiter="|")
                writer.writerow(["평론가 이름", "평점", "관람평"])

                for li in lis:
                    name = li.select_one('.name a').text.strip()
                    rating = li.select_one('.num').text.strip()
                    review = li.select_one('.review_txt').text.strip()
                    print("=" * 30)
                    print(name, rating, review)

                    # 각 항목을 별도의 행에 작성
                    review = review.strip()
                    writer.writerow([name, rating, review])
