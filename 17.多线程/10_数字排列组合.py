"""
需求:
问1, 2, 3, 4能组合成的四位数有几种情况, 按照5个一行输出。
要求:
1.要求同时包含1, 2, 3, 4这四个数字。
    1234, 1324均可
    1122, 1123不行
2. 要求数字1和3不能挨着。
    1324, 3124不行
    1234, 3412可以
3. 数字4不能开头。
4. 5行以内搞定(包括5行)
"""
import copy

# 思路: 把数字 → 字符串, 然后调用字符串的功能做判断, 即可.
# count = 0
# for s in [str(i) for i in range(1234, 4322)]:
#     if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4':
#         count += 1
#         print(s, end='\n' if count % 5 == 0 else '\t')


# 用一行代码解决：
print([int(s) for s in [str(i) for i in range(1234, 4322)] if
       '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4'])

# 需求：已知列表：my_list = ['aa','bb','cc','bb','bb','bb','dd']，删除所有bb元素，尽可能多的用不同的解决方案
my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']
my_list = [i for i in my_list if i != 'bb']
print(my_list)

my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']

"""
对比：

1. for s in my_list: ❌ 错误写法（遍历原列表）
遍历过程中原列表长度不断缩短，指针会跳过元素，删不干净
输出：['aa', 'cc', 'bb', 'dd']

2. for s in my_list[:]: ✅ 推荐（切片生成全新浅拷贝列表）
my_list[:] 会一次性复制整个列表生成新列表，循环全程遍历这份固定副本，原列表随意修改不影响循环迭代，可全部删除目标元素
输出：['aa', 'cc', 'dd']

3. for s in copy.copy(my_list): ✅ 浅拷贝模块实现
和切片效果完全一致，都是创建列表浅副本遍历；适合结构更复杂的列表，单纯一维字符串列表没必要用
需要开头导入模块：import copy

4. for s in copy.deepcopy(my_list): ✅ 深拷贝
完全递归拷贝所有层级数据，开销最大；一维简单列表场景完全多余，只有列表嵌套多层子列表时才需要深拷贝
"""
for s in my_list[:]:
    if s == 'bb':
        my_list.remove(s)
print(my_list)
