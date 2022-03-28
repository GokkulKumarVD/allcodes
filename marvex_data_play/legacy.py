#!/usr/bin/env python3
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

# def closureTask(stat, resonForAbrupt, dt_string1, dt_string2):
#     # Updating the Details to Database
#     try:
#         mydb = mysql.connector.connect(host="172.16.251.149", user="clookupuser", password="cL0okUpu$ErP@s$w0r9",
#                                        database="clookup")
#         mycursor = mydb.cursor()
#         sql = "INSERT INTO lakshya (Status, error, datentimebegin, datentimeend) VALUES (%s, %s, %s, %s)"
#         val = (stat, resonForAbrupt, dt_string1, dt_string2)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         # print(mycursor.rowcount, "record inserted.")
#         mycursor.close()
#         mydb.close()
#     except mysql.connector.IntegrityError as err:
#         aplhaerr += f'Connection Error at function closureTask(), Integrity Error: {err} | '


proceed = True



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

#-----------------------------------
x = datetime.now()


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

if proceed:
    aplhaerr = ''
    # Alpha Block - AHT, CSAT & FTR
    try:
        with open("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\rsa_key.p8", "rb") as key:
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
            # print(cs)
        except Exception as err:
            aplhaerr += f'Snowflake Connection Error: {err} |'

        try:
            # print('Download CSAT')


            raw_fetch = cs.execute(
                "SELECT b.ticketid ,b.AGENTEMAILID, to_timestamp(to_timestamp_ltz(b.AGENTASSIGNEDTIME)) assignment_time, queueid, "
                "max(c.EFFORTSCORE) as EFFORTSCORE FROM   STREAMS.PUBLIC.ASSIGN_AGENT b "
                "left join ( Select AGENTEMAILID, EFFORTSCORE, agentid, conversationid, chattype "
                "from STREAMS.PUBLIC.COLLECT_CSAT c where c.effortscore!=-99 "
                "and c.dt >= cast(timeadd('day', -1, CURRENT_DATE) AS varchar) ) c "
                "ON c.conversationid=b.conversationid AND "
                "c.agentid=b.agentid AND c.chattype='agent' "
                "WHERE (b.queueid ilike '%l2%' or b.queueid ilike '%priority%' or b.queueid ilike '%stores%' or b.queueid ilike '%genie%' "
                "or b.queueid ilike '%bau-cancellation%' or b.queueid ilike '%bau-couponrelated%' or b.queueid ilike '%bau-foodissues%' "
                "or b.queueid ilike '%bau-food-special-instruction%' or b.queueid ilike '%bau-orderstatus%' or b.queueid ilike '%bau-paymentrelated%' "
                "or b.queueid ilike '%delivery-instructions%' or b.queueid ilike '%fallback%' or b.queueid ilike '%general-issue%' or b.queueid ilike '%team-1%'"
                ") and b.orgid = 'swiggy' and "
                "b.AGENTEMAILID != 'NOTFILLED' and b.AGENTASSIGNEDTIME between {} and {}  group by 1,2,3,4;".format(
                    y_datetime, cy_datetime))



            surveys = pd.DataFrame(raw_fetch)
            surveys.columns = ['Ticketid', 'AGENTEMAILID', 'TIME_STAMP', 'Queue', 'EFFORTSCORE']
            surveys = surveys[['AGENTEMAILID', 'EFFORTSCORE', 'TIME_STAMP', 'Queue']]

            q_surveys = surveys[['AGENTEMAILID', 'Queue']]

            # surveys.to_csv("/var/lakshya/files/surveys.csv")
            raw_csat = surveys
            # surveys['TIME_STAMP'] = pd.to_datetime(surveys['TIME_STAMP'],unit='ms')
            surveys = surveys[['AGENTEMAILID', 'EFFORTSCORE']]

            # positive survey
            p_survey = surveys[surveys['EFFORTSCORE'] == 1]
            p_survey = p_survey.groupby('AGENTEMAILID').count()
            p_survey = p_survey.reset_index()
            p_survey.columns = ['AGENTEMAILID', 'positive_survey_count']

            # negative survey
            n_survey = surveys[surveys['EFFORTSCORE'] == 0]
            n_survey = n_survey.groupby('AGENTEMAILID').count()
            n_survey = n_survey.reset_index()
            n_survey.columns = ['AGENTEMAILID', 'negative_survey_count']

            csat = raw_csat[raw_csat['EFFORTSCORE'] != -99]
            csat = csat[['AGENTEMAILID', 'EFFORTSCORE', 'TIME_STAMP']]

            csat_agentwise = csat[['AGENTEMAILID', 'EFFORTSCORE']]

            csat_agentwise = csat_agentwise.groupby('AGENTEMAILID').mean() * 100
            csat_agentwise = csat_agentwise.reset_index()

            survey_count = csat.groupby('AGENTEMAILID').count()
            survey_count = survey_count.reset_index()
            survey_count.columns = ['AGENTEMAILID', 'p_n_survey_count', 'remove_this']
            survey_count = survey_count[['AGENTEMAILID', 'p_n_survey_count']]

            survey_count = survey_count.merge(n_survey, how='left', on='AGENTEMAILID')
            survey_count = survey_count.merge(p_survey, how='left', on='AGENTEMAILID')
            survey_count = survey_count.fillna("0")

            cs.close()
            first_block_0 = True
        except Exception as err:
            first_block_0 = False
        first_block_1 = True
    except Exception as err:
        aplhaerr += '#csatcode -> ' + str(err) + '<br>'
        first_block_1 = False


    # AHT
    try:
        with open("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\rsa_key.p8", "rb") as key:
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
            # print(cs)
        except Exception as err:
            aplhaerr += f'Snowflake Connection Error: {err} |'

        try:
            print('Before Download')

            raw_fetch = cs.execute("""select
                                    case
                                      when queueid like '%priority%' then 'Priority'
                                      when queueid like '%combined%' then 'CQ'
                                      when queueid  like '%stores%' and queueid  not like '%combined%' then 'stores'
                                      when queueid  like '%genie%' and queueid  not like '%combined%' then 'genie'
                                      else 'BAU' end Role,
                                    agent_email,
                                    sum(FRT_TOTAL+QUEUE_WAIT_TIME_TOTAL) FRT,
                                    Sum(AHT_TOTAL),
                                    Sum(CHAT_COUNT)
                                    from analytics.cc_cx.customer_interaction_live
                                    where EVENT_60MIN_SLOT between '{}' and '{}'  and ((queueid not like '%stores%' and queueid not like '%genie%' and queueid not like '%daily%'
                                    and queueid not in( 'l2-team-14','l2-team-1','l2-team-2','l2-team-10','all-go','daily-fallback',
                                    'cafe-queue','bengali','hindi','telugu','malayalam','kannada','marathi'
                                    )) OR queueid like '%combined%')
                                    group by 1,2;""".format(y_time, cy_today))






            aht = pd.DataFrame(raw_fetch)
            # aht.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\aht.csv")
            # aht.columns = ['ticket_id', 'AGENTEMAILID', 'aht_secs']
            # aht = aht[~aht['aht_secs'].isnull()]
            # aht1 = aht
            # aht = aht[['AGENTEMAILID', 'aht_secs']]
            # aht['aht_secs'] = aht['aht_secs'].astype('int64')
            #
            # # avg aht df
            # avg_aht = aht.groupby('AGENTEMAILID').mean().reset_index()

            aht.columns = ['queue', 'AGENTEMAILID', 'FRT', 'aht_secs', 'chat_count']
            aht_frt = aht[~aht['aht_secs'].isnull()]


            survey_count['no_survey'] = aht_frt['chat_count'] - survey_count['p_n_survey_count']
            # survey_count = survey_count[
            #     ['AGENTEMAILID', 'p_n_survey_count', 'positive_survey_count', 'negative_survey_count', 'no_survey']]
            survey_count.fillna(0, inplace=True)

            agent_wise = pd.merge(aht_frt, csat_agentwise, how='left', on='AGENTEMAILID')
            agent_wise = agent_wise.merge(survey_count, how='left', on='AGENTEMAILID')

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


            agent_wise['Partners'] = agent_wise['AGENTEMAILID'].apply(osp)
            agent_wise['EFFORTSCORE'] = agent_wise['EFFORTSCORE'].fillna(0)
            agent_wise.fillna(0, inplace=True)

            agent_wise['queue'] = agent_wise['queue'].str.lower()


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
                    return "L2_stores_genie"
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


            agent_wise['queue'] = agent_wise['queue'].apply(q_rename)

            # function to find csat scores based on q ids
            def score(agent_wise):
                if agent_wise['queue'] == "L2_food":
                    return 20 * (agent_wise['EFFORTSCORE'] - 25) / (25 * 1)

                elif agent_wise['queue'] == "L2_stores_genie":
                    return 20 * (agent_wise['EFFORTSCORE'] - 65) / (65 * 1)

                elif agent_wise['queue'] == "Genie":
                    return 20 * (agent_wise['EFFORTSCORE'] - 74) / (78 * 1)

                elif agent_wise['queue'] == "Stores":
                    return 20 * (agent_wise['EFFORTSCORE'] - 74.9) / (80 * 1)

                elif agent_wise['queue'] == "Priority":
                    return 25 * (agent_wise['EFFORTSCORE'] - 86) / (90 * 1)

                elif agent_wise['queue'] == "Bau-food":
                    return 15 * (agent_wise['EFFORTSCORE'] - 58.99) / (63 * 1)


            agent_wise['csat_score'] = agent_wise.apply(score, axis=1)


            # function to find FRT scores based on q ids
            def score(agent_wise):
                if agent_wise['queue'] == "L2_food":
                    return 0
                elif agent_wise['queue'] == "L2_stores_genie":
                    return 0
                elif agent_wise['queue'] == "Genie":
                    return 0
                elif agent_wise['queue'] == "Stores":
                    return 0
                elif agent_wise['queue'] == "Priority":
                    return 0
                elif agent_wise['queue'] == "Bau-food":
                    return 10 * (agent_wise['FRT'] - 15) / (10 * -1)


            agent_wise['FRT_score'] = agent_wise.apply(score, axis=1)


            # function to find AHT scores based on q ids
            def score(agent_wise):
                if agent_wise['queue'] == "L2_food":
                    return 20 * (agent_wise['aht_secs'] - 600) / (540 * -1)
                elif agent_wise['queue'] == "L2_stores_genie":
                    return 30 * (agent_wise['aht_secs'] - 840) / (660 * -1)
                elif agent_wise['queue'] == "Genie":
                    return 30 * (agent_wise['aht_secs'] - 330) / (299 * -1)
                elif agent_wise['queue'] == "Stores":
                    return 30 * (agent_wise['aht_secs'] - 330) / (299 * -1)
                elif agent_wise['queue'] == "Priority":
                    return 30 * (agent_wise['aht_secs'] - 273) / (260 * -1)
                elif agent_wise['queue'] == "Bau-food":
                    return 10 * (agent_wise['aht_secs'] - 221) / (200 * -1)


            agent_wise['aht_score'] = agent_wise.apply(score, axis=1)


            # fill frt with zeros for certain q
            def fill_zero(agent_wise):
                if agent_wise['queue'] != 'Bau-food':
                    return 0
                else:
                    return agent_wise['FRT']


            agent_wise['FRT'] = agent_wise.apply(fill_zero, axis=1)

            # converting from obj to float
            agent_wise['aht_score'] = agent_wise['aht_score'].astype('float')
            # total scores
            agent_wise['score'] = agent_wise['csat_score'] + agent_wise['FRT_score'] + agent_wise['aht_score']
            agent_wise.drop(columns=['FRT_score', 'csat_score', 'aht_score'], inplace=True)

            # remove agents name where chats taken are less than 10
            # agent_wise_q_list = agent_wise

            # unique q ids
            q_list = agent_wise['queue'].unique().tolist()


            less_chat_count = agent_wise.query('chat_count < 10')
            less_chat_count = less_chat_count[(less_chat_count['queue']) != 'L2_stores_genie']
            less_chat_count.drop_duplicates(subset=['AGENTEMAILID'], keep='first', inplace=True)

            ed_s_g = agent_wise[agent_wise['queue'] == 'L2_stores_genie']

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


            agent_wise = agent_wise[(agent_wise['chat_count']) >= 10]
            agent_wise = agent_wise[(agent_wise['queue']) != 'L2_stores_genie']

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

            this = agent_wise
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

                agent_wise1['csat_local_rank'] = agent_wise1.groupby('Partners')['EFFORTSCORE'].rank(ascending=False, method='min')
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




            first_block_2 = True
        except Exception as err:
            first_block_2 = False
        first_block_3 = True
    except Exception as err:
        aplhaerr += '#ahtcode -> ' + str(err) + '<br>'
        first_block_3 = False

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

    day_1_agent_wise.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\legacy.csv", index=False, header=True)





if not first_block_0 or not first_block_1 or not first_block_2 or not first_block_3:
    proceed = False
    try:
        # Pushing to DB
        closureTask('FAIL', 'Code Execution Error - ' + aplhaerr, dt_string, dt_string2)
    finally:
        overall = False
        print("-----------------------------------------------------------------------")
        print("Start Time: ", dt_string)
        print("Finish Time: ", dt_string2)
        print("FAILED")
        print("Error: ", aplhaerr)
        print("-----------------------------------------------------------------------")
        exit()
else:
    try:
        closureTask('SUCCESS', 'NA', dt_string, dt_string2)
    finally:
        print("-----------------------------------------------------------------------")
        print("Start Time: ",dt_string)
        print("Finish Time: ", dt_string2)
        print('SUCCESS')
        print("-----------------------------------------------------------------------")
        exit()

