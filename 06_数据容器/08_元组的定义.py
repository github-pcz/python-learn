
"""
元组定义：使用小括号定义，里面的元素使用逗号分隔， 数据可以是不同的数据类型

定义元组字面量
(元素，元素，元素)
定义元组变量
变量名称 = (元素，元素， 元素)
定义空元组
变量名称 = ()
变量名称 = tuple()

元组的操作方法
index  按照下表获取元素
count  统计某个元素的个数
len    统计元素的个数

注意事项：
不可修改内容（可以修改内部list的内部元素）

元组特点
和list基本相同，有序 任意数量，允许重复元素，唯一不同在于不可以修改
支持for和while遍历


"""

# 定义元组
t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()

print(f't1的类型是{type(t1)}, 内容是{t1}')
print(f't1的类型是{type(t2)}, 内容是{t2}')
print(f't1的类型是{type(t3)}, 内容是{t3}')

# 定义单个元素的元组  tips 定义单个元素，元素后面得加个逗号
t4 = ('hello')
print(f't4的类型是:{type(t4)}, t4的内容是:{t4}')

t44 = ('hello',)
print(f't5的类型是:{type(t44)}, t5的内容是:{t44}')

# 元素的嵌套
t5 = ( (1, 2, 3), (4, 5, 6))
print(f't5的类型是{type(t5)}, t5的值为{t5}')

# 下标索引去取出内容
element = t5[1][2]
print(f'从嵌套元组中取出的数据为：{element}')
print(f'从嵌套元组中取出的数据为：{t5[-1][-1]}')


# 元组的操作：index查找方法
t6 = ("hello", 'world', 'python', 'java')
index = t6.index('python')
print(f'index 的值为{index}')

# 元组的操作方法：count统计方法
t7 = ('ithiema', 'itcast', 'java', 'python', 'itcast')
count = t7.count('itcast')
print(f'统计itcast字符串的次数{count}')

# len函数统计元素的数量
t8 = ('ithiema', 'itcast', 'java', 'python', 'itcast')
num = len(t8)
print(f't8的长度为{num}')


# 元组的遍历while
index = 0
while index < len(t8):
    print(f'元组的元素有：{t8[index]}')
    index += 1

# 元组的遍历for
for e in t8:
    print(f'元素有{e}')


# 修改元组的内容  报错，禁止休息内容
# t8[0] = 'niaho'

# 定义一个元组, 元组中的内容不可变，但是元组内的非元组数据可以修改
t9 = ('java', 'itheima', [1, 2, 3])
print(f"t9的内容是{t9}")
t9[-1][-1] = 999
print(f'修改后的t9内容是：{t9}')


