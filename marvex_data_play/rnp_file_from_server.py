#!/usr/bin/env python3
from codecs import encode

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
from datetime import timedelta
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil

# time.sleep(120)

pd.options.mode.chained_assignment = None

# CurrentDateTime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# now.strftime('%A') #Day


day_1 = date.today() - timedelta(days=1)
day_1 = day_1.isoformat()
day_1 = day_1 + " 07:00:00"

day_2 = date.today() - timedelta(days=2)
day_2 = day_2.isoformat()
day_2 = day_2 + " 06:59:59"

try:
    with open("/var/lakshya/rsa_key.p8", "rb") as key:
        p_key = serialization.load_pem_private_key(
            key.read(),
            password='bOw(#!KAw0WwOW'.encode(),
            backend=default_backend()
        )
    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    ctx = snowflake.connector.connect(
        user='cc_user@swiggy.in',
        account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
        private_key=pkb,
        role='CC_AUTOMATION',
    )
    cs = ctx.cursor()

    raw_fetch = cs.execute("""WITH CHAT AS (Select *, case when queueid like '%priority%' then 'Priority'
                  when queueid like '%combined%' then 'CQ'
                  when queueid  like '%stores%' and queueid  not like '%combined%' then 'stores'
                  when queueid  like '%genie%' and queueid  not like '%combined%' then 'genie'
                  else 'BAU' end Role,
                                    case when agent_email like '%_ag@%' then 'Aegis'
                                                  when agent_email like '%_qup@%' then 'Quampetence'
                                                  when agent_email like '%_kt@%' then 'Kochar'
                                                  when agent_email like '%_cb@%' then 'CBSL'
                                                  when agent_email like '%_tm@%' then 'TM'
                                                  when agent_email like '%_rm@%' then 'RM'
                                                  when agent_email like '%_ison@%' then 'ISON'
                                                  when agent_email like '%_hrh@%' then 'HRH'
                                                  when agent_email like '%_fu@%' then 'Fusion'
                                                  when agent_email like '%_ae@%' then 'Assure edge'
                                                  when agent_email like '%_cscb@%' then 'CBSL'
                                                  when agent_email like '%_cskt@%' then 'Kochar'
                                                  when agent_email like '%kt_@%' then 'Kochar'
                                                  when agent_email like '%_31p@%' then '31P'
                                                  else 'In-House' end as Center              
                                    from facts.public.customer_interaction_fact
                                    where agent_email <>'Bot' and AGENT_ASSIGNMENT_TIME between '{}' and '{}'
                                    and (queueid ilike '%l2%' or queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%' 
                            or queueid ilike '%bau-cancellation%' or queueid ilike '%bau-couponrelated%' or queueid ilike '%bau-foodissues%' 
                            or queueid ilike '%bau-food-special-instruction%' or queueid ilike '%bau-orderstatus%' or queueid ilike '%bau-paymentrelated%' 
                            or queueid ilike '%delivery-instructions%' or queueid ilike '%fallback%' or queueid ilike '%general-issue%' or queueid ilike '%team-1%'
                            )
                                    group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19,20,21,22,23,24,25,26,27,28,29, 30,31,32,33,34,35,36,37,38,39,
                                    40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, 61,62,63,64,65, 66,67,68,69,70, 71,72,73,74,75,76),

                                    cc as( Select *, row_number() over (partition by agent_email order by AGENT_ASSIGNMENT_TIME Asc) as RN from Chat),

                                    BB as(Select * from CC), final as( Select a.agent_email,a.RN,
                                    count (case when a.RN<b.RN and a.conversation_closed_time>=b.AGENT_ASSIGNMENT_TIME then b.conversationid end) cun from cc a
                                    left join bb b on a.agent_email=b.agent_email group by 1,2),

                                    cun as( Select a.*, row_number() over (partition by entityid,NODELABEL,to_date(AGENT_ASSIGNMENT_TIME) order by AGENT_ASSIGNMENT_TIME Desc ) as RNK,
                                    case when b.cun+1>4 then 4 else b.cun+1 end Cuncurrency from cc a left join final b on a.agent_email=b.agent_email and a.RN=b.RN)

                                    select to_date(AGENT_ASSIGNMENT_TIME) date,
                                    a.Center,a.agent_email, role, count(conversationid) as interactions,
                                    count( case when effortscore in (1) then conversationid end) as promotors,
                                    count( case when effortscore in (1,0) then conversationid end) as all_csat,
                                    sum(case when (AHT_in_secs)>=0 then AHT_in_secs end) AHT,
                                    sum(case when (frt_in_secs)>=0 then frt_in_secs end) FRT,
                                    count(case when RNK>1 and entityid>1  then TICKET_ID end ) as ftnr,
                                    count(case when entityid>1 then TICKET_ID end)  as total_orders, sum(Cuncurrency) Cuncurrency from cun a  group by 1,2,3,4;""".format(
        day_2, day_1))

    df = pd.DataFrame(raw_fetch)

    df.columns = ['DATE', 'CENTER', 'AGENT_EMAIL', 'role', 'INTERACTIONS', 'PROMOTORS', 'ALL_CSAT', 'AHT', 'FRT',
                  'FTNR', 'TOTAL_ORDERS', 'CUNCURRENCY']

    data = df
    data['OVERALL AHT'] = data['AHT'] / data['INTERACTIONS']
    data['CSAT'] = (data['PROMOTORS'] / data['ALL_CSAT']) * 100
    data['FTR'] = ((data['TOTAL_ORDERS'] - data['FTNR']) / data['TOTAL_ORDERS']) * 100

    data = data[['DATE', 'AGENT_EMAIL', 'CENTER', 'role', 'CSAT', 'OVERALL AHT', 'FRT', 'INTERACTIONS']]
    data.columns = ['date', 'AGENTEMAILID', 'Partners', 'queue', 'EFFORTSCORE', 'aht_secs', 'FRT', 'chat_count']


    # finding OSPs
    def osp(x):
        if "_cb" in x:
            return "CBSL"
        elif "_kt" in x:
            return "KOCHAR"
        elif "_tm" in x:
            return "TECH MAHINDRA"
        elif "_gr" in x:
            return "GRASS ROOTS"
        elif "_fs" in x:
            return "FIVE SPLASH"
        elif "_ag" in x:
            return "AEGIS"
        elif "ijp" in x:
            return "CENTRAL FOLLOW UP"
        elif "new.city" in x:
            return "NEW CITY"
        elif "_rm" in x:
            return "RADICAL MINDS"
        elif "_hrh" in x:
            return "HRH"
        elif "_ison" in x:
            return "ISON"
        elif "_g7cr" in x:
            return "G7"
        elif "_qup" in x:
            return "quampetence"
        elif "_ae" in x:
            return "assured edge"
        else:
            return "IN HOUSE"


    data['partners'] = data['AGENTEMAILID'].apply(osp)

    legacy_req = data

    legacy_req['EFFORTSCORE'] = legacy_req['EFFORTSCORE'].fillna(0)
    legacy_req.fillna(0, inplace=True)

    legacy_req['queue'] = legacy_req['queue'].str.lower()


    # function to rename queue
    def q_rename(x):
        if 'l2-team-1' in x:
            return "L2_food"
        elif 'l2-team-2' in x:
            return "L2_food"
        elif 'l2-team13' in x:
            return "L2_food"
        elif 'l2-team-10' in x:
            return "L2_food"
        elif 'l2-team-14' in x:
            return "L2_food"
        elif 'edsg' in x:
            return "L2_food"
        elif 'genie' in x:
            return "Genie"
        elif 'stores' in x:
            return "Stores"
        elif 'priority' in x:
            return "Priority"
        # elif 'bau-cancellation' or 'bau-couponrelated' or 'bau-foodissues' or 'bau-food-special-instruction' or 'bau-orderstatus' or 'bau-paymentrelated ' or 'delivery-instructions' or 'fallback' or 'general-issue' or 'team-1' in x:
        #     return ''
        else:
            return "Bau-food"


    legacy_req['queue'] = legacy_req['queue'].apply(q_rename)


    # function to find csat scores based on q ids
    def score(legacy_req):
        if legacy_req['queue'] == "L2_food":
            return 20 * (legacy_req['EFFORTSCORE'] - 25) / (25 * 1)

        elif legacy_req['queue'] == "L2_stores_genie":
            return 20 * (legacy_req['EFFORTSCORE'] - 65) / (65 * 1)

        elif legacy_req['queue'] == "Genie":
            return 20 * (legacy_req['EFFORTSCORE'] - 74) / (78 * 1)

        elif legacy_req['queue'] == "Stores":
            return 20 * (legacy_req['EFFORTSCORE'] - 74.9) / (80 * 1)

        elif legacy_req['queue'] == "Priority":
            return 25 * (legacy_req['EFFORTSCORE'] - 86) / (90 * 1)

        elif legacy_req['queue'] == "Bau-food":
            return 15 * (legacy_req['EFFORTSCORE'] - 58.99) / (63 * 1)


    legacy_req['csat_score'] = legacy_req.apply(score, axis=1)


    # function to find FRT scores based on q ids
    def score(legacy_req):
        if legacy_req['queue'] == "L2_food":
            return 0
        elif legacy_req['queue'] == "L2_stores_genie":
            return 0
        elif legacy_req['queue'] == "Genie":
            return 0
        elif legacy_req['queue'] == "Stores":
            return 0
        elif legacy_req['queue'] == "Priority":
            return 0
        elif legacy_req['queue'] == "Bau-food":
            return 10 * (legacy_req['FRT'] - 15) / (10 * -1)


    legacy_req['FRT_score'] = legacy_req.apply(score, axis=1)


    # function to find AHT scores based on q ids
    def score(legacy_req):
        if legacy_req['queue'] == "L2_food":
            return 20 * (legacy_req['aht_secs'] - 600) / (540 * -1)
        elif legacy_req['queue'] == "L2_stores_genie":
            return 30 * (legacy_req['aht_secs'] - 840) / (660 * -1)
        elif legacy_req['queue'] == "Genie":
            return 30 * (legacy_req['aht_secs'] - 330) / (299 * -1)
        elif legacy_req['queue'] == "Stores":
            return 30 * (legacy_req['aht_secs'] - 330) / (299 * -1)
        elif legacy_req['queue'] == "Priority":
            return 30 * (legacy_req['aht_secs'] - 273) / (260 * -1)
        elif legacy_req['queue'] == "Bau-food":
            return 10 * (legacy_req['aht_secs'] - 221) / (200 * -1)


    legacy_req['aht_score'] = legacy_req.apply(score, axis=1)


    # fill frt with zeros for certain q
    def fill_zero(legacy_req):
        if legacy_req['queue'] != 'Bau-food':
            return 0
        else:
            return legacy_req['FRT']


    legacy_req['FRT'] = legacy_req.apply(fill_zero, axis=1)

    # converting from obj to float
    legacy_req['aht_score'] = legacy_req['aht_score'].astype('float')
    # total scores
    legacy_req['score'] = legacy_req['csat_score'] + legacy_req['FRT_score'] + legacy_req['aht_score']
    legacy_req.drop(columns=['FRT_score', 'csat_score', 'aht_score'], inplace=True)

    # remove agents name where chats taken are less than 10
    # agent_wise_q_list = agent_wise

    # unique q ids
    q_list = legacy_req['queue'].unique().tolist()

    less_chat_count = legacy_req.query('chat_count < 10')
    less_chat_count = less_chat_count[(less_chat_count['queue']) != 'L2_stores_genie']
    less_chat_count.drop_duplicates(subset=['AGENTEMAILID'], keep='first', inplace=True)

    ed_s_g = legacy_req[legacy_req['queue'] == 'L2_stores_genie']

    less_chat_count['global_rank'] = 0
    less_chat_count['csat_global_rank'] = 0
    less_chat_count['frt_global_rank'] = 0
    less_chat_count['aht_global_rank'] = 0

    less_chat_count['local_ranking'] = 0
    less_chat_count['csat_local_rank'] = 0
    less_chat_count['frt_local_rank'] = 0
    less_chat_count['aht_local_rank'] = 0

    # live.insert(loc=0, column='global_rank', value=0)
    # live.insert(loc=0, column='csat_global_rank', value=0)
    # live.insert(loc=0, column='frt_global_rank', value=0)
    # live.insert(loc=0, column='aht_global_rank', value=0)
    #
    # live.insert(loc=0, column='local_ranking', value=0)
    # live.insert(loc=0, column='csat_local_rank', value=0)
    # live.insert(loc=0, column='frt_local_rank', value=0)
    # live.insert(loc=0, column='aht_local_rank', value=0)

    legacy_req = legacy_req[(legacy_req['chat_count']) >= 10]
    legacy_req = legacy_req[(legacy_req['queue']) != 'L2_stores_genie']

    # rank only ed stores genie
    ed_s_g['local_ranking'] = ed_s_g['score'].rank(ascending=False, method='min')
    ed_s_g['global_rank'] = ed_s_g['score'].rank(ascending=False, method='min')

    ed_s_g['csat_global_rank'] = ed_s_g['EFFORTSCORE'].rank(ascending=False, method='min')
    ed_s_g['frt_global_rank'] = ed_s_g['FRT'].rank(ascending=True, method='min')
    ed_s_g['aht_global_rank'] = ed_s_g['aht_secs'].rank(ascending=True, method='min')

    ed_s_g['csat_local_rank'] = ed_s_g['EFFORTSCORE'].rank(ascending=False, method='min')
    ed_s_g['frt_local_rank'] = ed_s_g['FRT'].rank(ascending=True, method='min')
    ed_s_g['aht_local_rank'] = ed_s_g['aht_secs'].rank(ascending=True, method='min')

    # ed_s_g.fillna('0', inplace=True)

    # add a function to create seperate rankings for different queue ids
    n = q_list.__len__()

    this = legacy_req
    this_less = less_chat_count

    df_list = []
    agent_wise_output = pd.DataFrame()

    for i in q_list:

        # print(i)
        agent_wise1 = this
        less_chat_count1 = this_less

        agent_wise1 = agent_wise1[agent_wise1['queue'] == i]
        # less_chat_count1 = less_chat_count1[less_chat_count1['queue'] == i]

        agent_wise1['global_rank'] = agent_wise1['score'].rank(ascending=False, method='min')
        agent_wise1.sort_values(by=['global_rank'], inplace=True)

        agent_wise1['csat_global_rank'] = agent_wise1['EFFORTSCORE'].rank(ascending=False, method='min')
        agent_wise1['frt_global_rank'] = agent_wise1['FRT'].rank(ascending=True, method='min')
        agent_wise1['aht_global_rank'] = agent_wise1['aht_secs'].rank(ascending=True, method='min')

        # now finding local ranking
        agent_wise1['local_ranking'] = agent_wise1.groupby('Partners')['score'].rank(ascending=False, method='min')

        agent_wise1['csat_local_rank'] = agent_wise1.groupby('Partners')['EFFORTSCORE'].rank(ascending=False,
                                                                                             method='min')
        agent_wise1['frt_local_rank'] = agent_wise1.groupby('Partners')['FRT'].rank(ascending=True, method='min')
        agent_wise1['aht_secs'] = agent_wise1['aht_secs'].astype('float')
        agent_wise1['aht_local_rank'] = agent_wise1.groupby('Partners')['aht_secs'].rank(ascending=True, method='min')

        if i == 'L2_food':
            L2_df = agent_wise1
            df_list.append(L2_df)
        elif i == 'Priority':
            Priority_df = agent_wise1
            df_list.append(Priority_df)
        elif i == 'Stores':
            Stores_df = agent_wise1
            df_list.append(Stores_df)
        elif i == 'Genie':
            Genie_df = agent_wise1
            df_list.append(Genie_df)
        elif i == 'Bau-food':
            bau_food_df = agent_wise1
            df_list.append(bau_food_df)
        elif i == 'L2_stores_genie':
            L2_stores_genie_df = pd.concat([agent_wise1, ed_s_g])
            df_list.append(L2_stores_genie_df)

    agent_wise_output = pd.concat(df_list)

    agent_wise_output = pd.concat([agent_wise_output, less_chat_count])

    agent_wise_output['positive_survey_max_streak'] = 0
    agent_wise_output['FRT_max_streak'] = 0
    agent_wise_output['aht_max_streak'] = 0

    agent_wise = agent_wise_output[~(agent_wise_output['chat_count'] == 0)]

    dt = date.today() - timedelta(days=2)
    dt = dt.isoformat()

    agent_wise['date'] = dt

    # main dataframe
    day_1_agent_wise = agent_wise[
        ['date', 'AGENTEMAILID', 'EFFORTSCORE', 'FRT', 'aht_secs', 'positive_survey_max_streak', 'FRT_max_streak',
         'aht_max_streak', 'score', 'local_ranking', 'global_rank', 'csat_local_rank', 'csat_global_rank',
         'frt_local_rank', 'frt_global_rank', 'aht_local_rank', 'aht_global_rank', 'queue']]
    day_1_agent_wise.insert(loc=0, column='ID', value=['' for i in range(day_1_agent_wise.shape[0])])
    day_1_agent_wise.columns = ['ID', 'date', 'AGENTEMAILID', 'EFFORTSCORE', 'FRT', 'aht_secs',
                                'positive_survey_max_streak', 'FRT_max_streak', 'aht_max_streak', 'score',
                                'local_ranking', 'global_rank', 'csat_local_rank', 'csat_global_rank', 'frt_local_rank',
                                'frt_global_rank', 'aht_local_rank', 'aht_global_rank', 'queue']

    convert_dict = {'csat_local_rank': int,
                    'csat_global_rank': int,
                    'frt_local_rank': int,
                    'frt_global_rank': int,
                    'aht_local_rank': int,
                    'aht_global_rank': int,
                    'local_ranking': int,
                    'global_rank': int,
                    }

    day_1_agent_wise = day_1_agent_wise.astype(convert_dict)

    day_1_agent_wise.to_csv("/var/lakshya/files/legacy/legacy_2.csv", index=False, header=True)

    con = pymysql.connect(host='172.16.251.113',
                          user='gokkul-kumar',
                          password='p@S$w0rdf0rg)kku(S38fd()hH',
                          autocommit=True,
                          local_infile=1
                          )
    # Create cursor and execute Load SQL
    cursor = con.cursor()

    sql = "DELETE FROM lakshya.legacy_agent_wise WHERE date = current_date-2"

    cursor.execute(sql)

    cursor.execute(
        "LOAD DATA LOCAL INFILE '/var/lakshya/files/legacy/legacy_2.csv' "
        "INTO TABLE lakshya.legacy_agent_wise FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS")
    cursor.close()
    con.close()

    fromaddr = "cc.automation@swiggy.in"
    # toaddr = "vd.gokkulkumar@swiggy.in,sourav.verma@swiggy.in,wfm-rte@swiggy.in"
    toaddr = ['vd.gokkulkumar@swiggy.in', 'surajit.c@swiggy.in']
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    # msg['To'] = toaddr
    msg['To'] = ", ".join(toaddr)
    # storing the subject
    msg['Subject'] = "Legacry day - 2 successful"
    # string to store the body of the mail
    body = "legacy day - 2 successfully updated"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    # encode into base64
    # encoders.encode_base64(p)
    # p.add_header('Content-Disposition', "attachment; filename= %s")
    # attach the instance 'p' to instance 'msg'
    # msg.attach(p)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "xcdbqpvdmzvckhwh")
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    # terminating the session
    s.quit()
    print("done")
except Exception as err:
    error = ''
    error = str(err)

    fromaddr = "cc.automation@swiggy.in"
    # toaddr = "vd.gokkulkumar@swiggy.in,sourav.verma@swiggy.in,wfm-rte@swiggy.in"
    toaddr = ['vd.gokkulkumar@swiggy.in', 'surajit.c@swiggy.in']
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    # msg['To'] = toaddr
    msg['To'] = ", ".join(toaddr)
    # storing the subject
    msg['Subject'] = "Legacry day - 2 error"
    # string to store the body of the mail
    body = "There is an error in legacy day - 2 file" + error
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    # encode into base64
    # encoders.encode_base64(p)
    # p.add_header('Content-Disposition', "attachment; filename= %s")
    # attach the instance 'p' to instance 'msg'
    # msg.attach(p)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "xcdbqpvdmzvckhwh")
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    # terminating the session
    s.quit()
    print("done")