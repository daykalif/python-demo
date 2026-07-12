"""
案例 1：计算 n 的阶乘

递归调用概念
递归调用指的是在函数中自己调用自己的情况，执行过程是先层层递进，再逐层回归，必须要有明确的终结点（终止条件）。

阶乘公式
n 的阶乘公式：
f(n)=n×f(n−1)

其中终结点为：
f(1)=1
（1 的阶乘是 1）


递归展开示例（以计算 10! 为例）：
jc(10) = 10 * jc(9)
jc(9)  = 9 * jc(8)
jc(8)  = 8 * jc(7)
jc(7)  = 7 * jc(6) = 7 * 720 = 5040
jc(6)  = 6 * jc(5) = 6 * 120 = 720
jc(5)  = 5 * jc(4) = 5 * 24  = 120
jc(4)  = 4 * jc(3) = 4 * 6   = 24
jc(3)  = 3 * jc(2) = 3 * 2   = 6
jc(2)  = 2 * jc(1) = 2 * 1   = 2
jc(1)  = 1
"""


def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)


result = jc(5)
print(result)

# -------------------------------------------订单总金额计算函数-----------------------------------------------------------------
"""
案例 2：订单总金额计算函数
需求说明
定义函数 calc_order_cost，根据商品信息、优惠信息和运费信息，计算订单总金额，规则如下：
优惠券：商品总金额满 5000 才可使用，且抵扣金额不超过商品总价。
积分抵扣：商品总金额满 5000 才可使用，100 积分抵扣 1 元，积分只能整百抵扣，且抵扣金额不超过商品总价。
"""


# 方法一：
def calc_order_cost(*args, coupon, score, express):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量），格式为元组，如: ("鼠标", 188, 2)、("键盘", 388, 1)
    :param coupon: 优惠券金额
    :param score: 积分数量
    :param express: 运费金额
    :return: 订单的总金额
    """
    # 1. 计算商品总价
    total_price = 0
    for item in args:
        name, price, count = item
        total_price += price * count

    # 2. 计算优惠券抵扣
    coupon_discount = 0
    if total_price >= 5000:
        coupon_discount = min(coupon, total_price)

    # 3. 计算积分抵扣（100积分抵1元，只整百抵扣）
    score_discount = 0
    if total_price >= 5000:
        # 可抵扣的元数 = 积分 // 100
        score_discount = min(score // 100, total_price)

    # 4. 计算最终应付金额
    final_cost = total_price - coupon_discount - score_discount + express
    return final_cost


# 示例：2个商品，优惠券200元，积分500，运费15元
items = [("鼠标", 188, 2), ("键盘", 388, 1), ("显示器", 2499, 2)]
total = calc_order_cost(*items, coupon=200, score=500, express=15)
print("订单总金额：", total)


# 方法二：
def calc_order_cost2(*args, coupon=0, score=0, express=0):
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3.扣减积分
    if total_cost >= 5000 and score // 100 <= total_cost:  # //：整数除法
        total_cost -= score // 100

    # 4.添加运费
    total_cost += express

    return total_cost


items2 = ("鼠标", 188, 2), ("键盘", 388, 1), ("显示器", 2499, 2)
total2 = calc_order_cost2(*items2, coupon=200, score=500, express=15)
print("订单总金额：", total2)

items3 = ("鼠标", 188, 2), ("键盘", 388, 1), ("显示器", 2499, 2)
total3 = calc_order_cost2(*items3, express=15)
print("订单总金额：", total3)
