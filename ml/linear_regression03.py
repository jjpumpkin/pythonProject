import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("./datasets/heights.csv")
x = df['height']
y = df['weight']
plt.scatter(x, y)
plt.show()
x =np.array(x.round())
y =np.array(y.round())
# plt.show()
# 기울기 a , y절편 b
a = 0.1
b = 0.1
# 학습률
lr = 0.0001
# 몇번 반복 할지(에포크)
epochs = 2001
# x 값이 총 몇개인지
n =len(x)
for i in range(epochs):
    y_pred = a * x +b # 예측을 구하는 적
    error = y - y_pred # 실제 값과 비교한 오차
    a_diff = (2 /n) * sum(-x * (error)) # 오차를 구하는 함수를 a로 편미분
    b_diff = (2 / n) * sum(-(error))
    # 편미분이란 ? 여러 변수에 의해 정의된 함수에서 하나의 변수에 대해 미분하는 것
    # 나머지 변수는 고정 시키고, 특정 변수 하나에 대해서만 함수가 어떻게 변화하는지 알아보는,
    # 이 함수가 변수 x에 대해 어떻게 변화하는지, y에 대해 어떻게 변화하는지.
    a = a-lr * a_diff  # 학습률을 곱에 기준의 a 값을 업데이트
    b = b-lr * b_diff  # 학습률을 곱에 기준의 b값을 업데이트
    if i % 100 == 0:
        print(f"epoch=[i], 기울기a={a}, y절편={b}")
# 최적의 a, b
y_pred = a * x + b
plt.scatter(x, y)
plt.plot([min(x), max(y)], [min(y_pred),max(y_pred)])
plt.show()
