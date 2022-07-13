# class Student():
#     def __init__(self,mz):
#         print("构造方法,实例化类时执行")
#         self.name=mz

# A=Student('徐明高')
# print(A.name)


#继承父类的属性和方法
from re import X


class father():
    money='10000w'
    def company(self):
        print("有公司")

class son(father): #继承
    name='xxs'
    #子类可以重写父亲的属性和方法
    money='-111111w'
    def action(self):
        print("败光家产")

X=son()
print(X.name)
print(X.money)
X.company()
X.action()