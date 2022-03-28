#!/usr/bin/env python3
import os
import pandas as pd
import snowflake.connector
from datetime import date
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
import time


mydb = mysql.connector.connect(
    host='172.16.251.200',
    user='assetmgmt',
    passwd='Sw!ggy@dm1n',
    database='snipeit_data_060418',
)

mycursor = mydb.cursor()

if (mycursor):
    mycursor.execute("""select a.asset_tag as 'Asset Tag',a.serial as 'Serial',a.notes as 'InvoiceNo', m.model_number as 'Model',ma.name as 'Make',c.name as 'Category',s.name as 'Status',u.email as 'Checked Out To',l.name as'Location',
         a._snipeit_system_ram_2 as 'System RAM',a.purchase_date as 'Purchase-Date',a.warranty_months as 'Warrenty'
        ,a._snipeit_processor_3 as 'Processor',a._snipeit_hdd_size_4 as 'HDD Size',a._snipeit_operating_system_5 as 'Operating System', a.last_checkout as 'Allcoated_Date', u.updated_at as 'Status_change_date' ,u.activated as 'Emp_Status',
        a.purchase_date as 'PurchaseDate', a.purchase_cost as 'PurchaseCost' 
        ,l.address as 'Zone' from assets a
        join locations l on l.id = a.rtd_location_id
        join models m on m.id = a.model_id
        join status_labels s on s.id =a.status_id
        left join users u on u.id=a.assigned_to
        join categories c on c.id =m.category_id
        join manufacturers ma on ma.id = m.manufacturer_id
        where a._snipeit_system_ram_2 like '%'""")
    myresult = mycursor.fetchall()
    snipeit = pd.DataFrame(myresult)


    snipeit.columns=['Asset_Tag','Serial','InvoiceNo','Model','Make','Category','Status','Checked_Out_To',
                     'Location','System_RAM','Purchase_Date','Warranty','Processor','HDD_size','Operating_System',
                     'Allcoated_Date','Status_change_date','Emp_Status','PurchaseDate','PurchaseCost','Zone']


def flag_df(snipeit):
    if (snipeit['Status'] == 'Ready to Deploy') and (
            snipeit['Checked_Out_To'] != None):
        return 'Assign'
    else:
        return snipeit['Status']

snipeit['Revised_status'] = snipeit.apply(flag_df, axis=1)


# -------------------------netskope
import requests
import pandas as pd

response = requests.get('https://swiggygs.goskope.com/api/v1/clients?token=06b13f570337d098c143b6a96bb76743')
print (response.json())

json_data_here = response.json()

netskope = pd.json_normalize(json_data_here['data'])
netskope.to_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\netskope.csv")
netskope.columns=['attributes._id', 'attributes.client_install_time',
       'attributes.client_version', 'attributes.device_id',
       'attributes.host_info.device_make', 'attributes.host_info.device_model',
       'attributes.host_info.hostname', 'attributes.host_info.managementID',
       'attributes.host_info.nsdeviceuid', 'attributes.host_info.os',
       'attributes.host_info.os_version', 'attributes.last_event.actor',
       'attributes.last_event.event', 'attributes.last_event.npa_status',
       'attributes.last_event.status', 'attributes.last_event.timestamp',
       'attributes.users', 'attributes.user_added_time']

df = snipeit.merge(netskope, left_on="Asset_Tag",right_on="attributes._id", how='left')

def tf(df):
    if (df['Asset_Tag'] == df['attributes._id']):
        return 'TRUE'
    else:
        return 'FALSE'

df['STATUS'] = df.apply(tf, axis=1)


def assi(df):
    if (df['Checked_Out_To'] != None):
        return 'Assign'
    else:
        return df['Status']

df['Status'] = df.apply(assi, axis=1)

df = df[(df['Category'] == 'All-in-One') | (df['Category'] == 'Desktop') | (df['Category'] == 'Laptop') ]

df['attributes.users'] = df['attributes.users'].fillna('Nothing')

def assi(df):
    if (df['attributes.users'] == 'Nothing'):
        return ''
    else:
        x = df['attributes.users']
        listToStr = ' '.join([str(elem) for elem in x])
        a = listToStr.split("last_event")
        # print(a[-1])
        try:
            print(a[-1].index("username"))
            location =  a[-1].index("username") + 12
            print(location)
            last_location = a[-1].index("'}")
            print(last_location)
            le = a[-1]
            print(le)
            print(type(le))
            print('----------------------------------------')
            return le[location:last_location]
        except:
            return "last event found, but not user name"

df['attributes.users'] = df.apply(assi, axis=1)


# df = df[['Asset_Tag', 'Serial', 'InvoiceNo', 'Model', 'Category', 'Status',
#        'Checked_Out_To', 'Location', 'Zone', 'PurchaseDate', 'PurchaseCost',
#        'Revised_status', 'attributes._id', 'attributes.client_install_time',
#        'attributes.client_version', 'attributes.device_id',
#        'attributes.host_info.device_make', 'attributes.host_info.device_model',
#        'attributes.host_info.hostname', 'attributes.host_info.managementID',
#        'attributes.host_info.nsdeviceuid', 'attributes.host_info.os',
#        'attributes.host_info.os_version', 'attributes.last_event.actor',
#        'attributes.last_event.event', 'attributes.last_event.npa_status',
#        'attributes.last_event.status', 'attributes.last_event.timestamp',
#        'attributes.users', 'attributes.user_added_time', 'STATUS']]

# df = df[['Asset_Tag', 'Serial', 'InvoiceNo', 'Model', 'Category', 'Status',
#        'Checked_Out_To', 'Location', 'Zone', 'PurchaseDate', 'PurchaseCost',
#        'Revised_status', 'STATUS']]

df_pivot_count = df[['Status','STATUS']]
df_pivot_count_true = df_pivot_count[df_pivot_count['STATUS'] == 'TRUE']
df_pivot_count_true = df_pivot_count_true.groupby(df_pivot_count_true["Status"]).STATUS.agg(["count"])
df_pivot_count_true  = df_pivot_count_true.reset_index()

df_pivot_count_false = df_pivot_count[df_pivot_count['STATUS'] == 'FALSE']
df_pivot_count_false = df_pivot_count_false.groupby(df_pivot_count_false["Status"]).STATUS.agg(["count"])
df_pivot_count_false  = df_pivot_count_false.reset_index()


df['readable_last_event_time'] = time.strftime('%Y-%m-%d', time.localtime(df['attributes.last_event.timestamp']))

df['attributes.last_event.timestamp'] = df['attributes.last_event.timestamp'].fillna('0')
df['attributes.last_event.timestamp'] = df['attributes.last_event.timestamp'].astype('int64')

def assi(df):
    if df['attributes.last_event.timestamp'] == 0:
        return '0'
    else:
        return time.strftime('%Y-%m-%d', time.localtime(df['attributes.last_event.timestamp']))

df['readable_last_event_time'] = df.apply(assi, axis=1)

today = date.today()

