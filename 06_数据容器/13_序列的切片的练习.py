

# 有字符串"万过薪月，nohtyP学"  得到：黑马程序员

my_str = "万过薪月,员序程马黑来,nohtyP学"
# 开始和结束的也得反着写
new_str = my_str[9:4:-1]
new_str2 = my_str[-10:-15:-1]
new_str3 = my_str[9:4:-1]
print(f"new_str:{new_str}")
print(f"new_str2:{new_str2}")
print(f"new_str3:{new_str3}")
new_str_list = my_str.split(',')
new_str2 = new_str_list[1].replace('来', '')

new_str4 = new_str2[::-1]
print(f"new_str3:{new_str4}")

print("-------------------")

my_str = "万过薪月,员序程马黑来,nohtyP学"
# 先倒序再切片
str1 = my_str[::-1][9:14]
print(str1)

# 先切片再倒序
str2 = my_str[5:10][::-1]
print(str2)

# 分隔字符串
str3 = my_str.split(",")[1].replace('来', '')[::-1]
print(str3)