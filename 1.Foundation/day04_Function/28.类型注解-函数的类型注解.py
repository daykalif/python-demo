"""
函数 - 类型注解
为函数添加类型注解，主要是为参数和返回值添加类型提示;
对于需要团队写作开发和长期维护的项目，推荐使用类型注解
"""


# 示例1：计算平均分
def calc(scores: list[int]) -> float:
    return sum(scores) / len(scores)


# 示例2：返回最大值、最小值、平均值
def calc_data(scores: list[int]) -> tuple[int, int, float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v, min_v, avg_v


# 示例3:
def circle_area_len(r: float) -> tuple[float, float]:
    area = round(3.14 * r * r, 1)
    length = round(2 * 3.14 * r, 1)
    return area, length


# 调用函数
al = circle_area_len(8.5)
print(al)


# 示例4:
def calc_order_cost(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: float = 0.0) -> float:
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price) - coupon - score / 100 + express

    return total_cost


items = ("鼠标", 188, 2), ("键盘", 388, 1), ("显示器", 2499, 2)
total = calc_order_cost(*items, coupon=200, score=500, express=15)
print("订单总金额：", total)
