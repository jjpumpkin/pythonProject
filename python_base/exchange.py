import requests


# 달러 to 한화 함수를 작성해 주세요
# input 달러 금액 (ex: 10)
# output 원화 금액 (ex:13421.04544)

def fn_to_krw(chan):
    url = "https://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    if res.status_code ==200:
        data=res.json()
        change = data['rates']['KRW']* chan
        return change

print(fn_to_krw(10))
print(fn_to_krw(220.91))

usd = 220.91
print(f'%d 달러는 한화로 %.2f'%(usd,fn_to_krw(usd)))


def fn_change(money):
    url = f"https://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    if res.status_code ==200:
        data=res.json()
        exchange = data['rates'][money]
        return exchange

print()