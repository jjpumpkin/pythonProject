import numpy as np
import matplotlib.pyplot as plt

# 공부한 시간x1, 과외시간 x2, 성적 y
x1 =np.array([2,4,6,8])
x2 =np.array([0, 4, 2, 3])
y =np.array([81, 93, 91, 97])
fig =plt.figure()
ax =fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y)
plt.show()
plt.scatter (x1, y)
# plt.show()
# 기울기 a1 ,a2 y절편 b
a1 = 0
a2 =0
b = 0
# 학습률
lr = 0.01
# 몇번 반복 할지(에포크)
epochs = 2001
# x 값이 총 몇개인지
n =len(x1)
for i in range(epochs):
    y_pred = a1 * x1 + a2 * x2 +b # 예측을 구하는 적
    error = y - y_pred # 실제 값과 비교한 오차
    a1_diff = (2 /n) * sum(-x1 * (error)) # 오차를 구하는 함수를 a로 편미분
    a2_diff = (2 / n) * sum(-x2 * (error))  # 오차를 구하는 함수를 a로 편미분
    b_diff = (2 / n) * sum(-(error))
    # 편미분이란 ? 여러 변수에 의해 정의된 함수에서 하나의 변수에 대해 미분하는 것
    # 나머지 변수는 고정 시키고, 특정 변수 하나에 대해서만 함수가 어떻게 변화하는지 알아보는,
    # 이 함수가 변수 x에 대해 어떻게 변화하는지, y에 대해 어떻게 변화하는지.
    a1 = a1-lr * a1_diff  # 학습률을 곱에 기준의 a 값을 업데이트
    a2 = a2- lr * a2_diff  # 학습률을 곱에 기준의 a 값을 업데이트
    b = b-lr * b_diff  # 학습률을 곱에 기준의 b값을 업데이트
    if i % 100 == 0:
        print(f"epoch=[i], 기울기a1={a1}, 기울기 a2={a2} y절편={b}")
