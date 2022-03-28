import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plot

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\data_science\\k_means_clustering\\income.csv")

# convert all the numbers to the range of 0 to 1 to get accurate results in clustering
scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

plot.scatter(df['Age'],df['Income($)'])

# finding k number using elbow technique
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)

plot.xlabel('K')
plot.ylabel('Sum of squared error')
plot.plot(k_rng,sse)

# found K = 3


km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])

df['cluster'] = y_predicted

km.cluster_centers_

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plot.scatter(df1.Age,df1['Income($)'],color='green')
plot.scatter(df2.Age,df2['Income($)'],color='red')
plot.scatter(df3.Age,df3['Income($)'],color='black')
plot.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plot.legend()