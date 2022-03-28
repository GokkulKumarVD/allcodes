import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\baye rule\\titanic.csv')

df.drop(columns=['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'], inplace = True)


# check if any columns has null value
df.columns[df.isna().any()]

# age has null values
df['Age'] = df['Age'].fillna(df['Age'].mean())


le = LabelEncoder()

df['Sex'] = le.fit_transform(df['Sex'])

x = df.drop(columns=['Survived'])
y = df['Survived']

x_train ,x_test, y_train, y_test = train_test_split(x,y,train_size=0.7)

model = GaussianNB()
model.fit(x_train,y_train)

model.score(x_test,y_test)

model.predict(x_test)

# model.predict([[1,1,22,90]])

model.predict_proba(x_test)

cross_val_score(GaussianNB(),x_test,y_test)

cross_val_score(RandomForestClassifier(),x_test,y_test)
