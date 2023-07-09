
# 方式1， 直接print输出
print(type(666))
print(type(13.14))
print(type("你好"))

# 方式2  使用变量存储type()语句的结果

int_type = type(666)
float_type = type(13.14)
string_type = type("hello")

print(int_type)
print(float_type)
print(string_type)

# 方式3 使用type() 查看变量中存储的数据类型
money = 666
print(type(money))

score = 13.14
print(type(score))

name = "张三"
print(type(name))

fee = 13.14
print(fee)
print("fee type", type(fee))

fee = "学费"
print(fee)
print("fee type", type(fee))


