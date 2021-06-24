# coding=utf-8
import requests
import urllib3
import json
import datetime
import time
import itchat


def getStock():
    url = "https://hq.sinajs.cn/?_=0.07226633222210399&list=sh600271"
    urllib3.disable_warnings()
    res_post = requests.get(url).text
    if res_post[40:45] < "12.00":
        print(res_post[40:45] + "  " + time_now)
    # print(time_now)
    pass

def wechat():
    pass

if __name__ == "__main__":
    while True:
        time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')  # 刷新
        if "09:30:00.000000" <= time_now <= "11:30:00.000000" or "13:00:00.000000" <= time_now <= "15:00:00.000000":
            getStock()
            # wechat()
            time.sleep(10)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
        else:
            # print(time_now)
            time.sleep(300)