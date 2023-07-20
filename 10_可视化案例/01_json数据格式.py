
"""
演示JSON数据和python字典的相互转换

json是一种轻量级的 数据交互格式  采用完全独立于变成语言的文本格式来存储和表示数据 （就是字符串）

python语言使用json有很大的优势  因为json无非就是一个独立的字典或一个内部元素都是字典的列表
所以json 可以直接和python的字典或列表进行无缝转换


数据格式的转化
json.dumps(data)  方法将python数据转化为json  若是有中午需要带上 ensure_ascii=False 参数来确保中文的正常转换
json.loads(data)  方法把json数据转化为了python列表或者字典

"""

import json

# 准备列表 列表内的每个元素 都是字典 将其转换成json

data = [{"name": "张三", "age": 18}, {"name": "李四", "age": 22}, {"name": "王二", "age": 28}]

# 转成json
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)


# 准备字典 将字典转换成json
my_dict = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(my_dict, ensure_ascii=False)
print(type(json_str))
print(json_str)


# 将json字符串转换为python数据类型  [{k: v, k: v}, {k: v, k: v}]

s = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 22}, {"name": "王二", "age": 28}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name": "周杰伦", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)




