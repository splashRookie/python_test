score = int(input("请输入你的分数"))

if score >= 90:
    print("你的等级为：A")
elif score >= 80 and score < 90:
    print("你的等级为：B")
elif score >= 70 and score < 80:
    print("你的等级为：C")
elif score >= 60 and score < 70:
    print("你的等级为：D")
else:
    print("你的等级为：E")

