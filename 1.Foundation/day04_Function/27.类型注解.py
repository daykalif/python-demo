# 变量定义 - 指定类型注解

a2: int = 596  # 整数类型
score2: float = 98.5  # 浮点数类型
hobby2: str = "Python"  # 字符串类型
flag2: bool = True  # 布尔类型
pic2: None = None  # 空值类型

names2: list[str | int] = ["A", "C", 3]
# 列表，元素为字符串类型

phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
# 集合，元素为字符串类型

options2: dict[str, int] = {"count": 2, "total": 10}
# 字典，键为字符串类型，值为整数类型

goods2: tuple[str, int, int] = ("手机", 6999, 1)
# 元组，按顺序标注每个元素的类型：字符串、整数、整数


names2.append("X")
names2.append(10010)
names2.append(10086.2)

"""
类型推断：
Python 解释器会根据变量的赋值内容、表达式运算逻辑、函数 return 的结果，自动判断出对应数据的类型，不用开发者手动写上类型声明。

注意：只有在对变量进行直接赋值，或者涉及到变量的运算，容器的推导等场景时，才能进行类型推断。

类型注解只是起到语法提示的作用，不会影响代码的运行。
"""
num = 10  # 解释器自动推断num是int类型，不用写num:int=10
s = "hello"  # 自动推断s是str类型

a = 10
b = 3.14
c = a + b  # 整数 + 浮点数，解释器推断 c 是 float 类型

nums = [1, 2, 3]  # 推断为 list[int]
words = {"hello", "world"}  # 推断为 set[str]
info = {"id": 1, "score": 95}  # 推断为 dict[str, int]

"""
类型注解-小结：

1. 类型注解的写法
格式：变量名: 数据类型
示例：a: int = 10

2. 常见类型的写法
基础 / 容器类型：int、float、bool、str、None、list、set、tuple、dict
联合类型（多种可能类型）：str | int（表示可以是字符串或整数）

3. 使用类型注解的好处
代码结构更清晰、逻辑更安全、易于维护
提供更准确的代码自动提示（IDE 补全更智能）
提前发现代码潜在的类型错误（静态检查工具可识别）

补充说明:
如果对变量直接赋值、进行变量运算等场景，Python 会自动进行类型推断
Python 是动态类型语言，类型注解只是提示，并非强制约束，不会阻止代码运行时的类型变化
"""
