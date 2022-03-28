import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import ast
import csv
import mysql.connector
import pandas as pd
import json
from datetime import datetime, timezone

clientId = "b1a1f1ad8a0048b0904abd3bd34fed4a"
clientSecret = "X647FHMqqrMgv_7ODWpdgqVWAyGmGv4ZQdpf8QT2YWk"
clientAuth = HTTPBasicAuth(clientId, clientSecret)
username = "apiadmin"
userpassword = "^jZ2wv7%^ESc"

payload = "grant_type=password&username=" + username + "&password=" + userpassword
tokenURL = "https://s116350.mobicontrolcloud.com/MobiControl/api/token"
headers = {"Content-Type": "application/json"}
r = requests.post(tokenURL, headers=headers,  auth=clientAuth, data=payload)
dat = r.json()
token = dat['access_token']

token_b = "\"Bearer  " + token + "\""

print("{\"Authorization\":" + token_b)

Headers = "{\"Authorization\":" + token_b + "}"
Headers = ast.literal_eval(Headers)

url = "https://s116350.mobicontrolcloud.com/MobiControl/api/devices?take=10000"

response = requests.get(
          url,
          headers=Headers
        )

jsondata = response.json()

# new lines
with open('data.json', 'w') as f:
    json.dump(jsondata, f)

df = pd.read_json(r"C:/Users/vd.gokkulkumar/PycharmProjects/forit/data.json")


# data_file = open('C:/Users/vd.gokkulkumar/Desktop/ss/soti_data_check.csv', 'w', newline='')
# csv_writer = csv.writer(data_file)
#
# count = 0
# for data in jsondata:
#     if count == 0:
#         header = data.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(data.values())
#
# data_file.close()
#
# df = pd.read_csv("C:/Users/vd.gokkulkumar/Desktop/ss/soti_data_check.csv", encoding="cp1251")

df.to_csv("C:/Users/vd.gokkulkumar/Desktop/ss/st.csv", index=False)

df=pd.read_csv("C:/Users/vd.gokkulkumar/Desktop/ss/st.csv")

df.replace(to_replace=',', value='-', inplace=True)
df.replace(',','.', regex=True, inplace=True)
df.replace(to_replace= r'\\', value= '', regex=True, inplace=True)
# df.replace(to_replace='[]', value='-', regex=True, inplace=True)
df.fillna('0', inplace=True)
df['CellularTechnology'] = df['CellularTechnology'].astype(str)


def convert_timeformat(x):
    if x == '0':
        return '0'
    else:
        return pd.to_datetime(x)


df['LastAgentDisconnectTime'] = df['LastAgentDisconnectTime'].apply(convert_timeformat)


hr = df[~(df['LastAgentDisconnectTime'] == '0')]
notime = df[df['LastAgentDisconnectTime'] == '0']

utc_dt = datetime.now(timezone.utc)
dt = utc_dt.astimezone()
y = pd.to_datetime(dt)

active24 = hr[hr['LastAgentDisconnectTime'] >= y - pd.Timedelta(hours=24)]
active24['on'] = 'active_within_24hours'

deactive24 = hr[hr['LastAgentDisconnectTime'] < y - pd.Timedelta(hours=24)]
deactive24['on'] = 'inactive_within_24hours'

notime['on'] = 'inactive_within_24hours'

all = pd.concat([active24, deactive24, notime], axis=0)


all = all[["$type","AndroidForWork","BuildVersion","CellularTechnology","UserIdentities","AndroidAccountType","SafetynetAttestationStatus","AgentUpgradeEnabled","AgentVersion","PlugInVersion","AndroidApiLevel","AndroidDeviceAdmin","AndroidRcLibraryVersion","Antivirus","AsuLevel","Memory","BatteryStatus","CanResetPassword","CellularCarrier","CellularSignalStrength","CustomData","DeviceTerms","DeviceUserInfo","MultiUserDeviceInfo","ExchangeBlocked","ExchangeAccessRequest","ExchangeStatus","HardwareEncryptionCaps","HardwareEncryption","HardwareSerialNumber","MobileSerialNumber","HardwareVersion","ICCID","IMEI_MEID_ESN","InRoaming","IntegratedApplications","Ipv6","IsAgentCompatible","IsAgentless","IsEncrypted","IsOSSecure","LastCheckInTime","LastAgentConnectTime","LastAgentDisconnectTime","LastLoggedOnUser","NetworkBSSID","NetworkConnectionType","NetworkRSSI","NetworkSSID","OEMVersion","PasscodeEnabled","PasscodeStatus","PersonalizedName","PhoneNumber","SEForAndroidStatus","SelectedApn","SubscriberNumber","SupportedApis","EFOTAFirmwareVersion","CarrierCode","DeviceFirmwareUpgrade","BuildSecurityPatch","LifeGuardVersion","Elm","IsCharging","MXVersion","AndroidEnterpriseMigrationStatus","UserAccountsCount","ExchangeOnlineEmailAccess","IsAdminModeEnabled","TimeZone","Kind","CompliancePolicyStatus","ComplianceStatus","ComplianceItems","DeviceId","DeviceName","EnrollmentType","EnrollmentTime","Family","HostName","IsAgentOnline","CustomAttributes","MACAddress","BluetoothMAC","WifiMAC","Manufacturer","Mode","Model","OSVersion","Path","Platform","ServerName","on"]]

all.to_csv("C:/Users/vd.gokkulkumar/Desktop/ss/soti_data_check.csv", index=False)

# -------- data base
con = mysql.connector.connect(
    host='172.16.251.114',
    user='it-db-osp',
    passwd='p@S$w0rdf0rg)kku(S38fd()hH',
    database='sd_ae',
    allow_local_infile=True
)
cursor = con.cursor()

cursor.execute("delete from sd_ae.soti_data")
con.commit()



stmt = """LOAD DATA LOCAL INFILE 'C:/Users/vd.gokkulkumar/Desktop/projects/grafana_soti_cron/soti_data_check.csv' INTO TABLE sd_ae.soti_data
            FIELDS TERMINATED BY ',' 
            LINES TERMINATED BY '\r\n'
            IGNORE 1 LINES
        """

cursor.execute(stmt)
con.commit()

cursor.close()
con.close()

# df['LastAgentDisconnectTime'].replace('T',' ', regex=True, inplace=True)
# df['LastAgentDisconnectTime'].replace('Z','', regex=True, inplace=True)

