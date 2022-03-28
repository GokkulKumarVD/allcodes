from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB, GaussianNB

wine = datasets.load_wine()

dir(wine)

df = pd.DataFrame(data=wine.data, columns = wine.feature_names)

df['target'] = wine.target

# df.columns[df.isnull().any()]

x_train, x_test, y_train, y_test = train_test_split(df.drop(columns='target'), df.target, train_size=0.7)

model = GaussianNB()
model.fit(x_train,y_train)
model.score(x_test,y_test)

# model.predict([[14,3,3,15,200,3,3,2,2,5,1,3,2000]])

mn = MultinomialNB()
mn.fit(x_train,y_train)
mn.score(x_test,y_test)

