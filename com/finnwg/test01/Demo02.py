# -*- coding: utf-8 -*-
# @Time : 2021/4/20 15:01
# @Author : 17853
# @File : Demo02.py
# @Software: PyCharm

# a = input("请输入任意字符")
# if a == 'admin' :
#     print("你说的对")

# age = int(input("请输入你的年龄 : "))
# if age >= 18 :
#     print("你已经成年了")
# else :
#     print("你是未成年")
# if 0 <= age <= 17 :
#     print("你是未成年")
# elif 18 <= age <= 45 :
#     print("你是成年人")
# elif 46 <= age <= 60 :
#     print("油腻大叔")
# else :
#     print("你是老年人")
#

# i = int(input("请输入一个整数"))
# if i % 2 == 0 :
#     print('%d 是一个偶数' %i)
# else :
#     print(f"{i} 是一个奇数")
# a = 123
# print('a = ', a)

# year = int(input("请输入年份："))
# if (year % 4 == 0 and not(year % 100 == 0)) or year % 400 == 0 :
#     print(f'{year}是闰年')
# else :
#     print(f'{year}不是闰年')

# dog_age = float(input("请输入狗狗的年龄:"))
# if dog_age < 0.0 or dog_age > 20.0 :
#     print("请输入正确的年龄")
# else :
#     if dog_age <= 2.0 :
#         print(f"狗狗的年龄相当于人类的{dog_age * 10.5}岁")
#     else :
#         print(f"狗狗的年龄相当于人类的{2.0 * 10.5 + (dog_age - 2.0) * 4.0}岁")

# score = float(input("请输入小明的成绩："))
# if score < 0 or score > 100 :
#     print("请输入正确的成绩")
# else :
#     if score == 100:
#         print("奖励一辆BMW")
#     elif 80 <= score <= 99:
#         print("奖励一台iphone")
#     elif 60 <= score <= 79:
#         print("奖励一本参考书")
#     else:
#         print("什么奖励都没有")

# height = int(input("请输入身高，以厘米为单位"))
# money = int(input("请输入财富，以万为单位"))
# looks = int(input("请输入相貌分数"))
# if height > 180 and money > 1000 and looks > 500 :
#     print("我一定嫁给他")
# elif height > 180 or money > 1000 or looks > 500 :
#     print("嫁吧，比上不足，比下有余")
# else :
#     print("不嫁")

# while True :
#     print(True)

# i = 0
# sum = 0
# while i <= 100 :
#     if i % 2 != 0 :
#         sum += i
#     i += 1
# print(f"100以内所有奇数的和为{sum}")

# i = 0
# sum = 0
# count = 0
# while i < 100 :
#     if i % 7 == 0 :
#         sum += i
#         count += 1
#     i += 1
# print(f"{count} and {sum}")

# i = 100
# while i < 1000 :
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     # print(ge + shi + bai)
#     if ge ** 3 + shi ** 3 + bai ** 3 == i :
#         print(i)
#     i += 1

# i = int(input("请输入任意一个大于2的整数"))
# flag = True
# j = 2
# while j < i :
#     if i % j == 0 :
#        flag = False
#     j += 1
# if flag :
#     print(f'{i}是质数')
# else :
#     print(f'{i}不是质数')

# i = 2
# while i <= 100 :
#     flag = True
#     j = 2
#     while j < i :
#         if i % j == 0 :
#             flag = False
#         j += 1
#     if flag :
#         # print(f'{i}是质数')
#         print(f'{i}',end = ',')
#     # else :
#     #     print(f'{i}不是质数')
#     i += 1


# i = 1
# while i <= 9 :
#     j = 1
#     while j <= i :
#         print(f'{j} * {i} = {i * j}' , end = "\t")
#         j += 1
#     i += 1
#     print('')





