import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import pandas as pd

pd.set_option('display.max_columns',500)

with open("C:/Users/vd.gokkulkumar/Desktop/snowkey/rsa_key.p8", "rb") as key:
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


startdate =1641839400
enddate =1641925800
greaterthan =20
lesserthan =300
numbercalls =10




sqlq = "select * from STREAMS.PUBLIC.TELEPHONY_DP_CALL_LOG_EVENT where CALL_RECORDING_URL ilike '%airtel%' and CALL_ATTEMPTED_AT between {} and {} and ( CALL_DURATION between {} and {}  OR CALL_DURATION is NULL) limit {} ".format(
    startdate, enddate, greaterthan, lesserthan, numbercalls)

raw_fetch = cs.execute(sqlq)

df = pd.DataFrame(raw_fetch)

print(df)