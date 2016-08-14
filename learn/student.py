class Enemy:
    life = 3
    name = ''

    def __init__(self, name, life):
        self.name = name
        self.life = life
        print(self.name + ': Hello, I am ' + self.name + ' and I have ' + str(self.life) + ' lifes!')

    def attack(self):
        print(self.name + ': ouch ...')
        self.life -= 1

    def checkLife(self):
        if(self.life <= 0):
            print(self.name + ': I am dead')
        else:
            print(self.name + ': I have '+str(self.life)+' life')

en1 = Enemy('Alice', 5)
en2 = Enemy('David', 8)

en1.attack()
en1.checkLife()

en1.attack()
en1.checkLife()

en2.attack()
en2.checkLife()
