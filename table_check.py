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

user = getpass.getuser()


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

print(cs)


raw_fetch = cs.execute("SHOW COLUMNS in table secure_views.igcc_restaurant_recovery.city")

# raw_fetch = cs.execute("SELECT order_id AS base_order_id, NUM_ITEMS AS ordered_quantity FROM secure_views.igcc_restaurant_recovery.dp_place_order dpo ")

df = pd.DataFrame(raw_fetch)
print(df)