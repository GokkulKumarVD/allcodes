from datetime import datetime, timezone, date
import secrets
import string
import hashlib
import requests
import pandas as pd

def test_advanced_authentication(api_key_id):
    api_key = "X0PuJs0Ta5cCD4tp2aPGR39tipySTOn494SzCScWYSYndKMyJnGdRxQcsHIN0cIOyO98qBk5oNs6gMia6KvTmvzbaDnv0wLCXrzkutUjRymoj940sH975rJliNFx9tp8"

    # Generate a 64 bytes random string
    nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
    # Get the current timestamp as milliseconds.
    timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
    # Generate the auth key:
    auth_key = "%s%s%s" % (api_key, nonce, timestamp)
    # Convert to bytes object
    auth_key = auth_key.encode("utf-8")
    # Calculate sha256:
    api_key_hash = hashlib.sha256(auth_key).hexdigest()
    # Generate HTTP call headers
    headers = {
        "x-xdr-timestamp": str(timestamp),
        "x-xdr-nonce": nonce,
        "x-xdr-auth-id": str(12),
        "Authorization": api_key_hash,

    }
    data = {
        "request_data":{

        }
    }
    res = requests.post(url="https://api-swiggy.xdr.us.paloaltonetworks.com/public_api/v1/audits/agents_reports",
                        headers=headers,
                        json=data)

    json_data_here = res.json()

    for k, v in json_data_here.items():
        for ik, iv in v.items():
            if isinstance(iv, list):
                list_data = iv

    cortex_data = pd.DataFrame(list_data)

    cortex_data.to_csv("C:/Users/vd.gokkulkumar/Desktop/ss/cortex_versions.csv", index=False)
    return 0

# apikey = "X0PuJs0Ta5cCD4tp2aPGR39tipySTOn494SzCScWYSYndKMyJnGdRxQcsHIN0cIOyO98qBk5oNs6gMia6KvTmvzbaDnv0wLCXrzkutUjRymoj940sH975rJliNFx9tp8"

test_advanced_authentication(12)