import os

from appium import webdriver

import time

# desired_caps为字典格式 - 常用参数：
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}

# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(3)
# 定位到存储菜单栏
el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 下拉菜单
driver.drag_and_drop(el1, el2)

time.sleep(2)
driver.find_element_by_xpath("//*[@text='安全']").click()

driver.find_element_by_xpath("//*[@text='屏幕锁定方式']").click()
driver.find_element_by_xpath("//*[@text='图案']").click()
time.sleep(1)

# 绘制“Z”字
TouchAction(driver).press(x=120, y=440).move_to(x=480, y=0).move_to(x=-480, y=460).move_to(x=480, y=0).perform()


time.sleep(3)
driver.quit()