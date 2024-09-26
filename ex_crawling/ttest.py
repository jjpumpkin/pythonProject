import urllib.request as req
import os

# url로 이미지 저장하기
image_path="./img"
if not os.path.exists(image_path):
    os.mkdir(image_path)
url="https://image.a-rt.com/art/product/2023/09/13123_1695342188816.jpg?shrink=580:580"

req.urlretrieve(url, "신발2.jpg")

# 페이지 상세 설명 나오게

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