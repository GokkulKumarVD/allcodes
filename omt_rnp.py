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

if not filesavail:
    print('Files Unavailable')
    files = ''
    files += ' Sekeleton,' if not skeleton else ''
    files += ' Quality,' if not quality else ''
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
            first_block_1 = True
        except Exception as err:
            aplhaerr += '#OverallConnectionCode -> ' + str(err) + '<br>'
            first_block_1 = False

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
            first_block_2 = True
        except Exception as err:
            aplhaerr += '#InternalConnectionCode -> ' + str(err) + '<br>'
            first_block_2 = False

        # AHT, CSAT & FTR - STARTS HERE
        acferr = ''
        try:
            raw_fetch = cs.execute("""With CHAT as( Select *,case when AGENT_EMAIL like '%_g7cr@%' then 'G7' when AGENT_EMAIL like '%_kt@%' then 'Kochar' when AGENT_EMAIL like '%_fs@%' then 'Five Splash' when AGENT_EMAIL like '%_gr@%' then 'Grass Roots' when AGENT_EMAIL like '%_hrh@%' then 'HRH' when AGENT_EMAIL like '%_fu@%' then 'fusion' when AGENT_EMAIL like '%_rm@%' then 'Radical minds' else 'In-House' end as outsource_name,
                                        case when hour(AGENT_ASSIGNMENT_TIME) in (5,6,7,8,9,10,11)    then 'Break Fast' when hour(AGENT_ASSIGNMENT_TIME) in(12,13,14)     then 'Lunch' when hour(AGENT_ASSIGNMENT_TIME) in (15,16,17,18)    then 'Snacks' when hour(AGENT_ASSIGNMENT_TIME) in(19,20,21,22)  then 'Dinner' when hour(AGENT_ASSIGNMENT_TIME) in(23,0,1,2,3,4) then 'Late Night' else 'Non Peak Hours'  end as Chat_Peak
                                        from ANALYTICS.CC_CX_VIEWS.DE_FACT_TEMP where  to_date(AGENT_ASSIGNMENT_TIME) between '{}' and current_date-1 and  chattype = 'Agent' and ticket_id is not null group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39, 40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, 61,62,63,64,65, 66),
                                        cc as( Select *, row_number() over (partition by agent_email order by AGENT_ASSIGNMENT_TIME Asc) as RN from Chat), BB as(Select * from CC), final as( Select a.agent_email,a.RN,count (case when a.RN<b.RN and a.conversation_closed_time>=b.AGENT_ASSIGNMENT_TIME then b.conversationid end) cun from cc a left join bb b on a.agent_email=b.agent_email group by 1,2), final2 as( Select a.*, row_number() over (partition by to_date(AGENT_ASSIGNMENT_TIME),CLIENTORDERID,NODELABEL order by AGENT_ASSIGNMENT_TIME Desc ) as RNK, case when b.cun+1>4 then 4 else b.cun+1 end Cuncurrency from cc a left join final b on a.agent_email=b.agent_email and a.RN=b.RN) select to_date(AGENT_ASSIGNMENT_TIME) date, outsource_name, count(conversationid) as interactions, count( case when effortscore in (1) then conversationid end) as promotors, count( case when effortscore in (1,0) then conversationid end) as all_csat, Sum(case when (datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time))>=0 then datediff('second',AGENT_ASSIGNMENT_TIME,conversation_closed_time) end) AHT, count(case when RNK>1 and CLIENTORDERID>1  then TICKET_ID end ) FTNR_COUNT, sum(Cuncurrency) Concurrency from final2 group by 1,2""".format(first_day_of_month))

            alpha = pd.DataFrame(raw_fetch)
            cs.close()
            first_block_3 = True
        except Exception as err:
            aplhaerr += '#AHTFTRCSATDataFetchError -> ' + str(err) + '<br>'
            first_block_3 = False
        try:
            alpha.columns = ['DATE', 'OUTSOURCE_NAME', 'INTERACTIONS', 'PROMOTORS', 'ALL_CSAT', 'AHT', 'FTNR_COUNT', 'CONCURRENCY']
            alpha.drop(columns=['DATE'],inplace=True)

            alpha = alpha.groupby('OUTSOURCE_NAME').sum().reset_index()


            alpha['AHT_T'] = alpha['AHT']/alpha['INTERACTIONS']
            alpha['Con AHT'] = alpha['AHT_T']/ (alpha['CONCURRENCY']/alpha['INTERACTIONS'])
            alpha['DE Experience'] = alpha['PROMOTORS']/alpha['ALL_CSAT']
            alpha['FTR'] = 1-(alpha['FTNR_COUNT']/alpha['INTERACTIONS'])
            alpha['FTNR'] = 1-alpha['FTR']

            alpha = alpha[['OUTSOURCE_NAME', 'Con AHT', 'DE Experience', 'FTR']]

            first_block_4 = True
        except Exception as err:
            aplhaerr += '#DataManipulationAHTCSATFRT -> ' + str(err) + '<br>'
            first_block_4 = False

        # Checking Success Condition for Alpha Block
        if not first_block_1 or not first_block_2 or not first_block_3 or not first_block_4:
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


# quality block
# Quality - STARTS HERE
if proceed:
    qlerr = ''
    try:
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
        quality_block_1 = True
    except Exception as err:
        qlerr += '#QualityBlock_1 -> ' + str(err) + '<br>'
        quality_block_1 = False

    try:
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
        quality_block_2 = True
    except Exception as err:
        qlerr += '#QualityBlock_2 -> ' + str(err) + '<br>'
        quality_block_2 = False
    try:
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

# skeleton adherence block
if proceed:
    skelerr = ''
    # SkeletonAdherenceBlock_1
    try:
        skeleton = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\omt_rnp\\skeleton.csv")

        current_date = date.today().isoformat()
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
            elif "dr" in x:
                return "dr itm"

        skeleton['Site'] = skeleton['Site'].apply(sk_rename)

        sql = "Select dt,hour(BUCKET), sum(AVAILABLE_MINUTES), case when AGENTEMAIL like '%_g7cr@%' then 'G7' when AGENTEMAIL like '%_dit@%' then 'dr itm' when AGENTEMAIL like '%_kt@%' then 'Kochar' when AGENTEMAIL like '%_fs@%' then 'Five Splash' when AGENTEMAIL like '%_gr@%' then 'Grass Roots' when AGENTEMAIL like '%_hrh@%' then 'HRH' when AGENTEMAIL like '%_fu@%' then 'fusion' else 'In-House' end as outsource_name from analytics.cc_cx.deassistance_agents_productivity where bucket between ('{}') and ('{}') group by 1,2,4".format(first_day_of_month,current_date_of_month )

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
        skeleton_block_1 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_1 -> ' + str(err) + '<br>'
        skeleton_block_1 = False
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
        skeleton_block_2 = True
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_2 -> ' + str(err) + '<br>'
        skeleton_block_2 = False

    try:
        raw_fetch = cs.execute(sql)
        # print('fetched')
        sa = pd.DataFrame(raw_fetch)
        skeleton_block_3 = True
        # sa.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnp\\analytics_skeleton_snowflakes.csv")
    except Exception as err:
        skelerr += '#SkeletonAdherenceBlock_3 -> ' + str(err) + '<br>'
        skeleton_block_3 = False
    finally:
        cs.close()
    try:
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

# Overall Ranking + Anynymous - SRARTS HERE

if proceed:
    rankerr = ''
    try:
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
        rank_block_1 = True
    except Exception as err:
        rankerr += '#AHTWeightageBlock -> ' + str(err) + '<br>'
        rank_block_1 = False

    try:
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
        rank_block_2 = True
    except Exception as err:
        rankerr += '#DEexpWeightageBlock -> ' + str(err) + '<br>'
        rank_block_2 = False

    try:
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
        rank_block_3 = True
    except Exception as err:
        rankerr += '#ftrWeightageBlock -> ' + str(err) + '<br>'
        rank_block_3 = False
    try:
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
        rank_block_4 = True
    except Exception as err:
        rankerr += '#auditWeightageBlock -> ' + str(err) + '<br>'
        rank_block_4 = False

    try:
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
        rank_block_5 = True
    except Exception as err:
        rankerr += '#schedule_adherence_WeightageBlock -> ' + str(err) + '<br>'
        rank_block_5 = False

    try:
        alpha['total_w'] = alpha['a_w'] + alpha['de_w'] + alpha['ftr_w'] + alpha['audit_w'] + alpha['sa_w']
        alpha['Overall_rank'] = alpha['total_w'].rank(ascending= False, method='dense')

        alpha['DE Experience'] = round(alpha['DE Experience'],2)
        alpha['FTR'] = round(alpha['FTR'],2)
        alpha['SCHEDULE_ADHERENCE'] = round(alpha['SCHEDULE_ADHERENCE'],2)

        alpha = alpha[['CENTER','Overall_rank','Con AHT','AHT_RANK','DE Experience','DE Experience_RANK','FTR','FTR_RANK','SCHEDULE_ADHERENCE','SCHEDULE_ADHERENCE_RANK','Audit Score','Audit score rank','quality_exception']]
        rank_block_6 = True
    except Exception as err:
        rankerr += '#schedule_adherence_WeightageBlock -> ' + str(err) + '<br>'
        rank_block_6 = False

    if not rank_block_1 or not rank_block_2 or not rank_block_3 or not rank_block_4 or not rank_block_5 or not rank_block_6:
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
    alpha.to_csv("D:/OMT_RNP_REPORT_MTD/" + str(now.strftime("%d_%m_%Y")) + "/final.csv", index=False)

    # Moving Quality file
    source = 'C:/Apache24/htdocs/omt_rnp.source.upload/dumpupload/quality.csv'
    destination = 'D:/OMT_RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/quality.csv'
    dest = shutil.move(source, destination)

    # Copying Skeleton File
    source = 'C:/Apache24/htdocs/omt_rnp.source.upload/dumpupload/skeleton.csv'
    destination = 'D:/OMT_RNP_REPORT_MTD/' + str(now.strftime("%d_%m_%Y")) + '/skeleton.csv'
    dest = shutil.copy(source, destination)
except:
    print('Dump backup Failed')

if path.exists("C:\\Users\\sourav.verma\\Desktop\\OMT_RNP-CHAT\\assets\\final.csv"):
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
