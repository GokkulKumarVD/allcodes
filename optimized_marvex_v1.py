#!/usr/bin/env python3
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd
import snowflake.connector
import datetime
import numpy as np
import mysql.connector
import os.path
from os import path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

user = getpass.getuser()


# ContinuityVariable
proceed = True
filesavail = True

first_block_1 = True
first_block_2 = True
first_block_3 = True
first_block_4 = True
first_block_5 = True
first_block_6 = True
first_block_7 = True
first_block_8 = True
first_block_9 = True
first_block_10 = True
first_block_11 = True
first_block_12 = True
first_block_13 = True

# Email - Parent Function
def sendmailtostakeholder(mess_from_func, tolist, cclist, subj):
    from_address = "cc.automation@swiggy.in"
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
    username = 'cc.automation@swiggy.in'
    password = 'xcdbqpvdmzvckhwh'
    # Sending the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, toAddress, msg.as_string())
    server.quit()





print(datetime.datetime.now())
#  fetching data from marvex database
# importing required librarie(s)

# # Establishing conection
# try:
#    mydb = mysql.connector.connect(
#        host=os.getenv('mxhost'),
#        user=os.getenv('mxuser'),
#        passwd=os.getenv('mxpass'),
#        database=os.getenv('mxdb')
#    )
# except:
#    print('Unable to establish connection with MX-DB')
#
# # Setting connection cursor and fetching the data
# try:
#    mycursor = mydb.cursor()
#    if (mycursor):
#        mycursor.execute("select issueid from ticketinfo union select issueid from freshtickets")
#        myresult = mycursor.fetchall()
#        igcc_old_check = pd.DataFrame(myresult)
#        igcc_old_check.columns = ['issueid']
#        print(igcc_old_check)
#        igcc_old_check_list = igcc_old_check['issueid'].to_list()
# except:
#    print('Unable to fetch the data')


# # ending here


if proceed:
    aplhaerr = ''
    try:
    # WARESHOUSE CONNECTOR KEY
        with open("C:/Users/"+user+"/Desktop/projects/marvex/marvex_rsa_key.p8", "rb") as key:
           p_key = serialization.load_pem_private_key(
               key.read(),
               password=None,
               backend=default_backend()
           )

        pkb = p_key.private_bytes(
           encoding=serialization.Encoding.DER,
           format=serialization.PrivateFormat.PKCS8,
           encryption_algorithm=serialization.NoEncryption())

        ctx = snowflake.connector.connect(
           user='igcc_restaurant_recovery@swiggy.dev',
           account='swiggy.ap-southeast-1',
           private_key=pkb,
           role='igcc_restaurant_recovery',
           warehouse='NONTECH_WH_01'
        )
        cs = ctx.cursor()
        first_block_1 = True

    except Exception as err:
        aplhaerr += '#InternalConnectionCode -> ' + str(err) + '<br>'
        first_block_1 = False
    acferr = ''
    try:
       raw_fetch = cs.execute("""WITH raw_data AS
                                               (
                                                 SELECT r.dt AS resolutiongivendate,
                                                     r.issueid,
                                                     r.orderid AS base_order_id,
                                                     rr.agreed AS recovery_status,
                                                     rr.agreedat AS recovery_date,
                                                     rr.foodissueid AS id,
                                                     i.issuedescl1 AS issue,
                                                     i.issuedescl2 AS issue2,
                                                     r.resolutionid,
                                                     r.agentid AS agent_email,
                                                     r.approvedby AS approved_by_email,
                                                     a.VALUE::BOOLEAN AS is_resolved,
                                                     b.VALUE::bigint AS resolution_id,
                                                     c.VALUE::FLOAT AS resolutions_amount,
                                                     d.VALUE::VARCHAR AS resolutions_given,
                                                     e.VALUE::VARCHAR AS resolution_codes,
                                                     r.recommendationid,
                                                     items_quantity_impacted
                                                 FROM secure_views.igcc_restaurant_recovery.food_issue_resolution r
                                                 LEFT JOIN lateral flatten(input => isresolved ) a
                                                 LEFT JOIN lateral flatten(input => resolutionid) b
                                                   ON a.INDEX = b.INDEX
                                                 LEFT JOIN lateral flatten(input => resolutionsamount) c
                                                   ON a.INDEX = c.INDEX
                                                 LEFT JOIN lateral flatten(input => resolutionsgiven) d
                                                   ON a.INDEX = d.INDEX
                                                 LEFT JOIN lateral flatten(input => resolutioncodes) e
                                                   ON a.INDEX = e.INDEX
                                                 LEFT JOIN
                                                           (
                                                              SELECT i.foodissueid, issuedescl2,issuedescl1,
                                                                   sum(q.value::NUMBER) AS items_quantity_impacted
                                                              FROM secure_views.igcc_restaurant_recovery.food_issue i
                                                              CROSS JOIN lateral flatten(input => itemqtyimpacted, OUTER => TRUE) AS q
                                                              WHERE i.dt >= cast(dateadd('DAY',-7, to_date('2021-01-11')) AS VARCHAR)
                                                              GROUP BY 1,2,3
                                                           ) AS i
                                                   ON r.issueid = i.foodissueid
                                                 LEFT JOIN secure_views.igcc_restaurant_recovery.food_issue_restaurant_recovery rr
                                                   ON r.issueid=rr.foodissueid
                                                       AND rr.dt >= cast(dateadd('DAY',-7, to_date('2021-01-11')) AS VARCHAR)
                                                 WHERE r.dt = '2021-01-11'
                                               )
                                               , base_order_ordered_quantity AS
                                               (
                                                  SELECT order_id AS base_order_id,
                                                  sum(NUM_ITEMS) AS ordered_quantity
                                                  FROM secure_views.igcc_restaurant_recovery.dp_place_order dpo
                                                  INNER JOIN (
                                                                SELECT DISTINCT base_order_id
                                                                FROM raw_data
                                                                GROUP BY 1
                                                             ) b
                                                     ON try_cast(dpo.order_id AS BIGINT) = b.base_order_id
                                                  WHERE dpo.dt >= cast(dateadd('DAY',-30, to_date('2021-01-11')) AS VARCHAR)
                                                  GROUP BY 1
                                               )
                                               , base_order_details AS
                                               (
                                                 SELECT DISTINCT dpo.order_id AS base_order_id,
                                                                 dt AS base_order_date,
                                                                 order_total AS base_order_cust_payable,
                                                                 restaurant_id,
                                                                 r.NAME AS rest_name,
                                                                 area.name AS area_name,
                                                                 del.name AS delivery_partner,
                                                                 r.phone_numbers AS rest_phone_number,
                                                                 dpo.order_type,
                                                                 ordered_quantity
                                                 FROM secure_views.igcc_restaurant_recovery.dp_place_order dpo
                                                 LEFT JOIN secure_views.igcc_restaurant_recovery.partner_order_mapping pom
                                                     ON try_cast(dpo.order_id AS BIGINT) = try_cast(pom.order_id as BIGINT)
                                                 LEFT JOIN secure_views.igcc_restaurant_recovery.delivery_partners del
                                                     ON del.partner_id = pom.partner_id
                                                 INNER JOIN (
                                                              SELECT DISTINCT base_order_id
                                                              FROM raw_data
                                                              GROUP BY 1
                                                            ) b
                                                     ON try_cast(dpo.order_id AS BIGINT) = try_cast(b.base_order_id as BIGINT)
                                                 LEFT JOIN secure_views.igcc_restaurant_recovery.restaurants r
                                                     ON dpo.restaurant_id = r.id
                                                 LEFT JOIN secure_views.igcc_restaurant_recovery.area area
                                                     ON r.area_code = area.id
                                                 LEFT JOIN base_order_ordered_quantity q
                                                     ON try_cast(dpo.order_id AS BIGINT) = try_cast(q.base_order_id as BIGINT)
                                                 WHERE dpo.dt >= cast(dateadd('DAY',-30, to_date('2021-01-11')) AS VARCHAR)
                                                 GROUP BY 1,2,3,4,5,6,7,8,9,10
                                               )
                                               , rep_order_details AS
                                               (
                                                  SELECT orderid AS replicated_order_id,
                                                     max(CASE WHEN status='delivered' THEN 'Completed'
                                                              WHEN rnk = 1 THEN status
                                                         end) AS replicated_order_post_delivery_status
                                                  FROM (
                                                          SELECT dt, orderid, status, time_stamp, ROW_NUMBER() OVER (PARTITION BY orderid ORDER BY time_stamp DESC) rnk
                                                          FROM secure_views.igcc_restaurant_recovery.dp_update_de_order_status_event
                                                          WHERE dt >= cast(dateadd('DAY',-7, to_date('2021-01-11')) AS VARCHAR)
                                                        ) oft
                                                  INNER JOIN (
                                                                SELECT try_cast(lower(trim(resolution_codes)) AS NUMBER) AS rep_order_id
                                                                FROM raw_data
                                                                WHERE resolutions_given = 'REPLICATE_ORDER' and try_cast(resolution_codes AS NUMBER) <> -1
                                                                GROUP BY 1
                                                             ) re
                                                     ON cast(oft.orderid as varchar) = cast(re.rep_order_id as varchar)
                                                  WHERE oft.dt >= cast(dateadd('DAY',-7, to_date('2021-01-11')) AS VARCHAR)
                                                  GROUP BY 1
                                               )

                                               SELECT issueid, resolutiongivendate, r.base_order_id, base_order_date, base_order_cust_payable,
                                                   restaurant_id, rest_name,  rest_phone_number,
                                                   replicated_order_id, replicated_order_post_delivery_status,
                                                   issue, issue2, is_resolved,
                                                   resolution_id, resolutions_amount, resolutions_given, resolution_codes, agent_email, approved_by_email, 
                                                   CASE WHEN r.recommendationid='-1' THEN 'Not followed' ELSE 'Followed' end AS isrecommendationfollowed,
                                                   ordered_quantity, items_quantity_impacted
                                               FROM raw_data r
                                               LEFT JOIN base_order_details base
                                                   ON try_cast(r.base_order_id as bigint) = try_cast(base.base_order_id as bigint)
                                               LEFT JOIN rep_order_details rep
                                                   ON try_cast(r.resolution_codes AS BIGINT) = rep.replicated_order_id
                                               LEFT JOIN (SELECT order_id, post_status FROM secure_views.igcc_restaurant_recovery.dp_order_fact) o
                                                   ON o.order_id = rep.replicated_order_id ;""")

       food_issue_resolution = pd.DataFrame(raw_fetch)

       food_issue_resolution.columns = ['ISSUEID', 'RESOLUTIONGIVENDATE', 'BASE_ORDER_ID', 'BASE_ORDER_DATE',
                                        'ORDER_TOTAL', 'RESTAURANT_ID', 'REST_NAME', 'REST_PHONE_NUMBER',
                                        'REPLICATED_ORDER_ID', 'REPLICATED_ORDER_POST_DELIVERY_STATUS', 'ISSUE',
                                        'ISSUE2', 'IS_RESOLVED', 'RESOLUTION_ID', 'RESOLUTIONS_AMOUNT',
                                        'RESOLUTIONS_GIVEN', 'RESOLUTION_CODES', 'AGENT_EMAIL', 'APPROVED_BY_EMAIL',
                                        'ISRECOMMENDATIONFOLLOWED', 'ORDERED_QUANTITY', 'ITEMSIMPACTED']
       print(food_issue_resolution)

       print("fetching resto id and city id seperately and merging with main data")
       raw_fetch = cs.execute(
               "Select restaurant_id, city_id from secure_views.igcc_restaurant_recovery.dp_order_fact where DT between current_date-3 and current_date;")
       dp_order_fact1 = pd.DataFrame(raw_fetch)
       dp_order_fact1.columns = ['RESTAURANT_ID','CITY_CODE']

       raw_fetch = cs.execute(
           "Select distinct(restaurant_id) from secure_views.igcc_restaurant_recovery.dp_order_fact;")
       dp_order_fact2 = pd.DataFrame(raw_fetch)
       dp_order_fact2.columns = ['RESTAURANT_ID']

       dp_order_fact = dp_order_fact2.merge(dp_order_fact1, how='left', on = 'RESTAURANT_ID')

       dp_order_fact = dp_order_fact[~ (dp_order_fact['RESTAURANT_ID'].isna())]
       dp_order_fact = dp_order_fact[~ (dp_order_fact['CITY_CODE'].isna())]

       dp_order_fact['RESTAURANT_ID'] = dp_order_fact['RESTAURANT_ID'].astype('int64')
       dp_order_fact['RESTAURANT_ID'] = dp_order_fact['RESTAURANT_ID'].astype('str')
       dp_order_fact['CITY_CODE'] = dp_order_fact['CITY_CODE'].astype('int64')

       food_issue_resolution = food_issue_resolution.merge(dp_order_fact, how='left', on='RESTAURANT_ID')

       raw_fetch = cs.execute("""Select * from secure_views.igcc_restaurant_recovery.city;""")
       city = pd.DataFrame(raw_fetch)
       city.columns = ['CITY_CODE', 'REST_CITY_NAME']

       food_issue_resolution = food_issue_resolution.merge(city, how='left', on='CITY_CODE')
       food_issue_resolution.drop_duplicates(subset=['RESOLUTION_ID'], inplace=True)

       cs.close()
       first_block_2 = True
    except Exception as err:
        aplhaerr += '#fetching_main_files_error -> ' + str(err) + '<br>'
        first_block_2 = False




    try:
        # finding empty city names and filling it with another query
        temp_food_issue_resolution = food_issue_resolution[food_issue_resolution['REST_CITY_NAME'].isnull()]
        food_issue_resolution_city_names_blank = temp_food_issue_resolution['BASE_ORDER_ID'].to_list()

        if food_issue_resolution_city_names_blank.__len__() > 1:
            with open("C:/Users/" + user + "/Desktop/projects/marvex/marvex_rsa_key.p8", "rb") as key:
                p_key = serialization.load_pem_private_key(
                    key.read(),
                    password=None,
                    backend=default_backend()
                )

            pkb = p_key.private_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption())

            ctx = snowflake.connector.connect(
                user='igcc_restaurant_recovery@swiggy.dev',
                account='swiggy.ap-southeast-1',
                private_key=pkb,
                role='igcc_restaurant_recovery',
                warehouse='NONTECH_WH_01'
            )
            cs = ctx.cursor()

            print(datetime.datetime.now())
            raw_fetch = cs.execute(
                "select f.order_id, f.restaurant_id AS RESTAURANT_ID, sr.name AS REST_NAME, sc.name AS REST_CITY_NAME from secure_views.igcc_restaurant_recovery.dp_order_fact f join secure_views.igcc_restaurant_recovery.city sc on f.city_id=sc.id join secure_views.igcc_restaurant_recovery.restaurants sr on sr.id=f.restaurant_id where f.order_id in ({})".format(",".join([str(x) for x in food_issue_resolution_city_names_blank])))
            food_issue_resolution_city_names_blank = pd.DataFrame(raw_fetch)
            food_issue_resolution_city_names_blank.columns = ['ORDER_ID','RESTAURANT_ID','REST_NAME','REST_CITY_NAME']

            city_dict = food_issue_resolution_city_names_blank.set_index('ORDER_ID')['REST_CITY_NAME'].to_dict()
            food_issue_resolution['REST_CITY_NAME'] = food_issue_resolution['REST_CITY_NAME'].fillna(food_issue_resolution['BASE_ORDER_ID'].map(city_dict))

            cs.close()



        # removing false from isresolved (it's in boolean)
        food_issue_resolution = food_issue_resolution[(food_issue_resolution['IS_RESOLVED'] == 1)]

        # renaming df
        igcc = food_issue_resolution



        # taking data where issue is null
        igcc_issue_blank = igcc[igcc['ISSUE'].isnull()]
        list_id = list(igcc_issue_blank['BASE_ORDER_ID'])
        first_block_3 = True
    except Exception as err:
        aplhaerr += '#Main_file_merging_error -> ' + str(err) + '<br>'
        first_block_3 = False

    if(list_id.__len__() > 1):
       try:
           with open("C:/Users/"+user+"/Desktop/projects/marvex/marvex_rsa_key.p8", "rb") as key:
               p_key = serialization.load_pem_private_key(
                   key.read(),
                   password=None,
                   backend=default_backend()
               )

           pkb = p_key.private_bytes(
               encoding=serialization.Encoding.DER,
               format=serialization.PrivateFormat.PKCS8,
               encryption_algorithm=serialization.NoEncryption())

           ctx = snowflake.connector.connect(
               user='igcc_restaurant_recovery@swiggy.dev',
               account='swiggy.ap-southeast-1',
               private_key=pkb,
               role='igcc_restaurant_recovery',
               warehouse='NONTECH_WH_01'
           )
           cs = ctx.cursor()
           first_block_4 = True
       except Exception as err:
           aplhaerr += '#InternalConnectionCode -> ' + str(err) + '<br>'
           first_block_4 = False

       try:
           print('food issue & it fetches fast')
           print(datetime.datetime.now())
           raw_fetch = cs.execute("""Select ORDERID,FOODISSUEID, ISSUEDESCL1 from secure_views.igcc_restaurant_recovery.food_issue where orderid in ({})""".format(",".join([str(i) for i in list_id])))
           igcc_issue_blank = pd.DataFrame(raw_fetch)
           # igcc_issue_blank.to_csv("C:\\Users\\"+user+""\\Desktop\\projects\\marvex\\igcc_issue_blank.csv")
           # renaming igcc_issue_blank columns
           igcc_issue_blank.columns = ["orderid", "foodissueid", "issuedescl1"]

           # created dictionary and mapping with primary data
           dicts = igcc_issue_blank.set_index("foodissueid")['issuedescl1'].to_dict()
           igcc['ISSUE'] = igcc['ISSUE'].fillna(igcc['ISSUEID'].map(dicts))

           print(igcc_issue_blank)
           print("success")
           print(datetime.datetime.now())
           first_block_5 = True
       except Exception as err:
           aplhaerr += '# -> ' + str(err) + '<br>'
           first_block_5 = False





    # converting to lower case
    igcc['REST_NAME'] = igcc['REST_NAME'].astype('str')
    igcc['REST_NAME'] = igcc['REST_NAME'].apply(lambda x: x.lower())
    igcc['RESOLUTIONS_GIVEN'] = igcc['RESOLUTIONS_GIVEN'].str.lower()
    igcc['IS_RESOLVED'] = igcc['IS_RESOLVED'].astype(str)
    igcc['IS_RESOLVED'] = igcc['IS_RESOLVED'].str.lower()
    igcc['ISSUE'] = igcc['ISSUE'].str.lower()
    igcc['REST_PHONE_NUMBER'] = igcc['REST_PHONE_NUMBER'].astype(str)
    igcc['Status'] = ""


    # taking blank base order date and fetching details
    igcc['BASE_ORDER_DATE'] = igcc['BASE_ORDER_DATE'].fillna("NONE")
    igcc['BASE_ORDER_DATE'] = igcc['BASE_ORDER_DATE'].replace("NONE",np.nan)
    blank_dates = igcc[igcc['BASE_ORDER_DATE'].isnull()]
    list_id = list(blank_dates['BASE_ORDER_ID'])

    if(list_id.__len__() > 1):
       try:
           with open("C:/Users/"+user+"/Desktop/projects/marvex/marvex_rsa_key.p8", "rb") as key:
               p_key = serialization.load_pem_private_key(
                   key.read(),
                   password=None,
                   backend=default_backend()
               )

           pkb = p_key.private_bytes(
               encoding=serialization.Encoding.DER,
               format=serialization.PrivateFormat.PKCS8,
               encryption_algorithm=serialization.NoEncryption())

           ctx = snowflake.connector.connect(
               user='igcc_restaurant_recovery@swiggy.dev',
               account='swiggy.ap-southeast-1',
               private_key=pkb,
               role='igcc_restaurant_recovery',
               warehouse='NONTECH_WH_01'
           )
           cs = ctx.cursor()
           first_block_6 = True
       except Exception as err:
           aplhaerr += '#InternalConnectionCode -> ' + str(err) + '<br>'
           first_block_6 = False

       try:
           print('dp order fact next round')
           print(datetime.datetime.now())
           raw_fetch = cs.execute("select f.order_id, f.cust_payable,  sr.name,sr.phone_numbers, f.dt,sc.name as rest_city from secure_views.igcc_restaurant_recovery.dp_order_fact f join secure_views.igcc_restaurant_recovery.city sc on f.city_id=sc.id join secure_views.igcc_restaurant_recovery.restaurants sr on sr.id=f.restaurant_id where f.order_id in ({}) and dt IS NOT NULL".format(",".join([str(i) for i in list_id])))
           igcc_date_blank = pd.DataFrame(raw_fetch)
           # igcc_date_blank.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\marvex\\igcc_date_blank.csv")
           igcc_date_blank.columns = ['order_id', 'cust_payable', 'name', 'phone_numbers', 'dt', 'rest_city']

           igcc_date_blank['order_id'] = igcc_date_blank['order_id'].astype('str')
           igcc['BASE_ORDER_DATE'] = (
               igcc['BASE_ORDER_ID'].map(igcc_date_blank.set_index('order_id')['dt']).fillna(igcc['BASE_ORDER_DATE']))
           igcc['ORDER_TOTAL'] = (
               igcc['BASE_ORDER_ID'].map(igcc_date_blank.set_index('order_id')['cust_payable']).fillna(
                   igcc['ORDER_TOTAL']))
           igcc['REST_NAME'] = (
               igcc['BASE_ORDER_ID'].map(igcc_date_blank.set_index('order_id')['name']).fillna(igcc['REST_NAME']))
           igcc['REST_CITY_NAME'] = (
               igcc['BASE_ORDER_ID'].map(igcc_date_blank.set_index('order_id')['rest_city']).fillna(
                   igcc['REST_CITY_NAME']))

           print("end")
           print(datetime.datetime.now())
           first_block_7 = True
       except Exception as err:
           aplhaerr += '#issueblankDataFetchError -> ' + str(err) + '<br>'
           first_block_7 = False





    igcc['ISSUE'] = igcc['ISSUE'].fillna('Check in OMS')

    today = datetime.datetime.now()
    # change it to days = 2 if it is live
    DD = datetime.timedelta(days=2)
    earlier = (today - DD)
    igcc['BASE_ORDER_DATE']= pd.to_datetime(igcc['BASE_ORDER_DATE'])

    # working on replacement order ids
    igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].fillna("NONE")


    def flag_rep(igcc):
       if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order'):
           return igcc['RESOLUTION_CODES']

    igcc['REPLICATED_ORDER_ID'] = igcc.apply(flag_rep, axis = 1)


    igcc['REPLICATED_ORDER_ID'] = igcc['REPLICATED_ORDER_ID'].fillna('Not a replacement order')

    def replicate(igcc):
        if igcc['REPLICATED_ORDER_ID'] == 'Not a replacement order':
            return igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS']
        else:
            return 'NONE'

    igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc.apply(replicate, axis=1)


    def flag_rep(igcc):
       if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == 'NONE'):
           return 'Replacement not given'

    igcc['Status'] = igcc.apply(flag_rep, axis = 1)











    # igcc['REPLICATED_ORDER_ID'] = igcc['RESOLUTION_CODES']


    def flag_rep(igcc):
       if (igcc['RESOLUTION_CODES'] == '-1'):
           return 'Replicate order ID not generated'
       else:
           return igcc['Status']

    igcc['Status'] = igcc.apply(flag_rep, axis = 1)

    igcc_replicate = igcc[(igcc['Status'] == 'Replacement not given')]
    list_id_rep = list(igcc_replicate['REPLICATED_ORDER_ID'])

    # for item in list_id_rep[:]:
    #     if "-" in item:
    #         list_id_rep.remove(item)

    if (list_id_rep.__len__() > 1):
       try:
           with open("C:/Users/"+user+"/Desktop/projects/marvex/marvex_rsa_key.p8", "rb") as key:
               p_key = serialization.load_pem_private_key(
                   key.read(),
                   password=None,
                   backend=default_backend()
               )

           pkb = p_key.private_bytes(
               encoding=serialization.Encoding.DER,
               format=serialization.PrivateFormat.PKCS8,
               encryption_algorithm=serialization.NoEncryption())
           first_block_8 = True
       except Exception as err:
           aplhaerr += '#issueblankDataFetchError -> ' + str(err) + '<br>'
           first_block_8 = False


       try:
           ctx = snowflake.connector.connect(
               user='igcc_restaurant_recovery@swiggy.dev',
               account='swiggy.ap-southeast-1',
               private_key=pkb,
               role='igcc_restaurant_recovery',
               warehouse='NONTECH_WH_01'
           )
           cs = ctx.cursor()
           first_block_9 = True
       except Exception as err:
           aplhaerr += '#replicate order data error -> ' + str(err) + '<br>'
           first_block_9 = False

       try:
           print('dp_update_de_order_status')
           print(datetime.datetime.now())
           raw_fetch = cs.execute("select ORDERID, STATUS from secure_views.igcc_restaurant_recovery.dp_update_de_order_status_event where orderid in ({}) and status = 'delivered'".format(",".join([str(i) for i in list_id_rep])))
           igcc_rep = pd.DataFrame(raw_fetch)
           igcc_rep.to_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\igcc_rep.csv")


           print("end")
           print(datetime.datetime.now())
           first_block_10 = True
       except Exception as err:
           aplhaerr += '#replicate order data error -> ' + str(err) + '<br>'
           first_block_10 = False

       igcc_rep.columns = ['order_id', 'post_status']


       igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].replace("NONE",np.nan)

       igcc_rep['order_id'] = igcc_rep['order_id'].astype(str)

       # igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = (
       #     igcc['REPLICATED_ORDER_ID'].map(igcc_rep.set_index('order_id')['post_status'])
       #     .fillna(igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS']))

       dicts = igcc_rep.set_index("order_id")['post_status'].to_dict()
       igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].fillna(igcc['REPLICATED_ORDER_ID'].map(dicts))

    # now fetching phone numbers
    try:
        with open("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\marvex_rsa_key.p8", "rb") as key:
           p_key = serialization.load_pem_private_key(
               key.read(),
               password=None,
               backend=default_backend()
           )

        pkb = p_key.private_bytes(
           encoding=serialization.Encoding.DER,
           format=serialization.PrivateFormat.PKCS8,
           encryption_algorithm=serialization.NoEncryption())
        first_block_11 = True
    except Exception as err:
        aplhaerr += '#phone number data error -> ' + str(err) + '<br>'
        first_block_11 = False

    try:
       ctx = snowflake.connector.connect(
           user='igcc_restaurant_recovery@swiggy.dev',
           account='swiggy.ap-southeast-1',
           private_key=pkb,
           role='igcc_restaurant_recovery',
           warehouse='NONTECH_WH_01'
       )
       cs = ctx.cursor()
       first_block_12 = True
    except Exception as err:
       aplhaerr += '#phone number data error -> ' + str(err) + '<br>'
       first_block_12 = False

    try:
       raw_fetch = cs.execute("select id as RESTAURANT_ID, phone_numbers from secure_views.igcc_restaurant_recovery.restaurants")
       phn1 = pd.DataFrame(raw_fetch)
       phn1.columns = ['RESTAURANT_ID', 'phone_numbers']
       phn1.to_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\phone_numbers.TSV", sep='\t')

       phn = pd.read_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\phone_numbers.TSV", sep='\t', thousands=',')
       try:
           phn['phone_numbers'] = phn['phone_numbers'].str.split(',')
           phn = phn.explode('phone_numbers')
           phn = phn.loc[:, ~phn.columns.str.contains('Unnamed: 0')]
       except:
           phn = phn.loc[:, ~phn.columns.str.contains('Unnamed: 0')]
       print('Phone success')
       first_block_13 = True
    except Exception as err:
       aplhaerr += '#phone number data error -> ' + str(err) + '<br>'
       first_block_13 = False

    phn1['RESTAURANT_ID'] = phn1['RESTAURANT_ID'].astype('str')
    igcc = igcc.merge(phn1, how="left", on='RESTAURANT_ID')

    igcc['phone_numbers'] = igcc['phone_numbers'].astype('str')

    # enable this code once we get phone number in the query itself
    # def ph_ck(x):
    #     if len(x) < 1:
    #         return 'no_number'
    #     else:
    #         return x
    #
    # igcc['phone_numbers'] = igcc['phone_numbers'].apply(ph_ck)

    # disable this code once after getting phone numbers in query
    igcc['phone_numbers'] = 'nan'

    igcc['phone_numbers'] = igcc['phone_numbers'].replace('nan',np.nan)
    igcc['phone_numbers'] = igcc['phone_numbers'].replace('no_number',np.nan)


    # filling blank phone numbers
    no_resto_number = pd.read_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\No_Resto_Number.csv")
    no_resto_number.columns = ['RESTAURANT_ID','NAME','CITY_NAME','email','phone_numbers']
    no_resto_number = no_resto_number[['RESTAURANT_ID','phone_numbers']]

    dicts = no_resto_number.set_index("RESTAURANT_ID")['phone_numbers'].to_dict()
    igcc['phone_numbers'] = igcc['phone_numbers'].fillna(igcc['RESTAURANT_ID'].map(dicts))

    igcc['phone_numbers'] = igcc['phone_numbers'].replace(np.nan,'no_number')

    # removing unwated and bangalore
    igcc = igcc[~((igcc['ISSUE2'].str.contains("Found unwanted ingredients", na=False)) & (igcc['REST_CITY_NAME'] == 'Bangalore'))]
    def un_rem(x):
        if x is None:
            return "No"
        elif "Found unwanted ingredients" in x:
            return "Yes"
        else:
            return "no"

    igcc['unwated'] = igcc['ISSUE2'].apply(un_rem)

    # reading NAT account
    nat = pd.read_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\nat.csv")
    nat_list = nat['RESTAURANT_ID'].to_list()

    def flag_df(igcc):
       if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == 'cancelled'):
           return 'Replacement not given'
       elif (igcc['RESOLUTIONS_GIVEN'] == "coupon") and (igcc['IS_RESOLVED'] == "false"):
           return 'Coupon not given'
       elif (igcc['RESOLUTIONS_GIVEN'] == "refund") and (igcc['IS_RESOLVED'] == "false"):
           return 'Refund not given'
       elif (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (igcc['REPLICATED_ORDER_ID'] == "-1"):
           return 'Replacement failed'
       elif (igcc['BASE_ORDER_DATE'] < earlier):
           return 'Old dated'
       # enable this once after getting phone numbers in table
       # elif (igcc['phone_numbers'] == 'no_number'):
       #     return 'No resto number'
       elif (igcc['ISSUE'] != "missing_items") and (igcc['ISSUE'] != "missing items")and (igcc['ISSUE'] != "quality_issues") and (igcc['ISSUE'] != "quality issues") and (igcc['ISSUE'] != "wrong_items") and (igcc['ISSUE'] != "wrong items") and (igcc['ISSUE'] != "quantity_issues") and (igcc['ISSUE'] != "quantity issues") and (igcc['ISSUE'] != "special_instruction") and (igcc['ISSUE'] != "special instruction") and (igcc['ISSUE'] != "special instructions not followed") and (igcc['ISSUE'] != 'Check in OMS'):
           return 'Non resto related'
       elif (igcc['ISSUE'] == "wrong items") or (igcc['ISSUE'] == "wrong_items"):
           return 'Non voice tickets'
       elif (igcc['ISSUE'] == 'special_instruction'):
           return 'Special instruction'
       elif (pd.isnull(igcc['BASE_ORDER_DATE'])):
           return 'BOD missing'
       elif (igcc['RESTAURANT_ID'] in nat_list):
           return 'National account'
       elif (igcc['REST_NAME'] == "midpoint cafe") or (igcc['REST_NAME'] == "dhaba 21 by midpoint cafe"):
           return "Midpoint cafe"
       elif (igcc['ISSUE'] == "missing_items") & ((igcc['REST_CITY_NAME'] == "Hyderabad") or (igcc['REST_CITY_NAME'] == "Gurgaon") or (igcc['REST_CITY_NAME'] == "Kolkata") or (igcc['REST_CITY_NAME'] == "Bangalore") or (igcc['REST_CITY_NAME'] == "Chennai") or (igcc['REST_CITY_NAME'] == "Pune") or (igcc['REST_CITY_NAME'] == "Mumbai") or (igcc['REST_CITY_NAME'] == "Delhi") or (igcc['REST_CITY_NAME'] == "Faridabad") or (igcc['REST_CITY_NAME'] == "Vijayawada") or (igcc['REST_CITY_NAME'] == "Bhubaneswar") or (igcc['REST_CITY_NAME'] == "Chandigarh") or (igcc['REST_CITY_NAME'] == "Thiruvananthapuram") or (igcc['REST_CITY_NAME'] == "Lucknow") or (igcc['REST_CITY_NAME'] == "Vizag") or (igcc['REST_CITY_NAME'] == "Jaipur") or (igcc['REST_CITY_NAME'] == "Ahmedabad") or (igcc['REST_CITY_NAME'] == "Noida1") or (igcc['REST_CITY_NAME'] == "Coimbatore") or (igcc['REST_CITY_NAME'] == "Kochi") or (igcc['REST_CITY_NAME'] == "Nagpur")):
           return "Missing items GHK"
       elif (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] != 'delivered') & (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] != 'cancelled'):
           return "Waiting for ending staus"
       elif (igcc['unwated'] == "Yes") & (igcc['REST_CITY_NAME'] == "Bangalore"):
           return "Found unwanted ingredients & Bangalore"
       elif (igcc['ISSUE'] == 'Check in OMS'):
           return "Check in OMS"
       elif (igcc['RESOLUTIONS_GIVEN'] == "coupon") and (igcc['IS_RESOLVED'] == "true"):
           return "Work"
       elif (igcc['RESOLUTIONS_GIVEN'] == "refund"):
           return "Work"
       elif (igcc['RESOLUTIONS_GIVEN'] == "replicate_order") and (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == "delivered"):
           return "Work"

    igcc['Status'] = igcc.apply(flag_df, axis = 1)

    igcc = igcc[~(igcc['Status'] == 'Waiting for ending staus')]

    igcc['ID(NA)'] = ''
    igcc['WORKING_STATS(NA)'] = 'FRESH'
    igcc['ASSIGNEDTO(NA)'] = ''
    igcc['Curr_stat'] = ''
    igcc['actioned_date'] = datetime.datetime.now().strftime('%d-%m-%y')


    # def flag_df_final(igcc):
    #    if (igcc['Status'] != 'Replacement not given') and (igcc['Status'] != 'Coupon not given') and (igcc['Status'] != 'Refund not given') and (igcc['Status'] != 'Replacement failed') and (igcc['Status'] != 'Check in OMS') and (igcc['Status'] != 'Non resto related') and (igcc['Status'] != 'Non voice tickets') and (igcc['Status'] != 'Old dated') and (igcc['Status'] != 'BOD missing') and (igcc['Status'] != 'National account') and (igcc['Status'] != 'Midpoint cafe') and (igcc['Status'] != 'No resto number') and (igcc['Status'] != 'Missing items GHK') and (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] != 'Waiting for ending status') and (igcc['ISSUE'] != 'Special instruction'):
    #        return 'Work'
    #    else:
    #        return igcc['Status']

    # igcc['Status'] = igcc.apply(flag_df_final, axis = 1)

    igcc = igcc.loc[:, ~igcc.columns.str.contains('UNNAMED: 0')]
    igcc = igcc.loc[:, ~igcc.columns.str.contains('REST_PHONE_NUMBER')]
    igcc = igcc.loc[:, ~igcc.columns.str.contains('phone_numbers')]


    # merging manual phone numbers with snowflakes phone number
    phn = pd.concat([phn,no_resto_number])



    # adding language
    lang = pd.read_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\languages.csv")
    igcc = igcc.merge(lang,how='left',on='REST_CITY_NAME')

    igcc['Language'] = igcc['Language'].fillna('Hindi')


    igcc = igcc[['ISSUEID','RESOLUTIONGIVENDATE','BASE_ORDER_ID','BASE_ORDER_DATE','ORDER_TOTAL','RESTAURANT_ID','REST_NAME','REST_CITY_NAME','REPLICATED_ORDER_ID','REPLICATED_ORDER_POST_DELIVERY_STATUS','ISSUE','IS_RESOLVED','RESOLUTION_ID','RESOLUTIONS_AMOUNT','RESOLUTIONS_GIVEN','RESOLUTION_CODES','AGENT_EMAIL','APPROVED_BY_EMAIL','ISRECOMMENDATIONFOLLOWED','ORDERED_QUANTITY','ITEMSIMPACTED','Status','Language','ID(NA)','WORKING_STATS(NA)','ASSIGNEDTO(NA)','Curr_stat','actioned_date']]

    igcc.to_csv("C:\\Users\\"+user+"\\Desktop\\projects\\marvex\\igcc_working.csv", index=False)



    today = datetime.datetime.now()
    print("everything works")



if not first_block_1 or not first_block_2 or not first_block_3 or not first_block_4 or not first_block_5 or not first_block_6 or not first_block_7 or not first_block_8 or not first_block_9 or not first_block_10 or not first_block_11 or not first_block_12 or not first_block_13:
    try:
        # Calling Mail Function
        subject = "Marvex | Code Execution Error | "
        html = 'Marvex was unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>'
        tousers = ['vd.gokkulkumar@swiggy.in']
        ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
    finally:
        exit(print('Code Terminated'))
else:
    try:
        # Calling Mail Function
        subject = "Marvex | Success | "
        html = "Report has been successfully Uploaded!"
        tousers = ['vd.gokkulkumar@swiggy.in']
        ccusers = ['vd.gokkulkumar@swiggy.in']
        sendmailtostakeholder(html, tousers, ccusers, subject)
        print('Success - Mail')
    except:
        print('Failed to send mail for Success!')