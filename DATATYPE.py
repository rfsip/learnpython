#coding:utf-8
'''
pyton3有6种数据类型：Number、String、List、Tuple、Sets（集合）、Dictionary

Number: 支持 int、float、bool、complex。只有一种整数类型int，表示长整型。
        bool类型只有True False。
String: 长度不可变，用单引号和双引号表示。a="abc",其中a为变量，"abc"才是字符串。a可变。

除法: python3 除法有两种  '/'为精确除，结果为浮点数  10/3=3.33333333  9/3=3.0
                         '//'为地板除，结果为整型  10/3=3
'''
#练习：打印出下列变量的值
n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

'''

结果如下：
123
456.789
Hello,world
Hello,'Adam'
Hello,"Bart"
Hello,
Lisa!

'''
