import pandas as pd
import plotly.offline as po
import plotly.graph_objs as go

df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\pandas\\sn.csv", usecols=['queueid', 'aht_in_secs'])

dispowise = df.groupby(df['queueid']).mean()

dispowise = dispowise.sort_values(by=['aht_in_secs'])

dispowise['aht_in_secs'] = pd.to_datetime(dispowise["aht_in_secs"], unit='s')

dispowise.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\pandas\\dispowiseaht.csv")
dispowise.reset_index(level=0, inplace=True)
dispowise.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\pandas\\dispowiseaht.csv")
dispowise = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\pandas\\dispowiseaht.csv")
dispowise = go.Bar(x=dispowise['queueid'], y=dispowise['aht_in_secs'], name='AHT', marker={'color': '#F708C8'})
layout = go.Layout(title='Overall agents AHT')
fig = go.Figure(data=dispowise, layout=layout)
po.plot(fig, filename='C:\\this\\htdocs\\dispowiseaht.html')

input('Press ENTER to exit')
