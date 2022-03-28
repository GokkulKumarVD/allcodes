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


# ContinuityVariable
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








# CSAT
# try:
#     x = datetime.now()
#     if x.day == 1:
#         given_date = datetime.today().date()
#         first_day_of_month = given_date.replace(day=1)
#         first_day_of_month = given_date.replace(month=x.month - 1)
#         first_day_of_month = first_day_of_month.isoformat()
#     else:
#         given_date = datetime.today().date()
#         first_day_of_month = given_date.replace(day=1)
#         first_day_of_month = first_day_of_month.isoformat()
#
# except:
#     proceed = False

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

            if time_check >= 0 | time_check <= 6:
                print('above 24')
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

            else:
                print('below 24')
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
                        c_datetime, ce_datetime))


            surveys = pd.DataFrame(raw_fetch)
            surveys.columns = ['Ticketid', 'AGENTEMAILID', 'TIME_STAMP', 'Queue', 'EFFORTSCORE']
            surveys = surveys[['AGENTEMAILID', 'EFFORTSCORE', 'TIME_STAMP', 'Queue']]

            q_surveys = surveys[['AGENTEMAILID', 'Queue']]

            surveys.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\surveys.csv")
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

            survey_count = survey_count.merge(p_survey, how='left', on='AGENTEMAILID')
            survey_count = survey_count.merge(n_survey, how='left', on='AGENTEMAILID')
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
            # print('Before Download')

            if time_check >= 0 | time_check <= 6:
                raw_fetch = cs.execute(
                    "with chat_closure as ( select a.ticketid, a.AGENTID ,a.AGENTEMAILID,AGENTASSIGNEDTIME, d.time_stamp as conversation_closed_time from streams.public.assign_agent a LEFT JOIN streams.public.agent_csat_collection_trigger d ON        a.conversationid=d.conversationid AND       d.agentassignmenttime=a.agentassignedtime AND       d.agentid=a.agentid where (queueid ilike '%l2%' or queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%'or queueid ilike '%bau-cancellation%' or queueid ilike '%bau-couponrelated%' or queueid ilike '%bau-foodissues%'or queueid ilike '%bau-food-special-instruction%' or queueid ilike '%bau-orderstatus%' or queueid ilike '%bau-paymentrelated%'or queueid ilike '%delivery-instructions%' or queueid ilike '%fallback%' or queueid ilike '%general-issue%' or queueid ilike '%team-1%')and a.orgid = 'swiggy' and a.dt between dateadd(day,-1,current_date) and dateadd(day,+1,current_date) and conversation_closed_time is not null and a.agentid is not null ), snooze_flag as ( select distinct assignmentid as ticket_id , 'snooze' as flag, timestamp from STREAMS.PUBLIC.CRM_TICKET_ACTIONS_EVENT where orgid= 'swiggy' and dt  between dateadd(day,-1,current_date) and dateadd(day,+1,current_date) ), chat_snooze_details as ( select distinct action, assignmentid as ticket_id, timestamp, lag(action) over (partition by assignmentid order by timestamp,action ) as previous_action, lag(timestamp) over (partition by assignmentid order by timestamp,action ) as previous_action_timestamp, lead(action) over (partition by assignmentid order by timestamp,action ) as next_action, lead(timestamp) over (partition by assignmentid order by timestamp,action ) as next_action_timestamp from STREAMS.PUBLIC.CRM_TICKET_ACTIONS_EVENT where orgid = 'swiggy' and dt  between dateadd(day,-1,current_date) and dateadd(day,+1,current_date) ), presnooze as ( select distinct ticket_id, timestamp as first_snooze_time from chat_snooze_details where action='snoozed' and previous_action is null ), unsnooze_details as ( select distinct ticket_id, next_action_timestamp as unsnooze_time , row_number() over (partition by ticket_id order by next_action_timestamp) as rnk from chat_snooze_details where action ='unsnooze_ready' and next_action = 'unsnoozed' order by 1,2,3 ), snooze_details as ( select distinct ticket_id, next_action_timestamp  as snooze_time_1, row_number() over (partition by ticket_id order by timestamp) as rnk from chat_snooze_details where action='unsnoozed' and (next_action ='snoozed' or next_action is null) order by 1,2,3 ) , snooze_details_final as ( select distinct ticket_id, rnk, (case when snooze_time_1 is null then (cast(conversation_closed_time as bigint)/1000) else snooze_time_1 end) as snooze_time from snooze_details s left join chat_closure c on s.ticket_id=c.ticketid ), snooze_unsnooze_details as ( select a.ticket_id, a.rnk, a.unsnooze_time, b.snooze_time, datediff('second',to_timestamp_ltz(unsnooze_time),to_timestamp_ltz(snooze_time)) as snooze_unsnooze_time from unsnooze_details a inner join snooze_details_final b on a.ticket_id=b.ticket_id and a.rnk=b.rnk group by 1,2,3,4,5 ) ,chat as ( ( Select distinct c.ticketid ,concat(c.ticketid,'-0') ticket_id , c.AGENTID ,c.AGENTEMAILID agent_email ,to_timestamp(to_timestamp_ltz(c.AGENTASSIGNEDTIME)) AGENT_ASSIGNMENT_TIME ,to_timestamp(to_timestamp_ltz(case when p.first_snooze_time is not null then first_snooze_time else conversation_closed_time/1000 end)) as conversation_closed_time ,timediff(second, to_timestamp(to_timestamp_ltz(c.AGENTASSIGNEDTIME)), to_timestamp(to_timestamp_ltz(case when p.first_snooze_time is not null then first_snooze_time else conversation_closed_time/1000 end ))) aht_in_secs from chat_closure c left join presnooze p on c.ticketid =p.ticket_id ) union ( Select distinct a.ticket_id ticketid , concat(a.ticket_id,'-',a.rnk) ticket_id, c.agentid, c.agentemailid, to_timestamp(to_timestamp_ltz(a.UNSNOOZE_TIME)) AGENT_ASSIGNMENT_TIME ,to_timestamp(to_timestamp_ltz(a.SNOOZE_TIME)) conversation_closed_time ,timediff(second,to_timestamp(to_timestamp_ltz(a.UNSNOOZE_TIME)), to_timestamp(to_timestamp_ltz(a.SNOOZE_TIME))) aht_in_secs from snooze_unsnooze_details a inner join chat_closure c on a.ticket_id = c.ticketid ) ) ,final as( Select b.agent_email,B.ticket_iD,Sum(case when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME<=b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and a.agent_email=b.agent_email and a.conversation_closed_time >b.conversation_closed_time then 1 when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME<=b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and a.agent_email=b.agent_email and a.conversation_closed_time between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.aht_in_secs <> 0 then timediff(seconds,b.AGENT_ASSIGNMENT_TIME,a.conversation_closed_time) /b.AHT_in_secs when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and b.aht_in_secs <> 0 and a.agent_email=b.agent_email and a.conversation_closed_time <= b.conversation_closed_time then a.aht_in_secs /b.AHT_in_secs when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and b.aht_in_secs <> 0 and a.agent_email=b.agent_email and a.conversation_closed_time > b.conversation_closed_time then timediff(seconds,a.AGENT_ASSIGNMENT_TIME,b.conversation_closed_time) /b.AHT_in_secs else null end) cun from chat a left join chat b on a.agent_email=b.agent_email group by 1,2), final2 as( Select a.*, case when b.cun is null then 1 else b.cun+1 end Concurrency from chat a left join final b on a.ticket_id = b.ticket_id ) Select cast(TICKETID as integer) as TICKET_ID , AGENT_EMAIL , sum(CONC_AHT) CONC_AHT from ( Select distinct * , aht_in_secs/Concurrency as Conc_aht from final2 where AGENT_ASSIGNMENT_TIME > '{}' and AGENT_ASSIGNMENT_TIME > '{}') group by 1,2;".format(y_time, cy_today))
                # print('after  24')
            else:
                raw_fetch = cs.execute(
                    "with chat_closure as ( select a.ticketid, a.AGENTID ,a.AGENTEMAILID,AGENTASSIGNEDTIME, d.time_stamp as conversation_closed_time from streams.public.assign_agent a LEFT JOIN streams.public.agent_csat_collection_trigger d ON        a.conversationid=d.conversationid AND       d.agentassignmenttime=a.agentassignedtime AND       d.agentid=a.agentid where (queueid ilike '%l2%' or queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%'or queueid ilike '%bau-cancellation%' or queueid ilike '%bau-couponrelated%' or queueid ilike '%bau-foodissues%'or queueid ilike '%bau-food-special-instruction%' or queueid ilike '%bau-orderstatus%' or queueid ilike '%bau-paymentrelated%'or queueid ilike '%delivery-instructions%' or queueid ilike '%fallback%' or queueid ilike '%general-issue%' or queueid ilike '%team-1%') and a.orgid = 'swiggy' and a.dt between dateadd(day,-1,current_date-1) and dateadd(day,+1,current_date) and conversation_closed_time is not null and a.agentid is not null ), snooze_flag as ( select distinct assignmentid as ticket_id , 'snooze' as flag, timestamp from STREAMS.PUBLIC.CRM_TICKET_ACTIONS_EVENT where orgid= 'swiggy' and dt  between dateadd(day,-1,current_date-1) and dateadd(day,+1,current_date) ), chat_snooze_details as ( select distinct action, assignmentid as ticket_id, timestamp, lag(action) over (partition by assignmentid order by timestamp,action ) as previous_action, lag(timestamp) over (partition by assignmentid order by timestamp,action ) as previous_action_timestamp, lead(action) over (partition by assignmentid order by timestamp,action ) as next_action, lead(timestamp) over (partition by assignmentid order by timestamp,action ) as next_action_timestamp from STREAMS.PUBLIC.CRM_TICKET_ACTIONS_EVENT where orgid = 'swiggy' and dt  between dateadd(day,-1,current_date-1) and dateadd(day,+1,current_date) ), presnooze as ( select distinct ticket_id, timestamp as first_snooze_time from chat_snooze_details where action='snoozed' and previous_action is null ), unsnooze_details as ( select distinct ticket_id, next_action_timestamp as unsnooze_time , row_number() over (partition by ticket_id order by next_action_timestamp) as rnk from chat_snooze_details where action ='unsnooze_ready' and next_action = 'unsnoozed' order by 1,2,3 ), snooze_details as ( select distinct ticket_id, next_action_timestamp  as snooze_time_1, row_number() over (partition by ticket_id order by timestamp) as rnk from chat_snooze_details where action='unsnoozed' and (next_action ='snoozed' or next_action is null) order by 1,2,3 ) , snooze_details_final as ( select distinct ticket_id, rnk, (case when snooze_time_1 is null then (cast(conversation_closed_time as bigint)/1000) else snooze_time_1 end) as snooze_time from snooze_details s left join chat_closure c on s.ticket_id=c.ticketid ), snooze_unsnooze_details as ( select a.ticket_id, a.rnk, a.unsnooze_time, b.snooze_time, datediff('second',to_timestamp_ltz(unsnooze_time),to_timestamp_ltz(snooze_time)) as snooze_unsnooze_time from unsnooze_details a inner join snooze_details_final b on a.ticket_id=b.ticket_id and a.rnk=b.rnk group by 1,2,3,4,5 ) ,chat as ( ( Select distinct c.ticketid ,concat(c.ticketid,'-0') ticket_id , c.AGENTID ,c.AGENTEMAILID agent_email ,to_timestamp(to_timestamp_ltz(c.AGENTASSIGNEDTIME)) AGENT_ASSIGNMENT_TIME ,to_timestamp(to_timestamp_ltz(case when p.first_snooze_time is not null then first_snooze_time else conversation_closed_time/1000 end)) as conversation_closed_time ,timediff(second, to_timestamp(to_timestamp_ltz(c.AGENTASSIGNEDTIME)), to_timestamp(to_timestamp_ltz(case when p.first_snooze_time is not null then first_snooze_time else conversation_closed_time/1000 end ))) aht_in_secs from chat_closure c left join presnooze p on c.ticketid =p.ticket_id ) union ( Select distinct a.ticket_id ticketid , concat(a.ticket_id,'-',a.rnk) ticket_id, c.agentid, c.agentemailid, to_timestamp(to_timestamp_ltz(a.UNSNOOZE_TIME)) AGENT_ASSIGNMENT_TIME ,to_timestamp(to_timestamp_ltz(a.SNOOZE_TIME)) conversation_closed_time ,timediff(second,to_timestamp(to_timestamp_ltz(a.UNSNOOZE_TIME)), to_timestamp(to_timestamp_ltz(a.SNOOZE_TIME))) aht_in_secs from snooze_unsnooze_details a inner join chat_closure c on a.ticket_id = c.ticketid ) ) ,final as( Select b.agent_email,B.ticket_iD,Sum(case when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME<=b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and a.agent_email=b.agent_email and a.conversation_closed_time >b.conversation_closed_time then 1 when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME<=b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and a.agent_email=b.agent_email and a.conversation_closed_time between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.aht_in_secs <> 0 then timediff(seconds,b.AGENT_ASSIGNMENT_TIME,a.conversation_closed_time) /b.AHT_in_secs when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and b.aht_in_secs <> 0 and a.agent_email=b.agent_email and a.conversation_closed_time <= b.conversation_closed_time then a.aht_in_secs /b.AHT_in_secs when b.ticket_iD<>a.ticket_iD and a.AGENT_ASSIGNMENT_TIME between b.AGENT_ASSIGNMENT_TIME and b.conversation_closed_time and b.conversation_closed_time is not null  and a.conversation_closed_time is not null and b.aht_in_secs <> 0 and a.agent_email=b.agent_email and a.conversation_closed_time > b.conversation_closed_time then timediff(seconds,a.AGENT_ASSIGNMENT_TIME,b.conversation_closed_time) /b.AHT_in_secs else null end) cun from chat a left join chat b on a.agent_email=b.agent_email group by 1,2), final2 as( Select a.*, case when b.cun is null then 1 else b.cun+1 end Concurrency from chat a left join final b on a.ticket_id = b.ticket_id ) Select cast(TICKETID as integer) as TICKET_ID , AGENT_EMAIL , sum(CONC_AHT) CONC_AHT from ( Select distinct * , aht_in_secs/Concurrency as Conc_aht from final2 where AGENT_ASSIGNMENT_TIME > '{}' ) group by 1,2;".format(c_today_time))
                # print('below 24')

            aht = pd.DataFrame(raw_fetch)
            aht.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\aht.csv")
            aht.columns = ['ticket_id', 'AGENTEMAILID', 'aht_secs']
            aht = aht[~aht['aht_secs'].isnull()]
            aht1 = aht
            aht = aht[['AGENTEMAILID', 'aht_secs']]
            aht['aht_secs'] = aht['aht_secs'].astype('int64')

            # avg aht df
            avg_aht = aht.groupby('AGENTEMAILID').mean().reset_index()

            first_block_0_aht = True
        except Exception as err:
            first_block_0_aht = False
        first_block_1_aht = True
    except Exception as err:
        aplhaerr += '#ahtcode -> ' + str(err) + '<br>'
        first_block_1_aht = False

    # FRT
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
            # print('Before Download')

            if time_check >= 0 | time_check <= 6:
                raw_fetch = cs.execute(
                    "SELECT m.conversationid, try_cast(split_part(m.senderid,'-',2) AS bigint) AS agent_id, m.createdat AS createdat "
                    "FROM streams.public.dp_message_created m WHERE  sendertype = 'agent' and m.dt = CURRENT_DATE-1 "
                    "AND  mod(time_stamp, 24*60*60*1000) >= 7 * 60*60*1000"
                    "union "
                    "SELECT m.conversationid, try_cast(split_part(m.senderid,'-',2) AS bigint) AS agent_id, m.createdat AS createdat "
                    "FROM streams.public.dp_message_created m WHERE  sendertype = 'agent' and m.dt = CURRENT_DATE")

                # print('above 24')
            else:
                raw_fetch = cs.execute(
                    "SELECT m.conversationid, try_cast(split_part(m.senderid,'-',2) AS bigint) AS agent_id, m.createdat AS createdat "
                    "FROM streams.public.dp_message_created m WHERE  sendertype = 'agent' "
                    "and m.dt = CURRENT_DATE AND  mod(time_stamp, 24*60*60*1000) >= 7 * 60*60*1000")

                # print('below 24')

            # print('Download Completed')
            dp_message_created = pd.DataFrame(raw_fetch)
            dp_message_created.columns = ['CONVERSATIONID', 'AGENTID', 'CREATEDAT']

        finally:
            cs.close()

        first_block_2 = True
    except Exception as err:
        aplhaerr += '#FRT_lvl1 -> ' + str(err) + '<br>'
        first_block_2 = False

    # downloading FRT query seperately and then merge
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
            # print('Before Download')

            if time_check >= 0 | time_check <= 6:
                raw_fetch = cs.execute(
                    "SELECT AGENTASSIGNEDTIME,AGENTEMAILID,AGENTID,CONVERSATIONID, queueid "
                    "FROM streams.public.assign_agent b WHERE "
                    "(queueid ilike '%l2%' or  queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%' "
                    "or b.queueid ilike '%bau-cancellation%' or b.queueid ilike '%bau-couponrelated%' or b.queueid ilike '%bau-foodissues%' "
                    "or b.queueid ilike '%bau-food-special-instruction%' or b.queueid ilike '%bau-orderstatus%' or b.queueid ilike '%bau-paymentrelated%' "
                    "or b.queueid ilike '%delivery-instructions%' or b.queueid ilike '%fallback%' or b.queueid ilike '%general-issue%' or b.queueid ilike '%team-1%') "
                    "and b.dt = CURRENT_DATE-1 and orgid = 'swiggy' and mod(time_stamp, 24*60*60*1000) >= 7 * 60*60*1000 "

                    "union "

                    "SELECT AGENTASSIGNEDTIME,AGENTEMAILID,AGENTID,CONVERSATIONID, queueid "
                    "FROM streams.public.assign_agent b WHERE "
                    "(queueid ilike '%l2%' or  queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%' "
                    "or b.queueid ilike '%bau-cancellation%' or b.queueid ilike '%bau-couponrelated%' or b.queueid ilike '%bau-foodissues%' "
                    "or b.queueid ilike '%bau-food-special-instruction%' or b.queueid ilike '%bau-orderstatus%' or b.queueid ilike '%bau-paymentrelated%' "
                    "or b.queueid ilike '%delivery-instructions%' or b.queueid ilike '%fallback%' or b.queueid ilike '%general-issue%' or b.queueid ilike '%team-1%') "
                    "and b.dt = CURRENT_DATE")

                # print('above 24')
            else:
                raw_fetch = cs.execute(
                    "SELECT AGENTASSIGNEDTIME,AGENTEMAILID,AGENTID,CONVERSATIONID, queueid "
                    "FROM streams.public.assign_agent b WHERE "
                    "(queueid ilike '%l2%' or queueid ilike '%priority%' or queueid ilike '%stores%' or queueid ilike '%genie%' "
                    "or b.queueid ilike '%bau-cancellation%' or b.queueid ilike '%bau-couponrelated%' or b.queueid ilike '%bau-foodissues%' "
                    "or b.queueid ilike '%bau-food-special-instruction%' or b.queueid ilike '%bau-orderstatus%' or b.queueid ilike '%bau-paymentrelated%' "
                    "or b.queueid ilike '%delivery-instructions%' or b.queueid ilike '%fallback%' or b.queueid ilike '%general-issue%' or b.queueid ilike '%team-1%') "
                    "and b.dt = CURRENT_DATE and orgid = 'swiggy' and mod(time_stamp, 24*60*60*1000) >= 7 * 60*60*1000 ")

                # print('below 24')

            # print('Download Completed')
            assign_agent = pd.DataFrame(raw_fetch)
            assign_agent.columns = ['AGENTASSIGNEDTIME', 'AGENTEMAILID', 'AGENTID', 'CONVERSATIONID', 'queue']

            q_frt = assign_agent[['AGENTEMAILID', 'queue']]

            frt = pd.merge(assign_agent, dp_message_created[['CONVERSATIONID', 'AGENTID', 'CREATEDAT']], how='left',
                           on=['CONVERSATIONID', 'AGENTID'])

            frt = frt[(frt['AGENTASSIGNEDTIME']) <= (frt['CREATEDAT'])]

            frt_score = frt.groupby(['CONVERSATIONID', 'AGENTID', 'AGENTASSIGNEDTIME']).CREATEDAT.agg(
                ['min']).reset_index()

            frt_score.rename(columns={"min": "AGENT_FIRST_MESSAGE_TIME"}, inplace=True)

            # remove duplicate email id
            assign_agent.drop_duplicates(subset=['AGENTID'], inplace=True)

            frt_score = frt_score.merge(assign_agent, how='left', on='AGENTID')

            frt_score.drop(columns=['AGENTASSIGNEDTIME_y', 'CONVERSATIONID_y', 'queue'], inplace=True)

            frt_score.columns = ['CONVERSATIONID', 'AGENTID', 'AGENTASSIGNEDTIME', 'AGENT_FIRST_MESSAGE_TIME',
                                 'AGENTEMAILID']
            frt_score.sort_values(by=['AGENTASSIGNEDTIME'], ascending=True, inplace=True)

            # finding out the number of chats
            chat_count = frt_score.groupby('AGENTEMAILID').count().reset_index()
            chat_count = chat_count[['AGENTEMAILID', 'AGENTASSIGNEDTIME']]
            chat_count.columns = ['AGENTEMAILID', 'chat_count']

            survey_count = survey_count.merge(chat_count, how='left', on='AGENTEMAILID')
            survey_count['no_survey'] = survey_count['chat_count'] - survey_count['p_n_survey_count']
            survey_count = survey_count[
                ['AGENTEMAILID', 'p_n_survey_count', 'positive_survey_count', 'negative_survey_count', 'no_survey']]
            survey_count.fillna(0, inplace=True)

            # convert epoch to readable format
            frt_score['AGENT_FIRST_MESSAGE_TIME'] = pd.to_datetime(frt_score['AGENT_FIRST_MESSAGE_TIME'], unit='s')
            frt_score['AGENTASSIGNEDTIME'] = pd.to_datetime(frt_score['AGENTASSIGNEDTIME'], unit='s')

            # finding only seconds
            frt_score['FRT'] = frt_score['AGENT_FIRST_MESSAGE_TIME'] - frt_score['AGENTASSIGNEDTIME']

            frt_streak_data = frt_score[['AGENTEMAILID', 'FRT']]

            frt_by_agentwise = frt_score
            frt_by_agentwise = frt_by_agentwise[['AGENTEMAILID', 'FRT']]

            frt_by_agentwise['FRT'] = frt_by_agentwise['FRT'].dt.total_seconds()

            frt_by_agentwise = frt_by_agentwise.groupby('AGENTEMAILID').mean().reset_index()

            # print('FRT calculation done')

        finally:
            cs.close()

        first_block_3 = True
    except Exception as err:
        aplhaerr += '#FRT_lvl2 -> ' + str(err) + '<br>'
        first_block_3 = False

    try:
        # preparing for db
        csat_agentwise.fillna(0, inplace=True)
        agent_wise = pd.merge(frt_by_agentwise, csat_agentwise, how='left', on='AGENTEMAILID')
        agent_wise = pd.merge(agent_wise, avg_aht, how='left', on='AGENTEMAILID')
        agent_wise['AGENTEMAILID'] = agent_wise['AGENTEMAILID'].str.lower()


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
        first_block_4 = True
    except Exception as err:
        aplhaerr += '#preparing_for_db -> ' + str(err) + '<br>'
        first_block_4 = False

    try:
        # working on csat streak

        csat_streak_data = csat[['AGENTEMAILID', 'EFFORTSCORE', 'TIME_STAMP']]

        csat_streak_data['EFFORTSCORE'] = csat_streak_data['EFFORTSCORE'].fillna('NaN')

        csat_streak_data = csat_streak_data[~(csat_streak_data['EFFORTSCORE'] == 'NaN')]

        csat_streak_data.sort_values(by=['TIME_STAMP'], ascending=True, inplace=True)

        csat_streak_data = csat_streak_data[['AGENTEMAILID', 'EFFORTSCORE']]


        def cumsum_reset(arr):
            arr = arr.cumsum() - arr.cumsum().where(~arr).ffill().fillna(0).astype(int)

            return arr


        csat_streak = (
            csat_streak_data['EFFORTSCORE'].eq(1)
                .groupby(csat_streak_data['AGENTEMAILID']).apply(cumsum_reset)
                .groupby(csat_streak_data['AGENTEMAILID']).max()
                .reset_index(name='positive_survey_max_streak')
        )

        # frt streak

        frt_streak_data['FRT'] = frt_streak_data['FRT'].fillna('NaN')

        frt_streak_data = frt_streak_data[~(frt_streak_data['FRT'] == 'NaN')]

        frt_streak_data['FRT'] = frt_streak_data['FRT'] / np.timedelta64(1, 's')


        def check(x):
            if x < 15:
                return 1
            else:
                return 0


        frt_streak_data['met'] = frt_streak_data['FRT'].apply(check)


        def cumsum_reset(arr):
            arr = arr.cumsum() - arr.cumsum().where(~arr).ffill().fillna(0).astype(int)

            return arr


        frt_streak = (
            frt_streak_data['met'].eq(1)
                .groupby(frt_streak_data['AGENTEMAILID']).apply(cumsum_reset)
                .groupby(frt_streak_data['AGENTEMAILID']).max()
                .reset_index(name='FRT_max_streak')
        )

        # aht streak

        strk_aht = aht1

        strk_aht.sort_values(by=['ticket_id'], ascending=True, inplace=True)

        strk_aht = strk_aht[['AGENTEMAILID', 'aht_secs']]

        strk_aht['aht_secs'] = strk_aht['aht_secs'].fillna('NaN')

        strk_aht = strk_aht[~(strk_aht['aht_secs'] == 'NaN')]


        def strk(x):
            if x <= 300:
                return 1
            else:
                return 0


        strk_aht['met'] = strk_aht['aht_secs'].apply(strk)


        def cumsum_reset(arr):
            arr = arr.cumsum() - arr.cumsum().where(~arr).ffill().fillna(0).astype(int)

            return arr


        strk_aht_df = (
            strk_aht['met'].eq(1)
                .groupby(strk_aht['AGENTEMAILID']).apply(cumsum_reset)
                .groupby(strk_aht['AGENTEMAILID']).max()
                .reset_index(name='aht_max_streak')
        )

        # joining csat and frt streak

        streak = frt_streak.merge(csat_streak, how='left', on='AGENTEMAILID')
        streak = streak.merge(strk_aht_df, how='left', on='AGENTEMAILID')

        streak['positive_survey_max_streak'] = streak['positive_survey_max_streak'].fillna(0)

        agent_wise = pd.merge(agent_wise, streak, how='left', on='AGENTEMAILID')
        agent_wise['EFFORTSCORE'] = agent_wise['EFFORTSCORE'].fillna(0)
        agent_wise.fillna(0, inplace=True)


        # agent_wise['csat_score'] = agent_wise['EFFORTSCORE'] * 15
        # agent_wise['FRT_score'] = (30-agent_wise['FRT'])/30 *10*100
        # agent_wise['aht_score'] = (300 - agent_wise['aht_secs'])/300 *10*100
        #
        # agent_wise['score'] = agent_wise['csat_score'] + agent_wise['FRT_score'] + agent_wise['aht_score']
        # agent_wise.drop(columns=['FRT_score','csat_score','aht_score'], inplace=True)

        agent_wise = pd.merge(agent_wise, q_frt, how='left', on='AGENTEMAILID')

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

        # total scores
        agent_wise['score'] = agent_wise['csat_score'] + agent_wise['FRT_score'] + agent_wise['aht_score']
        agent_wise.drop(columns=['FRT_score', 'csat_score', 'aht_score'], inplace=True)

        # remove agents name where chats taken are less than 10
        # agent_wise_q_list = agent_wise

        # unique q ids
        q_list = agent_wise['queue'].unique().tolist()
        agent_wise.to_csv('C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\checkthis.csv')

        agent_wise = agent_wise.merge(chat_count, how='left', on='AGENTEMAILID')
        agent_wise.drop_duplicates(subset=['AGENTEMAILID'], keep='first', inplace=True)

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




        agent_wise_output.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\agent_wise.csv")

        # main df list
        # agent_performance_last_run
        agent_wise_output = agent_wise_output.merge(survey_count, how='left', on='AGENTEMAILID')
        live = agent_wise_output[
            ['AGENTEMAILID', 'Partners', 'EFFORTSCORE', 'FRT', 'aht_secs', 'score', 'csat_local_rank',
             'csat_global_rank', 'frt_local_rank', 'frt_global_rank', 'aht_local_rank', 'aht_global_rank',
             'local_ranking', 'global_rank', 'chat_count', 'p_n_survey_count', 'positive_survey_count',
             'negative_survey_count', 'no_survey', 'positive_survey_max_streak', 'FRT_max_streak', 'aht_max_streak',
             'queue']]

        live.fillna(0, inplace=True)
        live.insert(loc=0, column='id', value='')
        live['timestp'] = int(now_timestp)

        convert_dict = {'csat_local_rank': int,
                        'csat_global_rank': int,
                        'frt_local_rank': int,
                        'frt_global_rank': int,
                        'aht_local_rank': int,
                        'aht_global_rank': int,
                        'local_ranking': int,
                        'global_rank': int,
                        }

        live = live.astype(convert_dict)

        live.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\live.csv", index=False)

        agent_wise_output['global_rank'] = agent_wise_output['global_rank'].astype('int64')
        agent_wise_output['local_ranking'] = agent_wise_output['local_ranking'].astype('int64')

        # global rank table
        live_global_leader = agent_wise_output[agent_wise_output['global_rank'] < 2]
        live_global_leader = live_global_leader[
            ['AGENTEMAILID', 'Partners', 'EFFORTSCORE', 'FRT', 'aht_secs', 'score', 'queue']]
        live_global_leader.insert(loc=0, column='id', value='')
        live_global_leader['timestp'] = int(now_timestp)
        live_global_leader.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\live_global_leader.csv", index=False)

        # local rank leader
        live_local_leader = agent_wise_output[agent_wise_output['local_ranking'] < 2]
        live_local_leader = live_local_leader[
            ['AGENTEMAILID', 'Partners', 'EFFORTSCORE', 'FRT', 'aht_secs', 'score', 'queue']]
        live_local_leader.insert(loc=0, column='id', value='')
        live_local_leader['timestp'] = int(now_timestp)
        live_local_leader.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\live_local_leader.csv", index=False)

        # dataframe for thresholds
        data = [['Bau-food', 'aht', '200'], ['Bau-food', 'csat', '63'], ['Bau-food', 'frt', '10'],
                ['L2_stores_genie', 'aht', '660'], ['L2_stores_genie', 'csat', '65'],
                ['Stores', 'aht', '299'], ['Stores', 'csat', '80'],
                ['Priority', 'aht', '260'], ['Priority', 'csat', '90'],
                ['L2_food', 'aht', '540'], ['L2_food', 'csat', '25'],
                ['Genie', 'aht', '299'], ['Genie', 'csat', '78']]

        threshold_df = pd.DataFrame(data, columns=['queue', 'metric', 'threshold'])
        threshold_df.insert(loc=0, column='id', value='')
        threshold_df['timestp'] = int(now_timestp)
        threshold_df.to_csv('C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\threshold.csv', index=False)

        del raw_fetch, surveys, q_surveys, raw_csat, p_survey, n_survey, csat, csat_agentwise, survey_count, aht, aht1, avg_aht, dp_message_created, assign_agent, q_frt, frt, frt_score, chat_count, frt_streak_data, frt_by_agentwise, csat_streak_data, csat_streak, frt_streak, strk_aht, strk_aht_df, streak, agent_wise, less_chat_count, this, this_less, df_list, agent_wise1, less_chat_count1

        first_block_5 = True
    except Exception as err:
        aplhaerr += '#calculation_body -> ' + str(err) + '<br>'
        first_block_5 = False

    try:
        con = pymysql.connect(host='172.16.251.113',
                              user='lakshya_user_151',
                              password='bOw(#!KAw0WwOWlAK$hyAjak',
                              autocommit=True,
                              local_infile=1
                              )

        # print('Connected to DB: {}'.format('172.16.251.113'))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute("DROP TABLE lakshya.live_agent_wise")
        cursor.execute("DROP TABLE lakshya.live_global_leader")
        cursor.execute("DROP TABLE lakshya.live_local_leader")
        cursor.execute(""" CREATE TABLE `lakshya`.`live_agent_wise` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `AGENTEMAILID` text NOT NULL,
                `Partners` varchar(30) NOT NULL,
                `EFFORTSCORE` varchar(20) NOT NULL,
                `FRT` varchar(20) NOT NULL,
                `AHT` varchar(20) NOT NULL,
                `score` varchar(20) NOT NULL,
                `csat_local_rank` varchar(10) NOT NULL,
                `csat_global_rank` varchar(10) NOT NULL,
                `frt_local_rank` varchar(10) NOT NULL,
                `frt_global_rank` varchar(10) NOT NULL,
                `aht_local_rank` varchar(10) NOT NULL,
                `aht_global_rank` varchar(10) NOT NULL,
                `local_ranking` varchar(10) NOT NULL,
                `global_rank` varchar(10) NOT NULL,
                `chat_count` varchar(10) NOT NULL,
                `p_n_survey_count` varchar(10) NOT NULL,
                `positive_survey_count` varchar(10) NOT NULL,
                `negative_survey_count` varchar(10) NOT NULL,
                `no_survey` varchar(10) NOT NULL,
                `positive_survey_max_streak` varchar(10) NOT NULL,
                `FRT_max_streak` varchar(10) NOT NULL,
                `AHT_max_streak` varchar(10) NOT NULL,
                `queue` varchar(50) NOT NULL,
                `timestp` varchar(30) NOT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
            """)
        cursor.execute("""
                CREATE TABLE `lakshya`.`live_global_leader` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `AGENTEMAILID` text NOT NULL,
                  `Center` varchar(30) NOT NULL,
                  `EFFORTSCORE` varchar(20) NOT NULL,
                  `FRT` varchar(20) NOT NULL,
                  `AHT` varchar(20) NOT NULL,
                  `score` varchar(30) NOT NULL,
                  `queue` varchar(50) NOT NULL,
                  `timestp` varchar(30) NOT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
            """)
        cursor.execute("""
                CREATE TABLE `lakshya`.`live_local_leader` (
                  `id` int(11) NOT NULL AUTO_INCREMENT,
                  `AGENTEMAILID` text NOT NULL,
                  `Partners` varchar(30) NOT NULL,
                  `CSATEFFORTSCORE` varchar(20) NOT NULL,
                  `FRT` varchar(20) NOT NULL,
                  `AHT` varchar(20) NOT NULL,
                  `score` varchar(30) NOT NULL,
                  `queue` varchar(50) NOT NULL,
                  `timestp` varchar(30) NOT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
            """)
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live.csv' INTO TABLE lakshya.live_agent_wise FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live.csv' INTO TABLE lakshya.live_agent_wise_dump FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live_global_leader.csv' INTO TABLE lakshya.live_global_leader FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live_global_leader.csv' INTO TABLE lakshya.live_global_leader_dump FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live_local_leader.csv' INTO TABLE lakshya.live_local_leader FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/live_local_leader.csv' INTO TABLE lakshya.live_local_leader_dump FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        cursor.execute(
            "LOAD DATA LOCAL INFILE '/var/lakshya/files/live/threshold.csv' INTO TABLE lakshya.queue_threshold_metrics FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
        # print('Succuessfully loaded the table from csv.')
        cursor.close()
        con.close()

        first_block_6 = True
    except Exception as err:
        aplhaerr += '#upload_csv -> ' + str(err) + '<br>'
        first_block_6 = False

now2 = datetime.now()
dt_string2 = now2.strftime("%d/%m/%Y %H:%M:%S")

if not first_block_1 or not first_block_2 or not first_block_3 or not first_block_4 or not first_block_5 or not first_block_6 or not first_block_1_aht:
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