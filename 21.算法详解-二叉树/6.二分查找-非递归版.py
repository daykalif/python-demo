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


# 1．定义函数 binary_search()，表示：二分查找
def binary_search(my_list, target):
    # 1．定义变量start, end 分别表示列表的开始 和 结束索引．
    start = 0
    end = len(my_list) - 1

    # 2．循环查找，只要条件满足就一直找．
    while start <= end:
        # 3．计算中间值的 索引．
        mid = (start + end) // 2
        # 4．比较 要查找的元素 和 中值．
        if my_list[mid] == target:
            return True
        elif target < my_list[mid]:
            # 5．如果要查找的元素 比 中值小，去前半段(中值前) 查找．即：修改end的
            end = mid - 1
        else:
            # 6．如果要查找的元素 比 中值大，去后半段(中值后) 查找．即：修改start
            start = mid + 1
    # 7．走到这里，说明列表都遍历完了，还没找到，返回False
    return False


# 2．测试
if __name__ == '__main__':
    # 2.1 定义列表，记录：元素．
    my_list = [1, 4, 6, 7, 11, 22, 23, 34, 77, 99]
    # 2.2 查找元素．
    print(binary_search(my_list, 23))  # True
    print(binary_search(my_list, 25))  # True
