import requests
from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import urllib.request as req



option = webdriver.ChromeOptions()
option.add_argument('--headless')


url = "https://www.hanatour.com/package/international"

chromedriver_autoinstaller.install(True)


def fn_search():

    txt.delete("1.0", END)

    driver = webdriver.Chrome(options=option)

    user_input = entry.get()

    driver.implicitly_wait(1)

    driver.get(url)
    time.sleep(1)

    body = driver.find_element(By.TAG_NAME, 'body')

    input_search = driver.find_element(By.ID, 'input_keyword')
    input_search.send_keys(user_input)
    driver.find_element(By.CSS_SELECTOR, 'button.btn_search').click()

    driver.find_element(By.XPATH, '//a[contains(text(), "해외여행 더보기")]').click()

    time.sleep(5)

    res = requests.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    div = soup.select_one('.prod_list')
    if div:
        lis = div.find_all('li')

        for li in lis:
            name = li.select_one('.tit.eps2').text.strip()
            price = li.select_one('.price').text.strip()
            txt.insert(END, "=" * 30 + "\n")
            txt.insert(END, name + '\n')
            txt.insert(END, price + '\n')
            txt.insert(END, "=" * 30 + "\n")





    # print(soup.prettify())

def fn_image():
    query = entry.get()

    txt.delete("1.0", END)

    txt.insert(END, "=" * 30 + "\n")
    txt.insert(END, query+"이미지 검색 및 저장")
    txt.insert(END, "수집을 시작 합니다!! :-)" + '\n')
    txt.insert(END, "=" * 30 + "\n")

    count = 0
    del_count = 0
    file_path = ""

    url = f'https://www.google.com/search?q={query}'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(1)

    driver.find_element(By.XPATH, '//div[contains(text(), "이미지")]').click()

    current_h = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(f'window.scrollTo(0, {current_h});')

        time.sleep(2)

        new_h = driver.execute_script("return document.body.scrollHeight")

        if current_h == new_h:
            break;

        current_h = new_h


    body = driver.find_element(By.TAG_NAME, 'body')
    imgs = body.find_elements(By.TAG_NAME, 'img')
    img_set=set()

    for img in imgs:
        if img.get_attribute('src') != None:
            img_set.add(img.get_attribute('src'))

    print(img_set)
    driver.close()



    root  = './'
    img_dir= os.path.join(root, query)

    if not os.path.exists(img_dir):
        os.mkdir(img_dir)


    for i , v in enumerate(img_set):
        file_path = os.path.join(img_dir, str(i) + '.png')
        try:
            req.urlretrieve(v, file_path)
            count += 1
        except Exception as e:
            print(str(e))

    for filename in os.listdir(img_dir):
        file_path = os.path.join(img_dir, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            print(file_size, file_path)

            if file_size < 1024:
                print('delete file : ', file_size, file_path)
                os.remove(file_path)
                del_count += 1

    txt.insert(END, "=" * 30 + "\n")
    txt.insert(END, "저장된 사진의 경로 : " + file_path + '\n')
    txt.insert(END, "찾은 사진의 개수 : " + str(count) + '\n')
    txt.insert(END, "용량 미달로 삭제된 사진의 개수 : " + str(del_count) + '\n')
    txt.insert(END, "총 저장한 사진의 개수 : " + str(count - del_count) + '\n')
    txt.insert(END, "=" * 30 + "\n")

from tkinter import *

app = Tk()
app.title("Tour Search")

entry = Entry(app, width=150)
entry.pack()

btn = Button(app, text='여행 상품 검색', command=fn_search)
btn.pack()

btn2 = Button(app, text='구글 이미지 저장', command=fn_image)
btn2.pack()

btn3 = Button(app, text='Exit', command=exit)
btn3.pack()

txt = Text(app, width=150, height=50)
txt.pack()

btn.pack()
btn2.pack()
app.mainloop()
