# 문자열 포맷팅

# 방법1 (% 연산자 사용 %s 문자열 ,%d 정수, %.2f 소수점 2째 자리까지의 실수)
nm = "Nick"
age =20
height = 190.12951
formatted = "나는 %s 나이는 %d 키는 %.2f "% (nm,age,height)
print(formatted)

# 방법2 str,format()함수 사용
formatted2 = "나는 {0} 나이는 {1} 키는 {2} 진짜 {2}".format (nm,age,height)
print(formatted2)

# 방법3 . 파이선 3.6 이상에서 가능 (f-string)
print(f"나는 {nm} 나이는 {age} 키는 {height} 진짜 {height}")