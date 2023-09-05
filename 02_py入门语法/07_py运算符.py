"""
加减乘除  + - * /
取整除 //
取余 %
指数 **
"""

# 加
num1 = 1+1
print(num1)

# 减
num2 = 5 - 2
print(num2)

# 乘
num3 = 6 * 6
print(num3)

# 除  结果是浮点数
num4 = 8.7/2.3
print("num4:", num4)

# 取整除  结果是整数
num5 = 9.234//2.45
print("num5:", num5, type(num5))

# 取余
num6 = 9 % 4
print(num6)


# 幂
num7 = 2 ** 4
print(num7)

# 赋值运算符
num8 = 1 + 2 * 3
print("num8:", num8)

# 复合赋值运算符
num = 1
num += 1
print("num +=", num)

num -= 1
print("num -=", num)

num *= 4
print("num *= ", num)

num /= 2
print("num /=", num)

num = 5
num %= 3
print("num %= ", num)

num = 2
num **= 2
print("num **=", num, type(num))

num = 9
num //= 2
print("num //=", num, type(num))

num = 9
num //= 2.0
print("num //=", num, type(num))

