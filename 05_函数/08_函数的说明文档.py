
"""
演示对函数的文档说明
"""

def add(x, y):
    """
    接收两个参数进行想加的操作
    :param x: 想加的其中一个数
    :param y: 相加的另外一个数
    :return: 想加的结果
    """
    result = x + y
    print(f"两数想加的结果为：{result}")
    return result

add(5, 6)

