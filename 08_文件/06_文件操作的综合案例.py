"""
操作的综合案例
一份账单文件记录了消费信息 文件存储于d盘的bill.txt文件

需求：
- 读取文件
- 将文件写入到bill.txt.bak文件作为备份
- 同时将文件内标记为测试的的数据丢弃

"""
# 需要读取的文件
fr = open("d:/bill.txt", "r", encoding="utf-8")
# 需要写入的文件
fw = open("d:/bill.txt.bak", "w", encoding="utf-8")

# 读取文件遍历
for line in fr:
    line = line.strip()
    # 统计读取的一行数据中是否包含测试
    count = line.count("测试")
    # 若是包含测试，则改行的数据丢弃
    if count > 0:
        continue  #进入下一次循环
    else:
        fw.write(line)
        fw.write("\n")
# 刷新到磁盘文件
fw.flush()

# 文件的关闭
fr.close()
fw.close()
