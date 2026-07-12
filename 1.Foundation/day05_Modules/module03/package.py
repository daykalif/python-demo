# 1.导入模块

# 方式一：
import utils.my_fun

utils.my_fun.log_separator1()

# 方式二：
from utils import my_fun

my_fun.log_separator1()

# 方式三：注意，如果要通过如下方式导入包下所有模块，需要在 __init__.py中添加 __all__=[]
from utils import *

my_fun.log_separator1()
print(my_var.PI)

# 2.导入模块中的功能
# 相对路径：
from utils.my_fun import log_separator1, log_separator3

log_separator1()
log_separator3()

# 绝对路径：
from day05_Modules.module02.my_func import log_separator1, log_separator3

log_separator1()
log_separator3()
