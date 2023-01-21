# 不推荐使用 from...import *，因为导入多个模块时，相同内容后者会覆盖前者，并且冲突排查困难
from py01_test1 import *
from py02_test2 import *

print(title)
say_hello()

wangcai = Dog()
print(wangcai)
