import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\projection\\ito_pro.csv")

df.sort_values(by=['BA_order_prediction'], inplace = True)


x = df['BA_order_prediction'].values
y = df['chat_count'].values

plt.xlabel("BA_order_prediction")
plt.ylabel("Chat count")
plt.scatter(x,y)

reg = linear_model.LinearRegression()
reg.fit(df[['BA_order_prediction']], df[['chat_count']])

# Enter BA order prediction count

cc = reg.predict([[1089519]])

predicted_chat_count = int(cc[0])
print("predicted_chat_count :", + predicted_chat_count)

slot_chat_count = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\projection\\chat_pro_per.csv")

slot_chat_count = slot_chat_count[['Time', 'ITO', 'Week_type']]

slot_chat_count.sort_values(by=['Time'], inplace=True)


def week(x):
    if x == 'Sunday':
        return 1
    elif x == 'Monday':
        return 2
    elif x == 'Tuesday':
        return 3
    elif x == 'Wednesday':
        return 4
    elif x == 'Thursday':
        return 5
    elif x == 'Friday':
        return 6
    elif x == 'Saturday':
        return 7


slot_chat_count['Week_type_num'] = slot_chat_count['Week_type'].apply(week)


slot_chat_count_weekend = slot_chat_count[(slot_chat_count['Week_type_num'] == 1) | (slot_chat_count['Week_type_num'] == 7)]
slot_chat_count_weekdays = slot_chat_count[~(slot_chat_count['Week_type_num'] == 1) | (slot_chat_count['Week_type_num'] == 7)]

plt.scatter(slot_chat_count_weekend['Time'],slot_chat_count_weekend['ITO'],color='red',marker='+')
plt.scatter(slot_chat_count_weekdays['Time'],slot_chat_count_weekdays['ITO'],color='yellow')

w_n = {1:'sunday'
      ,2:'monday'
      ,3:'tuesday'
      ,4:'wednesday'
      ,5:'thursday'
      ,6:'friday'
      ,7:'saturday'}


week = 1


if week == 1:
    slot_chat_count = slot_chat_count[(slot_chat_count['Week_type_num'] == 1)]
    wt = '(weekends trend)'
elif week == 7:
    slot_chat_count = slot_chat_count[(slot_chat_count['Week_type_num'] == 7)]
    wt = '(weekends trend)'
else:
    slot_chat_count = slot_chat_count[~ (slot_chat_count['Week_type_num'] == 1) | (slot_chat_count['Week_type_num'] == 7)]
    wt = '(Weekdays trend)'

plt.scatter(slot_chat_count['Time'],slot_chat_count['ITO'],color='red')

slot_chat_count = slot_chat_count[['Time','ITO']]


x = slot_chat_count[['Time']]
y = slot_chat_count[['ITO']]

# best fit line 11


from sklearn.preprocessing import PolynomialFeatures
# for i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]:
#     print(i)
poly = PolynomialFeatures(degree = 10, interaction_only=False, include_bias=False, order='C')
X_poly = poly.fit_transform(x)
poly.fit(X_poly, y)
lin2 = linear_model.LinearRegression()
lin2.fit(X_poly, y)
plt.xticks(x.values)
plt.scatter(x, y, color = 'blue')
plt.plot(x, lin2.predict(poly.fit_transform(x)), color = 'red', label='ITO % of contact')
plt.legend()
plt.title('Regression')
plt.xlabel('Time')
plt.ylabel('ITO')

slot_wise_chat_count = []

for i in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6]:
    time = i

    val = lin2.predict(poly.fit_transform([[i]]))
    val = int(((float(val) * 100) * predicted_chat_count) / 100)
    if time == 4:
        val = val + 150
    if (week == 1 or week == 7) and (time == 5) :
        val = val + 100
    slot_wise_chat_count.append(val)

    print('Predicted chat at ' + str(i) + ': ' + str(val))


