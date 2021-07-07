# coding=utf-8
import csv
import requests


class interface_test(object):
    def __init__(self):
        pass

    def readcsv(self):
        list = []
        filePath = r'D:\Script\python\study\interface\interface_test\1.csv'
        with open(filePath,'r') as f:
            table = csv.reader(f)
            i = 0
            for row in table:
                if i == 0:
                    pass
                else:
                    list.append(row)
                i = i+1
        return list


    def login(self):
        for i in self.readcsv():
            url = 'http://localhost:8081/jwshoplogin/user/login.do'
            data = {'username':i[0],'password':i[1]}
            request = requests.post(url,data).text
            result = request.find(i[2])
            filePath = r'D:\Script\python\study\interface\interface_test\2.csv'
            with open(filePath,'a') as f:
                if result>0:
                    f.write(f'{i[0]},{i[1]},{i[2]},pass\n')
                else:
                    f.write(f'{i[0]},{i[1]},{i[2]},failed\n')


if __name__ == '__main__':
    interface_test().login()


