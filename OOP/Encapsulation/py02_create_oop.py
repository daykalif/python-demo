class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


tom = Cat()
tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)  # %x以十六进制输出  %d以十进制输出
