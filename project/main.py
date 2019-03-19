class hero(object):
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor


    def attack(self):
        print("shooting")
        print(self.hp)

    def hurt(self):
        print("%s普通攻击" % self.name)

class enemy(object):
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor

    def attack(self):
        print("")

    def hurt(self):
        print("%s普通攻击" % self.name)


def match():
    zf = hero('张飞', 500, 20, 50)
    bq = enemy('白起', 1000, 50, 20)

    if input()=='A':
        zf.hurt()
        bq.hp -= 20
        print("%s的血量为%d" % (bq.name, bq.hp))


match()