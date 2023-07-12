

my_str = "itheima itcast boxuegu"

# 统计it的个数
count = my_str.count('it')
print(f'{my_str}中包含it的个数为{count}个')

# 将空格替换为|
new_my_str = my_str.replace(' ', '|')
print(f'替换后的字符串为{new_my_str}')

# 按照|分隔得到列表
my_list = new_my_str.split('|')
print(f"分隔后的列表是{my_list}")


