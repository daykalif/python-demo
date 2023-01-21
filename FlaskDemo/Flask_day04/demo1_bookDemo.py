from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'fdjahfkalsdh'

# 指定使用的数据库的链接地址
# mysql://root:root@127.0.0.1:3306/test_27
# mysql:数据库类型； 第一个root:我的数据库用户名  第二个root:我的数据库密码；   127.0.0.1:3306: 地址和端口   booktest:创建的数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/booktest"
# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化:创建一个SQLAlchemy对象,需要放在config后面
db = SQLAlchemy(app)


class AddBookForm(FlaskForm):
    """自定义添加书籍的表单"""
    author = StringField('作者', validators=[InputRequired('请输入作者')])
    book = StringField('书名', validators=[InputRequired('请输入书名')])
    submit = SubmitField('添加')


# 定义模型
class Author(db.Model):
    """作者模型：一的一方"""
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义属性，以便作者模型可以直接通过该属性访问其多的一方的数据（书的数据）
    # backref 给 Book 也添加了一个author属性，可以通过 book.author 获取 book 所对应的作者信息
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    """书的模型：多的一方"""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 记录一的一方的id作为外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/', methods=['GET', 'POST'])
def index():
    """返回首页"""
    book_form = AddBookForm()

    # 如果book_form可以被提交
    if book_form.validate_on_submit():
        # 1.取出表单中的数据
        author_name = book_form.author.data  # 等同于author_name = request.form.get('author')
        book_name = book_form.book.data  # 等同于book_name = request.form.get('book')

        # 2.做具体业务逻辑代码实现
        # 2.1查询指定名字的作者
        author = Author.query.filter(Author.name == author_name).first()
        if not author:  # 指定名字的作者信息不存在
            try:
                # 添加作者信息到数据库
                # 初始化作者的模型对象
                author = Author(name=author_name)
                db.session.add(author)
                db.session.commit()

                # 添加书籍信息到数据库(指定其作者)
                book = Book(name=book_name)
                book.author = author  # 等同于 book = Book(name=book_name, author_id=author.id)

                db.session.add(book)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                flash("添加失败")
        else:
            book = Book.query.filter(Book.name == book_name).first()
            if not book:
                try:
                    # 添加书籍信息到数据库(指定其作者)
                    book = Book(name=book_name)
                    book.author = author  # 等同于 book = Book(name=book_name, author_id=author.id)

                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(e)
                    flash("添加失败")
            else:
                flash("书籍已存在")
    else:
        if request.method == "POST":
            flash('参数错误')

    # 1.查询数据
    authors = Author.query.all()
    # 2.将数据传入到模板中进行渲染返回
    return render_template('book1_demo.html', authors=authors, form=book_form)


@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    """删除作者以及作者所有的数据"""
    try:
        author = Author.query.get(author_id)
    except Exception as e:
        print(e)
        return "查询失败"
    if not author:
        return "作者不存在"
    # 删除作者及其所有书籍
    try:
        # 先删除书籍
        Book.query.filter(Book.author_id == author_id).delete()
        # 再删除指定作者
        db.session.delete(author)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return "删除失败"
    return redirect(url_for('index'))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    """删除书籍"""
    try:
        book = Book.query.get(book_id)
    except Exception as e:
        print(e)
        return "查询失败"
    if not book:
        return "书籍不存在"
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return "删除失败"
    return redirect(url_for('index'))


if __name__ == '__main__':
    # 删除所有的表
    db.drop_all()
    # 创建所有的表
    db.create_all()

    au1 = Author(name='老王')
    au2 = Author(name='老李')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()

    bk1 = Book(name="老王回忆录", author_id=au1.id)
    bk2 = Book(name="我读书少，你别骗我", author_id=au1.id)
    bk3 = Book(name="如何才能让自己更骚", author_id=au2.id)
    bk4 = Book(name="怎样征服美少女", author_id=au3.id)
    bk5 = Book(name="如何政府英俊少男", author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)
