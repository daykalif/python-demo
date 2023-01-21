# 别名需要驼峰命名
import py01_test1 as DogModule
import py02_test2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
