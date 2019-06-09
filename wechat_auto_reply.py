#!/usr/bin/env python
# coding=utf-8

import itchat
from itchat.content import *
import time

@itchat.msg_register('Text')
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        print(msg['CreateTime'])
        itchat.send_msg(u"[%s]收到好友@ %s的信息: %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])), 
                                                           msg['User']['NickName'], 
                                                           msg['Text']),
                                                           'filehelper')
        return u'我现在不在，一会儿联系您。\n已经收到您的信息: %s 。\n' % (msg['Text'])

if __name__ == "__main__":
    itchat.auto_login()
    myUserName = itchat.get_friends(update = True)[0]["UserName"]
    itchat.run()
