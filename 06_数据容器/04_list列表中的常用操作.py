"""

演示数据容器列表的常用操作

"""

my_list = ['itheima', 'itcast', 'python']

# 查找元素所在的下标索引

index = my_list.index('itcast')
print(index)

# 查找不存在的元素会报错
# index = my_list.index('hello')
# print(index)

# 修改特定下标索引的值
my_list[1] = 'java'
print(f'列表被修改过后值为：{my_list}')

# 指定位置插入新元素
my_list.insert(1, 'best')
print(f'插入元素后的列表为：{my_list}')


# 在列表的尾部进行追加数据
my_list.append("rust")
print(f'追加后的集合为:{my_list}')


# 在列表的尾部追加一批新的元素
other_lit = [1,2,3]
my_list.extend(other_lit)
print(f'追加一批后的数据为:{my_list}')


# 元素的删除（两种方式）
# 方式1  del 列表[下标]
my_list = ['itheima', 'itcast', 'python']
del my_list[0]
print(f'删除后的列表为{my_list}')

# 方式2 列表.pop(下标)
my_list = ['itheima', 'itcast', 'python']
element = my_list.pop(0)
print(f'删除后的列表数据为{my_list}, 删除的值为{element}')


# 删除某元素在列表中的第一匹配项
my_list = ['itheima', 'itcast', 'itheima',  'itcast', 'python']
my_list.remove('itheima')
print(f'通过remove删除后的列表结果为{my_list}')


# 清空列表
my_list = ['itheima', 'itcast', 'itheima',  'itcast', 'python']
my_list.clear()
print(f'列表被清空了，结果是{my_list}')


# 统计某元素在列表内的数量
my_list = ['itheima', 'itcast', 'itheima',  'itcast', 'python']
count = my_list.count('python')
print(f'统计python的次数为:{count}')


# 统计列表中全部的元素数量
my_list = ['itheima', 'itcast', 'itheima',  'itcast', 'python']
print(f'统计列表中所有的元素数量为{len(my_list)}')









