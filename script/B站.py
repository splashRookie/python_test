import os
import time

def tap_screen(x,y):
    os.system('adb shell input tap {} {}'.format(x,y))

def swipe_screen(x,y,m,n):
    os.system('adb shell input swipe {} {} {} {}'.format(x, y, m, n))

def left():
    os.system('adb shell input keyevent 21')

def right():
    os.system('adb shell input keyevent 22')

def enter():
    os.system('adb shell input keyevent 66')

def start_B():
    for i in range(0,16):
        right()
    enter()
    for i in range(0,1):
        right()
    enter()


def work():
    print('#0 start the game')

    for i in range(3):
        swipe_screen(500, 1200, 800, 400)

    tap_screen(300, 1200)

    tap_screen(1000, 500)
    time.sleep(2)
    tap_screen(980, 523)
    time.sleep(0.5)
    tap_screen(980, 523)
    time.sleep(0.5)
    tap_screen(980, 523)

    tap_screen(1000, 500)

    time.sleep(15)
    tap_screen(1000, 500)
    tap_screen(46, 999)


if __name__ == '__main__':
    start_B()
    # work()