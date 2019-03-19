import time
sum = 0
while True:
    userName = input("请输入您的账号：")
    psd = input("请输入您的密码：")
    if userName == "" or psd == "":
        print("账号或密码不能为空")
        continue
    if userName == "admin" and psd == "123456":
        print("登录成功")
        break
    elif userName != "admin" or psd != "123456":
        sum += 1
        print("账号或密码错误%d次，请重新输入" % sum)
        if sum >= 3:
            print("账号或密码输入错误超过3次，请等待10秒")
            time.sleep(10)
            sum = 0
            continue