"""
该文件用于 完成学生管理系统 的具体业务操作，即：增删改查，保存学生信息等...
"""
import time

# 导包
from student import Student


# 1.创建学生管理系统类
class StudentCMS(object):
    # 2.通过魔法方法init，初始化属性信息
    def __init__(self):
        # 3.创建一个空列表，用于存储学生信息
        self.stu_list = []  # [学生对象，学生对象，学生对象] --> [Student(...),Student(...),Student(...)]

        # 方便测试，添加一些学生信息
        # self.stu_list = [
        #     Student(name='德桦', gender='男', age=81, phone='111', desc='刻骨铭心'),
        #     Student(name='志奇', gender='男', age=22, phone='222', desc='我不是紫琦'),
        #     Student(name='紫琦', gender='男', age=66, phone='333', desc='有请志奇'),
        #     Student(name='冷哥', gender='男', age=88, phone='444', desc='谁动了我的水冷'),
        #     Student(name='卷帘', gender='男', age=52, phone='555', desc='谁动了我的大酱'),
        # ]

    # 3.定义函数，实现打印 管理系统 的界面
    @staticmethod
    def show_view():
        print('*' * 23)
        print('学生管理系统V2.0版')
        print("\t1. 添加学生信息")
        print("\t2. 删除学生信息")
        print("\t3. 修改学生信息")
        print("\t4. 查询学生信息")
        print("\t5. 显示所有学生信息")
        print("\t6. 保存学生信息")
        print("\t7. 退出系统")
        print('*' * 23)

    # 4.定义函数，实现添加学生信息功能
    def add_student(self):
        # 4.1 提示用户输入学生信息，并接收
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        age = input("请输入学生年龄：")
        phone = input("请输入学生手机号：")
        desc = input("请输入学生描述信息：")

        # 4.2 创建学生对象
        stu = Student(name, gender, age, phone, desc)

        # 4.3 将学生对象添加到列表中
        self.stu_list.append(stu)

        # 4.4 打印添加成功的信息
        print("添加学生信息成功\n", stu)

    # 5.定义函数，实现删除学生信息功能
    def del_student(self):
        # 5.1 提示用户输入要删除的学生编号，并接收
        del_name = input("请输入要删除的学生姓名：")

        # 5.2 遍历列表，获取每个学生对象
        for stu in self.stu_list:
            # 5.3 如果当前学生的姓名 和 要删除学生的姓名相同，则删除该学生对象
            if stu.name == del_name:
                # 5.4 删除列表中对应的学生对象
                self.stu_list.remove(stu)
                print("删除学生信息成功")
                break
        else:
            print("没有找到对应的学生信息")

    # 6.定义函数，实现修改学生信息功能
    def update_student(self):
        # 6.1 提示用户输入要修改的学生编号，并接收
        update_name = input("请输入要修改的学生姓名：")

        # 6.2 遍历列表，获取每个学生对象
        for stu in self.stu_list:
            # 6.3 如果当前学生的姓名 和 要修改学生的姓名相同，则修改该学生对象
            if stu.name == update_name:
                # 6.4 修改列表中对应的学生对象
                stu.age = int(input("请输入学生年龄："))
                stu.gender = input("请输入学生性别：")
                stu.phone = input("请输入学生手机号：")
                stu.desc = input("请输入学生描述信息：")
                print(f"学生 {update_name} 的信息修改成功")
                break
        else:
            print("没有找到对应的学生信息")

    # 7.定义函数，实现查询学生信息功能
    def search_one_student(self):
        # 7.1 提示用户输入要查找的学生编号，并接收
        search_name = input("请输入要查找的学生姓名：")

        # 7.2 遍历列表，获取每个学生对象
        for stu in self.stu_list:
            # 7.3 如果当前学生的姓名 和 要查找学生的姓名相同，则查找该学生对象
            if stu.name == search_name:
                # 7.4 查找列表中对应的学生对象
                print("查找学生信息成功")
                print(stu, end='\n\n')
                break
        else:
            print("没有找到对应的学生信息")

    # 8.定义函数，实现显示所有学生信息功能
    def search_all_student(self):
        # 8.1 判断列表长度是否为0，如果为0，提示用户没有数据
        if len(self.stu_list) == 0:
            print("没有数据，请先添加学生信息")
            return
        # 8.2 长度不为0，遍历列表，获取每个学生对象
        for stu in self.stu_list:
            print(stu)
        print()  # 增加一个空行

    # 9.定义函数，实现保存学生信息功能
    def save_student(self):
        # 9.1 关联 学生信息文件.
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            # 9.2 把 [学生对象, 学生对象...] → [字典, 字典...]
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            # 9.3 把字典列表，持久化到文件中.
            dest_f.write(str(stu_dict))  # 记得转成字符串再写入.

    # 10.定义函数，实现加载学生信息
    def load_student(self):
        # 10.1 加入异常处理，防止文件不存在
        try:
            # 10.2 关联学生信息文件.
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f:
                # 10.3 一次性读取所有数据.
                stu_data = src_f.read()  # '[字典, 字典...]'
                # 10.4 把上述的字符串，转为列表.
                stu_list = eval(stu_data)
                # 10.5 判断如果列表为空，就赋予空列表.
                if len(stu_list) == 0:
                    stu_list = []
                # 10.6 把stu_list(列表套字典) 转成 [学生对象, 学生对象...]，并赋值给 self.stu_list
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except Exception as e:
            # 10.7 走这里，说明文件不存在，创建文件即可
            with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
                pass

    # 11.定义函数，把上述所有业务逻辑跑通
    def start(self):
        # 11.1 加载学生信息
        self.load_student()

        # 11.2 死循环，不断地玩意儿
        while True:
            # 11.3 为了效果更明显，加入延长（休眠线程）
            time.sleep(1)

            # 11.4 打印学生管理系统的界面
            StudentCMS.show_view()

            # 11.5 提示用户录入要操作的编号，并接收
            choice = input("请输入你的选择：")

            # 11.6 根据用户输入的编号，执行相应的功能
            if choice == '1':
                print("添加学生信息\n")
                self.add_student()
            elif choice == '2':
                print("删除学生信息\n")
                self.del_student()
            elif choice == '3':
                print("修改学生信息\n")
                self.update_student()
            elif choice == '4':
                print("查询学生信息\n")
                self.search_one_student()
            elif choice == '5':
                print("显示所有学生信息\n")
                self.search_all_student()
            elif choice == '6':
                print("保存学生信息\n")
                self.save_student()
                print("保存学生信息成功\n")
            elif choice == '7':
                # 退出系统，做二次校验
                result = input("是否确定退出系统？(Y/N)")
                if result.lower() == 'y':
                    # 退出前，自动保存学生信息到文件
                    self.save_student()
                    print('谢谢您的使用，期待下次再会！')
                    break


# 12.在main中测试
if __name__ == '__main__':
    # 12.1 创建学生管理系统对象
    cms = StudentCMS()

    # 12.2 调用学生管理系统对象的start()函数，启动学生管理系统
    cms.start()
