from django.shortcuts import render
from django.http import HttpResponse

import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import pandas as pd
import os.path
import getpass
import os
import requests

# Create your views here.
def downloader(request):
    username = getpass.getuser()
    download_location = "C:/Users/"+username+"/Desktop/call_logs"


    def fetching():
        # snowflakes fetching data
        try:
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
            raw_fetch = cs.execute("""select * from STREAMS.PUBLIC.TELEPHONY_DP_CALL_LOG_EVENT where CALL_RECORDING_URL ilike '%airtel%' limit 5""")
            pd.set_option('display.max_columns',500)
            df = pd.DataFrame(raw_fetch)
            try:
                df.columns=['CALL_ATTEMPTED_AT','CALL_DIRECTION','CALL_RECORDING_URL','CALL_STATUS','CLIENT_FLOW_ID','CLIENT_FLOW_TYPE',
                            'CLIENT_ID','CLIENT_REQUEST_ID','CUSTOM_HANGUP_STATUS','REQUEST_CREATED_AT','UNREGISTERED_NUMBER','VENDOR_CALL_ID',
                            'VENDOR_ID','VIRTUAL_NUMBER','TIME_STAMP','UUID','EVENT_ID','SCHEMA_VERSION','DT']
                fetch = True
            except:
                fetch = False

            # if it is fetched successfully go next
            if fetch == True:
                call_list = df['CALL_RECORDING_URL'].to_list()
                n = 0
                for i in call_list:
                    # webbrowser.open(i)
                    n = n+1
                    print(i)

                    def download(url: str, dest_folder: str):
                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)  # create folder if it does not exist


                        filename = str(n)+".mp3"  # file names
                        file_path = os.path.join(dest_folder, filename)

                        r = requests.get(url, stream=True)
                        if r.ok:
                            print("saving to", os.path.abspath(file_path))
                            with open(file_path, 'wb') as f:
                                for chunk in r.iter_content(chunk_size=1024 * 8):
                                    if chunk:
                                        f.write(chunk)
                                        f.flush()
                                        os.fsync(f.fileno())
                        else:
                            print("Download failed: status code {}\n{}".format(r.status_code, r.text))

                    download(i, dest_folder=download_location)
            # if did not fetch
            else:
                return HttpResponse("Data not found!")
        except Exception as err:
            return HttpResponse("There is some technical glitch. Please contact IT team")


    fetching()

    return HttpResponse("Fetched all the details")
