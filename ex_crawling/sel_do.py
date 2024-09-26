from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

option=webdriver.ChromeOptions()
option.add_argument('--headless=old')

def fn_search():
    driver = webdriver.Chrome(options=option)
    driver.find_element(By.XPATH,)
from tkinter import *
app =Tk()
app.title("이미지 검색 수집기")
entry =Entry(app, width=100)
entry.pack()
btn =Button(app, text='수집',command=fn_search) #def fn_search():
btn.pack()
txt =Text(app, width=100, height=50)
txt.pack()
app.mainloop()


