import os
import requests

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))

import sys
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

from interface.tools.csvmanager import readcsv

# 针对多个接口联调测试
class workflow_updateInformation():
    def __init__(self):
        list = []
        table = readcsv('url')
        for i in table:
            list.append(i)
        self.BaseURL = f'{list[0][0]}'
        self.request = requests.session()

    # 读取文件
    def getdata(self):
        list = []
        table = readcsv('mul', 'update_Information_data.csv')
        for i in table:
            list.append(i)
        return list

    # 1、用户注册
    def test_register(self,i):
        url = self.BaseURL+"register.do"
        data = {'username':i[0],
                'password':i[1],
                'email':i[2],
                'phone':i[3],
                'question':i[4],
                'answer':i[5]}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户”{i[0]}“注册成功'
        else:
            return f'用户”{i[0]}“注册失败'

    # 2、用户登录
    def test_login(self,i):
        url = self.BaseURL+"login.do"
        data = {'username':i[0],'password':i[1]}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"登录成功'
        else:
            return f'用户"{i[0]}"登录失败'

    # 3、获取用户信息
    def test_getInformation(self,i,round):
        url = self.BaseURL+"get_information.do"
        data = {}
        request = self.request.post(url,data=data).json()
        result = (request['status'])
        if round == 1:
            if result == 0:
                return f'用户"{request["data"]["username"]}"个人信息为：{request["data"]}'
            else:
                return f'获取用户"{i[0]}"个人信息失败'
        else:
            if result == 0 and request['data']['email'] == i[6] and request['data']['phone'] == i[7] and request['data']['question'] == i[8] and request['data']['answer'] == i[9]:
                return f'用户"{request["data"]["username"]}"更新后的个人信息为：{request["data"]}'
            elif result == 0:
                return f'用户"{i[0]}"更新个人信息失败'
            else:
                return f'获取用户"{i[0]}"个人信息失败'


    # 4、修改个人信息
    def test_updateInformation(self,i):
        url = self.BaseURL + "update_information.do"
        data = {'email': i[6],
                'phone': i[7],
                'question': i[8],
                'answer': i[9]}
        request = self.request.post(url, data=data).json()
        result = (request['status'])
        if result == 0:
            return f'用户"{i[0]}"修改个人信息成功'
        else:
            return f'用户"{i[0]}"修改个人信息失败'



    def run(self):
        filePath = PKG_DIR.replace('script', 'result/mul_result/update_Information_result.csv')
        with open(filePath,'w',encoding='utf-8') as f:
            for i in self.getdata():
                f.write(self.test_register(i)+'\n'+
                        self.test_login(i)+'\n'+
                        self.test_getInformation(i,1)+'\n'+
                        self.test_updateInformation(i)+'\n'+
                        self.test_getInformation(i,2)+'\n'+
                        '\n')



if __name__ == '__main__':
    obj = workflow_updateInformation()
    obj.run()


