from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    my_list = [
        {
            "id": 1,
            "value": "aa"
        },
        {
            "id": 2,
            "value": "bb"
        },
        {
            "id": 3,
            "value": "cc"
        },
        {
            "id": 4,
            "value": "dd"
        },
        {
            "id": 5,
            "value": "ee"
        }
    ]
    return render_template('demo7_template.html', my_list=my_list)


if __name__ == '__main__':
    app.run(debug=True)
