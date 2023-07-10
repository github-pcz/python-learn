
"""
演示函数的变量的作用域
"""

# 演示局部变量 ，出了函数局部变量就不能使用了

def test_a():
    num = 10
    print(num)

# 调用
test_a()
# print(num)


# 全局变量

# num = 200
#
# def test_b():
#     print(f"test_a{num}")
#
#
# def test_c():
#     num = 100  #局部变量
#     print(f"test_b{num}")
#
# test_b()
# test_c()
# print(num)



num = 200

def test_b():
    print(f"test_a{num}")

# 可以使用global关键字讲局部变量升级为全局变量
def test_c():
    # 全局变量
    global num
    num = 100
    print(f"test_b{num}")

test_b()
test_c()
print(num)