"""
案例：自定义代码，模拟二叉树．

树结构解释:
    概述:
        它属于数据结构的一种，属于 非线性结构(N个前驱，N个后继)
    特点:
        1．有且只能有1个根节点．
        2．每个节点都可以有1个父节点 及 任意个子节点，根节点除外(没有父节点)．
        3．没有子节点的节点，称之为：叶子节点．
    常用分类:
        无序树:
        有序树:
        二叉树:
            完全二叉树：最后一层不满，其它都是满的．
            满二叉树：都是满的．
            非完全二叉树：中间有断的．
            平衡二叉树：任意节点的两个子树的高度差不超过1
        我们用的最多的就是：二叉树
    存储:
        顺序存储：既要存储数据，又要存储节点的关系．
        链式存储：采用节点(item, lchild, rchild)的方式，形成链表来存储
"""


# 1．定义Node类，表示二叉树的节点．
class Node:
    # 初始化属性
    def __init__(self, item):
        self.item = item  # 元素域，即：节点存储的数据．
        self.lchild = None  # 左子节点
        self.rchild = None  # 右子节点


# 2．自定义BinaryTree类，表示二叉树
class BinaryTree:
    # 2.1 初始化属性．
    def __init__(self, node=None):
        self.root = node  # 根节点，类似于：链表的 self.head 头节点

    # 2.2 定义add函数，表示：添加节点
    # 2.2 定义add函数，表示：添加节点
    def add(self, item):
        # 1．把item封装成节点
        new_node = Node(item)
        # 2．判断根节点是否为空，如果为空，设置当前节点为根节点
        if self.root is None:
            self.root = new_node
            return  # 核心
        # 3．创建队列，添加 根节点到队列中．
        queue = []
        queue.append(self.root)
        # 4．通过 while True死循环，找到空缺的节点位置．
        while True:
            # 5．获取队列的第1个元素．
            node = queue.pop(0)
            # 6．判断当前节点的左子树是否为空．
            if node.lchild is None:
                # 6.1 把新节点设置为当前节点的左子树，并结束．
                node.lchild = new_node
                return
            else:
                # 6.2 走这里，说明左子树不为空，把当前节点的左子树，添加到队列中．
                queue.append(node.lchild)

            # 7．判断当前节点的右子树是否为空．
            if node.rchild is None:
                # 7.1 把新节点设置为当前节点的右子树，并结束．
                node.rchild = new_node
                return
            else:
                # 7.2 走这里，说明右子树不为空，把当前节点的右子树，添加到队列中．
                queue.append(node.rchild)

    # 2.3 定义breadth_travel()函数，表示：广度优先遍历(逐层遍历，一层一层遍历)
    def breadth_travel(self):
        # 1．判断根节点是否为空．
        if self.root is None:
            return
        # 2．创建队列，添加 根节点到队列中．
        queue = []
        queue.append(self.root)
        # 3．循环打印内容，只要队列不为空，就一直遍历．
        while len(queue) != 0:
            # 4．获取队列的第1个元素．
            node = queue.pop(0)
            # 5．打印该节点的 元素域．
            print(node.item, end=' ')
            # 6．判断当前节点的左子树是否存在，存在就添加到队列中．
            if node.lchild is not None:
                queue.append(node.lchild)

            # 7．判断当前节点的右子树是否存在，存在就添加到队列中．
            if node.rchild is not None:
                queue.append(node.rchild)

    # 2.4 定义preorder_travel()函数，表示：深度优先之先序遍历(根左右)
    def preorder_travel(self, root):
        # 1．判断根节点是否不为空，不为空就打印．
        if root is not None:
            # 2．打印根节点的 元素域
            print(root.item, end=' ')
            # 3．递归遍历左子树．
            self.preorder_travel(root.lchild)
            # 4．递归遍历右子树．
            self.preorder_travel(root.rchild)

    # 2.5 定义inorder_travel()函数，表示：深度优先之中序遍历(左根右)
    def inorder_travel(self, root):
        # 1．判断根节点是否不为空，不为空就打印．
        if root is not None:
            # 2．递归遍历左子树．
            self.inorder_travel(root.lchild)
            # 3．打印根节点的 元素域
            print(root.item, end=' ')
            # 4．递归遍历右子树．
            self.inorder_travel(root.rchild)

    # 2.6 定义postorder_travel()函数，表示：深度优先之后序遍历(左右根)
    def postorder_travel(self, root):
        # 1．判断根节点是否不为空，不为空就打印．
        if root is not None:
            # 2．递归遍历左子树．
            self.postorder_travel(root.lchild)
            # 3．递归遍历右子树．
            self.postorder_travel(root.rchild)
            # 4．打印根节点的 元素域
            print(root.item, end=' ')


# 3．编写测试函数，用于测试对应的功能．
# 3.1 定义函数 dm01_测试节点和二叉树()
def dm01_测试节点和二叉树():
    # 1．创建节点
    node1 = Node('A')
    # 2．打印节点的 元素域，左子树，右子树．
    print(node1.item)  # A
    print(node1.lchild)  # None
    print(node1.rchild)  # None
    print('-' * 23)

    # 3．测试二叉树．
    # bt = BinaryTree()        # 空的
    # print(bt.root)           # None

    bt = BinaryTree(node1)
    print(bt.root)  # 根节点(的地址)
    print(bt.root.item)  # 根节点的元素域 → A


def dm02_模拟队列取元素():
    # 1．创建队列，特点：先进先出
    queue = []
    # 2．模拟往队列中添加元素．
    queue.append('A')
    queue.append('B')
    queue.append('C')
    # 3．模拟从队列中取出元素．
    print(queue.pop(0))  # A 删除索引为0的元素，并返回该元素，即：模拟从 队列中获取 元素．
    print(queue.pop(0))  # B
    print(queue.pop(0))  # C
    # 4．打印队列
    print(queue)  # ['A', 'B', 'C']


# 4．在main函数中具体测试
if __name__ == '__main__':
    # dm01_测试节点和二叉树()
    # dm02_模拟队列取元素()

    # 1．创建二叉树对象．
    bt = BinaryTree()
    # 2．添加元素．
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)

    # 3．广度优先遍历
    bt.breadth_travel()

    # 4.深度优先遍历
    print("-" * 23)
    bt.preorder_travel(bt.root)
    print("-" * 23)
    bt.inorder_travel(bt.root)
    print("-" * 23)
    bt.postorder_travel(bt.root)

