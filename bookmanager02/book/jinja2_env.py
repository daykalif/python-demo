from django.template.defaultfilters import date
from jinja2 import Environment


def environment(**option):
    # 1.创建Environment实例
    env = Environment(**option)

    # 2.指定（更新）jinja2的函数指向django的指定过滤器
    env.globals.update({
        'date': date
    })

    # 3.返回Environment实例
    return env
