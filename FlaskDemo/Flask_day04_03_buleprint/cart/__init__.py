# 第一步
from flask import Blueprint

# 第二步   static_folder="static"指定当前cart模块的静态文件，url_prefix="/cart"设置cart模块的公共前缀路径
# 第十一步  template_folder="templates"指定当前cart模块的模版文件
cart_blu = Blueprint("cart", __name__, static_folder="static", url_prefix="/cart", template_folder="templates")

# 第五步
from .views import *
