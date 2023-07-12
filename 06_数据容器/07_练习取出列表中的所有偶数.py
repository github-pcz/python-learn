
"""
定义一个列表[1,2,3,4,5,6,7,8,9,10]
遍历列表取出所有的偶数存入到一个新列表
使用while和for各遍历一次

"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def while_func(data):
    index = 0
    new_list = []
    while index < len(data):
        element = data[index]
        if element % 2 == 0:
            new_list.append(element)
        index += 1
    return new_list


def for_func(data):
    new_list = []
    for i in data:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


# 使用while操作
print(f"while操作的结果为:{while_func(my_list)}")
print(f"for操作的结果为:{for_func(my_list)}")