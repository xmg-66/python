# from calendar import c
# from posixpath import join


# company_list=['Alibaba','Baidu','Tencent','MeiTuan','JD']
# for i in company_list:
#     print('Hello {}, here is my resume!' .format(i))
# print()
# del company_list[0]
# company_list.pop()
# company_list.pop()
# company_list.remove('Tencent')
# for j in company_list:
#     print("{}, thank you for passing my resume. I will attend the interview on time!" .format(j))


# my_list=['P','y','t','h','o','n']
# print('Here is the original list:')
# print(my_list)
# print()
# print('The result of a temporary reverse order:')
# print(sorted(my_list,reverse=True))
# print()
# print('Here is the original list again:')
# print(my_list)
# print()
# print('The list was changed to:')
# my_list.sort(reverse=True)
# print(my_list)
# print()
# print('The list was changed to:')
# my_list.reverse()
# print(my_list)


# x=range(1,21)
# for i in x:
#     print(i)

# num=0
# while num <20:
#     num+=1
#     print(num)


# name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'] 
# friends=[]
# friends.append(name)
# food=['pizza', 'fish', 'potato', 'beef']
# friends.append(food)
# number=[3,6,0,3]
# friends.append(number)
# print(friends)

# number=[1,2,3,4]
# for i in number:
#     for j in number:
#         for k in number:
#             if i!=j and i!=k and j!=k:
#                 print(i,j,k)

# users_list=['Niuniu','Niumei','Niu Ke Le']
# for i in users_list:
#     print('Hi, {}! Welcome to Nowcoder!' .format(i) )
# print("Happy Programmers' Day to everyone!")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print('')


# my_list=range(1,1001)
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))
# print(round((sum(my_list))/(my_list[-1]),1))


# my_list=[]
# for i in range(0,20,2):
#     my_list.append(i)
# for j in my_list:
#     print(j)


# my_list=[]
# for i in range(1,51):
#     if i%5==0:
#         my_list.append(i)
# for j in my_list:
#     print(j)


# my_list=[]
# for i in range(1,11):
#     j=2**i
#     my_list.append(j)
# for k in my_list:
#     print(k)

# my_list=[]
# for i in range(1,11):
#     k=i*i*i
#     my_list.append(k)
# print(my_list)


# group_list= ['Tom', 'Allen', 'Jane', 'William', 'Tony']
# print(group_list[:2])
# print(group_list[1:4])
# print (group_list[-2:])

# user_list=['Niuniu','Niumei','HR','Niu Ke Le','GURR','LOLO']
# for i in user_list:
#     if i =='HR':
#         print('Hi, HR! Would you like to hire someone?')
#     else:
#         print('Hi, {}! Welcome to Nowcoder!' .format(i))

# my_list=[]
# if len(my_list) == 0:
#     print('my_list is empty!')
# else:
#     print('my_list is not empty!')

# current_users=['Niuniu','Niumei','GURR','LOLO']
# new_users=['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
# for i in new_users:
#     for j in current_users:
#         if i.lower() == j.lower():
#             print('The user name {} has already been registered! Please change it and try again!' .format(i))
#             break
#     else:
#         print('Congratulations, the user name {} is available!' .format(i))


# order_list=['rice', 'beef', 'chips', 'pizza', 'pizza', 'yogurt', 'tomato', 'rice', 'beef']
# price={'pizza':10,'rice':2,'yogurt':5}
# total_money=0
# for food in order_list:
#     if food in price:
#         print('{} is {} dollars' .format(food,price.get(food)))
#         total_money+=price.get(food)
#     else:
#         print('{} is 8 dollars' .format(food))
#         total_money+=8
# print(total_money)


# my_tuple=('Tom','Andy')
# print('Here is the original tuple:')
# for name in my_tuple:
#     print(name)
# print()
# try:
#     my_tuple[1]='Andy'
# except(TypeError):
#     print("my_tuple[1] = 'Allen' cause a TypeError: 'tuple' object does not support item assignment")
# print()
# my_tuple=('Tom','Allen')
# print('my_tuple was changed to:')
# for name2 in my_tuple:
#     print(name2)

# survey_list=['Niumei','Niu Ke Le','GURR','LOLO']
# result_dict={'Niumei': 'Nowcoder','GURR': 'HUAWEI'}
# for name in survey_list:
#     if name in result_dict.keys():
#         print(f'Hi, {name}! Thank you for participating in our graduation survey!')
#     else:
#         print(f'Hi, {name}! Could you take part in our graduation survey?')


# my_dict_1={'name': 'Niuniu','Student ID': 1}
# my_dict_2={'name': 'Niumei','Student ID': 2}
# my_dict_3={'name': 'Niu Ke Le','Student ID': 3}
# dict_list=[]
# dict_list.append(my_dict_1)
# dict_list.append(my_dict_2)
# dict_list.append(my_dict_3)
# for list in dict_list:
#     print("{}'s student id is {}." .format(list.get('name'),list.get('Student ID')))


# result_list = {'Allen': ['red', 'blue', 'yellow'],
#                'Tom': ['green', 'white', 'blue'],
#                'Andy': ['black', 'pink']}

# for i in sorted(list(result_list.keys())):
#   print(f"{i}'s favorite colors are:")
#   for j in result_list[i]:
#     print(j)


# def cal():
#     x=int(input())
#     y=int(input())
#     print(x-y)
#     print(y-x)
# cal()


# def replace(friend_list, index):
#     friend_list[index] =index
#     return None

# friend_list = ['Niu Ke Le', 'Niumei', 'Niuneng', 'GOLO']
# print(friend_list)

# for i in friend_list:
#     replace(friend_list,friend_list.index(i))

# print(friend_list)


# print('What kind of drink would you like?')
# kind_of_drink=input()
# if kind_of_drink == 'cola':
#     print('Below is your cola. Please check it!')
# else:
#     print(f'The {kind_of_drink} has been sold out!')

# #九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()

# def cn(a,b,c):
#     return a*b*c

# print (cn(1,3,4))


        
        