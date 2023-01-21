# 第三步
from . import cart_blu
# 第九步
from flask import render_template


# 第四步
@cart_blu.route('/list')
def cart_list():
    # 第十步
    return render_template('cart.html')
