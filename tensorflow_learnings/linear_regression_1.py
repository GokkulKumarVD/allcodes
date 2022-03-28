import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\linear_regression\\canada_per_capita_income.csv")
df.columns=['year','price']
# plt.xlabel('year')
# plt.ylabel('per capita income (US$)')
# plt.scatter(df[['year']],df[['per capita income (US$)']])

x = df[['year']]
y = df[['price']]



reg = linear_model.LinearRegression()

x_train,x_test,y_train,y_test  =  train_test_split(x,y,train_size=0.8)


reg.fit(x_train, y_train)
reg.predict(x_test)

reg.score(x_test,y_test)

# reg.predict([[put the value here]])


# ---------------------------multiple linear regression

import pandas as pd
import sklearn.linear_model
# import word2number

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\linear_regression\\hiring.csv")

reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']], df[['salary($)']])


# reg.predict([[6,10,10]])