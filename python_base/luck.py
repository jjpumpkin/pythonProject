import random

from urllib3.util.util import to_str


# 함수명 make_lotto
# input x
# output 로 또번호

def make_lotto():
    lotto_num =set()
    while len(lotto_num)<6:
        num=random.randint(1,45)
        lotto_num.add(num)
    return list(lotto_num)



# 자체적으로 정렬후 출력 하려면 sorted 를 이용한다.
def make_lotto2():
    lotto_num =set()
    while len(lotto_num)<6:
        num=random.randint(1,45)
        lotto_num.add(num)
    return sorted(list(lotto_num))



# 0~n개 출력
# 함수명: usesr_lotto
# input 0~n
# output 로 또번호, 'x x 번호가 적용된 로또 번호' <-message 리턴
# 사용자가 입력한 번호를 포함시켜서 로도번호 생성
# 단 6개 이상이 들어오면 5개짜기 포함시키고 1개 랜덤값


def user_lotto(*args):
    user_num = list(args)[ :5]
    print(user_num)
    m = ','.join(map(str,user_num)) + " 번호가 적용된 로또 "
    lotto = set(user_num)
    while len(lotto)<6:
        num=random.randint(1,45)
        lotto.add(num)
    return m,sorted(lotto)






# 자체 실행일 때만 실행이되도록 처리해줌
if __name__ == '__main__':
    # 기본 오름차순 정렬
    arr = make_lotto()
    arr.sort()
    print(arr)

    # 내림차순 정렬
    arr2 = make_lotto()
    arr2.sort(reverse=True)
    print(arr2)

    arr = [1,2,3]
    message = ','.join(map(str,arr)) # map(function, iterable)
    print(message)

    arr2=['1','2','3']
    message2 = ','.join(arr2)
    print(message2)
else:
    print("임포트 했군")

