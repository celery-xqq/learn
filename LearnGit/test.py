# -*- coding: utf-8 -*-
print ("hello world")
print("你好")


def solution(A):
    # write your code in Python 2.7
    A.sort()
    return max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3])