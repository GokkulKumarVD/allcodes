import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\logistic_regression\\HR_comma_sep.csv")

dummies = pd.get_dummies(df['salary'])
merged = pd.concat([df,dummies], axis = "columns")

final = merged.drop(columns=['salary'])

reg = LogisticRegression()

x = final[['satisfaction_level','average_montly_hours','promotion_last_5years','high','low','medium']]

y = final[['left']]

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.3)

reg.fit(x_train,y_train)

reg.score(x_test,y_test)

reg.predict([[0.90,0.35,1,1,0,0]])