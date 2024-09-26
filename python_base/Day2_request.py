'''
        requests 는 파이썬에서 http의 요청을 쉽게 보낼 수 있도록 해주는 라이브러리
        주로 웹 사이트나 api와 통신 할 때 사용됨.
            - GET,POST,PUT,DELETE 요청처리
            - 응답 내용 파싱 : JSON OR TEXT 형태로
            - 요청시 자동으로 URL 인코딩 처리
            - 예외처리 (HTTP요청 중 발생 할 수 잇는 오류에 대해 예외 처리를 제공)
'''
import requests
# 없 다면 pip install requests

url ='https://api.upbit.com/v1/market/all'
res = requests.get(url)
print(res.status_code) # 정상 처리 되었는지 코드 값을 리턴 200 : 정상
if res.status_code ==200:
    data = res.json() # json 형태로 파싱 -- 딕셔너리와 배열 형태로 파싱 for /key 값으로 접근 가능
    for v in data:
        print(v['korean_name'],v['market'])

# 현재시세 가져오는 함수.
# input : market(코인코드)
# output : 현재 시장가 trade_price
# url ='https://api.upbit.com/v1/ticker?markets=KRW-BTC'

def current_price(market):
    # url = 'https://api.upbit.com/v1/ticker?markets='+market
    url =f"https://api.upbit.com/v1/ticker?markets={market}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        price =data[0]['trade_price']
    return price
print(current_price('KRW-BTC'))
print(current_price('KRW-ETH'))