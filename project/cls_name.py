import time

class policeman():
    def __init__(self,name, hp, atk, gd):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gd = gd

    def shoot(self):
        print("%s发起攻击" % self.name)

    def hurt(self):
        print("%s受到伤害,剩余血量为%d"% (self.name, self.hp))


class enermy():
    def __init__(self,name, hp, atk, gd):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gd = gd

    def shoot(self):
        print("%s发起攻击" % self.name)

    def hurt(self):
        print("%s受到伤害,剩余血量为%d"% (self.name, self.hp))

def action():
    xiaoming = policeman('小明', 500, 40, 30)
    xiaolei = enermy('小雷', 300, 50, 20)

    xiaolei.shoot()

    xiaoming.hp -= (xiaolei.atk-xiaoming.gd)
    xiaoming.hurt()

    while xiaoming.hp > 0:
        xiaoming.hp -= 50
        print(xiaoming.hp)
        time.sleep(1)
        if xiaoming.hp < 50:
            xiaoming.hp -= xiaoming.hp
            print(xiaoming.hp)
            print("小明死亡了")



if __name__ == '__main__':
    action()

