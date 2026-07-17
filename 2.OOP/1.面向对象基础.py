# 定义类
class Car:
    pass


# 创建对象
c1 = Car()

# 动态地为对象添加属性 <----不推荐
c1.color = 'red'
c1.brand = 'BMW'
c1.name = 'X5'
c1.price = 500000

print(c1)
print(c1.brand)
print(c1.__dict__)  # 会将对象中的所有属性以字典的形式输出出来


# ------------------------------------------------------------------
# 定义类：
class Car:
    # __init__ 方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
    # self：是第一个参数，表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")


# 创建对象
c2 = Car("red", "BMW", "X5", 500000)
print(c2.__dict__)

"""
小结：

1．定义类时，类名的命名规范？
- 大驼峰命名法，UserInfo、UserAccount

2．定义类时，__init__方法的作用？self参数的作用？
- __init__ 是初始化方法，对象创建时自动调用，主要用于设置对象的初始状态（设置对象属性）
- self是类中定义的方法的第一个参数，表示当前创建的实例对象
"""


# ------------------------------ 定义类 实例方法 ------------------------------------
# 示例代码
class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")

    def total_cost(self, discount, rate=0.1):
        """
        计算提车的总费用，包含两个部分：车的价格，税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        return self.price * discount + self.price * rate

    def __str__(self):
        return f"{self.brand} --> {self.name} ==> {self.price}"

    def __eq__(self, other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name

    def __lt__(self, other):
        return self.price < other.price


c1 = Car("BMW", "X5", 500000)
print(c1)  # 打印对象，默认调用对象的 __str__ 方法

total_price = c1.total_cost(0.9, 0.1)
print(f"提车总价为：{total_price:.0f}")

total_price2 = c1.total_cost(0.9)
print(f"提车总价为：{total_price2:.0f}")

c1.running()

print(c1 == c2)  # 默认两个对象比较的是对象的内存地址，即是否是同一个对象。只有添加了 __eq__ 逻辑之后才比较对象的属性
print(c1 < c2)  # 默认两个对象直接不能比较大小。只有添加了 __lt__ 逻辑之后才可以比较

"""
1．什么是魔法方法？
• Python中提供的__xxx__形式的特殊方法
• 魔法方法无需手动调用，Python会在合适的时机自动调用

2．常用的魔法方法有哪些，作用是什么？
• __init__
• __str__
• __eq__
• __lt__ ，__le__ ，__gt__ ，__ge__


# 各魔法方法作用
__init__：构造方法，创建对象时自动执行，用于初始化对象属性
__str__：打印对象print()时自动执行，自定义对象字符串展示信息
__eq__：对应 == 运算符，自定义两个对象相等的判断规则
__lt__：对应 < 小于
__le__：对应 <= 小于等于
__gt__：对应 > 大于
__ge__：对应 >= 大于等于
"""


# ------------------------ 实例属性 与 类属性 ------------------------
class Car:
    # 类属性（所有实例对象共享的）
    wheel = 4  # 轮胎数量
    tax_rate = 0.1  # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost


# 测试
c1 = Car(c_color="白色", c_brand="BYD", c_name="汉", c_price=180000)
print(c1)

# 通过实例对象访问实例属性
print(c1.brand)

# 通过实例对象访问类属性
print(c1.wheel)  # 通过示例对象，查找属性时，会先找实例属性，如果实例属性中没有，则会找类属性

# 通过类名访问类属性
print(Car.wheel)

c2 = Car(c_color="黑色", c_brand="Tesla", c_name="Model Y", c_price=260000)
print(c2)
