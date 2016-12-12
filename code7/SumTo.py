# -*- coding=utf-8 -*-
"""定义一个函数加法器"""
def SumTo(aBound):
    theSum = 0
    for i in range(1,aBound+1):
        theSum = theSum + i

    return theSum

print SumTo(4)

print SumTo(100)