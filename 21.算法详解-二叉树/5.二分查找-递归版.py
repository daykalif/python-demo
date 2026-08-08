"""
案例：演示二分查找，递归版．

二分查找:
    概述:
        属于查找类算法，相对效率比较高，时间复杂度为: O(log n)
    前提:
        列表必须是有序的．
    原理: 假设列表是 升序 的
        1．比较 要查找的元素 和 列表的中值，如果一样就返回True，程序结束．
        2．如果 要查找的元素 比 中值小，去前半段(中值前) 查找．
        3．如果 要查找的元素 比 中值大，去后半段(中值后) 查找．
        4．重复上述动作，直至找完．如果都找完了，还找不到，就返回 False

"""


# 1．定义函数 binary_search_recursion()，表示：二分查找
def binary_search_recursion(my_list, target):
    """
    该函数是 二分查找的递归版，实现查找指定元素是否在列表中．
    :param my_list: 待查找的列表
    :param target: 要查找的元素
    :return: True:在, False:不在
    """
    # 1.1 获取列表的长度．
    n = len(my_list)

    # 1.2 判断列表是否为空．
    if n == 0:
        return False

    # 1.3 获取列表的 中值(的索引)
    mid = n // 2

    # 1.4 比较 要查找的元素 和 中值．
    if my_list[mid] == target:
        return True
    elif target < my_list[mid]:
        # 1.5 如果要查找的元素 比 中值小，去前半段(中值前) 查找，递归调用．
        return binary_search_recursion(my_list[:mid], target)
    else:
        # 1.6 如果要查找的元素 比 中值大，去后半段(中值后) 查找，递归调用．
        return binary_search_recursion(my_list[mid + 1:], target)

    # 1.7 走到这里，说明列表都遍历完了，还没找到，返回False
    return False


# 2．测试
if __name__ == '__main__':
    # 2.1 定义列表，记录：元素．
    my_list = [1, 4, 6, 7, 11, 22, 23, 34, 77, 99]
    # 2.2 查找元素．
    print(binary_search_recursion(my_list, 23))  # True
    print(binary_search_recursion(my_list, 25))  # True
