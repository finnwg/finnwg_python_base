# -*- coding: utf-8 -*-
# @Time : 2021/8/9 20:31
# @Author : 17853
# @File : Demo02.py
# @Software: PyCharm

# 序列(sequence)
# 序列是Python中最基本的一种数据结构
# 数据结构指计算机中数据存储的方式
# 序列用于保存一组有序的数据，所有的数据在序列中都有一个唯一的位置（索引）
#     并且序列中的数据会按照添加的顺序来分配索引
# 序列的分类：
#     可变序列：
#         > 列表（list）
#     不可变序列：
#         > 字符串（str）
#         > 元组（tuple）
#     刚刚我们所讲所有操作都是序列的通用操作


# 创建一个列表
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

print('修改前：', stus)

# 修改列表中的的元素
# 直接通过索引来修改元素
stus[0] = 'sunwukong'

print('修改后：', stus)


# 通过del来删除元素
del stus[2]
# print(stus)

# 通过切片来修改列表
# 在给切片进行赋值时，只能使用序列
stus[0:2] = ['牛魔王', '红孩儿', '铁扇公主']  # 使用新元素替换旧元素
stus[0:0] = ['二郎神']     # 向索引为0的位置插入元素
# 当设置了步长时，序列中元素的个数必须和切片中元素的个数一致
stus[::2] = ['黄袍怪'] * 4    # ValueError: attempt to assign sequence of size 1 to extended slice of size 4
# print(stus)


# 通过切片来删除元素
del stus[0:2]
del stus[::2]
stus[1:3] = []
# print(stus)


# 以上操作只适用于可变序列
s = 'hello'
# s[1] = 'a'      # TypeError: 'str' object does not support item assignment
# 不可变序列，无法通过索引来修改
# 可以通过list（）函数将其他的序列转换为list
s = list(s)
print(s)





