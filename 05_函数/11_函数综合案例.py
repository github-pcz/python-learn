

"""
个人银行
"""

money = 5000

name = None

name = input("请输入你的姓名：")


# 定义查询函数

def query(show_header):
    if show_header:
        print("--------查询余额-------")
    print(f"{name}您好，你当前账户余额为{money}元")


# 定义存款

def saving(num):
    global money
    money += num

    print(f"{name}, 您好，您存款{num}员成功")
    #调用查询
    query(False)


def get_money(num):
    global money
    money -= num
    print(f"{name}你好，您本次取钱{num}元")

    # 查余额
    query(False)

def main():
    print("-----------主菜单----------")
    print(f"{name}你好，欢迎来到个人银行")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入你的选择:")


while True:

    main()
    opera = input("请输入你的操作:")

    if opera == "1":
        query(True)
        continue
    if opera == "2":
        money_save = input("请输入存款金额:")
        saving(int(money_save))
        continue
    if opera == "3":
        money_get = input("请输入存款金额:")
        get_money(int(money_get))
        continue
    else:
        print("退出，期待你的下次使用")
        break
