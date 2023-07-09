
"""
演示布尔类型的定义
以及比较运算符的运用
"""

# 定义变量存储布尔类型的数据

bool_1 = True
bool_2 = False

print(f"bool_1变量的内容是{bool_1}, 类型是{type(bool_1)}, bool_2变量的内容是{bool_2}, 类型是{type(bool_2)}")

# 比较运算符的使用
# == , != , > , < , >= , <=

# 演示内容相等的比较
num1 = 10
num2 = 10
print(f"10 == 10 的结果是{num1 == num2}")

num1 = 10
num2 = 15
print(f"num1 != num2的结果是{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima 的结果为{name1 == name2}")

num1 = 10
num2 = 5
print(f"num1 > num2结果为{num1 > num2}")
print(f"num1 < num2结果为{num1 < num2}")

num1 = 10
num2 = 11
print(f"num1 >= num2结果为{num1 >= num2}")
print(f"num1 <= num2结果为{num1 <= num2}")


