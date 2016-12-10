# -*- coding=utf-8 -*-

try:
    a = 2
    b = 0
    c = a / b
except ZeroDivisionError as error:
    print error
