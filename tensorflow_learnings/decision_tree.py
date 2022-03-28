import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\decision_tree\\titanic.csv")

df = df.drop(columns=['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'])

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Sex_n'] = LabelEncoder().fit_transform(df['Sex'])

df.drop(columns=['Sex'], inplace=True)

x = df.drop(columns=['Survived'])

y = df['Survived']

model = DecisionTreeClassifier()

x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8)

model.fit(x_train,y_train)

model.score(x_test,y_test)
