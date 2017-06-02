#coding:UTF-8
'''
*函数名也是变量，可赋给其他变量

*python函数可返回多个值，本质上是返回的一个tuple。

*可通过from 文件名 import 函数名引用自定义模块。（需要将该文件的路径加入解释器路径
    或sys.path.append(路径)（关闭后失效）或
    将文件放入如'C:\\Users\\random\\AppData\\Local\\Programs\\Python\\Python35\\lib\\site-packages'中）

* 函数参数可在定义时使用默认参数，def a(n=5):...    !!!默认参数必须指向不变对象

* 函数参数可传入可变参数,自动组装为元组：def fun(*v):...   v可以是列表元组，可变个数对象。 l = [1,2.2,3,4,5,5]   fun(*l)

* 可传入关键字参数，自动组装为字典：def fun(a,b,**v):...   v是字典。  dict1 = ｛'1':1｝ fun(1,2,**dict1)
**********函数限制传入关键字参数的名称：def fun(a,b,*,city,job):...     传入的''关键字(key)组合''其key必须为city,job
总结：*组装元组  **组装字典，限制关键词在关键词前加一个参数*

*使用在函数中定义函数，可以将函数名作为函数的返回值。这样的好处是使函数的调用计算可控制。
     这种嵌套函数的参数传递在第一层函数。

*匿名函数lambda，无需定义函数，没有函数名也可直接使用。

'''

#hex()十进制转换为十六进制字符串:
def HEX(a):
    print(hex(a))
h = HEX
h(15)
print('\n\n')

#可变参数的传递
def hello(*str1):
    for i in str1:
        print(i)
list1 = ['12','34','56']
hello(*list1)
print('\n\n')

#关键词参数的传递
def H5(name,age,**dict2):
    print('name:',name,'age:',age,'other:',dict2)
H5('luguilin',22,city='Chongqing') #city是关键字！
print('\n\n')

#函数名作为返回值
def sum1(*n):
    def add():
        ax = 0
        for i1 in n:
            ax = ax+i1
        return ax
    return add
l3 = (1,2,3,4,5,6,7,8,9,0)#<function sum1.<locals>.add at 0x000001677B981400>
A1 = sum1(*l3)#
print(A1)
print(A1())
print('\n\n')

#使用递归解决汉诺塔问题

#计算有n层汉诺塔，需要多少次移动
def fact(n):
    if n == 1:
        return 1
    return 2*fact(n-1)+1
print("移动%d层汉诺塔至少需要%d次。"%(n,fact(n)))
#显示移动汉诺塔的规则
def move(n,a,b,c):
    if n == 1:
        print(move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
