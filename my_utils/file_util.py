

def print_file_info(file_name):
    """
    打印文件的内容
    :param file_name:
    :return: 文件的内容
    """
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print(f"文件的内容信息如下：{content}")
    except Exception as e:
        print(f"读取文件出错的异常信息为：{e}")
    finally:
        # 如果变量是None  表示False  如果有任何内容就是 True
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    追加内容到文件
    :param file_name: 文件路径
    :param data: 追加的数据
    :return: 追加后的结果
    """
    f = open(file_name, "a", encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()


# 测试代码
# if __name__ == '__main__':
    # print_file_info("d://bill.txt")
    # print_file_info("d://bill.txtxx")
    # append_to_file("d://bill.txt", "你好我好大家好")