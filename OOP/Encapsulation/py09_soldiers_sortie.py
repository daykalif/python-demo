# 一个对象的属性，可以是另外一个类创建的对象
class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model

        # 2.子弹的数量
        self.bullet_count = 0

    # 装填子弹的方法
    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

            # 2.发射数量，-1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))


# 定义没有初始值的属性
# None关键字，表示什么都没有
# 表示一个空对象，没有方法和属性，是一个特殊的常量
# 可以将None赋值给任何一个变量

class Soldier:
    def __init__(self, name):
        # 1.姓名
        self.name = name

        # 2.枪 - 新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断士兵是否有枪
        # 身份运算符：
        # 身份运算符用于比较两个对象的内存地址是否一致--是否是对同一个对象对引用
        # 在python中针对None比较时，建议使用is判断
        # is 与 == 区别：
        # is用于判断两个变量引用对象是否为同一个
        # ==用于判断引用变量的值是否相等
        if self.gun is None:    # if self.gun == None:
            print("[%s] 还没有枪..." % self.name)
            return
        # 2.高喊口号
        print("冲啊...[%s]" % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(50)

        # 4.让枪发射子弹
        self.gun.shoot()


# 1.创建枪对象
ak47 = Gun("AK47")

# 2.创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)
