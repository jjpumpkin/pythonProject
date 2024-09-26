import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)

image_path="./img2"
if not os.path.exists(image_path):
    os.mkdir(image_path)
url="https://abcmart.a-rt.com/display/category/main?ctgrNo=1000000246&page=1"
# driver.get(url)
# time.sleep(1)
# soup=BeautifulSoup(driver.page_source,"html.parser")
# # driver.close()
# # res=requests.get(url)
# # soup=BeautifulSoup(res.content,"html.parser")
# # print(soup.prettify())
# div= soup.select_one(".detail-thumbs-wrap")
# img = div.select_one('img')
# req.urlretrieve(img['src'], "신발.jpg")
# req.urlretrieve(v['src'], str(i)+".jpg")

driver=webdriver.Chrome()
driver.get(url)
time.sleep(1)
soup=BeautifulSoup(driver.page_source,"html.parser")
div = soup.select_one('.col-list.prod-list.category-prod-list.col-4.type-2')
imgs = div.select('.img-wrap')
file_name = ""
for i, v in enumerate(imgs):
    img = v.select_one('img')
    file_name = os.path.join(image_path, f"{i}.jpg")
    req.urlretrieve(img['src'], file_name)





