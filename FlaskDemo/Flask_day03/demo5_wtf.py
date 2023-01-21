from flask import Flask, render_template, session, g, flash, request
# 命令行运行：pip install flask-wtf
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo, InputRequired

app = Flask(__name__)

# 关闭csrf验证
app.config['WTF_CSRF_ENABLED'] = True
app.secret_key = 'dfsjkh'


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username, password, password2]):
            flash('参数不足')
        elif password != password2:
            flash('密码不一致')
        else:
            # 注册操作
            print(username, password, password2)
            return 'success'

    return render_template('temp5_wtf.html')


# 自定义表单类，文本字段、密码字段、提交按钮
class RegisterForm(FlaskForm):
    username = StringField("用户名：", validators=[InputRequired("请输入用户名")], render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码：", validators=[InputRequired("请输入密码")])
    password2 = PasswordField("确认密码：", validators=[InputRequired("请输入确认密码"), EqualTo("password", "两次密码不一致")])
    submit = SubmitField("注册")


# 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/register_wtf', methods=["get", "post"])
def register_wtf():
    register_form = RegisterForm()
    # 使用wtf表单帮我们做验证表单
    if register_form.validate_on_submit():
        # 取到表单中提交的值
        # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
        # 取值方式一：
        username = request.form.get("username")
        # 取值方式二：
        # username1 = register_form.username.data
        password = request.form.get("password")
        password2 = request.form.get("password2")
        # 假装做注册操作
        print(username, password, password2)
        return "success"
    else:
        if request.method == "POST":
            flash("参数有误或者不完整")

    return render_template('temp5_wtf.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
