import random
from operator import truediv

#random 난수 생성 기능 제공
# 업다운 게임
# 3번만 기회
# 사용자 입력이 맞으면 '정답' 작으면 '업', 크면 '다운' 출력
# 틀릴 때 마다 몇변의 기회가 있는지 출력
print(("*"*10)+" 업다운 게임 "+("*"*10))
flag =True
com_num = random.randint(1, 10)  # 1부터 10 사이의 정수 리턴
# count = 3
# while flag:
#
#     num = int(input("1~10 사이의 정수를 입력하세요: "))
#
#     if count >0:
#
#         if num > com_num:
#             print('다운')
#             count -=1
#             print('남은기회:',count)
#
#
#         elif num < com_num:
#             print('업')
#             count -=1
#             print('남은기회:', count)
#
#         else :
#             print('정답입니다')
#             break
#     elif count ==0:
#         print('다음 기회에... 정답은:',com_num)
#         break


cnt =3
while cnt >0:
    user_num = int(input("정수 입력"))
    # 업다운 조건
    if user_num < com_num:
        print("업!")
    elif user_num > com_num:
        print("다운!")
    elif user_num ==com_num:
        print("정답!")
        break
    cnt-=1
    if cnt != 0:
        print('남은 기회',cnt)
    else:
        print('다음 기회 정답은:',com_num)



