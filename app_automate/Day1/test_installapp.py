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

# 使用两台模拟机时通过udid区分不同设备，adb devices查看设备号填入即可
# desired_caps['udid'] = ''
# 不重置应用
desired_caps['noReset'] = True

# 通过启动参数安装apk



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

# driver.close_app()

# 安装腾讯新闻app, 腾讯新闻安装包名tengxunxinwen_5610.apk
driver.install_app(os.getcwd()+os.sep+"tengxunxinwen_5610.apk")

driver.quit()