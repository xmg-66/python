class Ikun(object):
    def __init__(self,age,name,address): #构造
        self.age=age
        self.name=name
        self.address=address
    def technical(self,action):
        self.action=action
        print('我是练习时长{}年半的个人练习生{},来自{},我会{},music!' .format\
            (self.age,self.name,self.address,self.action))
        Ikun.bark('你干嘛啊哈')
    def bark(sound):
        print(sound)
    def __del__(self):  #析构，删除对象
        print('{}已被清除' .format(self.name))
Fans=Ikun(2,'蔡徐坤','江苏省')
Fans.technical('唱跳rap篮球')
del Fans

Fans2=Ikun(5,'小黑子','上海市')
Fans2.technical('你干嘛啊')
Fans2.technical('孤独地叫')





