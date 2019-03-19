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

print("当前网络模式为：", driver.network_connection)

# value                Data/ Wifi/ Airplane Mode
# 0 None                 0 /  0  /   0
# 1 Airplane Mode        0 /  0  /   1
# 2 Wifi only            0 /  1  /   0
# 4 Data only            1 /  0  /   0
# 6 All network on       1 /  1  /   1

driver.set_network_connection(4)

print("当前网络模式为：", driver.network_connection)

time.sleep(3)

driver.quit()