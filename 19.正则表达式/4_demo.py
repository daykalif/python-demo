def dm03_replace替换字符串():
    import re
    sentence = "车主说:你的刹车片应该更换了啊,嘿嘿"

    # 正则表达式: 去除多余字符
    p = r"呢|吧|哈|啊|啦|嘿|嘿嘿"
    r = re.compile(pattern=p)
    mystr = r.sub("", sentence)
    print('mystr-->', mystr)

    # 正则表达: 删除除了汉字数字字母和，！？。.- 以外的字符
    # \u4e00-\u9fa5 是用来判断是不是中文的一个条件
    p = "[^，！？。\\.-\u4e00-\u9fa5_a-zA-Z0-9]"
    r = re.compile(pattern=p)
    mystr = r.sub("", sentence)
    print('mystr-->', mystr)

    # 半角变为全角 sentence.replace(",", "，") 逗号 感叹号 问号
    sentence = "你好."
    mystr = sentence.replace(".", "。")
    print('mystr-->', mystr)


if __name__ == '__main__':
    dm03_replace替换字符串()
