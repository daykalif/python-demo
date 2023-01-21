from flask import Flask, session

app = Flask(__name__)
# 使用session的话，需要配置SECRET_KEY
app.config['SECRET_KEY'] = 'lshajkfdshfa'


@app.route('/')
def index():
    user_id = session.get('user_id', '')  # 有就取出user_id,没有就返回""
    user_name = session['user_name']    # 获取user_name
    return '%s --- %s' % (user_id, user_name)


@app.route('/login')
def login():
    # 假装校验成功
    session['user_id'] = "1"
    session['user_name'] = "laowang"
    return 'success'


@app.route('/logout')
def logout():
    # 删除session
    session.pop('user_id', None)  # 删除user_id,如果有user_id,则返回，如果没有则返回None
    session.pop('user_name')    # 删除user_name
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
