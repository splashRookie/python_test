import os
import time

def tap_screen(x,y):
    os.system('adb shell input tap {} {}'.format(x,y))

def swipe_screen(x,y,m,n):
    os.system('adb shell input swipe {} {} {} {}'.format(x, y, m, n))

def listen_to_music():
    print('#0 start the game')

    # 打开QQ音乐
    tap_screen(130, 480)
    time.sleep(6)

    # 选择进入歌单
    swipe_screen(600, 1500, 600, 800)
    tap_screen(800, 1300)
    time.sleep(0.5)

    # 下滑歌单
    for i in range(5):
        swipe_screen(600, 1500, 700, 800)
        time.sleep(0.5)

    # 选择歌曲并打开播放页面
    tap_screen(800, 1300)
    time.sleep(0.5)
    tap_screen(600, 1850)



if __name__ == '__main__':
    listen_to_music()