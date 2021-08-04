import os
import unittest2
from result.HTMLTestRunner import HTMLTestRunner
from tools.csvmanager import readcsv

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))


if __name__ == '__main__':
    table = readcsv('config','测试框架配置文件.csv')
    table.sort(key = lambda item:item[0])
    for i in table:
        if i[3] == 'Y':
            suite = unittest2.defaultTestLoader.discover(f'..{i[1]}',f'{i[2]}')
            filePath = CUR_DIR.replace('test_driver','result/mul_result/register_result.html')
            with open(filePath,'wb') as file:
                HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester='YYJ').run(suite)