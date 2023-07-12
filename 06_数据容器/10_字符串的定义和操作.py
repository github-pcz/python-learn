

"""
再识字符串
尽管字符串不像是列表元组那样，一看就是存放了许多数据的容器
但不可否认的是，字符串同样也是容器中的一员

字符串是字符的容器，一个字符串可以存放任意数量的字符

"""

my_str = 'itheima and itcast'

# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]

# 不支持
# my_str[2] = 'H'

print(value)
print(value2)

# 同元组一样，字符串是一个无法修改的数据容器
# 所以修改指定下标的字符 移除特定下标的字符 追加字符等都是无法完成的。非要这样做只能得到一个新的字符串


# index方法
value = my_str.index('and')
print(f'在字符串{my_str}中查找and，其起始下标是{value}')

# replace(被替换的字符串, 想要替换成的字符串)
new_my_str = my_str.replace('it', '程序')
print(new_my_str)

# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(' ')
print(f'将字符串{my_str}进行split分隔后的得到：{my_str_list}, 类型是{type(my_str_list)}')

# strip方法
my_str = '  itheima and itcast  '
new_my_str = my_str.strip()  #不传参数是去除首尾的空格
print(f'字符串被strip后，结果是{new_my_str}')

my_str = '12itheima and itcast21'
new_my_str = my_str.strip('12')  #传参是去除指定的字符串，会将传入的字符串分隔，去除
print(f"字符串被strip('12')后，结果是{new_my_str}")

# 统计字符串中某字符串的出现次数count()
my_str = 'itheima and itcast'
count = my_str.count('it')
print(f'字符串{my_str}中的it出现了{count}次')

# 统计字符串的长度 len()
num = len(my_str)
print(f'my_str字符串的长度是{num}')


# 字符串的遍历
my_str = 'itheima and itcast'
index = 0
while index < len(my_str):
    print(f"{my_str[index]}", end='')
    index += 1


print()

for i in my_str:
    print(f'{i}', end='')










