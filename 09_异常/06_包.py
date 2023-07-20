
"""

演示python的包

什么是python包
包就是一个文件夹  里面可以存放好多的python的模块（代码文件） 通过包 在逻辑上将一批模块归为一类 方便使用

__init_.py文件的作用
创建包会默认自动创建的文件 通过这个文件来表示一个文件夹是python的包而非普通的文件夹

__all__变量的作用
同模块中学习到的作用一样 控制import * 能够导入的内容


"""
import my_package.my_module1
# 创建一个包 my_package
# 导入自定义包的模块 并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()



# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.info_print1()
# my_module2.info_print2()


# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()


# 通过__all__变量，控制import *
from my_package import *
my_module1.info_print1()