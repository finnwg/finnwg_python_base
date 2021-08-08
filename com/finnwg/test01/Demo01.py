# -*- coding: utf-8 -*-
# @Time : 2021/4/19 15:13
# @Author : 17853
# @File : Demo01.py
# @Software: PyCharm

# print('hello' + " " + "world")
# print('a' > 'b')
# print(not False)

a = 40
b = 30
c = 50

max = a if (a > b and a > c) else (b if b > c else c)
print(max)

print(1 or 2)
print(0 and 3)

if True :
    print(123)
    print('abc')
print("哈哈")
