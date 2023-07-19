
"""
演示自定义模块

__main__变量的作用是
if__main__="__main__"表示，只有当程序是直接右键执行的才会进入到if内部，如果是被导入进去的，则if无法进入

注意:不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导入的

__all__ 变量是为了控制哪些功能可以被导入，没写是默认是全部都可被导入  若写了则表明只可以导入__all__变量中规定的

"""

# 导入自定义的模块
# import my_module1 as mm
# mm.test(1, 2)


# from my_module1 import test
# test(1,2)


# 导入不同模块的的同名功能  后面的会覆盖前面的
# from my_module1 import test
# from my_module2 import test
# test(1, 2)


# __main__变量
# from my_module1 import test  #会直接执行方法


# __all__变量
# import的*只能使用__all__中给定的变量  若是有__all__变量，则限定在变量中的  没有限定  则可以使用所有的
# from my_module1 import *
#
# test_a(1, 3)
# test_b(1, 3)
