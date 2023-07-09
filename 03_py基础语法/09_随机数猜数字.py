"""
定义一个1-10的随机数，猜三次
"""

import random

num = random.randint(1, 10)
guest_num = int(input("输入你要猜的数字"))

if guest_num == num:
    print(f"第一次你就猜对了，随机的数字是{num}")
else:
    if guest_num > num:
        print("大了")
    else:
        print("小了")

    guest_num = int(input("再次输入你要猜的数字"))
    if guest_num == num:
        print("第二次猜对了")
    else:
        if guest_num > num:
            print("大了")
        else:
            print("小了")

        guest_num = int(input("再次输入你要猜的数字"))
        if guest_num == num:
            print("第三次猜对了")
        else:
            print("三次都猜错了")