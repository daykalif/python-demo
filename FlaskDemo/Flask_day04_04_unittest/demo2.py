from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# 用户登录
# 1.如果传入的参数不足，会返回errcode=-2
# 2.如果传入的账号与密码不正确会返回errcode=-1
# 3.如果账号与密码正确，errcode=0


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 判断参数是否为空
    if not all([username, password]):
        result = {
            "errcode": -2,
            "errmsg": "params error"
        }
        return jsonify(result)
    # a = 1 / 0
    # 如果账号密码正确
    # 判断账号密码是否正确
    if username == 'laowang' and password == '123456':
        result = {
            "errcode": 0,
            "errmsg": "success"
        }
        return jsonify(result)
    else:
        result = {
            "errcode": -1,
            "errmsg": "wrong username or password"
        }
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
