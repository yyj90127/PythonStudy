import random
import time

import requests

class get_iphone():
    def __init__(self):
        pass

    def get_pro(self):
        url = "https://www.apple.com.cn/shop/fulfillment-messages?pl=true&mt=compact&parts.0=MLTE3CH/A&searchNearby=true&store=R574"
        res = requests.get(url).json()
        num = len(res["body"]["content"]["pickupMessage"]["stores"])
        # print("pro:")
        for i in range(2,num-3):
            storeName = res["body"]["content"]["pickupMessage"]["stores"][i]["storeName"]
            pickupSearchQuote = res["body"]["content"]["pickupMessage"]["stores"][i]["partsAvailability"]["MLTE3CH/A"]["pickupSearchQuote"]
            if pickupSearchQuote != "暂无供应":
                print(storeName+":"+pickupSearchQuote)

    def get_pro_max(self):
        url = "https://www.apple.com.cn/shop/fulfillment-messages?pl=true&mt=compact&parts.0=MLHC3CH/A&searchNearby=true&store=R574"
        res = requests.get(url).json()
        num = len(res["body"]["content"]["pickupMessage"]["stores"])
        print("pro_max:")
        for i in range(2,num-3):
            storeName = res["body"]["content"]["pickupMessage"]["stores"][i]["storeName"]
            pickupSearchQuote = res["body"]["content"]["pickupMessage"]["stores"][i]["partsAvailability"]["MLHC3CH/A"]["pickupSearchQuote"]
            if pickupSearchQuote != "暂无供应":
                print(storeName+":"+pickupSearchQuote)


if __name__ == '__main__':
    obj = get_iphone()
    while True:
        obj.get_pro()
        # obj.get_pro_max()
        time.sleep(2)