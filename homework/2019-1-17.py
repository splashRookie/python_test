def triangle():
    n = 1
    while n < 6:
        print("*" * n)
        n += 1


triangle()



def sum(a,b):
    n = a + b
    print(n)

sum(1,3)

def is_odd(n):
    if n % 2 == 0:
        return "偶数"
    else:
        return "奇数"

m = is_odd(3)
print(m)


def money(m):
    if m > 5000:
        n = m * (1-0.1)
        return "实发工资为%d" % n
    else:
        return "工资未达到扣税标准"

real_money =money(5330)
print(real_money)
