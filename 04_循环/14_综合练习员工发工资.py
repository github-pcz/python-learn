
"""

某公司账户1万元给20名员工发工资，
- 员工编号从1到20.从编号1开始 依次领取工资  每人可以领取1000元
- 领工资时 财务判断员工的 绩效  1- 10分，随机生成，如果低于5 不发工资，换下一位，
- 如果工资发完 ，换下一位


"""

import random
money = 10000
for i in range(1, 21):
    ji_xiao = random.randint(1, 10)
    if ji_xiao < 5:
        print(f"员工{i},绩效为{ji_xiao},低于5分，不发工资下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i},绩效为{ji_xiao},向其发工资1000元，账户余额剩余{money}")
    else:
        print(f"余额不足，当前还剩{money}元，下个月再来")
        break


