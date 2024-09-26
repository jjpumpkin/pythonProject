from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

from ex_crawling.sel_hana import driver

url="https://www.hanatour.com/package/international"
# 백그라운드 실행되도록
option=webdriver.ChromeOptions()
option.add_argument('--headless=old')



def fn_search():
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    time.sleep(1)

    input_search =driver.find_element(By.ID, 'input_keyword')
    input_search.send_keys(entry.get())   # input  입력값
    driver.find_element(By.CSS_SELECTOR, 'button.btn_search').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="contents"]/div[3]/div[2]/div[1]/a').click()
    time.sleep(1)
    soup =BeautifulSoup(driver.page_source, 'html.parser')
    div =soup.select_one('.list')#클래스 .
    lis = div.find_all('li')
    for li in lis:
        name = li.select_one('.tit').text
        price = li.select_one('.price').text
        txt.insert(END, name + ":" + price +"\n" )

from tkinter import *
app =Tk()
app.title("tour search")
entry =Entry(app, width=100)
entry.pack()
btn =Button(app, text='search',command=fn_search) #def fn_search():
btn.pack()
txt =Text(app, width=100, height=50)
txt.pack()
app.mainloop()
