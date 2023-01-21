import re


def main():
    email = input("请输入邮箱地址")
    # 如果在正则表达式中需要用到了某些普通的字符，比如. 比如?等，仅仅需要在他们前面添加一个反斜杠进行转义
    ret = re.match(r"[a-zA-Z0-9]{4,20}@163\.com$", email)
    if ret:
        print("%s符合要求", email)
    else:
        print("%s不符合要求", email)


def main2():
    email2 = input("请输入邮箱地址")
    ret2 = re.match(r"[a-zA-Z0-9]{4,20}@(163|126)\.com$", email2)
    add_front = re.match(r"([a-zA-Z0-9]{4,20})@(163|126)\.com$", email2).group(1)

    html = '<h1>hhahhahha</h1>'
    re.match(r"<(\w*)>.*</\1>").group()

    html2 = '<body><h1>hhahhahha</h1></body>'
    re.match(r"<(\w*)><(\w*)>.*</\2></\1>").group()
    re.match(r"<(?P<body>\w*)><(?P<h1>\w*)>.*</(?P=p2)></(?P=p1)>").group()

    re.search(r"\d+", "阅读数为9999，点赞数为：1000").group()

    re.findall(r"\d+", "python=999, c=789, c++= 123")  # ['999','789','123]

    re.sub(r"\d+", '998', "python=997")

    re.sub(r"\d+", '998', "python=997")

    if __name__ == "__main__":
        main()
        # main2()
