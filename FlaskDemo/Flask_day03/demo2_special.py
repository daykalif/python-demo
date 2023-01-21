from flask import Flask, render_template, session, g, flash

app = Flask(__name__)
app.secret_key = 'dfsjkh'


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    session['name'] = 'laowang'
    g.name = 'xiaojie'
    flash('我是闪现的消息')
    return render_template('temp4_special.html')


if __name__ == '__main__':
    app.run(debug=True)
