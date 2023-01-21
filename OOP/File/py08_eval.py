# eval()函数十分强大--将字符串当成有效的表达式来求值并返回计算结果

# 基本的数学计算
print(eval("1+1"))

# 字符串重复
print(eval("'*' * 10"))

# 将字符串转换成列表
print(type(eval("[1,2,3,4,5]")))

# 将字符串转换成字典
print(type(eval("{'name':'xiaoming','age':'10'}")))

input_str = input("请输入算术题：")
print(eval(input_str))

"""
# 不要滥用eval，千万不要使用eval直接转换input的结果（比如运行该文件，在第15行中输入第20行代码，可以执行文件的增删操作，十分危险）
    __import__('os').system('ls')
    __import__('os').system('touch aaa') 
    __import__('os').system('rm aaa') 
    
# 等价代码：
    import os
    os.system("终端命令")

"""
