# 함수선언 def :
from idlelib.pyshell import restart_line


def adder(a,b):
    sum = a+b
    return sum

print (adder(10,2))
#  한수는 위에서 작성을 하고 밑에서 호출해야함
# return 은 0~n개 가능
def return_test():
    return 10, "^^",3.14
a,b,c = return_test()
print(a,b,c)
print(a)
data = return_test()
print(data)
# 각각 변수에 리턴값을 지정 할 수 있고 , 하나의 변수에 튜플 형식으로 저장이 가능하다.
# 디폴트 매개변수
def fn_default(nm, level=1):
    print(nm,level)
fn_default("펭수")
fn_default("길동",10)
# 매개변수가 하나만 들어올 경우 디폴트 값이 출력

# 가변 매개변수
def fn_clac (operator, *args):
    result =0
    if operator == '+':
        for n in args:
            result +=n
    elif operator =='*':
        result =1
        for n in args:
            result*=n
    return result

print(fn_clac('+',1,2,3,4,5,6,7))
print(fn_clac('+'))
print(fn_clac('*',2,10,9))
# 가변길이 파라미터의 경우 매개변수가 빠져도 오류가 나지않고 출력됨