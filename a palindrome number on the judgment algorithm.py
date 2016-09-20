# ---*---coding=utf-8---*---
char = input("请输入字符串: ")
num = len(char)//2
if len(char)%2 == 1:
    if char[:num] == char[-1:num:-1]:
        print('回文')
    else:
        print('不是回文')
else:
    if char[:num] == char[-1:num-1:-1]:
        print('回文')
    else:
        print('不是回文')