from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 宏
@app.route('/demo1')
def demo1():
    # return '<h1>嵇琳杰</h1><h3>嵇琳杰</h3>'
    return render_template('temp1_macro.html')


# 继承
@app.route('/demo2')
def demo2():
    return render_template('temp2_extend.html')


# 包含
@app.route('/demo5')
def demo5():
    return render_template('temp3_include.html')


if __name__ == '__main__':
    app.run(debug=True)
