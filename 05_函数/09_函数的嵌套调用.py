
"""
演示函数的嵌套调用
"""


def func_b():
    print("--b--")


def func_a():
    print("--a--")

    func_b()

    print("--c--")

# 调用a
func_a()