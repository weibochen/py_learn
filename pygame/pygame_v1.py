#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
import sys

def hello_world():
    # 任何Pygame程序均需要执行此语句进行模块的初始化
    pygame.init()
    # 设置窗口模式，（600,480）表示窗口像素
    # 此函数返回一个surface对象，　本程序不使用它，古没保存到对象变量中
    pygame.display.set_mode((600, 480))
    # 设置窗口标题
    pygame.display.set_caption("Hello World!")
    
    # 无限循环，直到接受到窗口关闭事件
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 将surface对象绘制在屏幕上
        pygame.display.update()

if __name__ == "__main__":
    hello_world()
