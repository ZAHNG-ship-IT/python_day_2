# iter() 不是用来“创建”迭代器的，
# 它是用来从一个可迭代对象中“获取”迭代器的。
# 真正负责创建迭代器的是你的类中定义的 __iter__() 方法。

#迭代器只能前进，不后退

#nex是迭代器的方法

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#####   StopIteration  用法
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
i = 0
while (i <30 ):####stopiteration 错误会跳出循环
    print(next(myiter))
    i +=1