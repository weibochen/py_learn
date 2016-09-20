# ---*---coding=utf-8---*---

#第一种方法
#取右半部分字符反转后与左半部分比较判断

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
		
#第二种方法
#依次取出每个字符进行比较，若有一个不同，便中断程序

char = input("请输入字符串: ")
num = len(char)//2
for i in range(num):
	if char[i] != char[-1-i]:
		print('不是回文')
		break
	elif i == num-1:
		print('回文')
	else:
		pass
		
		
#第三种方法
#直接把字符串反转后与原字符串比较

# ---*---coding=utf-8---*---
char = input("请输入字符串: ")
if char == char[::-1]:
	print('回文结构')
else:
	print('不是回文结构')

