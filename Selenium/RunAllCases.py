import unittest2
from lib.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # unittest2.TextTestRunner().run(suite)
    # 海盗商城
    suite = unittest2.defaultTestLoader.discover('./test_case','Eshop*.py')
    # 京东
    # suite = unittest2.defaultTestLoader.discover('./test_case','JD*.py')
    path = './report/TestReport.html'
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1,title='自动化测试报告',description='测试环境：Chrome', tester = 'YYJ').run(suite)