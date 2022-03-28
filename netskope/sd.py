import requests
url = "https://swiggygs.goskope.com/api/v1/clients"

# payload = "client_id%0A=###################&redirect_uri=#################%2F&client_secret=##############&code={}&grant_type=authorization_code&undefined=".format(code)

headers = {
    'token': "06b13f570337d098c143b6a96bb76743"
    }

response = requests.request("POST", url, headers=headers)
print(response.text)
