"""
对列表操作的常用练习
"""

# 定义一个列表并用变量接收他
age_list = [21, 25, 21, 23, 22, 20]

# 追加一个数字31到列表尾部
age_list.append(31)
print(f'追加后的列表为{age_list}')

# 追加一个新列表[29, 33, 30]到列表的尾部
entend_list = [29, 33, 30]
age_list.extend(entend_list)
print(f"追加列表后的列表为{age_list}")

# 取出第一个元素
# 方式1
first_age = age_list.pop(0)
print(f'取出的第一个元素是{first_age}')

# 取出最后一个元素
# last_age = age_list.pop(len(age_list) - 1)
# print(f'取出的最后一个元素为{last_age}')
print(f'取出的最后一个元素为{age_list[-1]}')

# 查找元素31在列表中的位置
print(f"age_list:{age_list}")
index = age_list.index(31)
print(f"index:{index}")
