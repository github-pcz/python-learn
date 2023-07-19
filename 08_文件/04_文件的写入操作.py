
"""

演示文件的写入  模式是 w

1、打开文件 open
2、写入文件 write
3、内容刷新 flush

注意：
直接调用write内容并未真正的写入文件 而是会积攒在程序的内存之中， 称之为缓冲区
直接调用flush的时候才会将内容写到磁盘中
这样是为了避免频繁的操作磁盘 导致效率下降 （攒一堆一次性的写入）

"""
import time
# 打开文件 不存在的文件 r   w   a
# f = open("d:/python.txt", "w", encoding='utf-8')
# # write写入
# f.write("hello word")
# # time.sleep(50000)
# # flush 刷新 将内存中积攒的内容写入到硬盘的文件中
# f.flush()
# # 关闭  自带flush的功能
# f.close()

# 打开一个存在的文件  会清空文件中原有的内容
f = open("d:/python.txt", "w", encoding='utf-8')
# write写入
f.write("who are you")
# time.sleep(50000)
# flush 刷新 将内存中积攒的内容写入到硬盘的文件中
f.flush()
# 关闭
f.close()






