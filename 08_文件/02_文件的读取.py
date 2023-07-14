

"""
演示文件的读取
"""
import time

# 打开文件

f = open('D:/test.txt', 'r', encoding='UTF-8')
print(type(f))

# 读取文件
# print(f'读取10个字节的结果是:{f.read(10)}')
print(f'读取全部内容的结果是:{f.read()}, 类型是：{type(f.read())}')
print('--------------------------------------')

# 读取文件 readLines
# lines = f.readlines()
# print(f'lines对象的类型是:{type(lines)}')    #读取文件的全部行 并封装到列表中
# print(f"liens对象的内容是:{lines}")

# 读取文件 readLine

# line1 = f.readline()
# print(f'line1对象的类型是:{type(line1)}')    #读取文件的一行 并封装到列表中
# print(f"line1对象的内容是:{line1}")

# line2 = f.readline()
# print(f'line2对象的类型是:{type(line2)}')    #读取文件的一行 并封装到列表中
# print(f"line2对象的内容是:{line2}")

# line3 = f.readline()
# print(f'line3对象的类型是:{type(line3)}')    #读取文件的一行 并封装到列表中
# print(f"line3对象的内容是:{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行的文件是：{line}")

# time.sleep(500000)

# 文件的关闭
# f.close()
# time.sleep(500000)

# with open 语法操作文件  执行完文件之后会自动将文件给关闭了
# with open('D:/test.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         print(f'每一行的数据是：{line}')



