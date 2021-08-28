import os
import time
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tools.csvReader import readcsv

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
filename = "calculator_result.csv"
filepath = PKG_DIR+"/result/"+filename

# 删除已存在的结果
if os.path.exists(filepath):
    os.remove(filepath)

class cal():
    def __init__(self):
        # 定义一个字典类型，存放参数设置
        self.caps={
            'automationName':'UiAutomator2',
            'platformName':'Android',
            'platformVersion':'8.0',
            'deviceName':'28d2e631',
            'appPackage':'com.miui.calculator',
            'appActivity':'.cal.CalculatorActivity'
        }
        self.driver=WebDriver('http://127.0.0.1:4723/wd/hub',self.caps)
        # 使用真机操作时存在延迟，需要在界面打开后设置一个等待时间


    def cal(self):
        # 读取文件
        table = readcsv("calculator_data.csv")
        with open(filepath,"a") as f:
            for i in table:
                x = i[0]
                func = i[1]
                y = i[2]
                res = i[3]
                #传入相关测试数据
                WebDriverWait(self.driver,30,0.5).until(expected_conditions.visibility_of_element_located((By.ID,'com.miui.calculator:id/btn_c_s'))).click()
                self.driver.find_element_by_id(f'com.miui.calculator:id/btn_{x}_s').click()
                if func == "+":
                    self.driver.find_element_by_id('com.miui.calculator:id/btn_plus_s').click()
                elif func == "-":
                    self.driver.find_element_by_id('com.miui.calculator:id/btn_minus_s').click()
                elif func == "*":
                    self.driver.find_element_by_id('com.miui.calculator:id/btn_mul_s').click()
                elif func == "/":
                    self.driver.find_element_by_id('com.miui.calculator:id/btn_div_s').click()
                self.driver.find_element_by_id(f'com.miui.calculator:id/btn_{y}_s').click()
                self.driver.find_element_by_id('com.miui.calculator:id/btn_equal_s').click()
                #获取运行结果
                time.sleep(2)
                result=self.driver.find_element_by_id('com.miui.calculator:id/result').text
                #进行结果比对

                if result.find(str(res)) != -1:
                    f.write(f"{x}{func}{y}{result} 测试通过"+'\n')
                else:
                    f.write(f"{x}{func}{y}{result} 测试失败"+'\n')
        self.driver.quit()



if __name__ == '__main__':
    cal().cal()