
"""



"""

# 有如下的列表对象
my_list = ['程序员', '传智播客', '程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast']


# 定义一个空集合
my_set = set()

# 通过for遍历列表
# 在for中添加到集合
for element in my_list:
    my_set.add(element)

# 得到去重的集合对象并打印输出
print(f'去重后的集合列表为{my_set}')