# -*- coding: UTF-8 -*-
import requests
from lxml import etree

class pachong(object):
    def __init__(self,fileName,endPage,):
        self.fileName = fileName
        self.endPage = endPage

    def openUrl(self):
        url = "http://10.253.76.148:5000/tool/getASignTool"
        res = requests.get(url)
        res.encoding = 'gbk'
        doc = etree.HTML(res.text)
        ele = doc.xpath('*//text()')
        print(ele)

    def requests(self):
        url = "http://10.253.76.148:5000/tool/getASignTool"
        cookies = {
            "remember_token" : "12|25fbe29b4348392d0c2634ce782e0aa0e4f63b1fd875a517c24b16ad0d577633aca14309f0471192c09c82a185b9f3498f71520dd3ac8a49e436d640876c0132",
            "session" : "eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiMzZjNDFmMjNmMDU4M2UzNzAyZjBiMzNlYjQ2ZGUwMjI5OWY0ZmU2YyIsInVzZXJfaWQiOiIxMiJ9.YMLK0A.XJ3IV5AmLs1pA1Ao3NV4023ZXaM"
        }
        headers = {
            "Content-Type": "multipart/form-data"
        }
        form_data = {
            "csrf_token": "IjM2YzQxZjIzZjA1ODNlMzcwMmYwYjMzZWI0NmRlMDIyOTlmNGZlNmMi.YMLSwQ.dPMUDD747-FZgT7UlkHLBzCWvPQ",
            "accountId": 11111,
            "baseUrl":"",
            "testFile": "(binary)",
            "asBut": "去加签"
        }
        res = requests.post(url, cookies=cookies, data=form_data, headers=headers)
        ele = etree.HTML(res.text).xpath("/html/body/div/div/main/div[2]/div[2]/ul/li/div/div/text()")[0]
        print(ele)

if __name__ == '__main__':
    a = pachong('C:/Users/yuanyijun/Desktop/爬虫.txt',10)
    a.openUrl()
    # a.requests()