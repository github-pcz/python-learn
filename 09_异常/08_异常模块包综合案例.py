
"""
综合练习案例
创建一个自定义包 名为 my_utils
在包内提供两个模块
str_util.py (字符串相关工具，包含如下功能)
    函数 str_reverse(s) 接收传入的字符串 将字符串反转返回
    函数 substr(s, x, y) 按照下标 x , y 对字符串进行切片

file_util.py(文件处理相关工具)
    函数：print_file_info(file_name)  接收传入文件的路径 打印文件的全部内容 若文件不存在 则捕获异常 输出提示信息 通过finally关闭文件对象
    函数：append_to_file(file_name, data) 接收文件路径以及传入的数据 将数据追加写入到文件中

构建出包后 尝试使用自己编写的工具包


"""

import my_utils.str_util
from my_utils.file_util import print_file_info, append_to_file


print(my_utils.str_util.str_reverse("hello"))
print(my_utils.str_util.substr("你猜猜我是谁", 1, 4))

print_file_info("d://bill.txt")
append_to_file("d://haha.txt", "这是我测试追加的内容")



