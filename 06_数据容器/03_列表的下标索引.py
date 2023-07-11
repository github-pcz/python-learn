
"""
列表中的每个元素，都有其位置下标索引，从前向后的方向，从0开始，依次递增


我们只需要按照下标索引，即可取的对应位置的元素

语法：列表[下标索引]

或者反向索引：
也就是从后向前， 从-1开始，依次递减（-1,-2,-3,-4,-5,.....）

"""

name_list = ['zhangsan', 'lisi', 55]

print(name_list[0])
print(name_list[1])
print(name_list[2], type(name_list[2]))
# 错误示范，通过下标索引取数据，一定不能超过下标的范围
# print(name_list[3])


print()

print(name_list[-1])
print(name_list[-2])
print(name_list[-3], type(name_list[-3]))


# 嵌套列表
num_list = [[99, 23, 35], [55, 66, 92]]

# 嵌套列表的取值
print(num_list[1][-2])
