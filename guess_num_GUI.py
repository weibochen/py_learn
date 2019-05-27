#!/usr/bin/env python
# coding=utf-8

import tkinter as tk
import random

number = random.randint(0, 1024)
running = True
num = 0
nmaxn = 1024
nminn = 0
# '关闭'按钮时间函数
def eBtnClose(event):
    root.destroy()


# '猜'按钮事件函数
def eBtnGuess(event):
    global nmaxn, nminn, num, running  # 全局变量
    if running:
        val_a = int(entry_a.get())  # 获取猜的数字并转换成数字
        if val_a == number:
            labelqval("恭喜答对了！")
            num += 1
            running = False
            numGuess()  # 显示猜的次数
        elif val_a < number:
            if val_a > nminn:
                nminn = val_a
                num += 1
                labelqval("小了哦，请输入" + str(nminn) + "到" + str(nmaxn) + "之间的任意整数：")
        else:
            if val_a < nmaxn:
                nmaxn = val_a
                num += 1
                labelqval("大了哦，请输入" + str(nminn) + "到" + str(nmaxn) + "之间的任意整数：")
    else:
        labelqval("恭喜你答对了！")


# 显示猜的次数
def numGuess():
    if num == 1:
        labelqval("一次答对！")
    elif num < 10:
        labelqval("很厉害了！")
    else:
        labelqval("您尝试的次数颤过了10次。。。 尝试次数：" + str(num))


def labelqval(vText):
    label_val_q.config(label_val_q, text=vText)  # 修改提示标签文字


if __name__ == "__main__":
    root = tk.Tk(className="猜数字游戏")
    root.geometry()
    label_val_q = tk.Label(root, width="80")
    label_val_q.pack(side="top")

    entry_a = tk.Entry(root, width="40")
    btnGuess = tk.Button(root, text="猜")
    entry_a.pack(side="left")
    entry_a.bind("<Return>", eBtnGuess)
    btnGuess.bind("<Button-1>", eBtnGuess)
    btnGuess.pack(side="left")
    btnClose = tk.Button(root, text="关闭")
    btnClose.bind("<Button-1>", eBtnClose)
    btnClose.pack(side="left")
    labelqval("请输入0到1024之间的任意整数：")
    entry_a.focus_set()
    print(number)
    root.mainloop()
