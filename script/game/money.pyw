import os
import time
import subprocess

def tap_screen(x,y):
    subprocess.call('adb shell input tap {} {}'.format(x,y), shell=True)

def swipe_screen(x,y,m,n):
    subprocess.call('adb shell input swipe {} {} {} {}'.format(x, y, m, n), shell=True)

def light_screen():
    subprocess.call('adb shell input keyevent 26', shell=True)


def do_money_work():
    tap_screen(1500, 900)   #  进入挑战
    time.sleep(8)
    tap_screen(1500, 900)  #  跳过
    time.sleep(35)  # 修改值
    tap_screen(1225, 960)  # 药
    # time.sleep(15)
    for i in range(10):
        tap_screen(1225, 960)
        time.sleep(0.5)
        i += 1
    print("1")
    time.sleep(5)
    for i in range(5):
        tap_screen(1225, 960)
        time.sleep(0.5)
        i += 1
    print("2")
    tap_screen(800, 500)
    time.sleep(15)      # 修改值
    for i in range(5):
        tap_screen(1225, 960)
        time.sleep(0.5)
        i += 1
    #  星
    print("next")
    tap_screen(800, 500)
    # 下次挑战
    time.sleep(2)
    tap_screen(1600, 980)
    time.sleep(5)
if __name__ == '__main__':
    # for m in range(10):
    #     do_money_work()
    #     m +=1
    #     print("完成第%d次" % m)

    do_money_work()
