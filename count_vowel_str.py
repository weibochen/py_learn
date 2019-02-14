# coding:utf-8
vowel_char = set('aeiou')
a = input('请输入英文单词：')
a = a.lower()
num = 0
for i in a:
	if i in vowel_char:
		num += 1
print(num)

for b in vowel_char:
	print(b, ':', a.count(b))
