import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("./datasets/Titanic Passengers.csv")
print(df.shape)
print(df.columns)
print(df.info())
# 1:생존, 0:...
print(df.head(10))
# 여자: 1, 남자:0
df['sex'] =df['sex'].map({'female':1 , 'male': 0})
# age 평균값으로
df['age']=df['age'].fillna(value=df['age'].mean())
print(df.head())
df['first']=df['pclass'].apply(lambda x :1 if x ==1 else 0)
df['business']=df['pclass'].apply(lambda x:1 if x ==2 else 0)
df['economy']=df['pclass'].apply(lambda x:1 if x ==3 else 0)

x=df[['sex','age','first','business','economy']]
y=df['survived']
print(x.tail())
# random_state 데이터 분할시 동일하게 선택 되도록
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

model = LogisticRegression()
model.fit(x_train, y_train)
print("기울기:", model.coef_)
print("y절편",model.intercept_)
print("테스트 성능",model.score(x_test, y_test))
JACK = np.array([0.0,20.0,0.0,0.0,1.0])
ROSE = np.array([1.0,27.0,1.0,0.0,1.0])
PANGSU = np.array([0.0,10.0,0.0,1.0,0.0])
NICK =np.array([0.0, 2.0,1.0,0.0,0.0])
sample = model.predict([JACK,ROSE,PANGSU,NICK])
print("sample:" ,sample)
print(model.predict_proba([JACK, ROSE, PANGSU,NICK]))

