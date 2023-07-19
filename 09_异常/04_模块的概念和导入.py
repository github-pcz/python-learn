

"""
演示模块的导入

模块在使用前需要导入、

[from 模块名] import [模块|类|变量|函数|*] [as 别名]

"""


# 使用import导入time模块使用sleep功能（函数）
# import time   #导入python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)       #通过.就可以使用模块内部的全部功能（类、函数、变量）
# print("我好")


# 使用from导入time的sleep功能（函数）
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")



# 使用*导入time模块的全部功能
# from time import *  # *表示全部功能都要
# print("你好")
# sleep(5)
# print("我好")


# 使用as给特定的功能加别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")














