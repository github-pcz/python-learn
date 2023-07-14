
"""
新建一个文件，读取文件的操作，统计某个字符出现的次数
"""


f = open("d:/test.txt", 'r', encoding="utf-8")


# 方式一  一次性读取所有的内容，计数字符串的个数
# content = f.read()
# num = content.count('h')
# print(f'方式一统计的个数是:{num}')


# 方式2  一行一行的读
# count = 0
# for line in f:
#     count += line.count('h')
# print(f"第二种方式获取h的次数为{count}")




# 方式三
# count = 0
# for line in f:
#     print(f"文件的每一行是:{line}")
#     for element in line:
#         if 'h' == element:
#             count += 1
#
# print(f'文件中出现h的次数为：{count}')
# 关闭文件
f.close()

