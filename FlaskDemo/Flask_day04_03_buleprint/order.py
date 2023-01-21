from flask import Blueprint

# 1.初始化蓝图
order_blu = Blueprint('order_name', __name__)


# 订单列表
# 2.使用蓝图去注册路由url
@order_blu.route('/order/list')
def order_list():
    return 'order_list'
