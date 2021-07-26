# coding=utf-8
import csv
import os
import requests

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from interface.tools.csvmanager import readcsv


class interface_get_information(object):
    def __init__(self):
        list = []
        table = readcsv('url')
        for i in table:
            list.append(i)
        self.interface_name = 'get_information'
        self.URL = f'{list[0][0]}{self.interface_name}.do'
        self.request = requests.session()

    def interface_test(self):
        url = self.URL
        data = {}
        request = self.request.post(url,data).json()
        return request


    def result(self):
        filename = self.interface_name+'_result.csv'
        filePath = PKG_DIR.replace('script', 'result/ind_result/'+filename)
        with open(filePath, 'w', encoding='utf-8') as f:
            result = self.interface_test()
            if str(result).find('id') > 0:
                f.write(f'获取用户个人信息成功，信息为：{result["data"]}\n')
            else:
                f.write(f'获取用户个人信息失败：{result["msg"]}\n')


if __name__ == '__main__':
    interface_get_information().result()