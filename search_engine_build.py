#!/usr/bin/env python
# coding=utf-8

import sys
import urllib
from urllib import request
from collections import deque
import re
from bs4 import BeautifulSoup
import lxml
import sqlite3
import jieba

# 入口
url = 'http://www.zut.edu.cn'

# 待爬取链接的集合，使用广度优先搜索
univisited = deque()

# 已访问的链接集合
visited = set()

univisited.append(url)

conn = sqlite3.connect('viewsu.db')
c = conn.cursor()

# 在创建table之前先吧之前的table删除
c.execute('drop table doc')
c.execute('create table doc(id int primary key, link text)')
c.execute('drop table word')
c.execute('create table word(term varchar(25) primary key, list test)')
conn.commit()
conn.close()
print('开始爬取'.center(50, '-'))
cnt = 0
print('开始。。。')
while univisited():
    url = univisited.popleft()
    visited.add(url)
    cnt += 1
    print('开始爬取第{}个链接'.format(cnt))

    # 爬取网页内容
    try:
        response = request.urlopen(url)
        content = response.read().decode('utf-8')
    except:
        continue
    # 寻找下一个可爬的链接，因为搜索的范围是网站内，所以对链接有格式要求，需要根据具体情况而定
    # 解析网页内容，可能有几种情况，这也是根据这个网站网页的具体情况写的
    soup = BeautifulSoup(content, 'lxml')

    # 本页面所有的新闻链接<a> 
    all_a = soup.fild_all('a', {'class':'c67214'}) 
    for a in all_a:
        #print(a.attrs['herf'])
        x = a.attrs['href']
        if re.match(r'http.+', x):





