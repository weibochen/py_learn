#! /usr/bin/env python
#! *_* coding: utf-8 *_*

import types


class Person(object):  # 基类必须继承与 object，否则在派生类中将无法使用 super（）函数
    def __init__(self, name="", age=20, sex="man"):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if type(name) != str:  # 内置函数type()返回被测对象的数据类型
            print("姓名必须是字符串！")
            return
        self.__name = name

    def setAge(self, age):
        if type(age) != int:
            print("年龄必须是整型！")
            return
        self.__age = age

    def setSex(self, sex):
        if sex not in ["男", "女"]:
            print("性别输入有误！")
            return
        self.__sex = sex

    def show(self):
        print("姓名：", self.__name)
        print("年龄：", self.__age)
        print("性别：", self.__sex)


# 定义一个子类（student 类），在其中增加一个图学年份私有属性（数据成员）
class Student(Person):
    def __init__(self, name="", age=20, sex="man", school_year=2016):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Student, self).__init__(name, age, sex)
        # Person.__init__(self, name, age, sex)#也可以这样初始化积累的私有数据成员
        self.setSchool_year(school_year)

    def setSchool_year(self, school_year):
        self.__school_year = school_year

    def show(self):
        Person.show(self)  # 调用基类的show()方法
        # super(Student, self).show() #　也可以这样调用基类的show()方法
        print("入学年份：", self.__school_year)


# 主程序
if __name__ == "__main__":
    zs = Person("张三", 19, "男")
    zs.show()
    ls = Student("李四", 18, "男", 2018)
    ls.show()
    ls.setAge(20)
    ls.show()
