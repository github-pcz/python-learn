
"""
判断1-100以内有多个偶数，并打印出来

"""

count = 0
for x in range(1, 101):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"1-100共有{count}个偶数")