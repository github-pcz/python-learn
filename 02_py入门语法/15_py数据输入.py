
"""
input语句(函数)
前面学习的print是将数据、字面量输出到屏幕上
在python中还有一个对应输入 input,用来获取键盘上的输入

- 数据输出 print
- 数据输入 input

使用很简单
- 使用input获取键盘的输入
- 使用变量接收、存储输入的值即可

tips:input接收的默认全是字符串

"""

# 第一种使用方式
# print("你是谁？")
# name = input()
# print("我是%s" % name)

# 第二种
# name2 = input('你是哪位啊?')
# print(f"我是{name2}")

# 输入数字类型，次处输出的是字符类型
num = input("请告诉我你的银行卡密码")
# print(f"我的银行卡密码是:{num} , 数据的类型是{type(num)}")

# 数字类型转换
num = int(num)
print("我的银行卡密码是：", num, type(num))

