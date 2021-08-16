import os
import time
from appium.webdriver.webdriver import WebDriver
from tools.csvReader import readcsv

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
filename = "calculator_result.csv"
filepath = PKG_DIR+"/result/"+filename

# 删除已存在的结果
if os.path.exists(filepath):
    os.remove(filepath)

# 定义一个字典类型，存放参数设置
caps={
    'automationName':'UiAutomator2',
    'platformName':'Android',
    'platformVersion':'8.0',
    'deviceName':'28d2e631',
    'appPackage':'com.miui.calculator',
    'appActivity':'.cal.CalculatorActivity'
}
driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# 使用真机操作时存在延迟，需要在界面打开后设置一个等待时间
time.sleep(5)

# 读取文件
table = readcsv("calculator_data.csv")
with open(filepath,"a") as f:
    for i in table:
        a = i[0]
        b = i[1]
        c = i[2]
        #传入相关测试数据
        driver.find_element_by_id('com.miui.calculator:id/btn_c_s').click()
        driver.find_element_by_id(f'com.miui.calculator:id/btn_{a}_s').click()
        driver.find_element_by_id('com.miui.calculator:id/btn_plus_s').click()
        driver.find_element_by_id(f'com.miui.calculator:id/btn_{b}_s').click()
        driver.find_element_by_id('com.miui.calculator:id/btn_equal_s').click()
        #获取运行结果
        time.sleep(2)
        result=driver.find_element_by_id('com.miui.calculator:id/result').text
        #进行结果比对

        if result.find(str(c)) != -1:
            f.write(f"{a}+{b}测试通过"+'\n')
        else:
            f.write(f"{a}+{b}测试失败"+'\n')
    driver.quit()