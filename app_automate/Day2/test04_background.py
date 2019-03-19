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

# 将app置于后台5s，再展现于前台
driver.background_app(5)

time.sleep(3)
driver.quit()