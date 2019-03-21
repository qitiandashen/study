import requests
import json


base_url = 'http://192.168.2.7:8088/bill/addBill?login_token=b10a810f84810b8e4dfe0a46ffdd6101'
body = {"amount": "44",
            "contractId": "75",
            "deadLineTime": "1540915200000",
            "details": "liukang",
            "endTime": "1539273600000",
            "startTime": "1539100800000",
            "type": "0"}
headers = {'content-type': 'application/json '}
response = requests.post(base_url, data=json.dumps(body), headers=headers)

print(response.status_code)
print(response.text)


