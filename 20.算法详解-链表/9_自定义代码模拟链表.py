"""
顺序表和链表的比较
链表与顺序表的各种操作复杂度如下所示：

操作	                        链表	                顺序表
访问元素	                    O(n)	            O(1)
在头部插入 / 删除	            O(1)	            O(n)
在尾部插入 / 删除	            O(n)	            O(1)
在中间插入 / 删除	            O(n)	            O(n)
"""

"""
案例：自定义代码模拟链表

链表介绍：
    概述:
        它属于数据结构之 线性结构的一种，每个节点都只能有 1个前驱 和 1个后继节点。
    作用:
        用于优化顺序表的弊端(如果没有足够的连续的内存空间，会导致扩容失败)
        链表扩容时，有地儿就行，连不连续无所谓。
    组成:
        由 节点 组成，其中节点由 元素域(数值域) 和 链接域(地址域)组成。
    分类:
        根据 节点类型不同，链表主要分为:
        单向链表：节点由1个数值域 和 1个地址域组成，前边节点的地址域存储的是后续节点的地址，最后1个节点的地址域为 None
        单向循环链表:
        双向链表:
        双向循环链表:
        详见今日随堂图片。

自定义代码模拟链表，思路分析：
1. 自定义SingleNode类，表示 节点类。
    属性：
        item    数值域(元素域)
        next    地址域(链接域)

2. 自定义SingleLinkedList类，表示：链表
    属性：
        head  表示头结点，指向第1个节点。
    行为：
        isEmpty()        判断链表是否为空
        length()         获取链表长度的
        travel()         遍历链表
        is_empty(self)   链表是否为空
        length(self)     链表长度
        travel(self.)    遍历整个链表
        add(self, item)  链表头部添加元素
        append(self, item) 链表尾部添加元素
        insert(self, pos, item) 指定位置添加元素
        remove(self, item) 删除节点
        search(self, item) 查找节点是否存在

3.测试
"""


# 1.自定义SingleNode类，表示 节点类。
class SingleNode:
    # 初始化属性
    def __init__(self, item):
        self.item = item  # 元素域（数值域）
        self.next = None  # 链接域（地址域）


# 2. 自定义SingleLinkedList类，表示：链表
class SingleLinkedList:
    # 1. 初始化属性.
    def __init__(self, node=None):
        self.head = node  # 链表的 头结点，指向第1个节点.

    # 2. is_empty(self) 链表是否为空
    def is_empty(self):
        # 思路：判断头结点是否为None，如果为None，则链表为空
        """
            # 写法一： if else
            if self.head is None:
                return True
            else:
                return False

            # 写法二： 三元表达式
            return True if self.head is None else False

            # 写法四：（能用，但是不推荐）
            return self.head == None
        """

        # 写法三：
        return self.head is None

    # 3. length(self) 链表长度
    def length(self):
        # 3.1 创建游标(表示当前节点)，默认从头结点开始.
        cur = self.head
        # 3.2 定义计数器.
        count = 0
        # 3.3 开始遍历，只要当前节点不为空，就一直循环.
        while cur is not None:
            # 3.4 计数器 + 1，然后 cur指向下个节点.
            count += 1
            cur = cur.next
        # 3.5 循环结束，列表长度已经获取了，返回即可.
        return count

    # 4. travel(self.) 遍历整个链表
    def travel(self):
        # 4.1 创建游标(表示当前节点)，默认从头结点开始.
        cur = self.head
        # 4.2 只要当前节点不为空，就一直循环.
        while cur is not None:
            # 4.3 打印当前节点的数值域.
            print(f'数值域: {cur.item}')
            # 4.4 修改当前节点，然后 cur指向下个节点.
            cur = cur.next

    # 5. add(self, item) 链表【头部】添加元素
    def add(self, item):
        # 5.1 创建新节点
        new_node = SingleNode(item)
        # 5.2 设置新节点的地址域 指向 头结点
        new_node.next = self.head
        # 5.3 设置头结点指向新节点.
        self.head = new_node
        print(f'【头部】添加的元素为: {new_node.item}')

    # 6. append(self, item) 链表【尾部】添加元素
    def append(self, item):
        # 6.1 封装新节点.
        new_node = SingleNode(item)
        # 6.2 判断列表如果为空，直接设置当前节点为头结点即可.
        if self.is_empty():
            self.head = new_node
        else:
            # 6.3 走到这里，说明链表不为空，需要找到尾结点.
            # 6.4 创建游标(表示当前节点)，默认从头结点开始.
            cur = self.head
            # 6.4 开始遍历，只要当前节点不为空，就一直循环.
            while cur.next is not None:
                # 6.5 游标后移.
                cur = cur.next
            # 6.6 走到这里 cur就是最后1个节点，设置它的地址域指向新节点即可
            cur.next = new_node
            print(f'【尾部】添加的元素为: {new_node.item}')

    # 7. insert(self, pos, item) 【指定位置】添加元素
    def insert(self, pos, item):
        # 7.1 判断索引是否越界，如果 ≤ 0 往前加.
        if pos <= 0:
            self.add(item)
        # 7.2 如果索引是 ≥ 长度的，就往后加.
        elif pos >= self.length():
            self.append(item)
        else:
            # 7.3 走这里，说明索引合法，即：中间的值。需找到插入位置前的哪个元素.
            # 7,4 创建游标(表示当前节点)，默认从头结点开始.
            cur = self.head
            # 7.5 定义变量，记录当前节点的位置(可以理解为索引，但是不是，因为链表没有索引)
            count = 0
            # 7.6 开始遍历，只要 当前节点的位置 < pos ，就一直循环.
            while count < pos - 1:
                # 7.7 走这里，说明还没有找到插入前的哪个节点，就：节点后移，计数器+1
                cur = cur.next
                count += 1
            # 7.8 走到这里，cur就是插入位置前的那个节点。先封装内容为新节点.
            new_node = SingleNode(item)
            # 7.9 设置 新节点的地址域 指向 插入位置前那个节点的 地址域
            new_node.next = cur.next
            # 7.10 设置 插入位置前的那个节点的地址域 指向 新节点
            cur.next = new_node
        print(f'【指定位置】添加的元素为: {new_node.item}')

    # 8. remove(self, item) 删除节点
    def remove(self, item):
        # 8.1 创建游标(表示当前节点)，默认从头结点开始.
        cur = self.head
        # 8.2 定义变量，记录要删除节点的 前驱节点.
        pre = None
        # 8.3 开始遍历，只要 当前节点不为空，就一直循环.
        while cur is not None:
            # 8.4 判断当前节点是否是要删除的节点.
            if cur.item == item:
                # 8.5 判断要删除的节点是否是头结点.
                if cur == self.head:
                    # 8.6 直接设置头结点为 当前节点的下个节点即可.
                    self.head = cur.next
                else:
                    # 8.7 走到这里,说明要删除的节点不是头结点.直接设置 前驱节点的地址域 指向 当前节点的地址域即可。
                    pre.next = cur.next
                    cur.next = None  # 删除节点，断开连接
                # 8.8 走这里，说明删除成功，直接返回结果即可，即：结束程序。
                print(f'【删除】的元素为: {cur.item}')
                return
            else:
                # 8.9 走这里，说明当前节点不是要删除的节点，就：游标后移，前驱节点后移.
                pre = cur
                cur = cur.next

    # 9. search(self, item) 查找节点是否存在
    def search(self, item):
        # 9.1 创建游标(表示当前节点)，默认从头结点开始.
        cur = self.head
        # 9.2 只要当前节点不为空，就一直循环.
        while cur is not None:
            # 9.3 判断当前节点是否是要找的节点，如果是就返回True
            if cur.item == item:
                return True
            # 9.4 如果当前节点不是要找的节点，就：游标后移.
            cur = cur.next
        # 9.5 走到这里，所有节点都找完了，还没找到，return False
        return False


# 3. 在main中测试
if __name__ == '__main__':
    # 3.1 测试节点类.
    node1 = SingleNode(10)
    # 3.2 打印当前节点的 元素域(数值域) 和 链接域(地址域)
    print(f'元素域(数值域): {node1.item}')  # 10
    print(f'链接域(地址域): {node1.next}')  # None
    print(f'node1对象: {node1}')  # 输出地址值；    也可以重写str魔法方法，改为打印属性值
    print(f'node1的类型: {type(node1)}')

    print('-' * 30)

    # 3.2 测试链表类.
    my_linkedlist = SingleLinkedList(node1)
    print(f'头结点为: {my_linkedlist.head}')
    print(f'头结点的元素域: {my_linkedlist.head.item}')  # 10
    print(f'头结点的地址域: {my_linkedlist.head.next}')  # None

    print('-' * 30)

    # 4. 完整测试.
    # 4.1 创建节点类.
    node2 = SingleNode('乔峰')

    # 4.2 将上述的节点作为头结点，创建链表.
    my_linkdlist = SingleLinkedList(node2)

    # 4.3 打印头结点.
    print(f'头结点为: {my_linkdlist.head}')
    print(f'头结点的数值域为: {my_linkdlist.head.item}')
    print('-' * 23)

    # 4.4 测试链表是否为空.
    print(my_linkdlist.is_empty())
    print('-' * 23)

    # 4.7 测试（往头部）添加元素.
    my_linkdlist.add('令狐冲')
    my_linkdlist.add('段誉')
    print('-' * 23)

    my_linkdlist.append('王语嫣')
    my_linkdlist.append('孟婉清')
    print('-' * 23)

    # 4.8 测试（指定位置）添加元素.
    my_linkdlist.insert(2, '小龙女')
    print('-' * 23)

    # 4.9 测试删除元素.
    my_linkdlist.remove('段誉')
    my_linkdlist.remove('乔峰')
    my_linkdlist.remove('孟婉清')
    print('-' * 23)

    # 4.10 测试查找元素是否存在.
    print(my_linkdlist.search('王语嫣'))
    print(my_linkdlist.search('孟婉清'))
    print('-' * 23)

    # 4.5 测试链表长度.
    print(f'链表长度为: {my_linkdlist.length()}')
    print('-' * 23)

    # 4.6 测试遍历链表.
    my_linkdlist.travel()
    print('-' * 23)
