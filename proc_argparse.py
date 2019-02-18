#!/usr/bin/python
# -*- coding=utf8 -*-
"""
# @Author : weber
# @Created Time : 2019-02-17 19:00:27
# @Description : 
"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
