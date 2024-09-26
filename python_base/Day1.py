# 주석 ctrl +/
# 주석은 코드 실행에 영향을 주지 않음.
'''
    다중 주석
    코드에 영향을 주지 않음
'''
from symbol import power

print('hi') #콘솔 프린트

num =10
print(num ,type(num))
# Type () <-내장 함수 변수의 타입을 리턴함

num =3.14 # 다른 타입을 할당해도 오류 안남
print (num ,type(num))
# 변수는 예약어 사용이 안되며 스네이크 표기법을 사용함 _ 사용
mem_nm ='Hello, Nick'
msg ='''
문자열이 길때 """ 따옴표 or 쌍 따옴표 3개로 열고닫음 (공백 까지 인식)
'''
print(msg)
print('Hello'*100) # 문자열 곱하기 가능
nm=mem_nm.replace('Hello','hi')
print(nm)
arr = nm.split(',') # 구분자로 잘라서 배열로 리턴.(디퐅르 공백1)
print(arr) #[] = 배열

# 동적 배열 (Dynamic Array)
# [] <-- 비어있는 배열
arr2 = [1,True,"Hi",[2,3,['Nick']]] # type 자유로움
print(arr2[1]) # index 값 1번 value 로 접근
print(arr2[3][2]) # index 3번에 2번째 요소
print(arr2[3][2][0]) # index 3번에 2번째 요소의 0번
print(arr2[-1])     # 배열의 마지막 요소에 접근
arr3 = [1,2,3,4,5] * 10 # 배열 곱하기 기능
print (arr3)

# 슬라이스 기능
print(arr3[1:4]) # 1번 인덱스부터 4 인덱스 -1 까지
print(arr3[ :3]) # 처음 부터 3 인덱스 -1 까지
print(arr3[3: ]) # 3 번부터 끝까지
print(len(arr3)) # len 사이즈를 리턴

# 튜플 배열과 같이 인덱스로 데이터에 접금하며 슬라이싱을 지원 (하지만 수정이 안됨)
t = (1,3,5) # 수정이 안되기 떄문에 초기값을 할당해야함
print(t[-1])
print(t[0])
print(t[1:])

t2 = (7,8)
print(t2)
t3 = t + t2 # 병합
# 병합은 가능하지만 수정은 불가능하다.
print(t3)
# t3[1] =1 오류남 튜플은 수정이 안됨.

# Dictonary (dict) key-value 쌍을 요소로 가지는 자료형
# {} 비어있는 딕셔너리
mate = {'펭수' : 100,'길동' : 90,'동길' : 80 }
print(mate,type(mate))
print(mate['펭수']) # key 로 value 접근
mate['펭수'] =99 # 수정
print(mate.items())

# set 중복을 허용하지 않으며
# set() <-- 비어있는 set 선언
lotto={1,2,2,4,5,6}
print(lotto,type(lotto))
#{} 로 표현하지만 {}선언은 비어있는 딕셔너리
my_set ={}
print(my_set,type(my_set))

my_set =set()
print(my_set,type(my_set))


