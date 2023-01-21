class Student(object):
    def __init__(self):
        self.xm = None
        self.bj = None

    def setName(self, name):
        self.xm = name

    def setBj(self, clz):
        self.bj = clz

    def console(self):
        print(self.xm, self.bj)


s1 = Student()
s1.setName('jilinjie')
s1.setBj('class1')
s1.console()
