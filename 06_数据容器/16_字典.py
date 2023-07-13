
"""
演示数据容器字典的定义

字典的key和value可以是任意的数据类型 （key不可为字典）
表明字典是可以嵌套的

"""


# 定义字典(定义的两种方式)
# 定义空字典
my_dict1 = {'王力宏': 99, '周杰伦': 88, '林俊杰': 77}
my_dict2 = {}
my_dict3 = dict()

print(f'字典1的内容是{my_dict1}, 类型是{type(my_dict1)}')
print(f'字典2的内容是{my_dict2}, 类型是{type(my_dict2)}')
print(f'字典3的内容是{my_dict3}, 类型是{type(my_dict3)}')


# 定义重复key的字典
my_dict1 = {'王力宏': 99, '王力宏': 88, '林俊杰': 77}
print(f'重复key字典的内容是{my_dict1}')

# 从字典中基于key获取value
my_dict1 = {'王力宏': 99, '周杰伦': 88, '林俊杰': 77}
score = my_dict1["王力宏"]
print(f'王力宏的分数为{score}')

# 定义嵌套字典
stu_score_dict = {
    '王力宏': {
        '语文': 77,
        '数学': 66,
        '英语': 33
    },
    '周杰伦': {
        '语文': 88,
        '数学': 86,
        '英语': 55
    },
    '林俊杰': {
        '语文': 99,
        '数学': 96,
        '英语': 66
    }
}
print(f'学生的考试信息为{stu_score_dict}')

# 看周杰伦的语文信息
zjl_chinese_score = stu_score_dict['周杰伦']['语文']
print(f"周杰伦的语文成绩是：{zjl_chinese_score}")

# 查看林俊杰的英语信息
ljj_english_score = stu_score_dict['林俊杰']['英语']
print(f'林俊杰的英语成绩是:{ljj_english_score}')




