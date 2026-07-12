"""
    Tuple(元祖)与列表类似，不同指出在于元祖的元素不能修改
    元祖表示多个元素组成的序列
    元祖在Python开发中，有特定的应用场景
    元祖用于存储一串信息，数据之间使用,分隔
    元祖用()定义
    元祖的索引从0开始
        索引就是数据在元祖中的位置编号
"""

info_tuple = ("zhangsan", "lisi", "wangwu")
print(type(info_tuple))
print(info_tuple[0])
empty_tuple = ()  # 定义空元祖

single_tuple = (5)
print(single_tuple)
print(type(single_tuple))  # int类型

single_tuple1 = (5,)
print(single_tuple1)
print(type(single_tuple1))  # tuple类型
