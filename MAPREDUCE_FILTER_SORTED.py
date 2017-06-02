#coding:UTF-8
'''
**************！！！！！！！*******************
Iterator是惰性序列，必须用list()、tuple()、set()将其显示出来。sum(Iterable)函数参数
  为序列。参数为序列的一定不要写成多个int。

*map(fun,Iterable)函数接收2个参数，将fun依次作用于Iterable的元素。并将结果作为
 Iterator返回。
*reduce(fun,Iterable)函数接收两个参数，将fun作用于前面的元素并对后面的元素进行累加计
 算，注意其返回值不是Iterator，不需要进行序列转换。
 *******注意：在python 3.0后，reduce不再是built-in function,需要引用：
             from functools import reduce
*filter(fun,Iterable),过滤函数，类似于map()，但是会通过每个元素的返回值决定是否保留
 该元素，最后将结果作为Iterator返回。
 *******注意：filter将函数作用与Iterable仅仅只是用于判断，返回结果并不会如同map()函数
              改变原序列的值，返回值一样是过滤后的原序列中的元素。***********
*sorted(Iterable，key=fun)函数可以对序列进行排序，将结果作为一个列表返回。key 是可选
 参数，是将key=fun作用于序列中的每个函数再进行排序。
 *******注意：将fun作用与序列中的每个元素仅仅是为了排序，并不会改变返回值，即排序是按
              照改变后的值排序，但是返回结果是将排序后的结果中改变后的值变回初始值再
              返回。这点与filter类似。
'''
#************************map************************
print(map(abs,(-1,2,-3,4,-5,6)))#<map object at 0x0000018683F03748>
print(list(map(abs,(-1,2,-3,4,-5,6))))#[1, 2, 3, 4, 5, 6]

#************************reduce************************
from functools import reduce
def add(x,y):
    return x+y
#print(list(reduce(sum,(1,2,3,4))))这是错的
print(reduce(add,(1,2,3,4)))#10   等价于add(add(add(1,2),3),4)

#************************filter************************
print(list(filter(abs,(-1,-3,4,5))))#[-1, -3, 4, 5]
def f(m):
    return m%2 == 0
print(list(filter(f,(-3,-2,-1,0,1,2,3,4,5))))#[-2, 0, 2, 4]

#************************sorted************************
print(sorted((-1,2,3,-4,-9,-6,7,5),key=abs))#[-1, 2, 3, -4, 5, -6, 7, -9]
