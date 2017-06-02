#coding:UTF-8
'''
list是有序集合，可更改元素。len()获得个数。
l[n]索引值0~n-1，可为负数，-1表示n-1。
list函数:
l.append(x):追加x到列表末尾。
l.insert(索引号，x):在指定索引号插入x, 原该索引号及以后的元素依次后移。
l.pop(i):删除指定位置的元素并返回被删除元素。默认为最后一个。
l.sort(reverse=0/1):排序，参考值可选，默认正序。
                    **对于可迭代对象采用sorted()全局函数。
l.index(x):返回第一次出现x的索引值。
l.count(x):返回x在list中的数量。
l.remove(x):取出第一次出现的x元素。
'''
'''
tuple是有序序列，元素不可变。
在定义tuple时其元素就被定义，一个元素其后面必须加',' eg : tl = (1,)
除了对元素的修改，其他函数与list一致。
'''
'''
**************join与split函数*************
str.split('i'):将字符串str以字符串中的i为界限分为list。（默认为空格）
'i'.join(iterable)：将可迭代序列按照'i'连接为字符串。（其中序列元素必须为str格式）

>>> '1 2 3 4 5 6 7 8 9'.split()
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> l = ['1','2','3']
>>> '-'.join(l)
'1-2-3'

'''

#列表生成式
a = [i for i in range(10)]
print(a)
print('\n')

#生成器，按需生成可迭代对象
'''
将列表生成式中的[]改为()或加上yield.
遇到yield返回，再次执行时在上次返回的yield处执行。
使用next()调用下一个值。或者使用循环来遍历。
**生成器的return要通过捕获StopIteration的value.
'''
aa = (i1 for i1 in range(10))
print(aa)
print(next(aa))
print('\n')
for i2 in aa:
    print(i2)
print('\n')

#练习索引
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ('Bob','Lisa','icefog')
]
#打印'Google'
print(L[0][1])
#打印'Python'
print(L[1][1])
#打印'icefog'
print(L[2][2])
