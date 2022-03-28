import pandas as pd

df = pd.read_csv('C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\marvex\\resolvedat.csv')

cdf = df.groupby(['closure_date','Agent_email'])['Tickets_closed'].sum()
cdf = cdf.reset_index()

adf = df.groupby(['Agent_email'])['AHT'].mean()
adf = adf.reset_index()

pdf = cdf.merge(adf, on='Agent_email', how='left')

pdf['Ticket_disposition'] = 'Total'

pdf=pdf[['closure_date','Agent_email','Ticket_disposition','Tickets_closed','AHT']]


fdf = pd.concat([df,pdf])

# fdf.to_csv('C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\marvex\\fdf.csv')



try:
    import sqlalchemy

    database_username = 'gokkul'
    database_password = 'php_learning'
    database_ip = 'localhost'
    database_name = 'marvex'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password,
                                                          database_ip, database_name), pool_recycle=1,
                                                   pool_timeout=57600).connect()

    fdf.to_sql(con=database_connection, name='marvex_db', if_exists='append', chunksize=1000, index=False)
except:
    print('error')