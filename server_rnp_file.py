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

# CurrentDateTime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# now.strftime('%A') #Day

# Checking Remaining Points for Excution of this Report
try:
    ctrf = 0
    ctrs = 0
    mydb = mysql.connector.connect(host="localhost", user="root", password="Wtf9437153438@@@", database="rnpchatmtd")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM master WHERE skipper = 'YES' AND status = 'FAIL' AND time LIKE '" + now.strftime(
        "%d/%m/%Y") + "%'"
    mycursor.execute(sql)
    myresult1 = mycursor.fetchall()
    if myresult1:
        for x in myresult1:
            ctrf += 1
    sql = "SELECT * FROM master WHERE status = 'SUCCESS' AND time LIKE '" + now.strftime("%d/%m/%Y") + "%'"
    mycursor.execute(sql)
    myresult2 = mycursor.fetchall()
    if myresult2:
        for y in myresult2:
            ctrs += 1
    mycursor.close()
    mydb.close()
    # Terminate if already a success today
    if ctrs > 0:
        exit(print('File already successfuly uploaded today'))
    if (ctrf < 7):
        # Eligible to Execute
        pointsrem = True
        pointsctr = 3 - ctrf
    else:
        pointsrem = False
except Exception as err:
    print('Error Occurred -> ', err)
    pointsrem = False
if not pointsrem:
    print('No Points |', ' Failed: ', ctrf, ' Success: ', ctrs)
    exit()
else:
    print(pointsctr)
    print('Rem')


# Email - Parent Function
def sendmailtostakeholder(mess_from_func, tolist, cclist, subj):
    from_address = "sourav.verma@swiggy.in"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subj
    msg['From'] = from_address
    to = tolist
    cc = cclist
    msg['To'] = ','.join(to)
    msg['Cc'] = ','.join(cc)
    toAddress = to + cc
    # Create the message (HTML).
    html = mess_from_func
    # Record the MIME type - text/html.
    part1 = MIMEText(html, 'html')
    # Attach parts into message container
    msg.attach(part1)
    # Credentials
    username = os.environ['emailid']
    password = os.environ['emailpass']
    # Sending the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, toAddress, msg.as_string())
    server.quit()


def closureTask(skipper, resonForAbrupt, status, dt_string):
    # Updating the Details to Database
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Wtf9437153438@@@",
                                       database="rnpchatmtd")
        mycursor = mydb.cursor()
        sql = "INSERT INTO master (skipper, reasonforabrupt, status, time) VALUES (%s, %s, %s, %s)"
        val = (skipper, resonForAbrupt, status, dt_string)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        mydb.close()
    except mysql.connector.IntegrityError as err:
        print('Integrity Error: ', err)


# ContinuityVariable
proceed = True
filesavail = True

# FirstDayOfMonth Code Block
try:
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
except:
    proceed = False
    try:
        # Calling Mail Function
        subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
        html = '#FirstDayOfMonth code block was unable to execute successfully'
        tousers = ['vd.gokkulkumar@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        closureTask('NO', 'Code Execution Error - FirstDayOfMonth', 'FAIL', dt_string)
    except:
        closureTask('NO', 'Code Execution Error - FirstDayOfMonth', 'FAIL', dt_string)
    finally:
        exit(print('FirstDayOfMonth Issue'))

# Checking Files Availability
if not path.exists("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\skeleton.csv"):
    filesavail = False
    try:
        # Calling Mail Function
        subject = "RnP Report | Skeleton File Not Uploaded | " + str(now.strftime("%d/%m/%Y"))
        html = 'Hi Arul,<br>This email is to gently remind you that the Skeleton file has not been uploaded yet.'
        tousers = ['arul.balaji@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in', 'vd.gokkulkumar@swiggy.in',
                   'setu.aggarwal@swiggy.in', 'wfm-mis@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        skeleton = False
    finally:
        skeleton = False
else:
    skeleton = True

if not path.exists("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\quality.csv"):
    filesavail = False
    try:
        # Calling Mail Function
        subject = "RnP Report | Quality File Not Uploaded | " + str(now.strftime("%d/%m/%Y"))
        html = 'Hi Chaithra,<br><br>This email is to gently remind you that the Quality file has not been uploaded yet.'
        tousers = ['chaithra.m@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in', 'vd.gokkulkumar@swiggy.in',
                   'rahul.athreyas@swiggy.in', 'anupama.stanly']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        quality = False
    finally:
        quality = False
else:
    quality = True

if not path.exists("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\quality_sm_spillage.csv"):
    filesavail = False
    try:
        # Calling Mail Function
        subject = "RnP Report | SM Spillage Quality File Not Uploaded | " + str(now.strftime("%d/%m/%Y"))
        html = 'Hi Chaithra,<br><br>This email is to gently remind you that the SM spillage Quality file has not been uploaded yet.'
        tousers = ['chaithra.m@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in', 'vd.gokkulkumar@swiggy.in',
                   'rahul.athreyas@swiggy.in', 'g.jyothi@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        quality_sm_spillage = False
    finally:
        quality_sm_spillage = False
else:
    quality_sm_spillage = True

if not path.exists("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\sprinklr.csv"):
    filesavail = False
    try:
        # Calling Mail Function
        subject = "RnP Report | Sprinklr File Not Uploaded | " + str(now.strftime("%d/%m/%Y"))
        html = 'Hi Arul,<br>This email is to gently remind you that the Sprinklr file has not been uploaded yet.'
        tousers = ['arul.balaji@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in', 'vd.gokkulkumar@swiggy.in',
                   'setu.aggarwal@swiggy.in', 'wfm-mis@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        sprinklr = False
    finally:
        sprinklr = False
else:
    sprinklr = True

if not filesavail:
    print('Files Unavailable')
    files = ''
    files += ' Sekeleton,' if not skeleton else ''
    files += ' Quality,' if not quality else ''
    files += ' Sprinklr,' if not sprinklr else ''
    files += ' quality_sm_spillage,' if not quality_sm_spillage else ''
    files = files[:-1]
    try:
        closureTask('YES', 'File Not Uploaded - ' + files, 'FAIL', dt_string)
    except:
        print('Failed to Upload into DB')
    proceed = False
    exit()
else:
    print('Files Available')

if proceed:
    aplhaerr = ''
    # Alpha Block - AHT, CSAT & FTR
    try:
        # OverallConnectionCode
        with open("C:/Users/sourav.verma/Desktop/RNP-CHAT/assets/rsa_key.p8", "rb") as key:
            p_key = serialization.load_pem_private_key(
                key.read(),
                password='bOw(#!KAw0WwOW'.encode(),
                backend=default_backend()
            )
        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
        first_block_1 = True
    except Exception as err:
        aplhaerr += '#OverallConnectionCode -> ' + str(err) + '<br>'
        first_block_1 = False
    try:
        # InternalConnectionCode
        ctx = snowflake.connector.connect(
            user='cc_user@swiggy.in',
            account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
            private_key=pkb,
            role='CC_AUTOMATION',
        )
        cs = ctx.cursor()
        first_block_2 = True
    except Exception as err:
        aplhaerr += '#InternalConnectionCode -> ' + str(err) + '<br>'
        first_block_2 = False

    # AHT, CSAT & FTR - STARTS HERE
    acferr = ''
    try:
        # AHTFTRCSATDataFetchError
        raw_fetch = cs.execute(
            "with CHAT as ( Select *,case when agent_email like '%_ag@%' then 'Aegis' when agent_email like '%_kt@%' then 'Kochar' when agent_email like '%_cb@%' then 'CBSL' when agent_email like '%_tm@%' then 'TM' when agent_email like '%_rm@%' then 'RM' when agent_email like '%_ison@%' then 'ISON' when agent_email like '%_hrh@%' then 'HRH' when agent_email like '%_fu@%' then 'Fusion' else 'In-House' end as Center from facts.public.customer_interaction_fact where agent_email <>'Bot' and to_date(AGENT_ASSIGNMENT_TIME) between '{}' and current_date-1 and queueid not in('l2-team-14','l2-team-1','l2-team-2','l2-team-10','team-2','all-stores','all-go','daily-fallback', 'cafe-queue','bengali','hindi','telugu','malayalam','kannada','marathi','stores-others','stores-payment-coupons', 'stores-post-delivery','stores-cancellation','stores-wimo','genie-del-instructions','genie-post-delivery', 'stores-modify-order','stores-d-i-instructions','genie-others','genie-cancellation','genie-wimo','genie-payments-coupons','team-go') group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39, 40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, 61,62,63,64,65, 66,67,68,69,70, 71,72,73,74,75), cc as( Select *, row_number() over (partition by agent_email order by AGENT_ASSIGNMENT_TIME Asc) as RN from Chat), BB as(Select * from CC), final as( Select a.agent_email,a.RN, count (case when a.RN<b.RN and a.conversation_closed_time>=b.AGENT_ASSIGNMENT_TIME then b.conversationid end) cun from cc a left join bb b on a.agent_email=b.agent_email group by 1,2), cun as( Select a.*, row_number() over (partition by entityid,NODELABEL,to_date(AGENT_ASSIGNMENT_TIME) order by AGENT_ASSIGNMENT_TIME Desc ) as RNK, case when b.cun+1>4 then 4 else b.cun+1 end Cuncurrency from cc a left join final b on a.agent_email=b.agent_email and a.RN=b.RN) select to_date(AGENT_ASSIGNMENT_TIME) date, a.Center, count(conversationid) as interactions, count( case when effortscore in (1) then conversationid end) as promotors, count( case when effortscore in (1,0) then conversationid end) as all_csat, Sum(case when (datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time))>=0 then datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time) end) AHT, count(case when RNK>1 and entityid>1  then TICKET_ID end ) as ftnr, count(case when entityid>1 then TICKET_ID end)  as total_orders, sum(Cuncurrency) Cuncurrency from cun a group by 1,2".format(
                first_day_of_month))

        df = pd.DataFrame(raw_fetch)
        cs.close()
        first_block_3 = True
    except Exception as err:
        aplhaerr += '#AHTFTRCSATDataFetchError -> ' + str(err) + '<br>'
        first_block_3 = False
    try:
        # DataManipulationAHTCSATFRT
        df.columns = ['DATE', 'CENTER', 'INTERACTIONS', 'PROMOTORS', 'ALL_CSAT', 'AHT', 'FTNR', 'TOTAL_ORDERS',
                      'CUNCURRENCY']
        df.drop(columns=['DATE'], inplace=True)
        data = df.groupby('CENTER').sum().reset_index()
        # AHT
        data['OVERALL AHT'] = data['AHT'] / data['CUNCURRENCY']
        # CSAT
        data['CSAT'] = (data['PROMOTORS'] / data['ALL_CSAT']) * 100
        # FTR
        data['FTR'] = ((data['TOTAL_ORDERS'] - data['FTNR']) / data['TOTAL_ORDERS']) * 100
        data.drop(columns=['INTERACTIONS', 'CUNCURRENCY', 'AHT', 'PROMOTORS', 'ALL_CSAT', 'FTNR', 'TOTAL_ORDERS'],
                  inplace=True)
        first_block_4 = True
    except Exception as err:
        aplhaerr += '#DataManipulationAHTCSATFRT -> ' + str(err) + '<br>'
        first_block_4 = False
    try:
        # RANKINGS_AHT_CSAT_FTR
        data['AHT_RANK'] = data['OVERALL AHT'].rank(ascending=True, method='dense')
        data['CSAT_RANK'] = data['CSAT'].rank(ascending=False, method='dense')
        data['FTR_RANK'] = data['FTR'].rank(ascending=False, method='dense')
        data = data[['CENTER', 'OVERALL AHT', 'AHT_RANK', 'CSAT', 'CSAT_RANK', 'FTR', 'FTR_RANK']]
        data = data.rename(columns={"OVERALL AHT": "AHT"})
        first_block_5 = True
    except Exception as err:
        aplhaerr += '##RANKINGS_AHT_CSAT_FTR -> ' + str(err) + '<br>'
        first_block_5 = False
    # Checking Success Condition for Alpha Block
    if not first_block_1 or not first_block_2 or not first_block_3 or not first_block_4 or not first_block_5:
        proceed = False
        try:
            # Calling Mail Function
            subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
            html = 'Aplha[AHT,CSAT & FRT] block(s) were unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>' + aplhaerr
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            alpha_block = False
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + aplhaerr, 'FAIL', dt_string)
        except Exception as err:
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + aplhaerr, 'FAIL', dt_string)
        finally:
            alpha_block = False
        exit(print('Code Terminated - Alpha'))

# AHT, CSAT & FTR - ENDS HERE


# # <------------------------------------------------------------------------------------------------------------------>


# Skeleton Adherence - BEGINS HERE
if proceed:
    skelerr = ''
    # SkeletonAdherenceBlock_1
    try:
        skeleton = pd.read_csv("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\skeleton.csv",
                               encoding='iso-8859-1')
        skeleton['Date'] = skeleton['Date'].astype('int64')
        ed = pd.read_csv("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\ED.csv")
        list_em = list(ed['Email'])
        # skeleton['Date'] = pd.to_datetime(skeleton['Date']).dt.strftime('%y-%m-%d')
        # skeleton.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnp\\skeleton.csv")
        # sa = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnp\\sa.csv")
        current_date = date.today().isoformat()
        current_date_of_month = current_date + " 06:59:59"
        x = datetime.now()
        if x.day == 1:
            given_date = datetime.today().date()
            first_day_of_month = given_date.replace(day=1)
            first_day_of_month = given_date.replace(month=x.month - 1)
            first_day_of_month = first_day_of_month.isoformat()
            first_day_of_month = first_day_of_month + " 07:00:00"
        else:
            given_date = datetime.today().date()
            first_day_of_month = given_date.replace(day=1)
            first_day_of_month = first_day_of_month.isoformat()
            first_day_of_month = first_day_of_month + " 07:00:00"

        sql = "select DT,hour(BUCKET),sum(AVAILABLE_MINUTES),case when AGENTEMAIL like '%_ag@%' then 'Aegis' when AGENTEMAIL like '%_kt@%' then 'Kochar' when AGENTEMAIL like '%_cb@%' then 'CBSL' when AGENTEMAIL like '%_rm@%' then 'RM' when AGENTEMAIL like '%_tm@%' then 'TM' when AGENTEMAIL like '%_hrh@%' then 'HRH' when AGENTEMAIL like '%_ison@%' then 'ISON' else 'In-House' end as Center from ANALYTICS.CC_CX.CHAT_AGENTS_PRODUCTIVITY where AGENTEMAIL not in ('{}') and BUCKET between ('{}') and ('{}') group by 1,2,4".format(
            "','".join([str(i) for i in list_em]), first_day_of_month, current_date_of_month)

        with open("C:/Users/sourav.verma/Desktop/RNP-CHAT/assets/rsa_key.p8", "rb") as key:
            p_key = serialization.load_pem_private_key(
                key.read(),
                password='bOw(#!KAw0WwOW'.encode(),
                backend=default_backend()
            )

        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
        skeleton_block_1 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_1 -> ' + str(err) + '<br>'
        skeleton_block_1 = False
    try:
        # SkeletonAdherenceBlock_2
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
        skeleton_block_2 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_2 -> ' + str(err) + '<br>'
        skeleton_block_2 = False
    try:
        # SkeletonAdherenceBlock_3
        raw_fetch = cs.execute(sql)
        sa = pd.DataFrame(raw_fetch)
        skeleton_block_3 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_3 -> ' + str(err) + '<br>'
        skeleton_block_3 = False
    finally:
        cs.close()
    try:
        # SkeletonAdherenceBlock_4
        # Data Manipulation
        sa.columns = ['DT', 'HOUR(BUCKET)', 'SUM(AVAILABLE_MINUTES)', 'CENTER']
        sa['SUM(AVAILABLE_MINUTES)'] = sa['SUM(AVAILABLE_MINUTES)'].astype('int64')
        sa['DT'] = pd.to_datetime(sa['DT']).dt.strftime('%d')
        sa['DT'] = sa['DT'].astype('int64')
        sa.sort_values(by=['DT', 'HOUR(BUCKET)'], ascending=True, inplace=True)
        sa['HOUR(BUCKET)'] = sa['HOUR(BUCKET)']
        sa['FTE'] = sa['SUM(AVAILABLE_MINUTES)'] / 60
        df = pd.merge(sa, skeleton, how='left', left_on=['DT', 'HOUR(BUCKET)', 'CENTER'],
                      right_on=['Date', 'Int', 'Site'])
        df.drop(columns=['Date', 'Int', 'Site'], inplace=True)
        df['FTE'] = df['FTE'].astype('int64')


        def deficit(df):
            if df['FTE'] >= df['Skeleton']:
                return 0
            else:
                return 1


        # Manipulation & Ranking
        df['deficit'] = df.apply(deficit, axis=1)
        deficit = df[['CENTER', 'deficit']]
        deficit = deficit.groupby('CENTER').mean() * 100
        deficit = deficit.reset_index()
        deficit['SCHEDULE_ADHERENCE'] = 100 - deficit['deficit']
        deficit.drop(columns=['deficit'], inplace=True)
        deficit['SCHEDULE_ADHERENCE_RANK'] = deficit['SCHEDULE_ADHERENCE'].rank(ascending=False, method='dense').astype(
            'int64')
        data = pd.merge(data, deficit, how='left', on='CENTER')
        skeleton_block_4 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_4 -> ' + str(err) + '<br>'
        skeleton_block_4 = False
    if not skeleton_block_1 or not skeleton_block_2 or not skeleton_block_3 or not skeleton_block_4:
        proceed = False
        try:
            # Calling Mail Function
            subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
            html = 'Skeleton Adherence block(s) were unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>' + skelerr
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            sm_spillage_block = False
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + skelerr, 'FAIL', dt_string)
        except Exception as err:
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + skelerr, 'FAIL', dt_string)
        finally:
            sm_spillage_block = False
        exit(print('Code Terminated - SA'))

# Skeleton Adherence - ENDS HERE


# <------------------------------------------------------------------------------------------------------------------>


# SM Spillage- STARTS HERE
if proceed:
    smerr = ''
    try:
        # SmSpillageBlock_1
        sprinklr = pd.read_csv("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\sprinklr.csv", engine='python')
        sprinklr['Order ID (Case)'] = sprinklr['Order ID (Case)'].astype('str')
        sprinklr['Order ID (Case)'] = sprinklr['Order ID (Case)'].replace('nan', np.nan)
        sprinklr.dropna(subset=['Order ID (Case)'], inplace=True)
        sprinklr['Order ID (Case)'] = sprinklr['Order ID (Case)'].str.replace(r'.0$', '')
        sprinklr = sprinklr[sprinklr['Order ID (Case)'].apply(lambda x: str(x).isdigit())]
        sprinklr = sprinklr[~(sprinklr['Order ID (Case)'].isnull())]
        sprinklr = sprinklr[~(sprinklr['Order ID (Case)'] == 0.0)]
        sprinklr.drop_duplicates(subset=['Order ID (Case)'], keep='first', inplace=True)
        # error.....it was in float, so converted to int, not it is in string and it shows error if i try to convert
        sprinklr['Order ID (Case)'] = sprinklr['Order ID (Case)'].astype('int64')
        list_orderid = list(sprinklr['Order ID (Case)'])
        # Sprinklr Data Fetch
        # sql = "with cte as( select distinct ORDER_ID, NODELABEL, L2_DISPOSITION, DT ,Agent_email as Last_agent ,Agent_assignment_time ,Last_message_time ,ticket_id ,(AHT_IN_SECS/86400) as AHT ,case when agent_email like '%_cb@%' then 'CBSL_Hyd' when agent_email like '%_kt@%' then 'Kochar' when agent_email like '%_ag@%' then 'Aegis_Kol' when agent_email like '%_tm@%' then 'Tech Mahindra' when agent_email like '%_rm@%' then 'RM_GGN' when agent_email like '%_ison@%' then 'ISON' when agent_email like 'Bot' then 'Bot' when queueid in( 'l2-team-14','l2-team-1','l2-team-2','l2-team-10') then 'ED-InHouse' else 'In-House' end as outsource_name ,Row_number() Over (Partition by order_id Order by last_message_time Desc) RN from facts.public.customer_interaction_fact where AGENT_Email <> 'Bot' and agent_id>0 and agent_id is not null and queueid <> 'all-stores' and queueid <> 'all-go' and queueid <> 'daily-fallback' and queueid <> 'cafe-queue' and queueid <> 'bengali' and queueid <> 'hindi' and queueid <> 'telugu' and queueid <> 'malayalam' and queueid <> 'kannada' and month(dt) = Month(current_date-1) and year(dt) = year(current_date -1) and dt <> current_date and Last_message_time is not null and order_id in ({}) ) Select * from cte order by dt desc".format(",".join([str(i) for i in list_orderid]))
        with open("C:/Users/sourav.verma/Desktop/RNP-CHAT/assets/rsa_key.p8", "rb") as key:
            p_key = serialization.load_pem_private_key(
                key.read(),
                password='bOw(#!KAw0WwOW'.encode(),
                backend=default_backend()
            )
        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
        sm_spillage_block_1 = True
    except Exception as err:
        smerr += '#SmSpillageBlock_1 -> ' + str(err) + '<br>'
        sm_spillage_block_1 = False

    try:
        # SmSpillageBlock_2
        ctx = snowflake.connector.connect(
            user='cc_user@swiggy.in',
            account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
            private_key=pkb,
            role='CC_AUTOMATION',
        )
        cs = ctx.cursor()
        sm_spillage_block_2 = True
    except Exception as err:
        smerr += '#SmSpillageBlock_2 -> ' + str(err) + '<br>'
        sm_spillage_block_2 = False

    try:
        # SmSpillageBlock_3
        raw_fetch = cs.execute(
            "with pred as( select order_id, max(PREDICTION) as PREDICTION from streams.public.fraud_segment_dp_event where month(dt) = month(current_date - 1) and year(dt) = year(current_date - 1) and dt <> current_date group by 1 ) select to_date(agent_assignment_time), case when agent_email like '%_cb@%' then 'CBSL' when agent_email like '%_kt@%' then 'Kochar' when agent_email like '%_ag@%' then 'Aegis' when agent_email like '%_tm@%' then 'Tech Mahindra' when agent_email like '%_rm@%' then 'RM' when agent_email like '%_ison@%' then 'ISON' when agent_email like 'Bot' then 'Bot' when queueid in( 'l2-team-14','l2-team-1','l2-team-2','l2-team-10') then 'ED-InHouse' else 'In-House' end as outsource_name, prediction, count(distinct ticket_id) from facts.public.customer_interaction_fact cif left join pred on pred.order_id = cif.order_id where month(agent_assignment_time) >= month(current_date - 1) and year(agent_assignment_time) >= year(current_date - 1) and agent_assignment_time <> current_date and agent_email<>'Bot' and agent_id>0 and agent_id is not null and queueid <> 'all-stores' and queueid <> 'all-go' and queueid <> 'daily-fallback' and queueid <> 'cafe-queue' and queueid <> 'bengali' and queueid <> 'hindi' and queueid <> 'telugu' and queueid <> 'malayalam' and queueid <> 'kannada' group by 1,2,3 order by 1,2;")
        center_wise = pd.DataFrame(raw_fetch)
        center_wise.columns = ['TO_DATE(AGENT_ASSIGNMENT_TIME)', 'OUTSOURCE_NAME', 'PREDICTION',
                               'COUNT(DISTINCT TICKET_ID)']
        center_wise.to_csv("C:\\Users\\sourav.verma\\Desktop\\RNP-CHAT\\assets\\center_wise_sm_spillage.csv")
        sm_spillage_block_3 = True
    except Exception as err:
        smerr += '#SmSpillageBlock_3 -> ' + str(err) + '<br>'
        sm_spillage_block_3 = False
    finally:
        cs.close()

    try:

        # sprinklr = pd.merge(sprinklr, chat_q[['ORDER_ID','OUTSOURCE_NAME']], how='left', left_on='Order ID (Case)', right_on='ORDER_ID' )
        q_sm = pd.read_csv("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\quality_sm_spillage.csv",
                           engine='python')
        q_sm.to_csv("C:\\Users\\sourav.verma\\Desktop\\RNP-CHAT\\assets\\quality_sm_spillage.csv")
        q_sm = q_sm[['LOB Responsible', 'Partner name ']]
        q_sm['LOB Responsible'] = q_sm['LOB Responsible'].str.lower()
        q_sm = q_sm[(q_sm['LOB Responsible'] == 'chat') | (q_sm['LOB Responsible'] == 'ed chat')]
        q_sm_gp = q_sm.groupby('Partner name ').count()
        q_sm_gp = q_sm_gp.reset_index()


        def renaming_q_sm_gp(x):
            if "Startek" in x:
                return "Aegis"
            elif "Tech M" in x:
                return "TM"
            elif "Inhouse" in x:
                return "In-House"
            elif "Kochar" in x:
                return "Kochar"
            elif "ISON" in x:
                return "ISON"
            elif "CBSL" in x:
                return "CBSL"


        q_sm_gp['Partner name '] = q_sm_gp['Partner name '].apply(renaming_q_sm_gp)

        q_sm_gp.columns = ['OUTSOURCE_NAME', 'LOB Responsible']


        # sprinklr = sprinklr[['OUTSOURCE_NAME']]
        # sprinklr['ESCALATION'] = 1
        # sprinklr = sprinklr.groupby('OUTSOURCE_NAME').count()
        # sprinklr = sprinklr.reset_index()

        def renaming(x):
            if "Aegis_Kol" in x:
                return "Aegis"
            elif "Aegis" in x:
                return x
            elif "CBSL_Hyd" in x:
                return "CBSL"
            elif "CBSL" in x:
                return x
            elif "ISON" in x:
                return "ISON"
            elif "Kochar" in x:
                return "Kochar"
            elif "Tech Mahindra" in x:
                return "TM"
            else:
                return "In-House"


        # sprinklr['OUTSOURCE_NAME'] = sprinklr['OUTSOURCE_NAME'].apply(renaming)

        # sprinklr = sprinklr.groupby("OUTSOURCE_NAME").sum().reset_index()

        center_wise = center_wise[['OUTSOURCE_NAME', 'COUNT(DISTINCT TICKET_ID)']]

        center_wise = center_wise.groupby('OUTSOURCE_NAME').sum().reset_index()

        center_wise['OUTSOURCE_NAME'] = center_wise['OUTSOURCE_NAME'].apply(renaming)
        center_wise = center_wise.groupby('OUTSOURCE_NAME').sum().reset_index()

        center_wise = pd.merge(center_wise, q_sm_gp, how='left', on='OUTSOURCE_NAME')

        center_wise['Quality_SM'] = (center_wise['LOB Responsible'] / center_wise['COUNT(DISTINCT TICKET_ID)']) * 100

        center_wise.drop(columns=['COUNT(DISTINCT TICKET_ID)'], inplace=True)
        center_wise.fillna(0, inplace=True)
        center_wise['Quality_SM_Rank'] = center_wise['Quality_SM'].rank(ascending=False, method='dense')

        data = pd.merge(data, center_wise, how='left', left_on='CENTER', right_on='OUTSOURCE_NAME')
        data.drop(columns=['OUTSOURCE_NAME'], inplace=True)
        sm_spillage_block_6 = True
    except Exception as err:
        smerr += '#SmSpillageBlock_6 -> ' + str(err) + '<br>'
        sm_spillage_block_6 = False
    if not sm_spillage_block_1 or not sm_spillage_block_2 or not sm_spillage_block_3 or not sm_spillage_block_6:
        proceed = False
        try:
            # Calling Mail Function
            subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
            html = 'SM Spillage block(s) were unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>' + smerr
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            sm_spillage_block = False
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + smerr, 'FAIL', dt_string)
        except Exception as err:
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + smerr, 'FAIL', dt_string)
        finally:
            sm_spillage_block = False
        exit(print('Code Terminated'))

# SM Spillage - ENDS HERE


# <------------------------------------------------------------------------------------------------------------------>


# Quality - STARTS HERE
if proceed:
    qlerr = ''
    try:
        # QualityBlock_1
        quality = pd.read_csv("C:\\Apache24\\htdocs\\rnp.source.upload\\dumpupload\\quality.csv")
        quality.columns = quality.columns[0:7]
        quality.columns = ['Agent ID', 'Agent email ID', 'Chat Id', 'Audit score', 'Type of Call', 'CENTER', 'Date']
        quality = quality[['Audit score', 'CENTER']]
        quality['CENTER'] = quality['CENTER'].str.lower()


        def check(x):
            if x <= 1:
                return x
            else:
                return x / 100


        quality['Audit score'] = quality['Audit score'].apply(check)
        # quality['Audit score'] = quality['Audit score'].map(lambda x : x.rstrip('%') )

        # quality['Audit score'] = quality['Audit score'].astype('int64')
        quality['Audit score'] = quality['Audit score'] * 100
        quality_block_1 = True
    except Exception as err:
        qlerr += '#QualityBlock_1 -> ' + str(err) + '<br>'
        quality_block_1 = False

    try:
        # QualityBlock_2
        def check(x):
            if "cbsl" in x:
                return "CBSL"
            elif "house" in x:
                return "In-House"
            elif "ison" in x:
                return "ISON"
            elif "kochar" in x:
                return "Kochar"
            elif "star" in x:
                return "Aegis"
            elif "aegis" in x:
                return "Aegis"
            elif "techm" in x:
                return "TM"
            elif "tm" in x:
                return "TM"


        quality['CENTER'] = quality['CENTER'].apply(check)
        quality = quality.groupby('CENTER').mean().reset_index()
        # quality['Audit score'] = round(quality['Audit score'],2)
        data = pd.merge(data, quality, how='left', on='CENTER')
        med = data['Audit score'].median()
        data['Audit score'] = data['Audit score'].fillna('Y')
        quality_block_2 = True
    except Exception as err:
        qlerr += '#QualityBlock_2 -> ' + str(err) + '<br>'
        quality_block_2 = False

    try:
        # QualityBlock_3
        def fil(data):
            if data['Audit score'] == 'Y':
                return "Yes"
            else:
                return "No"


        data['quality_exception'] = data.apply(fil, axis=1)
        data['Audit score'] = data['Audit score'].replace(to_replace='Y', value=med)
        data['Audit score rank'] = data['Audit score'].rank(ascending=False, method='dense')
        quality_block_3 = True
    except Exception as err:
        qlerr += '#QualityBlock_2 -> ' + str(err) + '<br>'
        quality_block_3 = False
    if not quality_block_1 or not quality_block_2 or not quality_block_3:
        proceed = False
        try:
            # Calling Mail Function
            subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
            html = 'Quality block(s) were unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>' + qlerr
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            sm_spillage_block = False
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + qlerr, 'FAIL', dt_string)
        except Exception as err:
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + qlerr, 'FAIL', dt_string)
        finally:
            quality_block = False
        exit(print('Code Terminated'))

# Quality - ENDS HERE


# <------------------------------------------------------------------------------------------------------------------>


# Overall Ranking + Anynymous - SRARTS HERE

if proceed:
    rankerr = ''
    try:
        # quality weightage based on rank
        # QualityWeightageBlock
        def a_w(data):
            if data['Audit score'] >= 83:
                if data['Audit score rank'] == 1:
                    return 110 * 20
                elif data['Audit score rank'] == 2:
                    return 105 * 20
                elif data['Audit score rank'] == 3:
                    return 110 * 20
                elif data['Audit score rank'] == 4:
                    return 95 * 20
                else:
                    return 90 * 20

            elif data['Audit score'] >= 80 and data['Audit score'] < 83:
                return 20 * 89
            elif data['Audit score'] >= 75 and data['Audit score'] < 80:
                return 20 * 88
            elif data['Audit score'] >= 70 and data['Audit score'] < 75:
                return 20 * 87
            elif data['Audit score'] >= 65 and data['Audit score'] < 70:
                return 20 * 86
            else:
                return 20 * 85


        data['audit_w'] = data.apply(a_w, axis=1)

        data['audit_w'] = data['audit_w'] / 100
        rank_block_1 = True
    except Exception as err:
        rankerr += '#QualityWeightageBlock -> ' + str(err) + '<br>'
        rank_block_1 = False

    try:
        # SM is based on rank
        # SMWeightageBlock
        def sm(x):
            if x == 1:
                return 90 * 10
            elif x == 2:
                return 95 * 10
            elif x == 3:
                return 100 * 10
            elif x == 4:
                return 105 * 10
            else:
                return 110 * 10


        data['sm_w_c'] = data['Quality_SM_Rank'].apply(sm)

        data['sm_w_c'] = (data['sm_w_c'] / 100)
        rank_block_2 = True
    except Exception as err:
        rankerr += '#SMWeightageBlock -> ' + str(err) + '<br>'
        rank_block_2 = False

    try:
        # CSAT based on rank
        # CsatWeightageBlock
        def csat_w(x):
            if x > 4:
                return 90 * 15
            elif x == 4:
                return 95 * 15
            elif x == 3:
                return 100 * 15
            elif x == 2:
                return 105 * 15
            elif x == 1:
                return 110 * 15


        data['csat_w'] = data['CSAT_RANK'].apply(csat_w)
        data['csat_w'] = (data['csat_w'] / 100)
        rank_block_3 = True
    except Exception as err:
        rankerr += '#CsatWeightageBlock -> ' + str(err) + '<br>'
        rank_block_3 = False

    try:
        # ftr based on score
        # FTRWeightageBlock
        def f_w(x):
            if x < 87:
                return 90 * 15
            elif x > 87.01 and x < 89.01:
                return 95 * 15
            elif x > 89.01 and x < 91:
                return 100 * 15
            elif x > 91.01 and x < 93:
                return 105 * 15
            elif x > 93:
                return 110 * 15


        data['ftr_w'] = data['FTR'].apply(f_w)
        data['ftr_w'] = (data['ftr_w'] / 100)
        # data['schedule_w'] = (13/100) * data['SCHEDULE_ADHERENCE']
        rank_block_4 = True
    except Exception as err:
        rankerr += '#FTRWeightageBlock -> ' + str(err) + '<br>'
        rank_block_4 = False

    try:
        # skeleton based on rank
        # SkeletonWeightageBlock
        def sk_w(x):
            if x < 92:
                return 90 * 12.50
            elif x >= 92.01 and x <= 94:
                return 95 * 12.50
            elif x >= 94.01 and x <= 95:
                return 100 * 12.50
            elif x >= 95.01 and x <= 97:
                return 102 * 12.50
            else:
                return 110 * 12.50


        data['schedule_w'] = data['SCHEDULE_ADHERENCE'].apply(sk_w)

        data['schedule_w'] = (data['schedule_w'] / 100)
        data['schedule_w'] = (data['schedule_w'] / 100)
        rank_block_5 = True
    except Exception as err:
        rankerr += '#SkeletonWeightageBlock -> ' + str(err) + '<br>'
        rank_block_5 = False

    try:
        # AHTWeightageBlock
        # AHT based on score
        def aht(x):
            if x > 540:
                return 90 * 20
            elif x > 511 and x < 540:
                return 95 * 20
            elif x > 480 and x < 510:
                return 100 * 20
            elif x > 440 and x < 479:
                return 105 * 20
            elif x < 440:
                return 110 * 20


        data['aht_w_c'] = data['AHT'].apply(aht)

        data['aht_w_c'] = (data['aht_w_c'] / 100)
        data['aht_w_c'] = (data['aht_w_c'] / 100)
        rank_block_6 = True
    except Exception as err:
        rankerr += '#AHTWeightageBlock -> ' + str(err) + '<br>'
        rank_block_6 = False

    try:
        # OverallRankFinalBlock
        data['all_w'] = data['csat_w'] + data['ftr_w'] + data['schedule_w'] + data['audit_w'] + data['aht_w_c'] + data[
            'sm_w_c']

        data['Overall_Rank'] = data['all_w'].rank(ascending=False, method='dense')

        data.drop(columns=['csat_w', 'ftr_w', 'schedule_w', 'audit_w', 'aht_w_c', 'sm_w_c', 'all_w'], inplace=True)

        data = data[
            ['CENTER', 'Overall_Rank', 'AHT', 'AHT_RANK', 'CSAT', 'CSAT_RANK', 'FTR', 'FTR_RANK', 'SCHEDULE_ADHERENCE',
             'SCHEDULE_ADHERENCE_RANK', 'Quality_SM', 'Quality_SM_Rank', 'Audit score', 'Audit score rank',
             'quality_exception']]
        data['AHT'] = round(data['AHT'], 2)
        data['CSAT'] = round(data['CSAT'], 2)
        data['FTR'] = round(data['FTR'], 2)
        data['SCHEDULE_ADHERENCE'] = round(data['SCHEDULE_ADHERENCE'], 2)
        data['Audit score'] = round(data['Audit score'], 2)
        data = data.sample(frac=1)
        data['Quality_SM_Rank'] = data['Quality_SM'].rank(ascending=True, method='dense')
        data['Quality_SM'] = round(data['Quality_SM'], 2)
        data['CENTER'] = data['CENTER'].replace('Aegis', 'Startek')
        data['Overall_Rank'] = data['Overall_Rank'].astype(int)
        data['AHT_RANK'] = data['AHT_RANK'].astype(int)
        data['CSAT_RANK'] = data['CSAT_RANK'].astype(int)
        data['FTR_RANK'] = data['FTR_RANK'].astype(int)
        data['Quality_SM_Rank'] = data['Quality_SM_Rank'].astype(int)
        data['Audit score rank'] = data['Audit score rank'].astype(int)
        data['automated_date'] = now.strftime("%d/%m/%Y")

        rank_block_7 = True
    except Exception as err:
        rankerr += '#OverallRankFinalBlock -> ' + str(err) + '<br>'
        rank_block_7 = False
    if not rank_block_1 or not rank_block_2 or not rank_block_3 or not rank_block_4 or not rank_block_5 or not rank_block_6 or not rank_block_7:
        proceed = False
        try:
            # Calling Mail Function
            subject = "RnP Report | Code Execution Error | " + str(now.strftime("%d/%m/%Y"))
            html = 'Overall Ranking Block(s) were unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>' + rankerr
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            sm_spillage_block = False
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + rankerr, 'FAIL', dt_string)
        except Exception as err:
            # Pushing to DB
            closureTask('NO', 'Code Execution Error - ' + rankerr, 'FAIL', dt_string)
        finally:
            overallrank_block = False
        exit(print('Code Terminated'))

# <------------------------------------------------------------------------------------------------------------------->

# Uploading the file into Databse - Resolute
uploadfailed = False
stopcode = False
if proceed:
    try:
        import sqlalchemy

        database_username = os.environ['usernameforrnpres']
        database_password = os.environ['passforres']
        database_ip = os.environ['ipforres']
        database_name = os.environ['rnrdb']
        database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                       format(database_username, database_password,
                                                              database_ip, database_name), pool_recycle=1,
                                                       pool_timeout=57600).connect()

        data.to_sql(con=database_connection, name='rnp_dashboard', if_exists='append', chunksize=1000, index=False)
    except Exception as err:
        uploadfailed = True
        err = str(err)
        if str(err).find('Duplicate entry') > -1 and err.find('center_autodate_unique') > -1:
            print('Duplicate')
        else:
            stopcode = True;
            try:
                # Calling Mail Function
                subject = "RnP Report | Data Upload Error | " + str(now.strftime("%d/%m/%Y"))
                html = 'The was some issue while uploading the data into DB <br><br>' + err
                tousers = ['vd.gokkulkumar@swiggy.in']
                ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
                sendmailtostakeholder(html, tousers, ccusers, subject)
            except:
                print('Failed to send mail for Error Reporting')
            try:
                closureTask('NO', 'Unable to Upload the file into Database ' + err, 'Failed', dt_string)
            except:
                print('Failed to upload into DB')
    finally:
        database_connection.close()

# Checking upload status and deciding to continue or exit the code
if uploadfailed and stopcode:
    exit(print('Code Terminated - Unable to upload the data'))
else:
    try:
        closureTask('YES', 'NA', 'SUCCESS', dt_string)
    except:
        print('Failed to upload success status')

# Creating Backup for Dump
try:
    os.makedirs('D://RNP_REPORT_MTD//' + str(now.strftime("%d_%m_%Y")), exist_ok=True)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    # Moving Processed data
    data.to_csv("D:/RNP_REPORT_MTD/" + str(now.strftime("%d_%m_%Y")) + "/final.csv", index=False)

    # Moving Quality file
    source = 'C:/Apache24/htdocs/rnp.source.upload/dumpupload/quality.csv'
    destination = 'D:/RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/quality.csv'
    dest = shutil.move(source, destination)

    # Moving SM Quality file
    source = 'C:/Apache24/htdocs/rnp.source.upload/dumpupload/quality_sm_spillage.csv'
    destination = 'D:/RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/quality_sm_spillage.csv'
    dest = shutil.move(source, destination)

    # Moving Sprinklr File
    source = 'C:/Apache24/htdocs/rnp.source.upload/dumpupload/sprinklr.csv'
    destination = 'D:/RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/sprinklr.csv'
    dest = shutil.move(source, destination)

    # Copying Skeleton File
    source = 'C:/Apache24/htdocs/rnp.source.upload/dumpupload/skeleton.csv'
    destination = 'D:/RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/skeleton.csv'
    dest = shutil.copy(source, destination)
except:
    print('Dump backup Failed')

if path.exists("C:\\Users\\sourav.verma\\Desktop\\RNP-CHAT\\assets\\final.csv"):
    # Overall Ranking - ENDS HERE
    if proceed:
        try:
            # Calling Mail Function
            subject = "RnP Report | Success | " + str(now.strftime("%d/%m/%Y"))
            html = "Report has been successfully Uploaded!"
            tousers = ['vd.gokkulkumar@swiggy.in']
            ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
            sendmailtostakeholder(html, tousers, ccusers, subject)
            print('Success - Mail')
        except:
            print('Failed to send mail for Success!')

        exit(print('Success!'))
else:
    print('Unable to save file')
