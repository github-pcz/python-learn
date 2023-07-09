


"""

练习使用for循环打印99乘法表

"""

# 通过外层循环控制行数
for i in range(1, 10):

    # 通过内层循环控制列数
    for j in range(1, i+1):
        # 输出每一行的内容
        print(f"{j} * {i} = {i*j}\t", end='')
    # 换行
    print()




