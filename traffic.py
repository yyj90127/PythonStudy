# coding=utf-8
import requests
import urllib3
import math
import datetime
import clipboard
import ui

class traffic(object):

    def __init__(self, name, lineid, stopid, direction):
        self.name = name
        self.lineid = lineid
        self.stopid = stopid
        self.direction = direction

    def getBusInfo(self):
        urllib3.disable_warnings()
        url = "http://apps.eshimin.com/traffic/gjc/getArriveBase?name={}&lineid={}&stopid={}&direction={}".format(self.name, self.lineid, self.stopid, self.direction)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"}
        res_post = requests.get(url, headers=headers).json()
        if len(res_post) == 0:
            return self.lineid[1:4]+"路尚未发车"
        else:
            # 距离X站
            stopdis = res_post["cars"][0]["stopdis"]
            # 距离X米
            distance = res_post["cars"][0]["distance"]
            # 车牌号
            pterminal = res_post["cars"][0]["terminal"]
            # 还剩X分钟
            time = math.floor(int(res_post["cars"][0]["time"])/60)
            return ("{}路还有{}站，预计{}分钟后到，达距离{}米。".format(self.lineid[1:4],stopdis,time,distance))

if __name__ == '__main__':
    if datetime.datetime.now().hour > 14:
        toHome733 = traffic("733%E8%B7%AF","073300","13","1").getBusInfo()
        toHome932 = traffic("932%E8%B7%AF", "093200", "19", "0").getBusInfo()
        print(toHome733+"\n"+toHome932)
        clipboard.copy(toHome733+"\n"+toHome932)
    else:
        toCompany720 = traffic("720%E8%B7%AF","072000","18","1").getBusInfo()
        toCompany733 = traffic("733%E8%B7%AF","073300","2","0").getBusInfo()
        toCompany932 = traffic("932%E8%B7%AF","093200","3","1").getBusInfo()
        toCompany56 = traffic("56%E5%8C%BA%E9%97%B4", "005680", "7", "1").getBusInfo()
        print(toCompany720+"\n"+toCompany733+"\n"+toCompany932+"\n"+toCompany56)
        clipboard.copy(toCompany720+"\n"+toCompany733+"\n"+toCompany932+"\n"+toCompany56)

    v = ui.load_view()
    v.present("sheet")