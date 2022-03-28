# https://api-swiggy.xdr.us.paloaltonetworks.com

# X0PuJs0Ta5cCD4tp2aPGR39tipySTOn494SzCScWYSYndKMyJnGdRxQcsHIN0cIOyO98qBk5oNs6gMia6KvTmvzbaDnv0wLCXrzkutUjRymoj940sH975rJliNFx9tp8


import requests

def test_standard_authentication(api_key_id, api_key):
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key
    }
    parameters = {}
    request_data = {}
    res = requests.post(url="https://api-swiggy.xdr.us.paloaltonetworks.com/public_api/v1/endpoints/get_endpoints",
                        headers=headers,
                        json=parameters)
    data = res.json()
    print(data)
    return res

apikey = "X0PuJs0Ta5cCD4tp2aPGR39tipySTOn494SzCScWYSYndKMyJnGdRxQcsHIN0cIOyO98qBk5oNs6gMia6KvTmvzbaDnv0wLCXrzkutUjRymoj940sH975rJliNFx9tp8"

test_standard_authentication(12, apikey)