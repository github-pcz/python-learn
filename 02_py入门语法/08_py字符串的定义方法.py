
"""
字符串在python中有多种的定义方式
1、单引号定义法
2、双引号定义法
3、三引号定义法(支持换行操作, 若是使用变量接收就变成字符串，不接收就做为多行注释使用)

"""
name = '张三'
print(name, type(name))
name = "张三"
print(name, type(name))
name = """
        张三
        李四
        王五
       """
print(name, type(name))


# 在字符串中包含双引号
name = 'ni"ha"oa'
print(name)

# 在字符串包含单引号
name = "ni'shi'shui"
print(name)

# 使用转义字符 \ 解除引号的效用
name = "我\'是\"谁"
print(name)

name = '我是\"无敌\'的'
print(name)