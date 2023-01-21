poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"
        ]
for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, "　"))  # strip()方法去除字符串前后的空白字符
