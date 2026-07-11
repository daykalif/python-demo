"""
为什么要用集合？

场景：在业务中，需要定义一个变量，来批量存储用户的手机号（唯一的）。
列表 list、元组 tuple 可以存吗？ 不可以，因为这两种类型是可以存储重复元素的。
解决方案：此时就可以使用集合 set 来存储，set 会自动去重，存储不重复的元素。
"""

"""
集合（set）知识点提取
一、集合介绍
集合（set）是一种无序的、不可重复、可修改的数据容器。

二、集合定义
# 定义集合
s1 = {"C", "D", "X", "T", "O", "U"}

# 定义空集合
s2 = set()

三、注意事项
空集合的定义不可以使用 {}，{} 表示的是空字典。
由于集合是无序的，因此不支持下标索引访问。
"""

# 定义
s1 = {4, 2, 5, 7, 12, 0, 2, 5, 8, 0}
print(s1)  # {0, 2, 4, 5, 7, 8, 12}
print(type(s1))

# 初始化集合s1
s1 = {100, 200, 300, 400, 500, 600, 700, 800}
print(s1)

# 用add()向集合添加单个新元素1200
s1.add(1200)
print(s1)

# 从集合s1中移除元素200
s1.remove(200)
# 打印移除后的集合
print(s1)

# 随机删掉s1里一个元素，把被删掉的元素赋值给变量e
e = s1.pop()
# 打印被删除的那个元素
print(e)
# 打印删除元素之后剩余的集合
print(s1)

# 清空集合s1
s1.clear()
# 打印清空后的集合
print(s1)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

# 差集 difference(): 求两个集合的差集（存在于第一个集合，但不存在与第二个集合）
print(s2.difference(s3))  # {'A', 'B', 'D', 'X'}
print(s3.difference(s2))  # {'Z'}

# 并集 union(): 求两个集合的并集
print(s2.union(s3))  # {'A','B','C','D','E','X','Y','Z'}
print(s3.union(s2))  # 同上再输出一遍

# 交集 intersection(): 求两个集合的交集
print(s2.intersection(s3))
print(s3.intersection(s2))

# ------------------------------------集合set 小结-------------------------------------------------
"""
集合 (set) 的特点？
无序、不可重复、可修改（不要依赖显示顺序）

集合 (set) 的定义及常用操作
定义 1：集合名 = {元素 1, 元素 2, 元素 3...}
定义 2：集合名 = set ()

常用操作：
添加：s1.add (..)
删除：s1.remove (..) /s1.pop () /s1.clear ()
交、并、差集：s1.intersection (s2) /s1.union (s2) /s1.difference (s2)
"""

# ------------------------------ 集合 set 案例 ------------------------------
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# ----------------------1. 找出同时选修了法语和艺术的学生----------------------
# 方式一：交集intersection
french_art_inter = french_set.intersection(art_set)
print("1.1 同时选修法语和艺术的学生：", french_art_inter)

# 方式二：&
french_art_inter2 = french_set & art_set
print("1.2 同时选修法语和艺术的学生：", french_art_inter2)

# ----------------------2. 找出同时选修了所有四门课程的学生----------------------
all_inter = football_set.intersection(basketball_set, french_set, art_set)
print("2.1 同时选修四门课程的学生：", all_inter)

all_inter2 = football_set & basketball_set & french_set & art_set
print("2.2 同时选修四门课程的学生：", all_inter2)

# ----------------------3. 找出选修了足球，但是没有选修篮球的学生----------------------
# 方式一：差集difference
football_only = football_set.difference(basketball_set)
print("3.1 选修足球未选修篮球的学生：", football_only)

# 方式二：-
football_only2 = football_set - basketball_set
print("3.2 选修足球未选修篮球的学生：", football_only2)

# 方式三：集合推导式 --> 快速构建集合，语法：{往集合中添加的数据 for s in set1 if 条件}
football_only3 = {s for s in football_set if s not in basketball_set}
print("3.3 选修足球未选修篮球的学生：", football_only3)

# ----------------------4. 统计每一个学生选修的课程数量----------------------
# 方式一：
# 4.1 获取全体学生名单 -- 并集(|)
# 两种等价写法：链式union 或 | 运算符
# all_set = football_set.union(basketball_set).union(french_set).union(art_set)
all_set = football_set | basketball_set | french_set | art_set

# 4.2 统计每个学生选修课程数量
# 把四个集合所有学生平铺进一个列表，重复出现次数=选课门数
all_list = [*football_set, *basketball_set, *french_set, *art_set]

for s in all_set:
    print(f"{s} 选修了 {all_list.count(s)} 门课程")

# 方式二：
course_dict = {}
# 遍历所有学生和对应课程集合
course_map = [
    ("足球", football_set),
    ("篮球", basketball_set),
    ("法语", french_set),
    ("艺术", art_set)
]
for course_name, stu_set in course_map:
    for stu in stu_set:
        course_dict[stu] = course_dict.get(stu, 0) + 1

print("4. 每位学生选修课程数量：")
for student, count in sorted(course_dict.items()):
    print(f"{student}: {count}门")
