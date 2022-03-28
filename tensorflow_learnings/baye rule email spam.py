import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\baye rule\\spam.csv")

le = LabelEncoder()

df['spam'] = le.fit_transform(df['Category'])
df.drop(columns=['Category'], inplace=True)
# df['Category'] = df.Category.apply(lambda x: 1 if x==1 else 0)

X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam)


emails = ['Hey mohan, can we get together to watch footbal game tomorrow?',
          'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!']

clf = Pipeline([('cv',CountVectorizer())
                ,('mb',MultinomialNB())])

clf.fit(X_train,y_train)

clf.predict(emails)

clf.score(X_test,y_test)


