"""
while和for都是循环操作：

想跳过某次循环或者跳出某次循环

对于该场景：提供break和continue，提供直接结束和临时跳过

continue:中断本次循环，直接进入下一次循环，可以用于for和while循环效果一样

"""


# 演示continue

# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")


# 演示continue的嵌套应用

# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")


# 演示break的使用

# for i in range(1, 6):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")


# 演示break的嵌套循环

for i in range(1, 6):
    print("第一句")
    for j in range(1, 6):
        print("第二句")
        break
        print("第三句")
    print("第四句")