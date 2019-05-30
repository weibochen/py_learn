#!/usr/bin/env python
# coding=utf-8

import sqlite3


def print_word(string):
    print(string.center(50, "-"))


# 打开数据库
def open_db():
    conn = sqlite3.connect("contact.db")
    cur = conn.execute(
        "Create table if not exists tongxunlu(usernum integer primary key, username varchar(128), password varchar(128), address varchar(125), telnum varchar(128))"
    )
    return cur, conn


# 查询全部信息
def show_all_db():
    print_word("处理后的数据")
    hel = open_db()
    cur = hel[1].cursor()
    cur.execute("select * from tongxunlu")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h),
        print
    cur.close()


# 输入信息
def into():
    usernum = input("请输入学号：")
    username = input("请输入姓名：")
    password = input("请输入密码：")
    address = input("请输入地址：")
    telnum = input("请输入手机号码：")
    return usernum, username,  password, address, telnum


# 往数据库中添加内容
def add_db():
    print_word("欢迎使用添加数据功能")
    person = into()
    hel = open_db()
    hel[1].execute(
        "insert into tongxunlu(usernum, username, password, address, telnum)values(?,?,?,?,?)",
        (person[0], person[1], person[2], person[3], person[4]),
    )
    hel[1].commit()
    print_word("恭喜你，数据添加成功。")
    show_all_db()
    hel[1].close()


# 删除数据库中的内容
def del_db():
    print_word("欢迎使用输出数据库功能")
    del_choice = input("请输入想要删除的学号：")
    hel = open_db()
    hel[1].execute("delete form tongxunlu where usernum = " + del_choice)
    print_word("恭喜你，数据删除成功！")
    show_all_db()
    hel[1].close()


# 修改数据库的内容
def alter():
    print_word("欢迎使用修改数据库功能")
    change_choice = input("请输入想要修改的学生的学号：")
    hel = open_db()
    person = into()
    hel[1].execute(
        "update tongxunlu set usernum=?, username=?, password=?, address=?, telnum=? where usernum="
        + change_choice,
        (person[0], person[1], person[2], person[3], person[4]),
    )
    hel[1].commit()
    show_all_db()
    hel[1].close()


# 查询数据
def search_db():
    print_word("欢迎使用查询数据库功能")
    choice = input("请输入要查询的学生的学号：")
    hel = open_db()
    cur = hel[1].cursor()
    cur.execute("select * from tongxunlu where usernum=" + choice)
    hel[1].commit()
    print_word("恭喜你，你要查询的数据如下：")
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    hel[1].close()


# 是否继续
def conti(a):
    choice = input("是否继续？（y or n）:")
    if choice == "y":
        a = 1
    else:
        a = 0
    return a


if __name__ == "__main__":
    flag = 1
    while flag:
        print_word("欢迎使用数据库通讯录")
        choice_show = """
                    请选择你的进一步选择：
                    （添加）往数据库里面添加内容
                    （删除）删除数据库中的内容
                    （修改）修改数据库中的内容
                    （查询）查询数据库中的内容
                    选择你想要进行的操作:
                    """
        choice = input(choice_show)
        if choice == "添加":
            add_db()
            flag = conti(flag)
        elif choice == "删除":
            del_db()
            flag = conti(flag)
        elif choice == "修改":
            alter()
            flag = conti(flag)
        elif choice == "查询":
            search_db()
            flag = conti(flag)
        else:
            print("你输入有误，请重新输入！")
            flag = conti(flag)
