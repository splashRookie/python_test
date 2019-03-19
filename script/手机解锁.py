import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def tap_screen(x,y):
    os.system('adb shell input tap {} {}'.format(x,y))

def swipe_screen(x,y,m,n,i):
    os.system('adb shell input swipe {} {} {} {} {}'.format(x, y, m, n, i))

def light_screen():
    os.system('adb shell input keyevent 64')

def save_screen():
    os.system('adb shell screencap -p /sdcard/sv.png')
    os.system('adb pull /sdcard/sv.png')


#  235 1275   235 1575   540 1575   840 1575

def lockoff():
    # light_screen()   # 点亮
    # time.sleep(0.5)

    desired_caps = {}

    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0.0'
    desired_caps['deviceName'] = '8BN0217626000181'

    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.HWSettings'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    wlan = driver.find_element_by_xpath("//*[@text='无线和网络']")
    wlan.click()
    # TouchAction(driver).

    #
    # swipe_screen(500, 300, 800, 1000, 1)   # 进入解锁界面
    # time.sleep(0.5)

    # swipe_screen(235, 1275, 235, 1575, 1000)  # 解锁
    # swipe_screen(235, 1575, 840, 1575, 1000)
    # TouchAction.press(self, x=1,y=1).wait(2000)\
    # .move_to(x=300, y=300)


if __name__ == '__main__':
    lockoff()
    # light_screen()