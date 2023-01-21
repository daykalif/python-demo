poem_str = "\t\n登鹳雀楼 王之涣 \n\t 白日依山尽\t\n 黄河入海流 \n 欲穷千里目 \t 更上一层楼"
print(poem_str)

# 1.拆分 字符串
poem_list = poem_str.split()
print(poem_list)

# 2.合并字符串
result = "　".join(poem_list)
print(result)
