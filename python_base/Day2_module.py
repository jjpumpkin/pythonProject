import math
# math모듈 안에 있느 factorial 함수 호출
print(math.factorial(5))
from math import factorial as f
# math 모듈 안에 있는 factorial 함수를 f로 별칭을 붙여서 호출
print(f(10))

import luck
print(luck.make_lotto())
# 해당 파일 내에 다른 로직들도 같이 출력이 됨.
