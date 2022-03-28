#!/usr/bin/env python3
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd
# import pymysql.cursors
import time
import webbrowser
import os
from os import mkdir, makedirs
from datetime import date
import glob
import shutil
import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os.path
from os import path
import mysql.connector
import numpy as np
import getpass

user = getpass.getuser()




# FirstDayOfMonth Code Block
    # FirstDayOfMonth
x = datetime.now()
if x.day == 1:
    given_date = datetime.today().date()
    first_day_of_month = given_date.replace(day=1)
    first_day_of_month = given_date.replace(month=x.month - 1)
    first_day_of_month = first_day_of_month.isoformat()
else:
    given_date = datetime.today().date()
    first_day_of_month = given_date.replace(day=1)
    first_day_of_month = first_day_of_month.isoformat()










with open("C:\\Users\\"+user+"\\Desktop\\projects\\omt_rnp\\rsa_key.p8", "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password='bOw(#!KAw0WwOW'.encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())


try:
    ctx = snowflake.connector.connect(
        user='cc_user@swiggy.in',
        account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
        private_key=pkb,
        #        database='STREAMS',
        # warehouse='NONTECH_WH_01',
        role='CC_AUTOMATION',
        # schema='CC_AUTOMATION_DATA_READER'
    )
    cs = ctx.cursor()
    print(cs)
except:
    print("Some error occurred while connection")

try:
    print('Before Download')

        # AHT, CSAT & FTR - STARTS HERE
    raw_fetch = cs.execute("""With CHAT as( Select *,case when AGENT_EMAIL like '%_g7cr@%' then 'G7' when AGENT_EMAIL like '%_kt@%' then 'Kochar' when AGENT_EMAIL like '%_fs@%' then 'Five Splash' when AGENT_EMAIL like '%_gr@%' then 'Grass Roots' when AGENT_EMAIL like '%_hrh@%' then 'HRH' when AGENT_EMAIL like '%_fu@%' then 'fusion' when AGENT_EMAIL like '%_rm@%' then 'Radical minds' else 'In-House' end as outsource_name,
                                case when hour(AGENT_ASSIGNMENT_TIME) in (5,6,7,8,9,10,11)    then 'Break Fast' when hour(AGENT_ASSIGNMENT_TIME) in(12,13,14)     then 'Lunch' when hour(AGENT_ASSIGNMENT_TIME) in (15,16,17,18)    then 'Snacks' when hour(AGENT_ASSIGNMENT_TIME) in(19,20,21,22)  then 'Dinner' when hour(AGENT_ASSIGNMENT_TIME) in(23,0,1,2,3,4) then 'Late Night' else 'Non Peak Hours'  end as Chat_Peak
                                from ANALYTICS.CC_CX_VIEWS.DE_FACT_TEMP where  to_date(AGENT_ASSIGNMENT_TIME) between '{}' and current_date-2 and  chattype = 'Agent' and ticket_id is not null group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39, 40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, 61,62,63,64,65, 66),
                                cc as( Select *, row_number() over (partition by agent_email order by AGENT_ASSIGNMENT_TIME Asc) as RN from Chat), BB as(Select * from CC), final as( Select a.agent_email,a.RN,count (case when a.RN<b.RN and a.conversation_closed_time>=b.AGENT_ASSIGNMENT_TIME then b.conversationid end) cun from cc a left join bb b on a.agent_email=b.agent_email group by 1,2), final2 as( Select a.*, row_number() over (partition by to_date(AGENT_ASSIGNMENT_TIME),CLIENTORDERID,NODELABEL order by AGENT_ASSIGNMENT_TIME Desc ) as RNK, case when b.cun+1>4 then 4 else b.cun+1 end Cuncurrency from cc a left join final b on a.agent_email=b.agent_email and a.RN=b.RN) select to_date(AGENT_ASSIGNMENT_TIME) date, outsource_name, count(conversationid) as interactions, count( case when effortscore in (1) then conversationid end) as promotors, count( case when effortscore in (1,0) then conversationid end) as all_csat, Sum(case when (datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time))>=0 then datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time) end) AHT, count(case when RNK>1 and CLIENTORDERID>1  then TICKET_ID end ) FTNR_COUNT, sum(Cuncurrency) Concurrency from final2 group by 1,2""".format(first_day_of_month))

    alpha = pd.DataFrame(raw_fetch)
finally:
    cs.close()

alpha.columns = ['DATE', 'OUTSOURCE_NAME', 'INTERACTIONS', 'PROMOTORS', 'ALL_CSAT', 'AHT', 'FTNR_COUNT', 'CONCURRENCY']
alpha.drop(columns=['DATE'],inplace=True)

alpha = alpha.groupby('OUTSOURCE_NAME').sum().reset_index()


alpha['AHT_T'] = alpha['AHT']/alpha['INTERACTIONS']
alpha['Con AHT'] = alpha['AHT_T']/ (alpha['CONCURRENCY']/alpha['INTERACTIONS'])
alpha['DE Experience'] = alpha['PROMOTORS']/alpha['ALL_CSAT']
alpha['FTR'] = 1-(alpha['FTNR_COUNT']/alpha['INTERACTIONS'])
alpha['FTNR'] = 1-alpha['FTR']

alpha = alpha[['OUTSOURCE_NAME', 'Con AHT', 'DE Experience', 'FTR']]



        # Checking Success Condition for Alpha Block


# quality block
# Quality - STARTS HERE

        # QualityBlock_1
quality = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\omt_rnp\\omt_quality.csv")

quality = quality[['Audit Score','Location']]
quality.rename(columns={'Location':'OUTSOURCE_NAME'}, inplace = True)
quality['OUTSOURCE_NAME'] = quality['OUTSOURCE_NAME'].str.lower()

def check(x):
    if x <= 1:
        return x
    else:
        return x/100

quality['Audit Score'] = quality['Audit Score'].apply(check)
        # quality['Audit score'] = quality['Audit score'].map(lambda x : x.rstrip('%') )

        # quality['Audit score'] = quality['Audit score'].astype('int64')
quality['Audit Score'] = quality['Audit Score'] * 100


        # QualityBlock_2
def check(x):
    if "fs" in x:
        return "Five Splash"
    elif "g7" in x:
        return "G7"
    elif "grass" in x:
        return "Grass Roots"
    elif "hrh" in x:
        return "HRH"
    elif "house" in x:
        return "In-House"
    elif "kochar" in x:
        return "Kochar"

quality['OUTSOURCE_NAME'] = quality['OUTSOURCE_NAME'].apply(check)


quality = quality.groupby('OUTSOURCE_NAME').mean().reset_index()
# quality['Audit score'] = round(quality['Audit score'],2)


alpha = pd.merge(alpha, quality, how='left', on='OUTSOURCE_NAME')

med = alpha['Audit Score'].median()

alpha['Audit Score'] = alpha['Audit Score'].fillna('Y')

        # QualityBlock_3
def fil(data):
    if data['Audit Score'] == 'Y':
        return "Yes"
    else:
        return "No"

alpha['quality_exception'] = alpha.apply(fil, axis=1)

alpha['Audit Score'] = alpha['Audit Score'].replace(to_replace='Y',value=med)

        # rankings
alpha['AHT_RANK'] = alpha['Con AHT'].rank(ascending = True,method = 'dense')
alpha['DE Experience_RANK'] = alpha['DE Experience'].rank(ascending = False,method = 'dense')
alpha['FTR_RANK'] = alpha['FTR'].rank(ascending = False,method = 'dense')
alpha['Audit score rank'] = alpha['Audit Score'].rank(ascending=False, method='dense')
alpha['DE Experience'] = alpha['DE Experience'] * 100
alpha['FTR'] = alpha['FTR'] * 100
alpha = alpha[['OUTSOURCE_NAME','Con AHT','AHT_RANK','DE Experience','DE Experience_RANK','FTR','FTR_RANK','Audit Score','Audit score rank','quality_exception']]




# Quality - ENDS HERE

skeleton = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\omt_rnp\\skeleton.csv")

current_date = datetime.today().date()
current_date = given_date.replace(day= x.day - 1)
# current_date = date.today().isoformat()
current_date = current_date.isoformat()
current_date_of_month = current_date + " 06:59:59"

first_day_of_month = first_day_of_month + " 07:00:00"

skeleton['Site'] = skeleton['Site'].str.lower()

def sk_rename(x):
    if "house" in x:
        return "In-House"
    elif "kochar" in x:
        return "Kochar"
    elif "grass" in x:
        return "Grass Roots"
    elif "7" in x:
        return "G7"
    elif "five" in x:
        return "Five Splash"
    elif "hrh" in x:
        return "HRH"

skeleton['Site'] = skeleton['Site'].apply(sk_rename)

sql = "Select dt,hour(BUCKET), sum(AVAILABLE_MINUTES), case when AGENTEMAIL like '%_g7cr@%' then 'G7' when AGENTEMAIL like '%_kt@%' then 'Kochar' when AGENTEMAIL like '%_fs@%' then 'Five Splash' when AGENTEMAIL like '%_gr@%' then 'Grass Roots' when AGENTEMAIL like '%_hrh@%' then 'HRH' when AGENTEMAIL like '%_fu@%' then 'fusion' else 'In-House' end as outsource_name from analytics.cc_cx.deassistance_agents_productivity where bucket between ('{}') and ('{}') group by 1,2,4".format(first_day_of_month,current_date_of_month )

with open("C:/Users/"+user+"/Desktop/projects/chat_rnp/rsa_key.p8", "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password='bOw(#!KAw0WwOW'.encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())
try:
    ctx = snowflake.connector.connect(
        user='cc_user@swiggy.in',
        account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
        private_key=pkb,
        #        database='STREAMS',
        # warehouse='NONTECH_WH_01',
        role='CC_AUTOMATION',
        # schema='CC_AUTOMATION_DATA_READER'
    )
    cs = ctx.cursor()
except:
    print("Some error occurred while connection")

try:
    raw_fetch = cs.execute(sql)
    # print('fetched')
    sa = pd.DataFrame(raw_fetch)
    skeleton_block_3 = True
    # sa.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnp\\analytics_skeleton_snowflakes.csv")
finally:
    cs.close()
    # SkeletonAdherenceBlock_4
    # Data Manipulation
sa.columns = ['DT','HOUR(BUCKET)','AVAILABLE_MINUTES','CENTER']
sa['AVAILABLE_MINUTES'] = sa['AVAILABLE_MINUTES'].astype('int64')
sa = sa.groupby(['DT','HOUR(BUCKET)','CENTER']).sum().reset_index()

sa['DT'] = pd.to_datetime(sa['DT']).dt.strftime('%d')
sa['DT'] = sa['DT'].astype('int64')
sa.sort_values(by=['DT','HOUR(BUCKET)'],ascending=True, inplace=True)

sa['FTE'] = round(sa['AVAILABLE_MINUTES'] / 60,0)
df = pd.merge(sa, skeleton,  how='left', left_on=['DT','HOUR(BUCKET)','CENTER'], right_on = ['Date','Int','Site'])

df.drop(columns=['Date','Int','Site'],inplace=True)
df['FTE'] = df['FTE'].astype('int64')

def deficit(df):
    if df['FTE'] >= df['Skeleton']:
        return 0
    else:
        return 1

df['deficit'] = df.apply(deficit,axis=1)

deficit = df[['CENTER','deficit']]
deficit = deficit.groupby('CENTER').mean()*100
deficit = deficit.reset_index()

deficit['SCHEDULE_ADHERENCE'] = 100 - deficit['deficit']

deficit.drop(columns = ['deficit'],inplace = True)

deficit['SCHEDULE_ADHERENCE_RANK'] = deficit['SCHEDULE_ADHERENCE'].rank(ascending = False, method = 'dense').astype('int64')

alpha.rename(columns={'OUTSOURCE_NAME':'CENTER'}, inplace = True)

alpha = pd.merge(alpha,deficit,how='left',on='CENTER')



# Skeleton Adherence - ENDS HERE

# Overall Ranking + Anynymous - SRARTS HERE

        # finding quality weightage
def a_w_f(x):
    if x > 360:
        return 20*90
    elif x > 330 and x <=360:
        return 20*95
    elif x >= 270 and x <= 330:
        return 20*100
    elif x >= 240 and x < 270:
        return 20*105
    else:
        return 20*110

alpha['a_w'] = alpha['Con AHT'].apply(a_w_f)


        # finding de experience weightage
def de_w_f(x):
    if x < 50:
        return 20*90
    elif x >= 50 and x < 53:
        return 20*95
    elif x >= 53 and x <= 55:
        return 20*100
    elif x >= 55 and x <= 57:
        return 20*105
    else:
        return 20*110

alpha['de_w'] = alpha['DE Experience'].apply(de_w_f)


        # finding ftr experience weightage
def ftr_w_f(x):
    if x < 90:
        return 15*90
    elif x >= 90 and x < 91:
        return 15*95
    elif x >= 91 and x <= 92:
        return 15*100
    elif x >= 92 and x <= 93:
        return 15*105
    else:
        return 15*110

alpha['ftr_w'] = alpha['FTR'].apply(ftr_w_f)

        # finding audit score weightage
def audit_w_f(x):
    if x < 81:
        return 25*90
    elif x >= 81 and x < 83:
        return 25*95
    elif x >= 83 and x <= 85:
        return 25*100
    elif x > 85 and x <= 87:
        return 25*105
    else:
        return 25*110

alpha['audit_w'] = alpha['Audit Score'].apply(audit_w_f)


        # finding schedule adherence weightage
def sa_w_f(x):
    if x < 92:
        return 12.5*90
    elif x >= 92 and x < 94:
        return 12.5*95
    elif x >= 94 and x <= 95:
        return 12.5*100
    elif x > 95 and x <= 97:
        return 12.5*105
    else:
        return 12.5*110

alpha['sa_w'] = alpha['SCHEDULE_ADHERENCE'].apply(sa_w_f)


alpha['total_w'] = alpha['a_w'] + alpha['de_w'] + alpha['ftr_w'] + alpha['audit_w'] + alpha['sa_w']
alpha['Overall_rank'] = alpha['total_w'].rank(ascending= False, method='dense')

alpha['DE Experience'] = round(alpha['DE Experience'],2)
alpha['FTR'] = round(alpha['FTR'],2)
alpha['SCHEDULE_ADHERENCE'] = round(alpha['SCHEDULE_ADHERENCE'],2)

alpha = alpha[['CENTER','Overall_rank','Con AHT','AHT_RANK','DE Experience','DE Experience_RANK','FTR','FTR_RANK','SCHEDULE_ADHERENCE','SCHEDULE_ADHERENCE_RANK','Audit Score','Audit score rank','quality_exception']]

alpha = alpha.sample(frac=1)

alpha.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\omt_rnp\\final_omt.csv")

# <------------------------------------------------------------------------------------------------------------------->

