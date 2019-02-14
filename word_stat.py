# ---*---coding=utf-8---*---
import re

f = open('test.txt', 'r')
fr = f.read()
items = re.findall(r'[a-zA-Z]+', fr)#排除所有不是英文字母的字符
f.close()
print(items)

num = 0
counters = {}
for item in items:
	num += 1
	if item in counters:
		counters[item] += 1
	else:
		counters[item] = 1

print(num)

print(counters.items())#把字典变成列表
print([(counter, word) for word, counter in counters.items()])

seq = sorted([(counter, word) for word, counter in counters.items()], reverse=1)
print(seq)
print(seq[0][1])
