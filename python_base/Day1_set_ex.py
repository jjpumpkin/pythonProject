# 로또 번호 생성
# 사용자 입력 수량 만큼
# 1~45의 6자리 로또 번호를 생성하여 출력하시오.
# 6개의 1~45 수는 중복이 있으며 안됨 {1,2,2,3,4,5} 안됨

import random
lott_num = random.randint(1, 45)

# #비어있는 셋
# ex =set()
# # 요소 추가
# ex.add(5)
# print(ex)
# #set  길이
# print(len(ex))
# user_in =int(input("몇개 생성할까요?"))



use_in = int(input("수량 입력："))
for i in range(use_in):
    ex = set()
    while len(ex)<6:
        lott_num = random.randint(1, 45)
        ex.add(lott_num)
    print("행운의 로또 번호:",ex)




