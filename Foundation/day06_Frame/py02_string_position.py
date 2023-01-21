# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对其输出以下内容
poem = ["登鹳雀楼", "王之涣", "白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))  # 居中对齐 shift+option+B输入全半角空格

for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "　"))  # 向左对齐

for poem_str in poem:
    print("|%s|" % poem_str.rjust(10, "　"))  # 向右对齐
