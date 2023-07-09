"""
生成一个随机1-100的整数  通过while循环 配合input 判断输入的数字是否等于随机数
- 无限次机会直到猜中为止
- 每一次猜不中提示是大了还是小了
- 猜完之后提示猜了多少次

"""
import random

# 随机数
num = random.randint(1, 100)
# 累加多少次
count = 0

# 标识
flag = True

while flag:
    guest_num = int(input("请输入你猜想的数字:"))
    count += 1
    if guest_num == num:
        print(f"恭喜你猜对了,共猜了{count}次")
        # 设置为False就是终止循环的条件
        flag = False
    else:
        if guest_num > num:
            print("猜大了")
        else:
            print("猜小了")
print(f"你共猜了多少次{count}")


