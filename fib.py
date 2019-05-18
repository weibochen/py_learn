#!/usr/bin/env python
# coding=utf-8
import sys
import time
from numba import jit, njit

@njit
def int fib(int num):
    if num < 2:
        return 1
    return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    s = time.time()
    num = int(sys.argv[1])
    fib(num)
    e = time.time()
    print(e - s)
