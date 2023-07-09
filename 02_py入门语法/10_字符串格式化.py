

name = "pcz"

# 其中的%s  %标识我要占位  s标识将变量变成字符串放到占位的地方
message = "学it就来找 %s" % name
print(message)


# 多个变量的占位，用括号括起来，且中间用都好隔开
# %d 用整数占位 小数位会丢失精度
tel = 110.23
message = "学it就来找 %s  我的电话是 %d" % (name, tel)
print(message)

# %s 标识占用字符串  %d标识占用整数 %f标识占用浮点型
price = 143.99
message = "我这边的学费是 %f " % price
print(message)

