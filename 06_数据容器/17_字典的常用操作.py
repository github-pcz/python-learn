"""
演示字典的常用操作
"""

my_dict = {'王力宏': 99, '周杰伦': 88, '林俊杰': 77}

# 新增元素
my_dict['张信哲'] = 66
print(f'字典经过新增后的结果是{my_dict}')

# 更新元素
my_dict['周杰伦'] = 33
print(f'字典经过更新后的结果是{my_dict}')

# 删除元素
score = my_dict.pop('周杰伦')
print(f'取出周杰伦的成绩是{score}分，取出分数后的字典是：{my_dict}')

# 清空元素
my_dict.clear()
print(f'清空数据后的字典为{my_dict}')

# 获取全部的key
my_dict = {'王力宏': 99, '周杰伦': 88, '林俊杰': 77}
keys = my_dict.keys()
print(f'字典的全部keys是：{keys}, keys的类型是{type(keys)}')

# 遍历字典
# 方式1
for key in keys:
    value = my_dict[key]
    print(f'字典：{key}的值为{value}')

# 第二种方式
for key in my_dict:
    print(f'2字典：{key}的值为{my_dict[key]}')

# 统计字典内的元素数量 len()函数
num = len(my_dict)
print(f'字典中的元素数量是{num}个')

