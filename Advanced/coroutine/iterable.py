import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    classmate = Classmate()
    classmate.add('刘能')
    classmate.add('谢广坤')
    classmate.add('赵四')

    # print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))
    # classmate_iterator = iter(classmate)
    # print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
    # print("迭代器__next__的返回值是：", next(classmate_iterator))

    for temp in classmate:
        print(temp)


if __name__ == '__main__':
    main()
