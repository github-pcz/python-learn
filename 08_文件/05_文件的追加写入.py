"""
演示文件的追加写入
模式是  a  append

注意：不存在的文件会创建  已存在的文件会在文件后面直接追加内容

"""

# 打开不存在的文件
# f = open("d:/python.txt", "a", encoding="utf-8")
# # write写入
# f.write("你是谁")
# # flush 刷新
# f.flush()
# # 关闭 close
# f.close()


f = open("d:/python.txt", "a", encoding="utf-8")
# write写入
f.write("\n你是谁啊？")
# flush 刷新
f.flush()
# 关闭 close
f.close()




