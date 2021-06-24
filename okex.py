# coding=utf-8
import requests
import urllib3
import json
import time


class Stock(object):

    def __init__(self, coin, highPrice, lowPrice, sleepTime = 1):
        self.coin = coin
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.sleepTime = sleepTime

    def getStock(self):
        url = "https://www.okexcn.com/v2/spot/markets/ticker?symbol=" + self.coin + "_usdt&t=" + str(round(time.time() * 1000))
        urllib3.disable_warnings()
        res_post = requests.Session().get(url).json()
        return res_post["data"]["last"]

    def printInfo(self):
        while True:
            if float(self.getStock()) >= self.highPrice:
                print("可抛售！！！！！")
            if float(self.getStock()) <= self.lowPrice:
                print("可买入！！！！！")
            else:
                print('{}{} = {}'.format(self.coin,"_usdt",self.getStock()))
                time.sleep(self.sleepTime)

if __name__ == "__main__":
    # 币种，卖出价，买入价，间隔时间
    Stock('btc',60000,46000,3).printInfo()

