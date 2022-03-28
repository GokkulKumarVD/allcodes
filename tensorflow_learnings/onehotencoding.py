import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\linear_regression\\carprices.csv")

dummies = pd.get_dummies(df['Car Model'])

merged = pd.concat([df,dummies], axis = 'columns')

# we must always remove one columns from dummies to avoid onehotcoding trap
final = merged.drop(columns=['Car Model','Mercedez Benz C class'])

x = final[['Mileage','Age(yrs)','Audi A5','BMW X5']]
y = final[['Sell Price($)']]

reg = LinearRegression()
reg.fit(x,y)

# we are finding mercedes price so all other cars columns must be zero
reg.predict([[50000,10,0,0]])

# close to 1 is the accurate model
reg.score(x,y)
