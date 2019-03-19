import os
from PIL import Image
import pytesseract


os.system("adb shell screencap -p /sdcard/screen.png")

os.system("adb pull /sdcard/screen.png ./pic")

text = pytesseract.image_to_string(Image.open("screen.png"), lang="chi_sim")

print(text)



# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from time import sleep
#
#
# desired_caps = {
#                 'platformName': 'Android',
#                 'deviceName': '127.0.0.1:62001',
#                 'platformVersion': '1.0.32',
#                 'appPackage': 'com.tencent.mobileqq',
#                 'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
#                 'noReset': "true"
#                 }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# sleep(5)
#
# jiu = 'resourceId("com.tencent.mobileqq:id/name").index(6)'
# loc = driver.find_element_by_android_uiautomator(jiu).location
# print("获取九宫格坐标位置：%s"%loc)
# s = driver.find_element_by_android_uiautomator(jiu).size
# print("获取九宫格宽和高：%s"%s)
#
# # 获取九个点的坐标
# gongge = {}
# gongge[1] = (None, loc["x"]+s["width"]/6, loc["y"]+s["height"]/6)
# gongge[2] = (None, loc["x"]+s["width"]/6*3, loc["y"]+s["height"]/6)
# gongge[3] = (None, loc["x"]+s["width"]/6*5, loc["y"]+s["height"]/6)
# gongge[4] = (None, loc["x"]+s["width"]/6, loc["y"]+s["height"]/6*3)
# gongge[5] = (None, loc["x"]+s["width"]/6*3, loc["y"]+s["height"]/6*3)
# gongge[6] = (None, loc["x"]+s["width"]/6*5, loc["y"]+s["height"]/6*3)
# gongge[7] = (None, loc["x"]+s["width"]/6, loc["y"]+s["height"]/6*5)
# gongge[8] = (None, loc["x"]+s["width"]/6*3, loc["y"]+s["height"]/6*5)
# gongge[9] = (None, loc["x"]+s["width"]/6*5, loc["y"]+s["height"]/6*5)
# print(gongge)
#
# def pianyi(a=1,b=2):
#     '''计算从a点到b点的偏移量'''
#     g1 = gongge[a]
#     g2 = gongge[b]
#     r = (None, g2[1]-g1[1], g2[2]-g1[2])
#     return r
#
# # 执行解锁
# TouchAction(driver).press(*gongge[1]).wait(300).move_to(*pianyi(1,2)).wait(300).move_to(*pianyi(2,3)).wait(
#     300).move_to(*pianyi(3,5)).wait(300).move_to(*pianyi(5,7)).wait(300).move_to(*pianyi(7,8)).wait(300).move_to(*pianyi(8,9)).wait(
#     300).release().perform()