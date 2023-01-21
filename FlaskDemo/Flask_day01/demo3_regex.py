from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    # 自定义正则转换器

    # 方法1:
    # regex = "[0-9]{6}"

    # 方法2:
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 取到第一个参数，给regex属性赋值
        self.regex = args[0]


class ListConverter(BaseConverter):
    def to_url(self, value):
        """使用url_for的时候，对视图函数传的参数进行处理，处理完毕之后以便能够进行路由匹配"""
        result = ','.join(str(v) for v in value)
        return result

    """自定义转换器"""
    regex = "(\\d+,?)+\\d$"

    def to_python(self, value):
        """当匹配到参数之后，对参数做进一步处理之后，再返回给视图函数中"""
        return value.split(",")


app = Flask(__name__)

# 方法1:将自己的转换器添加到默认的转换器列表中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["list"] = ListConverter


@app.route('/')
def index():
    return 'index'


# 规则：/user/6位数组 [0-9]{6}
# 自定义转换器

# 方法1:
# @app.route('/user/<re:user_id>')
# def demo1(user_id):
#     return 'demo1 %s' % user_id

# 方法2:
@app.route('/user1/<re("[0-9]{6}"):user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/users/<list:user_ids>')
def demo3(user_ids):
    # 如何才能在视图函数中接受到的user_ids就是一个列表
    return "用户的id列表是 %s" % user_ids


@app.route('/demo4')
def demo4():
    return redirect(url_for('demo3', user_ids=[1, 2, 3, 4]))


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
