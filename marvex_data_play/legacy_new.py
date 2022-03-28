#!/usr/bin/env python3
# !/usr/bin/env python3
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd
import pymysql
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
import warnings
from datetime import datetime
from datetime import timedelta

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)

username = getpass.getuser()

now = datetime.now()
now_timestp = datetime.now().timestamp()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

time_check = now.strftime("%H")
time_check = int(time_check)

pd.set_option('display.max_columns', 500)

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)

# ------------------------
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
c_today = now.strftime("%Y-%m-%d")
c_time = " 07:00:00"
c_today_time = c_today + c_time
c_date_time_obj = datetime.strptime(c_today_time, '%Y-%m-%d %H:%M:%S')
c_datetime = int(c_date_time_obj.timestamp())

ce_time = " 23:59:00"
ce_today_time = c_today + ce_time
ce_date_time_obj = datetime.strptime(ce_today_time, '%Y-%m-%d %H:%M:%S')
ce_datetime = int(ce_date_time_obj.timestamp())

# -----------------------------------
x = datetime.now()

aplhaerr = ''

if x.day == 1:
    from datetime import datetime, timedelta

    y_date = datetime.now() - timedelta(1)
    y_date = y_date.strftime("%Y-%m-%d")
    y_time = " 07:00:00"
    y_time = y_date + y_time
    y_date_time_obj = datetime.strptime(y_time, '%Y-%m-%d %H:%M:%S')
    y_datetime = int(y_date_time_obj.timestamp())
else:
    y_date = datetime.today().date()
    y_date = y_date.replace(day=x.day - 1)
    y_date = y_date.strftime("%Y-%m-%d")
    y_time = " 07:00:00"
    y_time = y_date + y_time
    y_date_time_obj = datetime.strptime(y_time, '%Y-%m-%d %H:%M:%S')
    y_datetime = int(y_date_time_obj.timestamp())

cy_today = c_today + " 06:59:00"
cy_date_time_obj = datetime.strptime(cy_today, '%Y-%m-%d %H:%M:%S')
cy_datetime = int(cy_date_time_obj.timestamp())

try:
    with open("C:/Users/vd.gokkulkumar/Desktop/projects/rnr/rsa_key.p8", "rb") as key:
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
        #        database='STREAMS',
        # warehouse='NONTECH_WH_01',
        role='CC_AUTOMATION',
        # schema='CC_AUTOMATION_DATA_READER'
    )
    cs = ctx.cursor()

    try:
        raw_fetch = cs.execute("""with Atten as(
        select AGENTEMAIL, case when hour(bucket)<7 then to_date(bucket)-1 else to_date(bucket) end
        DTt,sum(AVAILABLE_MINUTES) Ready_hours,sum(LOGIN_MINUTES) as Login_Hours
        from "ANALYTICS"."CC_CX"."CHAT_AGENTS_PRODUCTIVITY"
        where BUCKET between '{}' and '{}'
        group by 1,2),
        CHAT as(
        Select *,
              case
            when agent_email like '%_ag@external.swiggy.in' then 'OS-Startek'
            when agent_email like '%_qup@external.swiggy.in' then 'OS-QUP'
            when agent_email like '%_ae@external.swiggy.in' then 'OS-ASR'
            when agent_email like '%_kt@external.swiggy.in' then 'OS-Kochar'
          when agent_email like '%kt_@external.swiggy.in' then 'OS-Kochar'
         when agent_email like '%cscb@external.swiggy.in' then 'OS-CBSL'
          when agent_email like '%cskt@external.swiggy.in' then 'OS-Kochar'

          when agent_email like '%_cb@external.swiggy.in' then 'OS-CBSL'
            when agent_email like '%_tm@external.swiggy.in' then 'OS-TM'
            when agent_email like '%_ison@external.swiggy.in' then 'OS-ISON'
            when agent_email like '%_hrh@external.swiggy.in' then 'OS-HRH'
            when agent_email like '%_fu@external.swiggy.in' then 'OS-Fusion'
            when agent_email like '%_31p@external.swiggy.in' then 'OS-31p'

          else 'In-House' end as Center,

        case
          when queueid like '%priority%' then 'Priority'
          when queueid like '%combined%' then 'CQ'
          when queueid  like '%stores%' and queueid  not like '%combined%' then 'stores'
         when queueid  like '%genie%' and queueid  not like '%combined%' then 'genie'
        else 'BAU' end Role

        from facts.public.customer_interaction_fact
        where agent_email <>'Bot' and AGENT_ASSIGNMENT_TIME between '{}' and '{}'
        and (queueid ilike '%l2%' or queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%' 
                        or queueid ilike '%bau-cancellation%' or queueid ilike '%bau-couponrelated%' or queueid ilike '%bau-foodissues%' 
                        or queueid ilike '%bau-food-special-instruction%' or queueid ilike '%bau-orderstatus%' or queueid ilike '%bau-paymentrelated%' 
                        or queueid ilike '%delivery-instructions%' or queueid ilike '%fallback%' or queueid ilike '%general-issue%'  or queueid ilike '%meat%' or queueid ilike '%team-1%'
                        )
        group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
        19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
        40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,
        61,62,63,64,65, 66,67,68,69,70, 71,72, 73,74,75,76),



           cc as(
        Select *,
        row_number() over (partition by agent_email order by AGENT_ASSIGNMENT_TIME Asc) as RN
        from Chat),

        BB as(Select * from CC),
        final as(
        Select a.agent_email,a.RN,count
        (case when a.RN<b.RN and a.conversation_closed_time>=b.AGENT_ASSIGNMENT_TIME then b.conversationid end) cun
        from cc a left join bb b on a.agent_email=b.agent_email
        group by 1,2),

        cun as(
        Select a.*,
          case when hour(AGENT_ASSIGNMENT_TIME)<7 then to_date(AGENT_ASSIGNMENT_TIME)-1 else to_date(AGENT_ASSIGNMENT_TIME) end datee,
          row_number() over (partition by entityid,NODELABEL order by AGENT_ASSIGNMENT_TIME Desc ) as FT,
        case when b.cun+1>4 then 4 else b.cun+1 end Cuncurrency from cc a left join final b on a.agent_email=b.agent_email and a.RN=b.RN)


           select
           datee,
        a.agent_email,a.Center, a.Role,
        count(distinct Ticket_id) as interactions,
        sum(case when frt_in_secs>=0 then frt_in_secs else 0 end) as over_all_frtinsec,
         count(case when frt_in_secs>=0 then ticket_id end) as frt_count,

        count( case when effortscore in (1) then ticket_id end) as promotors,
        count( case when effortscore in (1,0) then ticket_id end) as all_csat,
        Sum(AHT_IN_SECS)/60 AHT,


        Sum(case when queue_wait_time_in_secs>=0 then queue_wait_time_in_secs end ) as queue_wait_time,
                      b.Ready_hours,
                      count(case when FT>1 and entityid>1 then TICKET_ID end ) ftnr,
                     count(case when entityid>1 then TICKET_ID end ) total_orders,
                      sum(Cuncurrency) Cuncurrency,
                      b.Login_Hours

         from cun a left join Atten b on a.agent_email=b.AGENTEMAIL and a.datee=b.dtt

         group by 1,2,3,4,12,16""".format(y_time, cy_today, y_time, cy_today))

        legacy = pd.DataFrame(raw_fetch)

        # legacy.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\data.csv")
    except:
        print("error")

    # calculation avg aht, frt, csat
    legacy.columns = ['date', 'agentemail', 'center', 'queue', 'interactions', 'over_all_frt', 'frt_count', 'promotors',
                      'all_csat',
                      'aht', 'queue_wait_time', 'ready_hours', 'ftnr', 'total_orders', 'cuncurrency', 'login_hours']

    legacy.fillna(0, inplace=True)

    # removing error rows
    legacy = legacy[legacy['frt_count'] > 0]

    # calculating
    legacy['avg_csat'] = (legacy['promotors'] / legacy['all_csat']) * 100
    legacy['avg_frt_seconds'] = (legacy['over_all_frt']) / legacy['frt_count']
    legacy['avg_aht_mins'] = legacy['aht'] / legacy['frt_count']
    legacy['avg_aht_mins'] = legacy['avg_aht_mins'].astype('float')

    legacy_req = legacy[
        ['date', 'agentemail', 'center', 'queue', 'avg_csat', 'avg_aht_mins', 'avg_frt_seconds', 'interactions']]

    legacy_req.columns = ['date', 'AGENTEMAILID', 'Partners', 'queue', 'EFFORTSCORE', 'aht_secs', 'FRT', 'chat_count']


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


    legacy_req['partners'] = legacy_req['AGENTEMAILID'].apply(osp)

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

    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.isoformat()
    # agent_wise['date'] = yesterday.strftime('%y-%m-%d')
    agent_wise['date'] = yesterday

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

    day_1_agent_wise.to_csv("C:/Users/vd.gokkulkumar/Desktop/projects/rnr/legacy.csv", index=False, header=True)

    try:
        con = pymysql.connect(host='172.16.251.113',
                              user='gokkul-kumar',
                              password='p@S$w0rdf0rg)kku(S38fd()hH',
                              autocommit=True,
                              local_infile=1
                              )
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(
            "LOAD DATA LOCAL INFILE 'C:/Users/vd.gokkulkumar/Desktop/projects/rnr/legacy.csv' "
            "INTO TABLE lakshya.legacy_agent_wise FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS")
        cursor.close()
        con.close()

        updated = True
    except Exception as err:
        aplhaerr += '#upload_csv -> ' + str(err) + '<br>'
        updated = False
except:
    print("error")
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import shutil

    # time.sleep(120)

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
    msg['Subject'] = "Legacry error"

    # string to store the body of the mail
    body = "There is an error in legacy file"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    # encode into base64
    # encoders.encode_base64(p)

    # p.add_header('Content-Disposition', "attachment; filename= %s")

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

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