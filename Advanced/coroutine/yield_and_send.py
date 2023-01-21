def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        res = yield a
        print('>>>>>ret>>>>>>', res)
        a, b = b, a + b
        current_num += 1


obj = create_num(10)

ret = obj.send(None)
print(ret)

ret = next(obj)
print(ret)

ret = obj.send("hahaha")
print(ret)

obj2 = create_num(20)
while True:
    try:
        result = next(obj2)
        print(result)
    except Exception as ret:  # except StopIteration:
        break
