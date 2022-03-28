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
from datetime import timedelta
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil

con = pymysql.connect(host='172.16.251.113',
                      user='gokkul-kumar',
                      password='p@S$w0rdf0rg)kku(S38fd()hH',
                      autocommit=True,
                      local_infile=1
                      )
# Create cursor and execute Load SQL
cursor = con.cursor()

cursor.execute(
    "LOAD DATA LOCAL INFILE 'C:/Users/vd.gokkulkumar/Desktop/projects/freshdeskdata/datafiltered.csv' "
    "INTO TABLE bow_forms_data.tier_p3_p_unclassified FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS")
cursor.close()