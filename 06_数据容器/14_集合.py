

"""
集合的演示

集合是无序的，不支持下标的索引访问
但是集合和列表一样是支持修改的，所以我们来看集合的修改方法

无序（不支持下标索引）、不允许重复

set()定义或者{1，2，3}指定值

"""

# 集合的定义
my_set = {'hello', 'nihao', 'hello', 'nihao','hello', 'nihao','hello', 'nihao'}
# 定义空集合
my_set_empty = set()

print(f'my_set的内容是{my_set}，类型是{type(my_set)}')
print(f'my_set_empty的内容是{my_set_empty}，类型是{type(my_set_empty)}')

# 添加新元素
my_set.add("python")
print(f"my_set添加元素后的结果是{my_set}")

# 移除元素
my_set.remove("nihao")
print(f'my_set移除nihao元素后的结果是{my_set}')



my_set = {'hello', 'nihao', 'python'}
# 随机取出一个元素
element = my_set.pop()
print(f"随机取出的元素是{element}, 取出元素后的结果为{my_set}")

# 清空集合
my_set.clear()
print(f'集合被清空后为{my_set}')

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集后的结果为{set3}")
print(f"取出差集后,原有set1的结果为{set1}")
print(f"取出差集后,原有set2的结果为{set2}")


# 消除两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}

set1.difference_update(set2)
print(f"消除差集后，set1的结果为{set1}")
print(f"消除差集后，set2的结果为{set2}")

# 两个集合合并为一个集合
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"2集合合并后的结果为：{set3}")
print(f"合并后集合1为：{set1}")
print(f"合并后集合2为：{set2}")

# 统计集合元素数量len()
set1 = {1, 2, 3, 4, 4, 5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")


# 集合的遍历(集合不支持下标索引遍历)
set1 = {1, 2, 3, 4, 5}
for i in set1:
    print(f'{i}', end='')





