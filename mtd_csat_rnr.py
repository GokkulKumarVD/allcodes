#!/usr/bin/env python3
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
# import pymysql.cursors
import time
import webbrowser
import os
from os import mkdir, makedirs
from datetime import datetime
from datetime import date
import glob
import shutil
import pandas as pd
import datetime
import numpy as np
import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



import getpass

username = getpass.getuser()

pd.set_option('display.max_columns', 500)

# CSAT
x = datetime.datetime.now()
if x.day == 1:
    from datetime import datetime
    given_date = datetime.today().date()
    first_day_of_month = given_date.replace(day=1)
    first_day_of_month = given_date.replace(month = x.month-1)
    first_day_of_month = first_day_of_month.isoformat()
else:
    from datetime import datetime
    given_date = datetime.today().date()
    first_day_of_month = given_date.replace(day=1)
    first_day_of_month = first_day_of_month.isoformat()




with open("C:\\Users\\"+username+"\\Desktop\\projects\\rnr\\rsa_key.p8", "rb") as key:
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

    mtd_csat = cs.execute("SELECT DT,AGENTEMAILID, EFFORTSCORE FROM streams.public.collect_csat where chattype = 'agent' AND ORGID = 'swiggy' and AGENTEMAILID != 'NOTFILLED' and EFFORTSCORE <> -99 and dt between '{}' and current_date;".format(first_day_of_month))

    print('Download Completed')
    surveys = pd.DataFrame(mtd_csat)
    surveys.columns = ['DT','AGENTEMAILID', 'EFFORTSCORE']
    surveys = surveys.groupby(['DT','AGENTEMAILID']).mean()*100

    surveys.to_csv("C:\\Users\\"+username+"\\Desktop\\projects\\rnr\\mtd_best_surveys.csv")
finally:
    cs.close()