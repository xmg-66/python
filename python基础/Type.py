#tuple      不能修改元素
x=(1,1.3,True,(1,2,3),[1,2,3],{"username":"xmg"})
print(x)
print(len(x))

#下标
print(x[0])
print(x[-1])
print("-----------------------------------")

#list       

y=[1,2,(1,2,3),[1,2,3],{"age":18}]
y2=[1,3,4,6,1]
print(len(y))
print(max(y2))
print(min(y2))
print(y2.count(1)) #元素次数
print(y.index([1,2,3])) #元素位置
#列表截取
print(y[0])
print(y[-1])
print(y[1:])
print(y[1:4])
y.append("尾部增加元素")
y[2]=33333 #修改元素值
y.insert(0,555) #指定位置插入元素
y.pop(4) #pop()默认最后一个元素
#del company_list[0] 删除表第一个元素
#y.extend(y2) 双表连接
#y.clear() 删除全部元素
y2.pop
print("y的值为{}" .format(y))
print("y2的值为{zhi}" .format(zhi=y2))

