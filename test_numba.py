#!/usr/bin/env python
# coding=utf-8
from numba import jit, njit
import sys
import time


@njit
def test(num):
    ss = 0
    for i in range(num):
        ss += 2 ** i
    return ss


if __name__ == "__main__":
    start = time.time()
    num = int(sys.argv[1])
    ss = test(num)
    print(ss)
    end = time.time()
    print("Run time: ", round(end - start, 2))
