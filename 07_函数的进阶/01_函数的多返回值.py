
"""

多个返回值


"""

# 按照返回值的顺序 写对应顺序的多个变量接收即可
# 变量之间用逗号分隔
# 支持不同类型的return

def test_return():
    return 1, 'hello', True

x, y, z= test_return()

print(f'函数返回的多个值为{x},{y},{z}')