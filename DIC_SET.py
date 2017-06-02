#coding:UTF-8
'''
dict和set是无序序列，无重复key元素，set相当于无vlaue的dict。
最常用的key是str。
用空间换取查找时间，通过哈希算法查找。
dict = {'1':1,'2':2,3:'3'}
set1 = {1,2,3}
set2 = set([1,2,3])
添加元素：dict[key] = value,无序添加
判断key是否存在：1.key in dict   返回True/False
                2.dict.get(key,i)  不存在返回i，默认None
