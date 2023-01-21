from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    my_int = 10
    my_str = '<h1>嘿嘿</h1>'
    my_list = [1, 2, 3]
    my_dict = {
        "id": "1",
        "name": "laowang"
    }
    my_dict_list = [{
        "good_name": '白菜',
        "price": 4
    }, {
        "good_name": '萝卜',
        "price": 7
    }]
    return render_template('demo6_jinjia2.html', aaa=my_int, bbb=my_str, ccc=my_list, ddd=my_dict,
                           my_dict_list=my_dict_list)


# 自定义过滤器：
# 方式一：装饰器的形式
# @app.template_filter('lireverse')
def do_lireverse(li):
    # 将传入的列表生成一个新的列表
    temp = list(li)
    # 反转
    temp.reverse()
    return temp


# 方式二：直接添加过滤器
app.add_template_filter(do_lireverse, 'lireverse')

if __name__ == '__main__':
    app.run(debug=True)
