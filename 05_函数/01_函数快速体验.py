
"""
快读体验函数的使用和开发


"""


# 需求统计字符串的长度，不适用内置的函数

str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数的变量

# count = 0
# for i in str1:
#     count += 1
# print(f"字符串{str1}的长度为{count}")

# count = 0
# for i in str2:
#     count += 1
# print(f"字符串{str2}的长度为{count}")

# count = 0
# for i in str3:
#     count += 1
# print(f"字符串{str3}的长度为{count}")

# 可以使用函数来优化整个过程

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}")

my_len(str1)
my_len(str2)
my_len(str3)

