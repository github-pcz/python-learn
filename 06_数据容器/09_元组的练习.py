

"""
定义一个元组


"""

# 记录用户的姓名 年龄 爱好
user_info = ('周杰伦', 11, ['football', 'music'])

# 查询年龄的下标位置
index = user_info.index(11)
print(f'年龄的下标位置为{index}')

#查询学生的姓名
user_name = user_info[0]
print(f'学生的姓名为{user_name}')

# 删除学生爱好中的football
del user_info[-1][0]
print(f'删除football后的元素数据为：{user_info}')


# 增加爱好coding到爱好list内
user_info[-1][0] = 'coding'
print(f"添加爱好后的元组为{user_info}")

