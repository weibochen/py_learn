# coding:utf-8
vowel_char = ['a', 'e', 'i', 'o', 'u']
a = input('请输入英文单词：')
for i in list(a):
	if i.lower() not in vowel_char:
		b = a.replace(i, '')
		print(a)
		print(b + '-' + i + 'ay')
		break
