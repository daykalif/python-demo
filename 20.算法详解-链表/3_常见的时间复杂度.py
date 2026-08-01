"""
常见时间复杂度的关系

1. 常见的时间复杂度有哪些？
常数阶，对数阶，线性阶，平方阶，立方阶。。。

所消耗的时间从小到大:
O(1) < O(logn) < O(n) < O(nlogn) < O(n²) < O(n³)
时间复杂度越低，效率越高

备注:
O(logn)：大O计数法：时间T与问题的规模变化曲线；二分法
O(nlogn)：一个for循环是n 另外一个for循环是二分法，组合在一起
"""

# 时间复杂度：O(1)
i = 8
j = 6
sum = i + j


# 时间复杂度：O(logn)；问题规模是n，i不是一个一个的变化，而是2倍2倍的变化，接近n；相当于二分查找
def func(n):
    i = 1
    while i <= n:
        i = i * 2


# 时间复杂度：O(n)
def cal(m, n):
    sum_1 = 0
    for i in range(1, m):  # 时间复杂度：O(n)
        sum_1 += i

    sum_2 = 0
    for j in range(1, n):  # 时间复杂度：O(n)
        sum_2 += j
    return sum_1 + sum_2
