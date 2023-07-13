

def use_info(name, age, gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


# 掌握位置参数
use_info('小明', 20, '男')

# 掌握关键字参数
use_info(gender='女', name= '小王', age = 18)  #可以不按照参数的定义顺序传参
use_info('甜甜', gender='女', age=22)

# 掌握不定长参数


# 默认值的设置必须放在最后
def use_info(name, age, gender = '男'):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
use_info('小天', 13)
use_info('小天', 13, "女")


# 掌握缺省参数
# 不定长  *号
# 不定长传入的形式参数会作为元组存在，接收不定长的数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是{args}")
    return args

x , y  = user_info(1, 2)
print(f"x,y的值分别是{x},{y}")

user_info(1, 2, 3, '小明', '男孩')

# 不定长  - 关键字不定长 **号  key-word
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是{kwargs}")
    return kwargs

user_info(name="张三", age = 18)
x, y = user_info(name="张三", age = 18)
print(f"kwargs的结果是{x},{y}")