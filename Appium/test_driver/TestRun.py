# 使用HTMLTestRunner生成测试报告
import unittest
from tools.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('../script','workflow*.py')
    path = '../result/TestReport.html'
    with open(path,'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title='自动化测试报告', description='测试环境：Chrome', tester = 'YYJ').run(suite)