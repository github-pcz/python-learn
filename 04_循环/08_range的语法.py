
"""
range语法的演示
range的功能主要就是获取一个数字序列
"""

# 方式一
# 获取从0到num的整数，不含num
for x in range(5):
    print(x, end='')
print()

# 方式二
# 左闭又开
for x in range(5, 10):
    print(x, end='')
print()


# 方式三
# 左闭又开，步进为2，
for x in range(5, 10, 2):
    print(x, end='')
print()