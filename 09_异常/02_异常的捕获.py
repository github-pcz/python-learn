
"""
异常捕获的基本语法

try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
[else]:
    未出现异常时应做的事情
[finally]:
    不管出不出现异常都要做的事情

"""

# 基本捕获语法
# try:
#     f = open("d:/abc.txt", "r", encoding='utf-8')
# except:
#     print("出现异常了 因为文件不存在  我将open的模式改为w模式去打开")
#     f = open("d:/abc.txt", "w", encoding='utf-8')


# 捕获指定的异常
# try:
#     print(name)
#     # 1/0
# except NameError as e:
#     print("出现了变量未定义异常")
#     print(e)


# 捕获多个异常
# try:
#     print(name)
#     # 1/0
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量为定义或者 除0的异常")
#     print(e)


# 捕获所有的异常
try:
    # 1/0
    # print(name)
    f = open("d:/123.txt", "r", encoding='utf-8')
    # print("hello")
except Exception as e:
    f = open("d:/123.txt", "w", encoding='utf-8')
    print("出现异常了")
else:
    # 没有异常执行的语句
    print("好高兴没有出现异常")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()




