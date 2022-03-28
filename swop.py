import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import os
import time
import shutil
from datetime import date
import datetime



user = getpass.getuser()

os.system("C:\\Users\\"+user+"\\Desktop\\report_dl.bat")

time.sleep(120)

today = datetime.datetime.utcnow().date()
yesterday = today - datetime.timedelta(days=1)
yesterday = yesterday.strftime("%d_%m_%y")

print("hey")

fromaddr = "cc.automation@swiggy.in"
# toaddr = "vd.gokkulkumar@swiggy.in,sourav.verma@swiggy.in,wfm-rte@swiggy.in"

toaddr = ['vd.gokkulkumar@swiggy.in', 'sourav.verma@swiggy.in','wfm-rte@swiggy.in']



# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
# msg['To'] = toaddr
msg['To'] = ", ".join(toaddr)

# storing the subject
msg['Subject'] = "SWOP dump (Automated email) " + yesterday

# string to store the body of the mail
body = "PFA"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "SWOP Dump "+yesterday+ ".csv"
attachment = open("C:\\Users\\" +user+ "\\Downloads\\getdata.csv", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "xcdbqpvdmzvckhwh")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

attachment.close()

# terminating the session
s.quit()



# os.system("C:\\Users\\"+user+"\\Desktop\\projects\\swop\\reset_db.bat")



os.rename(r'C:/Users/'+user+'/Downloads/getdata.csv',r'C:/Users/'+user+'/Downloads/getdata'+yesterday+'.csv')

shutil.move('C:/Users/'+user+'/Downloads/getdata'+yesterday+'.csv', 'C:/Users/sourav.verma/Desktop/projects/swop/dump/getdata'+yesterday+'.csv')