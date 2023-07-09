"""
演示 if elif else的使用

这个判读是互斥且有顺序的
只要前面有一个是满足的就不会进入到下一个


"""

# height = int(input("请输入你的身高"))
# vip_level = int(input("请输入你的vip等级（1-5）"))
# day = int(input("请告诉我今天几号(1-30)"))
#
# if height < 120:
#     print("身高未超可以游玩")
# elif vip_level > 3:
#     print("你是尊贵的vip用户可以玩")
# elif day == 1:
#     print("今天是1号可以免费玩")
# else:
#     print("您的条件不满足不可以玩")



if int(input("请输入你的身高")) < 120:
    print("身高未超可以游玩")
elif int(input("请输入你的vip等级（1-5）")) > 3:
    print("你是尊贵的vip用户可以玩")
elif int(input("请告诉我今天几号(1-30)")) == 1:
    print("今天是1号可以免费玩")
else:
    print("您的条件不满足不可以玩")