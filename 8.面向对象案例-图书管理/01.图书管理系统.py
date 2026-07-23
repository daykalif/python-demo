from abc import ABC, abstractmethod
import json


# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 书籍ID
        self.title = title  # 书名
        self.author = author  # 作者
        self.total_num = total_num  # 总数量
        self.__available_num = total_num  # 可用数量

    # 借书
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    # 还书
    def return_book(self):
        self.__available_num += 1

    # 查询可用数量
    def get_available_num(self):
        return self.__available_num


"""
抽象类：
是一种只能被继承，不能被直接实例化的类，作用就是规定子类必须要实现哪些方式，强制子类必须遵守统一的代码规范

Python中的抽象类，需要继承 abc 模块中的 ABC 类（Abstract Base Class），并使用 @abstractmethod 装饰器来定义抽象方法。
"""


# 会员类
class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员卡号
        self.name = name  # 会员姓名
        self.__password = password  # 密码
        self.__borrowed_books = []  # 借阅书籍列表

    # 获取会员最大借阅数量（需要在子类中实现）
    @abstractmethod
    def get_max_books(self) -> int:
        pass

    # 借书
    def borrow_book(self, book: Book):
        # 1.判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("会员 %s 借阅数量已达到最大限制，请归还书籍后再借阅。" % self.name)
            return False

        # 2.借阅书籍
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print("会员 %s 借阅《%s》成功。" % (self.name, book.title))
            return True
        else:
            print("会员 %s 借阅《%s》失败，书籍已借完。" % (self.name, book.title))
            return False

    # 还书
    def return_book(self, book: Book):
        # 1.判断书籍是否在借阅列表中
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print("会员 %s 归还《%s》成功。" % (self.name, book.title))
            return True
        else:
            print("会员 %s 没有借阅《%s》。" % (self.name, book.title))
            return False

    # 获取密码
    def get_password(self):
        return self.__password

    # 获取借阅书籍列表
    def get_borrowed_books(self):
        return self.__borrowed_books


# 普通会员类
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3


# vip会员
class VipMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level  # vip等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level


# 图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}  # 书籍列表 --> {"AI001": Book对象, "AI002": Book对象, ...}
        self.members = {}  # 会员列表 --> {"N001": Member对象, "N002": Member对象, ...}
        self.current_member: Member | None = None  # 当前登录会员

        # 加载数据（书籍，会员）
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载 data/books.json中的数据
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book_data in books_data:
                book = Book(
                    book_data["编号"],
                    book_data["标题"],
                    book_data["作者"],
                    book_data["数量"]
                )
                self.books[book_data["编号"]] = book
            print("书籍数据加载完成。")

    def load_members_data(self):
        # 加载 data/members.json中的数据
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member_data in members_data:
                # 根据卡号区分是普通会员还是vip会员
                if member_data["卡号"].startswith("N"):
                    member = NormalMember(
                        member_data["卡号"],
                        member_data["姓名"],
                        member_data["密码"]
                    )
                else:
                    member = VipMember(
                        member_data["卡号"],
                        member_data["姓名"],
                        member_data["密码"],
                        member_data["会员等级"]
                    )
                self.members[member_data["卡号"]] = member
            print("会员数据加载完成。")

    # 登录
    def login(self):
        print("\n【登录】")
        member_id = input("请输入会员卡号：")
        password = input("请输入密码：")

        # 1.判断会员是否存在
        if member_id not in self.members:
            print("会员 %s 不存在。" % member_id)
            return False

        # 2.判断密码是否正确
        if self.members[member_id].get_password() != password:
            print("密码错误。")
            return False

        # 3.登录成功
        self.current_member = self.members[member_id]
        print("登录成功，欢迎 %s" % self.current_member.name)
        return True

    # 借阅图书
    def borrow_book(self):
        # 1.展示出当前图书馆的图书列表
        for book in self.books.values():
            print("编号：%s，标题：%s，作者：%s，总数：%s，可借数量：%s" % (
                book.book_id, book.title, book.author, book.total_num, book.get_available_num()))

        # 2.获取用户输入的图书编号，执行借书操作
        book_id = input("请输入图书编号：")
        if book_id in self.books:
            book = self.books[book_id]
            self.current_member.borrow_book(book)
        else:
            print("图书 %s 不存在。" % book_id)

    # 归还图书
    def return_book(self):
        # 1.展示出当前会员借阅的图书列表
        print("【已经借阅的图书列表：】")
        for book in self.current_member.get_borrowed_books():
            print("编号：%s，标题：%s" % (book.book_id, book.title))

        # 2.获取用户输入的图书编号，执行还书操作
        book_id = input("请输入图书编号：")
        if book_id in self.books:
            book = self.books[book_id]
            self.current_member.return_book(book)
        else:
            print("图书 %s 不存在。" % book_id)

    # 查询借阅列表
    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已经借阅的图书列表：】")
            for book in borrowed_books:
                print("编号：%s，标题：%s" % (book.book_id, book.title))
        else:
            print("当前没有借阅任何图书。")

    def run(self):
        print("【图书馆管理系统】")
        while True:
            print("1. 登录")
            print("2. 借书")
            print("3. 还书")
            print("4. 查询借阅")
            print("5. 退出")
            choice = input("请输入你的选择：")
            match choice:
                case "1":
                    self.login()
                case "2":
                    self.borrow_book()
                case "3":
                    self.return_book()
                case "4":
                    self.show_borrowed_books()
                case "5":
                    print("退出系统。")
                    break
                case _:
                    print("无效的选择，请重新输入。")


if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()
