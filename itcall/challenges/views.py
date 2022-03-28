from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# ----------------
#!/usr/bin/env python3
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd
import pymysql
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
import warnings
from datetime import datetime
import sys


# Create your views here.


def jan(request):
    warnings.simplefilter(action='ignore', category=FutureWarning)
    pd.set_option('mode.chained_assignment', None)

    # with open("/var/lakshya/rsa_key.p8", "rb") as key:
    with open("C:/Users/vd.gokkulkumar/Desktop/projects/rnr/rsa_key.p8", "rb") as key:
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
        #        database='STREAMS',
        # warehouse='NONTECH_WH_01',
        role='CC_AUTOMATION',
        # schema='CC_AUTOMATION_DATA_READER'
    )
    cs = ctx.cursor()
    # print(cs)

    raw_fetch = cs.execute(
        "SELECT b.ticketid ,b.AGENTEMAILID, to_timestamp(to_timestamp_ltz(b.AGENTASSIGNEDTIME)) assignment_time, queueid, "
        "max(c.EFFORTSCORE) as EFFORTSCORE FROM   STREAMS.PUBLIC.ASSIGN_AGENT b "
        "left join ( Select AGENTEMAILID, EFFORTSCORE, agentid, conversationid, chattype "
        "from STREAMS.PUBLIC.COLLECT_CSAT c where c.effortscore!=-99 "
        "and c.dt >= cast(timeadd('day', -1, CURRENT_DATE) AS varchar) ) c "
        "ON c.conversationid=b.conversationid AND "
        "c.agentid=b.agentid AND c.chattype='agent' "
        "WHERE (b.queueid ilike '%l2%' or b.queueid ilike '%priority%' or b.queueid ilike '%stores%' or b.queueid ilike '%genie%' "
        "or b.queueid ilike '%bau-cancellation%' or b.queueid ilike '%bau-couponrelated%' or b.queueid ilike '%bau-foodissues%' "
        "or b.queueid ilike '%bau-food-special-instruction%' or b.queueid ilike '%bau-orderstatus%' or b.queueid ilike '%bau-paymentrelated%' "
        "or b.queueid ilike '%delivery-instructions%' or b.queueid ilike '%fallback%' or b.queueid ilike '%general-issue%' or b.queueid ilike '%meat%' or b.queueid ilike '%team-1%'"
        ") and b.orgid = 'swiggy' and "
        "b.AGENTEMAILID != 'NOTFILLED' and b.AGENTASSIGNEDTIME between 1629682200 and 1629768540  group by 1,2,3,4;")

    surveys = pd.DataFrame(raw_fetch)
    surveys.columns = ['Ticketid', 'AGENTEMAILID',
                       'TIME_STAMP', 'Queue', 'EFFORTSCORE']
    surveys = surveys[['AGENTEMAILID',
                       'EFFORTSCORE', 'TIME_STAMP', 'Queue']]

    q_surveys = surveys[['AGENTEMAILID', 'Queue']]

    surveys.to_csv(
        "C:/Users/vd.gokkulkumar/Desktop/projects/rnr/testingpython.csv")

    return HttpResponse("it works!")


def feb(request):
    return HttpResponse("february")

# def index(request, month):
#     if month == "januaryindex":
#         monthtext = ("calling jan month")
#     elif month == "februaryindex":
#         monthtext = ("calling february")
#     elif month == "marchindex":
#         monthtext = ("calling march")
#     else:
#         return HttpResponseNotFound("this month is not yet available")
#     return HttpResponse(monthtext)


# Instead of above if conditions, we can use dictionary
challenges_months = {
    "januaryindex": "calling jan month",
    "februaryindex": "calling feb month",
    "marchindex": "calling march month",
    "aprilindex": "calling april",
    "mayindex": "mayindex",
    "juneindex": "juneindex",
    "julyindex": "julyindex",
    "augustindex": "augustindex",
    "septemberindex": "septemberindex",
    "octoberindex": "octoberindex",
    "novemberindex": "novemberindex",
    "decemberindex": None
}


def index(request, month):
    try:
        task = challenges_months[month]
        # return HttpResponse(task)
        # ---------------------------------
        # redirecthtml = render_to_string("challenges/challenge.html")
        # return HttpResponse(redirecthtml)
        # --------------------------------
        return render(request, "challenges/challenge.html", {
            "task": task,
            "month_name" : month
        })
    except:
        return HttpResponseNotFound("page not found")


def indexnum(request, month):
    month_name = list(challenges_months.keys())
    month_name_index = month_name[month - 1]
    # /challenges/month_name
    redirect_month = reverse("mm", args=[month_name_index])
    # return HttpResponseRedirect("/challenges/" + month_name_index)
    return HttpResponseRedirect(redirect_month)


def mainpage(request):
    # list_month = ""
    months = list(challenges_months.keys())

    # for month in months:
    #     redirect_month = reverse("mm", args=[month])
    #     list_month += f"<li><a href='{redirect_month}'>{month.capitalize()}</a></li>"

    # redirecting = f"<ul>{list_month}</ul>"

    # return HttpResponse(redirecting)

    return render(request, "challenges/index.html", {
        "months":months
    })


def monthly_challenge(request, month):
    challenge_months = monthly_challenge[month]
    redirecthtml = render_to_string("challenges/challenge.html")
    return HttpResponseRedirect(redirecthtml)
