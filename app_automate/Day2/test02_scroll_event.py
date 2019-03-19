import os

from appium import webdriver
import time

# desired_caps为字典格式 - 常用参数：
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

el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")

el2 = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# driver.swipe(450, 1000, 450, 600)
driver.scroll(el2, el1)

time.sleep(3)
driver.quit()