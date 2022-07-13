#Person类
class Person():
    name='徐明高'
    age=21
    sex='男'
    weight=106

    #成员方法,首参必须为self开头
    def run(self,distance):
        print("{}每天跑{}km" .format(self.name,distance)) #self可以引用成员变量
        # return "徐明高nb"
        self.exercise() #调用成员方法

    def exercise(self):
        print("{}每天做100个俯卧撑" .format(self.name))


#使用类：
#Person实例化类，调用类
#p：实例化

p=Person()
print(p.name)#引用类的成员变量
p.run(57)     #第一个参数默认不传
# print(p.run(57) ) #返回值




