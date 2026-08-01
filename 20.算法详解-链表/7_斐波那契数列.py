"""
案例：求阶乘
公式: n! = n * (n - 1)!
大白话: 5! = 5 * 4 * 3 * 2 * 1 = 120
出口: 1! = 1

分析流程：
        5! = 5 * 4!
            4! = 4 * 3!
                3! = 3 * 2!        规律
                    2! = 2 * 1!
                        1! = 1    出口
"""


# 场景2：求阶乘．

def factorial(n):
    # 出口
    if n == 1:
        return 1
    # 规律
    return n * factorial(n - 1)


print(factorial(5))
