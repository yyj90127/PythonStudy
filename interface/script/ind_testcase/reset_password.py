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


class interface_reset_password(object):
    def __init__(self):
        list = []
        table = readcsv('url')
        for i in table:
            list.append(i)
        self.interface_name = 'reset_password'
        self.URL = f'{list[0][0]}{self.interface_name}.do'
        self.request = requests.session()

    def getdata(self):
        list = []
        filename = self.interface_name+'_data.csv'
        table = readcsv('ind', filename)
        for i in table:
            list.append(i)
        return list

    def interface_test(self,i):
        url = self.URL
        data = {'passwordOld':i[0],
                'passwordNew':i[1]}
        request = self.request.post(url,data).json()
        return request


    def result(self):
        filename = self.interface_name+'_result.csv'
        filePath = PKG_DIR.replace('script', 'result/ind_result/'+filename)
        with open(filePath, 'w', encoding='utf-8') as f:
            for i in self.getdata():
                result = self.interface_test(i)
                if str(result).find('成功') > 0:
                    f.write(f'修改密码成功\n')
                else:
                    f.write(f'修改密码失败：{result["msg"]}\n')


if __name__ == '__main__':
    interface_reset_password().result()