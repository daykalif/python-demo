import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    classmate = Classmate()
    classmate.add('刘能')
    classmate.add('广坤')
    classmate.add('赵四')

    for temp in classmate:
        print(temp)


if __name__ == '__main__':
    main()
