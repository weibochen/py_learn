#!/usr/bin/env python
# coding=utf-8

import requests
import json
import itchat
from itchat.content import *

itchat.auto_login()

def tuling(info):
    appkey = 'feed526ff94e4923b2e6c67e57caca38'
    url = 'http://www.tuling123.com/openapi/api?key=%s&info=%s'%(appkey, info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

def group_id(name):
    df = itchat.search_chatrooms(name = name)
    return df[0]['UserName']

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s' % tuling(msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    item = group_id(u'想要设置的群的名称')
    if msg['FromUserName'] == item:
        itchat.send(u'%s' % tuling(msg['Text']), item)

itchat.run()
