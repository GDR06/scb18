# -*- coding: utf-8 -*- 
# @Time : 2020/12/22 18:14 
# @Author : GDR 
# @File : test2.py

print('hello world!')


'''
标识符：变量名、project name、package name、python文件、函数名
命名的规则：
1) 只能是字母数字下划线
2) 不能以数字开头
3) 不能使用关键字（python底层设计）
4) 建议：见名知意，数字字母、字母之间、最好用下划线隔开，阅读性比较高，scb18、ScbPython(驼峰规则)
5) 格式规范：python之禅、PEP8规范---拓展
'''


import keyword
print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

# 注释  --> 养成习惯    1）解释  方便理解   2）方便阅读
# 单行注释   #  快捷键/取消  ctrl + /
# 多行注释  ''' '''

# 代码格式
# 1）红色波浪线  报错信息   ---尝试翻译报错信息，尝试解决
# 2）代码格式：顶格写，对齐：子代码才会有缩进--函数/for循环/if判断等

print('hello world!')   #print 内置函数   ---python种写好了直接拿来用的，功能：打印/输出内容到控制台
print('hello 小猪锅')
print('hello GDR')

# 变量：存储数据
# 变量名命名：满足标识符命名的规则
# 变量名使用：一定要先声明，才能使用

str = 'hello GDR!'   #定义/声明了一个变量，赋值：字符串--- 任意数据类型
num = 6
print(str)
print(num)