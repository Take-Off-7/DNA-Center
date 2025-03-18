import requests
import json

#################### LOGIN ####################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(
    url,
    auth=(user,pw),
    verify=False
).json()
# print(response)

token = response['Token']
# print(token)

#################### GET CLIENT STATS ####################

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

querystring = {'timestamp':""}

headers = {'x-auth-token': token}

response = requests.get(
    url,
    headers=headers,
    params=querystring,
    verify=False
).json()

# print(json.dumps(response, indent=2, sort_keys=True))

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'ALL':
        print(f"Clients: {score['clientCount']}")

    elif score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")

    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")
