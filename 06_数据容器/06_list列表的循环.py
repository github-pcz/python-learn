

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    循环控制变量通过下标索引来控制，默认0
    每一次循环将下标索引变量加一
    循环条件：当下标索引变量<列表的元素数量
    :return:
    """

    # 定义一个变量来标记列表的下标
    index = 0
    my_list = [2, 5, 7, 2, 9, 0]
    while index < len(my_list):
        element = my_list[index]
        print(f"元素是：{element}")
        index += 1

list_while_func()


def list_for_func():
    """
    for循环遍历列表
    :return:
    """
    my_list = [2, 5, 7, 2, 9, 0]
    for i in my_list:
        print(f'列表中的元素为：{i}')

list_for_func()

