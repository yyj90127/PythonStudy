from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")

# 后台登录
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").clear()
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").clear()
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()

# 商品管理
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone12 pro max")
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
brand = driver.find_element_by_class_name("select")
Select(brand).select_by_value("1")
driver.find_element_by_name("is_hot").click()
driver.find_element_by_link_text("商品规格").click()
driver.find_element_by_name("_shop_price[0]").clear()
driver.find_element_by_name("_shop_price[0]").send_keys("10099.00")
driver.find_element_by_name("_market_price[0]").clear()
driver.find_element_by_name("_market_price[0]").send_keys("10899.00")
driver.find_element_by_name("_cost_price[0]").clear()
driver.find_element_by_name("_cost_price[0]").send_keys("8999.00")
driver.find_element_by_link_text("商品图册").click()
# driver.find_element_by_css_selector("#uploader .placeholder label[style]").click()
driver.find_element_by_name("file").send_keys("C:/Users/yuanyijun/Desktop/epolicy.jpg")
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())
result = driver.switch_to.alert.text
driver.switch_to.alert.accept()
if result == "上传成功":
    driver.find_element_by_class_name("button_search").click()
else:
    print("上传照片失败")