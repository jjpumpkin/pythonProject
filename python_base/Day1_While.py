# 반복문은 while<조건식> 이 true 일 떄 반복
i =1
while i<=5:
    i += 1
    if i ==2:
        continue # continue 를 만나면 하위내용을 건너뒴
        #break # 만나면 반복문 즉시 종료
    print(i)
    # python 은 증감 연산자는 없음
    flag = True
    while flag:
        msg = input("종류(q)")
        if msg ==0:
            flag = False