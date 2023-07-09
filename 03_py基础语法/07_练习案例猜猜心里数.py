"""

定义一个心里数

基于input输入猜想的数，通过if elif else 判断猜的是否正确

"""

num = 5
if int(input("猜猜我想的数是几?")) == num:
    print("恭喜一次猜对")
elif int(input("再猜一次")) == num:
    print("猜对了")
elif int(input("最后再猜一次")) == num:
    print("恭喜最后一次猜对了")
else:
    print("很遗憾三次都错了")
