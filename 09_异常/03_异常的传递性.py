"""
异常是具有传递性的
 func1有异常没捕获
 func2调用func1
 main调用func2 并对异常进行捕获这时也能对异常进行捕获  这就是异常的传递性

"""


def func1():
    print("func1 开始执行")
    num = 1/0
    print("func1 结束执行")

def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了  异常的信息为 {e}")


main()