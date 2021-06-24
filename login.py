#-- coding:UTF-8 --

import requests
import urllib3
import json

url = "https://api-test.firstbx.com/europa/open/v1/saas/login"

data = {
    "userName":"13482780523",
    "password":"yyj90127",
    "code":"888888",
    "remember": True
}

header = {
    "Connection":"keep-alive",
    "Content-Length":"80",
    "accept":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "content-type":"application/json",
    "Origin":"https://saas-test.firstbx.com",
    "Sec-Fetch-Site":"same-site",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://saas-test.firstbx.com/m/user",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9"
}
# header = {'Connection': 'close', }

urllib3.disable_warnings()
res = requests.post(url, json=data, headers = header, verify=False).json()
print(json.dumps(res,indent=4,ensure_ascii=False))