
"""
演示lambda匿名函数

使用lambda定义
语法：
lambda 传入参数: 函数体（一行代码）

注意事项
匿名函数用于临时构建一个函数，只用一次的场景
匿名函数的定义中，函数体只能写一行代码 要是函数体要写多行代码 不可用lambda匿名函数  应用def定义带名函数


"""

def test_func(compute):
    result = compute(1, 2)
    print(f"结果是{result}")

# 同过lambda匿名函数的形式 将匿名函数作为参数传入
test_func(lambda x, y: x + y)
test_func(lambda x, y: x + y)



