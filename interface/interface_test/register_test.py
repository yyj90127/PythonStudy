import requests
from interface.tools.csvmanager import readcsv


class register_test():
    def __init__(self):
        self.url = 'http://localhost:8081/jwshoplogin/user/register.do'

    def test_register(self):
        for i in self.getdata():
            data = {'username':i[0],
                     'password':i[1],
                     'email':i[2],
                     'phone':i[3],
                     'question':i[4],
                     'answer':i[5]}
            request = requests.session().post(self.url,data=data).json()
            print(request)


    def getdata(self):
        list = []
        table = readcsv('register_data.csv')
        for i in table:
            list.append(i)
        return list



if __name__ == '__main__':
    obj = register_test()
    obj.test_register()