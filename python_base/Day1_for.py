# 반복문 for
arr =['펭수','길동','동길']
# 방법 1. 값만 필요할 때
for v in arr:
    print(v)
# 방법2. 값, 인덱스 둘다 필요할 때
for i , v in enumerate(arr):
    print(i,v)
# 방법3. 단순 횟수 반복
for i in range(3):
    print(i)
for i in range(len(arr)):
    print(arr[i])

for i in range(1,4):
    print(i) # 1부터 ~4(-1) 까지
for i in range(2,11,2):
    print(i) # 2 부터 11(-1) 까지 2씩 증가


# 딕셔너리 for문
    # 키- 값으로 순서를 보장 하지 않지만 3.6 이루부터 보장함
    dic ={"수학":100,"영어":60,"국어":90}
    for k in dic:
        print(k,dic[k])

