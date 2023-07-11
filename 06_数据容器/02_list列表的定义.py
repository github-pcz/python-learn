
"""
演示数据容器之list列表
语法：[元素,元素,元素,....]
"""


# 定义一个list列表

# my_list = ['itheima', 'itcast', 'python']
# print(my_list)
# print(type(my_list))

# my_list2 = ['itheima', 666, True]
# print(my_list2)
# print(type(my_list2))

# 定义一个嵌套的列表
my_list3 = [[1, 2, 3], [4, 5, 6]]
print(my_list3)

print(type(my_list3))

# 列表的定义的两种方式
list1 = list()
list2 = []
list3 = [1, 2, 3]

# 什么是元素？
# 数据容器内的每一份数据称之为元素

# 元素的类型有限制吗
# 元素的类型没有任何限制,甚至元素也可以是列表，这样就定义了嵌套列表




for i in my_list3:
    for j in i:
        print(j, end='')
