#第一种方法
a = input("请输入任意字符串： ")
b = a[::-1]
print(b)

#第二种方法
a = input("请输入任意字符串： ")
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]  
print(b)

#第三种方法
a = input("请输入任意字符串： ")
c = reversed(a)
print(c)
b = "".join(reversed(a))
print(b)

#第四种方法
a = input("请输入任意字符串： ")
b = list(a)
print(b)
b.reverse()
print(b)
b = "".join(b)
print(b)

#第五种方法
from functools import reduce
a = input("请输入任意字符串： ")
b = reduce(lambda x, y: x + y, a)
b = reduce(lambda x, y: y + x, a)
print(b)

