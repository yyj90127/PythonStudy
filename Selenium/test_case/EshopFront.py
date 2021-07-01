import os
import sys
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
if PKG_DIR not in sys.path:
    sys.path.append(PKG_DIR)

import time
import unittest2
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from test_case.BaseTestCase import setUpClassAndtearDownClass


class Eship(setUpClassAndtearDownClass):
    def setUp(self):
        # 登录
        self.driver.get('http://localhost/index.php?m=user&c=public&a=login')
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("password")
        # self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/ul/li[5]/input").click()
        # 使用submit方法提交表单
        self.driver.find_element_by_id("username").submit()

    def tearDown(self):
        # 登出
        self.driver.find_element_by_link_text("[退出]").click()

    def test_shopping(self):
        # 进入商城购物
        self.driver.find_element_by_link_text("进入商城购物").click()

        # 搜索商品
        self.driver.find_element_by_name("keyword").send_keys("iphone")
        self.driver.find_element_by_class_name("btn1").click()
        self.driver.find_element_by_class_name("shop_01").click()

        # 切换窗口
        # 1、找到新窗口名字
        new_window = self.driver.window_handles[-1]
        # 2、切换到新窗口
        self.driver.switch_to.window(new_window)

        # 加入购物车
        self.driver.find_element_by_id("joinCarButton").click()

        # 去购物车结算
        self.driver.find_element_by_class_name("shopCar_T_span3").click()
        self.driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()

        # 添加新的收货地址
        self.driver.find_element_by_class_name("add-address").click()
        self.driver.find_element_by_name("address[address_name]").send_keys("测试")
        self.driver.find_element_by_name("address[mobile]").send_keys("13312345678")
        # 下拉框
        shen = self.driver.find_element_by_id("add-new-area-select")
        Select(shen).select_by_visible_text("上海市")
        shi = self.driver.find_elements_by_class_name("add-new-area-select")[1]
        Select(shi).select_by_visible_text("上海市")
        qu = self.driver.find_elements_by_tag_name("select")[2]
        Select(qu).select_by_index("8")
        self.driver.find_element_by_name("address[address]").send_keys("四川北路1234号123室")
        self.driver.find_element_by_name("address[zipcode]").send_keys("200021")
        self.driver.find_element_by_class_name("aui_state_highlight").click()

        time.sleep(1)
        # 断言：判断网页标题是否正确
        self.assertEquals("核对订单信息 - 道e坊商城 - Powered by Haidao",self.driver.title)

    def test_Personal(self):
        self.driver.find_element_by_link_text("账号设置").click()
        self.driver.find_element_by_partial_link_text("人资").click()
        self.driver.find_element_by_id("true_name").clear()
        self.driver.find_element_by_id("true_name").send_keys("测试")
        self.driver.find_element_by_css_selector("[value='1']").click()
        # 输入生日
        # 1、删除readonly属性(使用JavaScript语句)
        # JavaScript语句 = '通过id属性获取页面元素+删除指定属性'
        script = 'document.getElementById("date").removeAttribute("readonly")'
        # 执行JavaScript语句
        self.driver.execute_script(script)
        # 2、清空输入框的内容
        self.driver.find_element_by_id("date").clear()
        # 3、输入日期
        self.driver.find_element_by_id("date").send_keys("1990-02-02")
        self.driver.find_element_by_id("qq").clear()
        self.driver.find_element_by_id("qq").send_keys("40607222")
        # 点击确定
        self.driver.find_element_by_css_selector("[value='确认']").click()
        WebDriverWait(self.driver,30,0.5).until(expected_conditions.alert_is_present())
        update_status = self.driver.switch_to.alert.text
        print(update_status)
        self.driver.switch_to.alert.accept()

        time.sleep(1)
        # 断言：判断网页地址是否正确
        self.assertEquals(self.driver.current_url,"http://localhost/index.php?m=user&c=user&a=userinfo")
        # 断言：判断qq输入内容是否正确
        self.assertEquals("40607222",self.driver.find_element_by_id("qq").get_attribute('value'))
        # 断言：检查元素的文本
        self.assertEquals("QQ：",self.driver.find_element_by_css_selector('body > div.main.w1100 > div > div.content.fr > div.ziliao > dl > dd > ul > form > li:nth-child(6) > span').text)


if __name__ == '__main__':
    unittest2.main()