"""

演示判断语句的嵌套使用

"""

if int(input("输入你的身高")) > 120:
    print("请在输入你的等级")
    if int(input("你的等级是：")) > 3:
        print("你是vip可以玩")
    else:
        print("您不是vip得买票")
else:
    print("未成年免费玩")

