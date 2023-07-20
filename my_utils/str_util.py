

def str_reverse(s):
    """
    将传入的字符内容反转
    :param s: 参数
    :return: 反转后的内容
    """
    return s[::-1]

def substr(s, x, y):
    """
    裁剪指定位置的字符串
    :param s: 字符串
    :param x: 开始位置
    :param y: 结束位置
    :return: 裁剪后的字符串
    """
    return s[x:y]


# 测试代码
# if __name__ == '__main__':
#     print(str_reverse("hello"))
#     print(substr("hello", 1, 3))