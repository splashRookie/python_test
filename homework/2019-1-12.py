"""
从键盘输入身高，如果身高没有超过150cm，
输出“进动物园不用买票”
否则输出”需要买票”
"""

# height = int(input())
# if height <= 150:
#     print("进动物园不用买票")
# else:
#     print("需要买票")



# 输入 是否有票，1 有票，0没有票，根据用户输入
# 进行判断  如果是 1  输出 欢迎进站 ，否则 ，请去购票

# ticket = input()
# if ticket == '1':
#     print("欢迎进站")
# elif ticket == '0':
#     print("请去购票")

# 媳妇承认错误，重复输出 说一百遍"媳妇儿，我错了"
# i=0
# while i <= 100:
#     print("媳妇儿，我错了")
#     i += 1


# 猜拳游戏

import random
while 1:
    # stone = 0
    # paper = 1
    # scissors = 2
    re1 = int(input("请出拳："))
    re2 = random.randint(0,2)
    if (re1 ==1 and re2 == 0) or (re1 ==2 and re2 == 1) or (re1 ==0 and re2 == 2):
        print("我：%s 电脑：%s 我赢了" % ( re1, re2))
    elif (re1 ==0 and re2 == 1) or (re1 ==1 and re2 == 2) or (re1 ==2 and re2 == 0):
        print("我：%s 电脑：%s 电脑赢了"% ( re1, re2))
    elif (re1 ==0 and re2 == 0) or (re1 ==1 and re2 == 1) or (re1 ==2 and re2 == 2):
        print("我：%s 电脑：%s 平局"% ( re1, re2))
    else:
        print("输入有误")
        continue