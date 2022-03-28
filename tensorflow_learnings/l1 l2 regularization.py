import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\regularization\\train.csv")

# clean the data
df.isnull().sum()

# df.dropna(inplace=True)

df_join = pd.get_dummies(df['SaleCondition'], drop_first=True)

df = pd.concat([df,df_join], axis="columns")
df.drop(columns=['SaleCondition'], inplace=True)

df['MasVnrArea'].fillna(df['MasVnrArea'].mean(), inplace=True)

le = LinearRegression()

x = df.drop(columns=['SalePrice'])
y = df.SalePrice

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.7)

le.fit(x_train,y_train)

le.score(x_test,y_test)

# use lasso and rigid reularization for overfitting problems

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=50)

lasso.fit(x_train,y_train)

from sklearn.linear_model import Ridge

Ridge = Ridge(alpha=50)

Ridge.fit(x_train,y_train)

Ridge.score(x_test,y_test)

