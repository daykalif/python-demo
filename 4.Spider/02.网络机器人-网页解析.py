from lxml import html

# 读取 HTML 文件
with open('resources/仙逆人物志.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

    # 解析html的文本，将其转换为一个文档对象
    document = html.fromstring(html_text)

    # 解析表头 - xpath语法
    table_header = document.xpath('//table/thead/tr/th/text()')
    print(table_header)

    # 解析表格中的数据 - xpath语法
    table_data = document.xpath('//table/tbody/tr')
    print(table_data)

    for tr in table_data:
        print(tr.xpath('./td/text()'))

    # ---------------------------------------- xpath演示 ----------------------------------------
    # 解析表头 - xpath语法
    # /table/thead/tr/th/text()：表示从跟节点开始匹配
    # //table/thead/tr/th/text()：从任意为止开始匹配
    # td_list = document.xpath('/html/body/div/table/tbody/tr/td/text()')
    # th_list = document.xpath('//table/thead/tr/th/text()')

    td_list = document.xpath('//tbody/tr/td/text()')
    th_list = document.xpath("//thead/tr/th/text()")

    # tr[2]: 表示匹配第二个tr标签
    td_list2 = document.xpath('//tbody/tr[2]/td/text()')

    # last(): 表示匹配最后一个
    td_list3 = document.xpath('//tbody/tr[last()]/td/text()')
    td_list4 = document.xpath('//tbody/tr[last()-1]/td/text()')

    # p[@class]: 表示匹配class属性为p的标签
    p_list = document.xpath('//p[@class]/text()')

    # p[@class="mb-3"]: 表示匹配class属性为mb-3的p标签
    p_list2 = document.xpath('//p[@class="mb-3"]/text()')

    # *：表示匹配任意标签
    th_list2 = document.xpath("//thead/tr/*/text()")

    # @src: 表示匹配src属性
    # @*: 表示匹配任意属性
    a_list = document.xpath("//img/@src")
    a_list2 = document.xpath("//img/@*")
