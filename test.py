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


with open("C:/Users/vd.gokkulkumar/Desktop/important/rsa_key.p8", "rb") as key:
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

raw_fetch = cs.execute("Select * from facts.public.customer_interaction_fact limit 5")

df = pd.DataFrame(raw_fetch)
print(df)
cs.close()

