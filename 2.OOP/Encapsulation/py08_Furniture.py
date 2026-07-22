# 1.创建家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f 平米" % (self.name, self.area)


# 3.创建房子类
class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # python能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f【剩余：%.2f】\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)
        # 5.判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return

        # 6.将家具的名称添加到列表中
        self.item_list.append(item.name)

        # 7.计算剩余面积
        self.free_area -= item.area

    # 2.创建家具


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 4.创建房子对象
my_home = House("两室一厅", 80)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
