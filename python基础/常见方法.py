print(2333)            #整数int
print(2.333)           #小数float
print(True,False)      #布尔值bool      
print(None)            #空noneType
print("你好")          #字符串str
print((1,3.3,4,"你好"))       #元组 tuple
print([1,3.3,4,"你好"])       #数组/列表 list
print({"地址":"浙江省","年龄":18})       #字典 dict json格式"key":"value"

#字符串字母大写函数:upper()   小写:lower()  首字母大写，其他小写:title() 
#例 a="adada"  print(a.upper())
#去除字符串空格  strip()头尾 lstrip()左边 rstrip()右边 
"""
多行注释
"""
print(1,end='')     #不换行
print(2)

print(1,end="(●'◡'●)")     
print(2)


type()  #数据类型   
len()   #数据长度
print()
input()
exit()  #退出


list=[1,2,3]
try:
    print(list[4])
except:
    print("出错了")
