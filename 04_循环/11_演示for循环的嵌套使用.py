"""
演示嵌套应用的for循环
"""
i = 0
for i in range(1, 11):
    print(f"第{i}天向小美表白")

    for j in range(1, 11):
        print(f"第{i}次送的第{j}朵玫瑰")

    print("花送完，开始表白")

print(f"第{i}天表白成功")