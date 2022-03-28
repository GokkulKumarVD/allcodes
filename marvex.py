# !/usr/bin/env python3
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
import pymysql
import sys

warnings.simplefilter(action='ignore', category=FutureWarning)

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
first_block_14 = True
first_block_15 = True


# gokkul

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


def uploadrunningstat(flag, message, aligned):
    try:
        mydb = mysql.connector.connect(
            host='172.16.251.114',
            user='marvexfreshuploader',
            passwd='m@rv3><fre$HpAs$upl)@dER',
            database='marvexigcc'
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO cronuploadstat (flag, message, aligned) VALUES (%s, %s, %s)"
        val = (flag, message, aligned)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
    except Exception as err:
        exit()


print("running")

print(datetime.datetime.now())
#  fetching data from marvex database
# importing required librarie(s)

# Establishing conection
try:
    # block_1
    mydb = mysql.connector.connect(
        host='172.16.251.114',
        user='marvexfreshuploader',
        passwd='m@rv3><fre$HpAs$upl)@dER',
        database='marvexigcc',
    )
except:
    exit(print('Connection Error : MX-DB'))

# Setting connection cursor and fetching the datatry:
try:
    # block_2
    aplhaerr = ''
    mycursor = mydb.cursor()
    if (mycursor):
        mycursor.execute("select RESOLUTION_ID from ticketinfo union select RESOLUTION_ID from freshtickets")
        myresult = mycursor.fetchall()
        igcc_old_check = pd.DataFrame(myresult)
        print("old order ids")
        print(igcc_old_check)
        # FETCH STORE RESTO IDS TO EXCLUDE FROM THE TICKET

        # mycursor.execute("select restid from restidtoexclude;")
        # myresult = mycursor.fetchall()
        # igcc_store_orders = pd.DataFrame(myresult)
        # igcc_store_orders.columns = ['store_resto_ids']
        igcc_store_orders = pd.read_csv("/var/marvexfreshuploader/marvex/storeid.csv", encoding='unicode_escape')
        igcc_store_orders.columns = ['Txn ID', 'Resturant Name']
        store_resto_ids_list = igcc_store_orders['Txn ID'].to_list()

        print(store_resto_ids_list)
        if len(igcc_old_check) > 1:
            print("here")
            igcc_old_check.columns = ['resolutionid']
            igcc_old_check_list = igcc_old_check['resolutionid'].to_list()
            print(igcc_old_check)
            print(len(igcc_old_check_list))
        mycursor.close()
        mydb.close()
        proceed = True
except Exception as err:
    proceed = False
    igcc_old_check_list = []
    aplhaerr += '#block_2 -> ' + str(err) + '<br>'

# # ending here


if proceed:
    aplhaerr = ''
    try:
        # block_3
        # WARESHOUSE CONNECTOR KEY
        with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
            account='swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
            private_key=pkb,
            role='igcc_restaurant_recovery',
            warehouse='NONTECH_WH_01'
        )
        cs = ctx.cursor()
        first_block_1 = True
        proceed = True

    except Exception as err:
        proceed = False
        aplhaerr += '#block_3 -> ' + str(err) + '<br>'
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
                                                               WHERE i.dt >= cast(dateadd('DAY',-7, to_date(current_date)) AS VARCHAR)
                                                               GROUP BY 1,2,3
                                                            ) AS i
                                                    ON r.issueid = i.foodissueid
                                                  LEFT JOIN secure_views.igcc_restaurant_recovery.food_issue_restaurant_recovery rr
                                                    ON r.issueid=rr.foodissueid
                                                        AND rr.dt >= cast(dateadd('DAY',-7, to_date(current_date)) AS VARCHAR)
                                                  WHERE r.dt = current_date
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
                                                   WHERE dpo.dt >= cast(dateadd('DAY',-30, to_date(current_date)) AS VARCHAR)
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
                                                  WHERE dpo.dt >= cast(dateadd('DAY',-30, to_date(current_date)) AS VARCHAR)
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
                                                           WHERE dt >= cast(dateadd('DAY',-7, to_date(current_date)) AS VARCHAR)
                                                         ) oft
                                                   INNER JOIN (
                                                                 SELECT try_cast(lower(trim(resolution_codes)) AS NUMBER) AS rep_order_id
                                                                 FROM raw_data
                                                                 WHERE resolutions_given = 'REPLICATE_ORDER' and try_cast(resolution_codes AS NUMBER) <> -1
                                                                 GROUP BY 1
                                                              ) re
                                                      ON cast(oft.orderid as varchar) = cast(re.rep_order_id as varchar)
                                                   WHERE oft.dt >= cast(dateadd('DAY',-7, to_date(current_date)) AS VARCHAR)
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
        dp_order_fact1.columns = ['RESTAURANT_ID', 'CITY_CODE']

        raw_fetch = cs.execute(
            "Select distinct(restaurant_id) from secure_views.igcc_restaurant_recovery.dp_order_fact;")
        dp_order_fact2 = pd.DataFrame(raw_fetch)
        dp_order_fact2.columns = ['RESTAURANT_ID']

        dp_order_fact = dp_order_fact2.merge(dp_order_fact1, how='left', on='RESTAURANT_ID')

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

        food_issue_resolution = food_issue_resolution[~(food_issue_resolution['RESOLUTION_ID'].isin(igcc_old_check_list))]
        cs.close()
        first_block_2 = True
        proceed = True
    except Exception as err:
        proceed = False
        aplhaerr += '#block_4 -> ' + str(err) + '<br>'

    try:
        # block_5

        # excluding store resto ids
        food_issue_resolution = food_issue_resolution[~food_issue_resolution.RESTAURANT_ID.isin(store_resto_ids_list)]

        # finding empty city names and filling it with another query
        temp_food_issue_resolution = food_issue_resolution[food_issue_resolution['REST_CITY_NAME'].isnull()]
        food_issue_resolution_city_names_blank = temp_food_issue_resolution['BASE_ORDER_ID'].to_list()

        if food_issue_resolution_city_names_blank.__len__() > 1:
            with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
                "select f.order_id, f.restaurant_id AS RESTAURANT_ID, sr.name AS REST_NAME, sc.name AS REST_CITY_NAME from secure_views.igcc_restaurant_recovery.dp_order_fact f join secure_views.igcc_restaurant_recovery.city sc on f.city_id=sc.id join secure_views.igcc_restaurant_recovery.restaurants sr on sr.id=f.restaurant_id where f.order_id in ({})".format(
                    ",".join([str(x) for x in food_issue_resolution_city_names_blank])))
            food_issue_resolution_city_names_blank = pd.DataFrame(raw_fetch)
            food_issue_resolution_city_names_blank.columns = ['ORDER_ID', 'RESTAURANT_ID', 'REST_NAME',
                                                              'REST_CITY_NAME']

            city_dict = food_issue_resolution_city_names_blank.set_index('ORDER_ID')['REST_CITY_NAME'].to_dict()
            food_issue_resolution['REST_CITY_NAME'] = food_issue_resolution['REST_CITY_NAME'].fillna(
                food_issue_resolution['BASE_ORDER_ID'].map(city_dict))

            cs.close()



        # removing false from isresolved (it's in boolean)
        food_issue_resolution = food_issue_resolution[(food_issue_resolution['IS_RESOLVED'] == 1)]

        # renaming df
        igcc = food_issue_resolution

        # dropping duplicate rows
        # igcc.drop_duplicates('RESOLUTION_ID', keep='first', inplace=True)

        # taking data where issue is null
        igcc_issue_blank = igcc[igcc['ISSUE'].isnull()]
        list_id = list(igcc_issue_blank['BASE_ORDER_ID'])
        first_block_3 = True
        proceed = True
    except Exception as err:
        proceed = False
        aplhaerr += '#Main_file_merging_error -> ' + str(err) + '<br>'
        first_block_3 = False

    if (list_id.__len__() > 1):
        try:
            with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
            raw_fetch = cs.execute(
                "Select ORDERID,FOODISSUEID, ISSUEDESCL1 from secure_views.igcc_restaurant_recovery.food_issue where orderid in ({})".format(
                    ",".join([str(i) for i in list_id])))
            igcc_issue_blank = pd.DataFrame(raw_fetch)
            # igcc_issue_blank.to_csv("C:\\Users\\"+user+""\\Desktop\\projects\\marvex\\igcc_issue_blank.csv")
            # renaming igcc_issue_blank columns
            igcc_issue_blank.columns = ["orderid", "foodissueid", "issuedescl1"]

            # created dictionary and mapping with primary data
            dicts = igcc_issue_blank.set_index("foodissueid")['issuedescl1'].to_dict()
            igcc['ISSUE'] = igcc['ISSUE'].fillna(igcc['ISSUEID'].map(dicts))

            # print(igcc_issue_blank)
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
    igcc['BASE_ORDER_DATE'] = igcc['BASE_ORDER_DATE'].replace("NONE", np.nan)
    blank_dates = igcc[igcc['BASE_ORDER_DATE'].isnull()]
    list_id = list(blank_dates['BASE_ORDER_ID'])

    if (list_id.__len__() > 1):
        try:
            with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
            raw_fetch = cs.execute(
                "select f.order_id, f.cust_payable,  sr.name,sr.phone_numbers, f.dt,sc.name as rest_city from secure_views.igcc_restaurant_recovery.dp_order_fact f join secure_views.igcc_restaurant_recovery.city sc on f.city_id=sc.id join secure_views.igcc_restaurant_recovery.restaurants sr on sr.id=f.restaurant_id where f.order_id in ({}) and dt IS NOT NULL".format(
                    ",".join([str(i) for i in list_id])))
            igcc_date_blank = pd.DataFrame(raw_fetch)
            # igcc_date_blank.to_csv("/var/marvexfreshuploader/marvex/igcc_date_blank.csv")
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

    today = datetime.datetime.now().date()
    # change it to days = 2 if it is live
    DD = datetime.timedelta(days=2)
    earlier = (today - DD)
    igcc['BASE_ORDER_DATE'] = pd.to_datetime(igcc['BASE_ORDER_DATE'])

    # working on replacement order ids
    igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].fillna("NONE")


    def flag_rep(igcc):
        if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order'):
            return igcc['RESOLUTION_CODES']


    igcc['REPLICATED_ORDER_ID'] = igcc.apply(flag_rep, axis=1)

    igcc['REPLICATED_ORDER_ID'] = igcc['REPLICATED_ORDER_ID'].fillna('Not a replacement order')


    def replicate(igcc):
        if igcc['REPLICATED_ORDER_ID'] == 'Not a replacement order':
            return igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS']
        else:
            return 'NONE'


    igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc.apply(replicate, axis=1)


    def flag_rep(igcc):
        if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (
                igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == 'NONE'):
            return 'Replacement not given'


    igcc['Status'] = igcc.apply(flag_rep, axis=1)


    # igcc['REPLICATED_ORDER_ID'] = igcc['RESOLUTION_CODES']

    def flag_rep(igcc):
        if (igcc['RESOLUTION_CODES'] == '-1'):
            return 'Replicate order ID not generated'
        else:
            return igcc['Status']


    igcc['Status'] = igcc.apply(flag_rep, axis=1)

    igcc_replicate = igcc[(igcc['Status'] == 'Replacement not given')]
    list_id_rep = list(igcc_replicate['REPLICATED_ORDER_ID'])

    # for item in list_id_rep[:]:
    #     if "-" in item:
    #         list_id_rep.remove(item)

    if (list_id_rep.__len__() > 1):
        try:
            with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
            raw_fetch = cs.execute(
                "select ORDERID, STATUS from secure_views.igcc_restaurant_recovery.dp_update_de_order_status_event where orderid in ({}) and status = 'delivered'".format(
                    ",".join([str(i) for i in list_id_rep])))
            igcc_rep = pd.DataFrame(raw_fetch)
            igcc_rep.to_csv("/var/marvexfreshuploader/marvex/igcc_rep.csv")

            print("end")
            print(datetime.datetime.now())
            first_block_10 = True
        except Exception as err:
            aplhaerr += '#replicate order data error -> ' + str(err) + '<br>'
            first_block_10 = False

        igcc_rep.columns = ['order_id', 'post_status']

        igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].replace("NONE",
                                                                                                              np.nan)

        igcc_rep['order_id'] = igcc_rep['order_id'].astype(str)

        # igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = (
        #     igcc['REPLICATED_ORDER_ID'].map(igcc_rep.set_index('order_id')['post_status'])
        #     .fillna(igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS']))

        dicts = igcc_rep.set_index("order_id")['post_status'].to_dict()
        igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] = igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].fillna(
            igcc['REPLICATED_ORDER_ID'].map(dicts))

    # now fetching phone numbers
    try:
        with open("/var/marvexfreshuploader/marvex/marvex_rsa_key.p8", "rb") as key:
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
        raw_fetch = cs.execute(
            "select id as RESTAURANT_ID, phone_numbers from secure_views.igcc_restaurant_recovery.restaurants")
        phn1 = pd.DataFrame(raw_fetch)
        phn1.columns = ['RESTAURANT_ID', 'phone_numbers']
        phn1.to_csv("/var/marvexfreshuploader/marvex/phone_numbers.TSV", sep='\t')

        phn = pd.read_csv("/var/marvexfreshuploader/marvex/phone_numbers.TSV", sep='\t', thousands=',')

        try:
            phn['phone_numbers'] = phn['phone_numbers'].str.split(',')
            phn = phn.explode('phone_numbers')
            phn = phn.loc[:, ~phn.columns.str.contains('Unnamed: 0')]
        except:
            phn = phn.loc[:, ~phn.columns.str.contains('Unnamed: 0')]

        print('Phone success')
        print(phn)
        first_block_13 = True
    except Exception as err:
        aplhaerr += '#phone number data error -> ' + str(err) + '<br>'
        first_block_13 = False

try:
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

    igcc['phone_numbers'] = igcc['phone_numbers'].replace('nan', np.nan)
    igcc['phone_numbers'] = igcc['phone_numbers'].replace('no_number', np.nan)

    # filling blank phone numbers
    no_resto_number = pd.read_csv("/var/marvexfreshuploader/marvex/No_Resto_Number.csv")
    no_resto_number.columns = ['RESTAURANT_ID','phone_numbers']
    no_resto_number = no_resto_number[['RESTAURANT_ID', 'phone_numbers']]
    no_resto_number['RESTAURANT_ID'] = no_resto_number['RESTAURANT_ID'].astype('str')
    dicts = no_resto_number.set_index("RESTAURANT_ID")['phone_numbers'].to_dict()
    igcc['phone_numbers'] = igcc['phone_numbers'].fillna(igcc['RESTAURANT_ID'].map(dicts))
    igcc['phone_numbers'] = igcc['phone_numbers'].replace(np.nan, 'no_number')
    # removing unwated and bangalore
    # igcc = igcc[~((igcc['ISSUE2'].str.contains("Found unwanted ingredients", na=False)) & (igcc['REST_CITY_NAME'] == 'Bangalore'))]
    # igcc['ISSUE2'] = igcc['ISSUE2'].fillna('nothing')
    igcc['ISSUE2'] = igcc['ISSUE2'].fillna('nothing')
    igcc['ISSUE2'] = igcc['ISSUE2'].str.replace(r'[', '')
    igcc['ISSUE2'] = igcc['ISSUE2'].str.replace(r']', '')


    def un_rem(x):
        if "Found unwanted ingredients" not in x:
            return "no"
        else:
            return "Yes"


    igcc['unwated'] = igcc['ISSUE2'].apply(un_rem)

    # def un_rem(x):
    # 	if "nothing" in x:
    # 		return "empty"
    # 	elif "Found unwanted ingredients" in x:
    # 		return "Yes"
    # 	else:
    # 		return "no"
    #
    # igcc['unwated'] = igcc['ISSUE2'].apply(un_rem)

    # reading NAT account
    nat = pd.read_csv("/var/marvexfreshuploader/marvex/nat.csv")
    nat_list = nat['RESTAURANT_ID'].to_list()

    # exclude halidram for quality and quantity
    halidram = pd.read_csv("/var/marvexfreshuploader/marvex/halidram.csv")
    halidram_list = halidram['ID'].to_list()

    # reading missing items excluding resto id
    # missing_items_city = pd.read_csv("/var/marvexfreshuploader/marvex/missing_items_city.csv")
    # missing_items_city_list = missing_items_city['ID'].to_list()
    # print('It works')
    igcc['RESTAURANT_ID'].fillna(0, inplace=True)
    igcc['RESTAURANT_ID'] = igcc['RESTAURANT_ID'].astype('int64')

    def flag_df(igcc):
        if (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (
                igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == 'cancelled'):
            return 'Replacement not given'
        elif (igcc['RESOLUTIONS_GIVEN'] == "coupon") and (igcc['IS_RESOLVED'] == "false"):
            return 'Coupon not given'
        elif (igcc['RESOLUTIONS_GIVEN'] == "refund") and (igcc['IS_RESOLVED'] == "false"):
            return 'Refund not given'
        elif (igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') and (igcc['REPLICATED_ORDER_ID'] == "-1"):
            return 'Replacement failed'
        elif (igcc['BASE_ORDER_DATE'] < earlier):
            return 'Old dated'
        elif (igcc['phone_numbers'] == 'no_number'):
            return 'No resto number'
        elif (igcc['ISSUE'] != "missing_items") and (igcc['ISSUE'] != "missing items") and (
                igcc['ISSUE'] != "quality_issues") and (igcc['ISSUE'] != "quality issues") and (
                igcc['ISSUE'] != "wrong_items") and (igcc['ISSUE'] != "wrong items") and (
                igcc['ISSUE'] != "quantity_issues") and (igcc['ISSUE'] != "quantity issues") and (
                igcc['ISSUE'] != "special_instruction") and (igcc['ISSUE'] != "special instruction") and (
                igcc['ISSUE'] != "special instructions not followed") and (igcc['ISSUE'] != 'Check in OMS'):
            return 'Non resto related'
        elif (igcc['ISSUE'] == "wrong items") or (igcc['ISSUE'] == "wrong_items"):
            return 'Non voice tickets'
        elif (igcc['ISSUE'] == 'special_instruction'):
            return 'Special instruction'
        elif (pd.isnull(igcc['BASE_ORDER_DATE'])):
            return 'BOD missing'
        elif (igcc['REST_NAME'] == "burger king") or (igcc['REST_NAME'] == "burger king") or (
              igcc['REST_NAME'] == "corner house ice cream") or (igcc['REST_NAME'] == "mcdonald's") or (
              igcc['REST_NAME'] == "dunkin donuts") or (igcc['REST_NAME'] == "starbucks coffee") or (
              igcc['REST_NAME'] == "natural ice cream") or (igcc['REST_NAME'] == "nic natural ice cream") or (
              igcc['REST_NAME'] == "nic natural ice creams") or (igcc['REST_NAME'] == "domino's pizza") or (
              igcc['REST_NAME'] == "nic natural ice creams - zirakpur"):
            return 'National account'
        elif (igcc['RESTAURANT_ID'] in nat_list):
            return 'National account / pvt brand'
        elif (igcc['RESTAURANT_ID'] in halidram_list) & ((igcc['ISSUE'] != "quantity_issues") or (igcc['ISSUE'] != "quality_issues")):
            return 'Halidram not callable'
        elif (igcc['REST_NAME'] == "midpoint cafe") or (igcc['REST_NAME'] == "dhaba 21 by midpoint cafe"):
            return "Midpoint cafe"
        elif (igcc['REST_CITY_NAME'] == "Mangaluru") or (igcc['REST_CITY_NAME'] == "Manipal"):
            return "Mangaluru/manipal not callable"
        elif (igcc['ISSUE'] == "missing_items"):
            return "Missing items GHK"
        elif ((igcc['RESOLUTIONS_GIVEN'] == 'replicate_order') & (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] != 'delivered') & (igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] != 'cancelled')):
            return "Waiting for ending staus"
        elif (igcc['unwated'] == "Yes") & (igcc['REST_CITY_NAME'] == 'Bangalore'):
            return "Found unwanted ingredients & Bangalore"
        elif (igcc['ISSUE'] == 'Check in OMS'):
            return "Check in OMS"
        elif (igcc['RESOLUTIONS_GIVEN'] == "coupon") and (igcc['IS_RESOLVED'] == "true"):
            return "Work"
        elif (igcc['RESOLUTIONS_GIVEN'] == "refund"):
            return "Work"
        elif (igcc['RESOLUTIONS_GIVEN'] == "replicate_order") and (
                igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'] == "delivered"):
            return "Work"
        # print('It works 2')


    igcc['Status'] = igcc.apply(flag_df, axis=1)

    # def nat(x):
    #     if x in nat_list:
    #         return 'National account / pvt brand'
    #
    # igcc['Status'] = igcc['RESTAURANT_ID'].apply(nat)

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
    phn = pd.concat([phn, no_resto_number])

    # adding language
    lang = pd.read_csv("/var/marvexfreshuploader/marvex/languages.csv")
    igcc = igcc.merge(lang, how='left', on='REST_CITY_NAME')

    igcc['Language'] = igcc['Language'].fillna('Hindi')


    def lang(x):
        if x != 'Hindi' and x != 'Kannada' and x != 'Telugu' and x != 'Tamil' and x != 'Malayalam':
            return 'Hindi'
        else:
            return x


    igcc['Language'] = igcc['Language'].apply(lang)

    igcc = igcc[['ISSUEID', 'RESOLUTIONGIVENDATE', 'BASE_ORDER_ID', 'BASE_ORDER_DATE', 'ORDER_TOTAL', 'RESTAURANT_ID',
                 'REST_NAME', 'REST_CITY_NAME', 'REPLICATED_ORDER_ID', 'REPLICATED_ORDER_POST_DELIVERY_STATUS', 'ISSUE',
                 'IS_RESOLVED', 'RESOLUTION_ID', 'RESOLUTIONS_AMOUNT', 'RESOLUTIONS_GIVEN', 'RESOLUTION_CODES',
                 'IS_RESOLVED', 'RESOLUTION_ID', 'RESOLUTIONS_AMOUNT', 'RESOLUTIONS_GIVEN', 'RESOLUTION_CODES',
                 'AGENT_EMAIL', 'APPROVED_BY_EMAIL', 'ISRECOMMENDATIONFOLLOWED', 'ORDERED_QUANTITY', 'ITEMSIMPACTED',
                 'Status', 'Language', 'ID(NA)', 'WORKING_STATS(NA)', 'ASSIGNEDTO(NA)', 'Curr_stat', 'actioned_date']]
    igcc.columns = ['ISSUEID', 'RESOLUTIONGIVENDATE', 'BASE_ORDER_ID', 'BASE_ORDER_DATE', 'BASE_ORDER_CUST_PAYABLE',
                    'RESTAURANT_ID', 'REST_NAME', 'REST_CITY_NAME', 'REPLICATED_ORDER_ID',
                    'REPLICATED_ORDER_POST_DELIVERY_STATUS', 'ISSUE', 'IS_RESOLVED', 'RESOLUTION_ID',
                    'RESOLUTIONS_AMOUNT', 'RESOLUTIONS_GIVEN', 'RESOLUTION_CODES', 'AGENT_EMAIL', 'APPROVED_BY_EMAIL',
                    'ISRECOMMENDATIONFOLLOWED', 'ORDERED_QUANTITY', 'ITEMS_QUANTITY_IMPACTED', 'Status', 'Language',
                    'ID', 'workingstats', 'ASSIGNEDTO', 'curr_tkt_status', 'actioned_date']
    # igcc.drop_duplicates(subset=['ISSUEID'], keep='first', inplace=True)
    # igcc = igcc[~(igcc['REPLICATED_ORDER_POST_DELIVERY_STATUS'].isnull())]
    igcc.to_csv("/var/marvexfreshuploader/marvex/igcc_working.csv", index=False)
    today = datetime.datetime.now()
    print("everything works")
except Exception as err:
    aplhaerr += '#block14 -> ' + str(err) + '<br>'
    first_block_14 = False

# #Uploading to Database
# try:
# 	import sqlalchemy
# 	database_username = 'marvexfreshuploader'
# 	database_password = 'm@rv3><fre$HpAs$upl)@dER'
# 	database_ip       = '172.16.251.114'
# 	database_name     = 'marvexigcc'
# 	database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
# 	                                               format(database_username, database_password,
# 	                                               database_ip, database_name), pool_recycle=1, pool_timeout=57600).connect()
# 	igcc.to_sql(con=database_connection, name='freshtickets', if_exists='append', index= False)
# except Exception as err:
# 	aplhaerr += '#block15 -> ' + str(err) + '<br>'
# 	first_block_15 = False

try:
    con = pymysql.connect(
        host='172.16.251.114',
        user='marvexfreshuploader',
        password='m@rv3><fre$HpAs$upl)@dER',
        autocommit=True,
        local_infile=1
    )
    print('Connected to DB: {}'.format('172.16.251.114'))
    # Create cursor and execute Load SQL
    cursor = con.cursor()
    cursor.execute(
        "LOAD DATA LOCAL INFILE '/var/marvexfreshuploader/marvex/igcc_working.csv' INTO TABLE marvexigcc.ticketinfo FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n'")
    print('Succuessfully loaded the table from csv.')
    con.close()

except Exception as err:
    aplhaerr += '#block15 -> ' + str(err) + '<br>'
    first_block_15 = False

if not first_block_1 or not first_block_2 or not first_block_3 or not first_block_4 or not first_block_5 or not first_block_6 or not first_block_7 or not first_block_8 or not first_block_9 or not first_block_10 or not first_block_11 or not first_block_12 or not first_block_13 or not first_block_14 or not first_block_15:
    try:
        # Calling Mail Function
        # subject = "Marvex | Code Execution Error | "
        # html = 'Marvex was unable to execute successfully!<br><br>HashCode(s) with ErrorMessage(s):<br>'
        # tousers = ['vd.gokkulkumar@swiggy.in']
        # ccusers = ['rahul.kp@swiggy.in', 'sourav.verma@swiggy.in']
        # sendmailtostakeholder(html, tousers, ccusers, subject)
        print('Err: ', str(aplhaerr))
        uploadrunningstat('FAIL', 'Err->' + str(aplhaerr), today.hour)
    finally:
        exit(print('Code Terminated'))
else:
    try:
        # Calling Mail Function
        # subject = "Marvex | Success | "
        # html = "Report has been successfully Uploaded!"
        # tousers = ['vd.gokkulkumar@swiggy.in']
        # ccusers = ['vd.gokkulkumar@swiggy.in']
        # sendmailtostakeholder(html, tousers, ccusers, subject)
        # print('Success - Mail')
        uploadrunningstat('SUCCESS', 'NA', today.hour)
    except:
        print('Failed to send mail for Success!')
    finally:
        exit()

