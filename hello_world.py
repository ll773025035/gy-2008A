#
# print("hello world")
#
#  a变量名 =赋值符 "hello world"值
# a="hello world"
#
# print(a)
#
# b=[1,5,6,4,3]
# b[3]=9
# print(b)
#
# c=(2,5,1,5,6,6)
# print(c)
#
# d={6,8,1,3,5,4,6}
# print(d)
#
# a=5
# b="6"
# print(a+int(b))
# print(str(a)+b)
#
# a=True
# b=6
# print(a+b)
#
# a=2.5
# b=5
# print(a+float(b))
#
# d={"name":"森林","职业":"老司机","关键字":"损骰"}
# print(d)
# print(d["职业"])
#
# l=[5,6,1,2,3,8]
# print(tuple(l))
# print(set(l))
#
# t=(5,6,1,5,4,3,7)
# print(list(t))
# print(set(t))
#
# s={6,7,4,2,5,6}
# print(list(s))
# print(tuple(s))
#
# a="agadgw"
# b=["a",5,2,"g",6]
# c=("a",4,2,6,"d",4)
# d={"a",2,7,45,"w"}
# e={"name":"森林","职业":"老司机","sex":"女"}
# print("a" in a)
# print("a" in b)
# print("a" in c)
# print("a" in d)
# print("职业" not in e)
#
# money=1000000
# if(money<5000000):
#     print("森林老司机带飞")
# elif(money<10000000):
#     print("买豪车")
# elif(money<100000000):
#     print("买豪宅")
# elif(money<1000000000):
#     print("买专机")
# else:
#     print("让森林当鸭")

# for i in range(1000000):
#     print(i)
#     print("让森林当鸭")

# while True:
#     print("森林，老袁，晓天老骚包")
# for i in range (1,21):
#     if i in [1,2,3,17,19]:
#         continue
#     print(i)
#     print("森林损色")for i in range (1,21):
#     if i in [1,2,3,17,19]:
#         continue
#     print(i)
#    print("森林损色")

# -*- coding: utf-8 -*-

#1到1000有5的过

# for i in range(1,1001):
#     if (i //10 % 10 == 5 or i // 10 // 10 == 5 or i % 10 % 10 == 5):
#         continue
#     print(i)
#
#
# for i in range(1,1001):
#     if i in (i //10 % 10 == 5 , i // 10 // 10 == 5 , i % 10 % 10 == 5):
#         continue
#     print(i)
#
# for i in range(1,10):
#     for x in range(1,i+1):
#         print(str(x)+"*"+str(i)+"="+str(i*x),end=' ')
#     print()
#
# for i in range(1,10):
#     for x in range(1, i + 1):
#          print('%s*%s=%s'%(i,x,i*x), end=' ')
#     print()


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}'.format(j, i, i*j), end='\t')
#     print()

# def div(a,b):
#     if b == 0:
#         print("被除数不能为0")
#     else:
#         print(a / b)
# div(20,30)
# div(80,20)
# div(90,30)
# div(10,0)

# i%10 == 5 个位数去5
# i//10%10 == 5 十位数去5
# i//100%10 == 5 百位数去5
# i //1000 ==5 千位数去5
# for i in range(1,10001):
#     if (i%10 == 5 or i//10%10 == 5 or i//100%10 == 5 or i //1000 ==5):
#         continue
#     print(i)

# def gas(a=6,b=9):
#     return a+b
# print(gas(6,5))
# print(gas(b=5))
# print(gas(2))

# def k(a,*sadf,b=2,**sadfg):
#     print(a)
#     print(sadf)
#     print(b)
#     print(sadfg)
# k(1,"森林",3,"qwer",4,7,6,b="asdf",jk=6,s=4)

# a = 20
# def bbb():
#     a=50
#     print(a)
# bbb()
# print(a)

# a="1234567890"
# b="123456"
#
# print(a[2:-1])
# print(a[-5:])
# print(a[-1:])
# print(a[-7:-4])
# print(a[::2])

# a = "  dsaasdgdasd  "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# aaa="森林，老司机，吹牛逼"
# aaa=aaa.replace('，',',')
# print(aaa)
# print(aaa.split(','))
# print(aaa.find('牛'))
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(j,i,i*j),end='\t')
#     print()
#
# l=[1,2,3,4,5,6,7,8,9,0]
# l[2]=25
# l.append(4)
# l.insert(5,36)
#
#
#
# print(l)


# l = [10,1,35,61,89,36,55]
# for i in range(len(l)-1,0,-1):
#     for j in range(0, i):
#         if (l[j] > l[j + 1]):
#             l[j], l[j + 1] = l[j + 1], l[j]
#         print(i)
#         print(j)
#         print(l)

# set1 = set("abcabc")
# print(set1)
# s = 0
# for i in range(1,101):
#     s+=i
# print(s)
#
# c = 10 # 全局变量
#
# def aaa():
#     b = 20 # 局域变量
#     c = 30
#     print(b)
#     print(c)
# print(c)
# aaa()
# print(c)

# a="adsfsdgfsdgsvzfsd"
# b="a,d,s,f,s,d,g,f,s,d,g,s,v,z,f,s,d"
# b=b.replace(",","_")
# print(b)
# b="_".join(a)
# print(b)
# 下面有两个队伍，，a不和x对战，b不和y,z，请写代码实现。
# team1 = ['a','b','c']
# team2 = ['x','y','z']
# for i in team1:
#     for j in team2:
#         if (i == "a" and j == "x") or (i == "b" and j == "y") or (i == "b" and j == "z"):
#             continue
#         else:
#             print('{} VS {}'.format(i,j))

# class str_demo():
#
#     def __init__(self):
#         print("魔法方法")
#
#     def replace(self):
#         print("实例方法")
#
#     @classmethod
#     def split(cls):
#         print("类方法")
#     @staticmethod
#     def static():
#         print("静态方法")
#
# str_demo.split()
# str_demo()
# str_demo().replace()

# import requests

# import random
# l = random.choices("0123456789",k=8)
# print(("135")+("".join(l)))

#编写一个返回随机手机号的方法
# def phone():
#     import random
#     l = random.choices("0123456789", k=8)
#     return print(("135") + ("".join(l)))
# phone()

# 编写一个返回长度为5内容随机的字符串方法
# def aaa(str,num):
#     import random
#     a = random.choices(str, k=num)
#     return print("".join(a))
# aaa("fghjkfghjkljkgxddas",5)
#
# def aaa():
#     import random
#     d=random.randint(1, 20)
#     a = random.choices("fghjkflhjryurjuljkgxddas", k=d)
#     return print("".join(a))
# aaa()


#编写一个返回随机姓名的方法
# def name():
#     import random
#     b = random.choices("赵钱孙李周吴郑王", k=1)
#     c = random.choices("波力金斯森亚林新天阳", k=1)
#     return print(("".join(b))+("".join(c)))
# name()


# import random
# def random_name():
#     xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
#     zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
#     xing = random.choice(xing_list)
#     zi_length = random.randint(1,2)
#     res = random.choices(zi_list, k=zi_length)
#     zi="".join(res)
#     return xing + zi
#
# print(random_name())


# print("aa")
# print("bb")
# try:
#     # r = open("a.txt","r")
#     print(1 / 2)
# except (FileNotFoundError,ZeroDivisionError) as e:
#     print(e)
#     print("程序执行遇到了问题")
#     print("重新打开文件")
# else:
#     print("程序运行没报错")
# finally:
#     print("不管程序有没有报错都会运行")
# print("cc")


# def aaa(jj):
#     list = jj
#     print(list)
# aaa([1,2,3])


print("最新代码")

print("森林")
