# -*- coding: utf-8 -*- 
# @Time : 2020/12/23 22:13 
# @Author : GDR 
# @File : python122302.py

"""
函数：特定功能的代码封装成函数，用的时候再去调用函数  ---提高代码的复用率

1、函数的定义语法：
def 函数名():          ----定义函数，函数名要遵循-->标识符命名规则
    函数体(实现功能的代码)

注意：函数定义了之后，调用它才会被执行，不调用就不执行
调用？-----函数名()

2、函数的参数：  ——可能会变化，定义为函数的参数，调用的时候传入参数
1) 必备参数：定义后必须要传入的，不传会报错(必须放在最前面，否则报错)
2) 默认/缺省参数：定义时可以设置一个默认的值。
   调用函数的时候可以不传参（使用默认值）
   也可以传参，传参的话直接覆盖掉默认值
注意：默认参数放在必备参数后面！
3) 不定长参数：不确定传参的个数，可传可不传
*args:  在它之前的参数都接收实参之后，接收剩下的位置传参的参数   以元组类型保存
**kwargs(关键字传参): 在它之前的参数都被接收实参之后，接收剩下的关键字传参的参数  以字典类型保存
---必须在位置传参之后



3、参数传入方式
1)  位置传参： 严格按照位置参数来传入  (必备参数，默认参数，args)
2)  关键字传参： 必须指定参数名传参    (**kwargs)
3)  混合传参：关键字传参，必须在位置参数之后


函数的返回值：函数如果有一个值，需要给到调用者来使用，那么就定义返回值
关键词：return
1) 可定义也可不定义，若没有定义返回值，自动执行 return None
2) 返回值也可以定义多个，逗号分隔，以元组的形式接收
3) 返回值必须在函数的最后，返回值后面的代码都不会执行

"""

# 需求：判断工作是否是一个值得继续下去的工作？   工资？

def good_job(salary,bonus,subsidy = 300,*args,**kwargs):     # 定义函数同时，定义参数--变量  ---形参
    sum1 = salary + bonus + subsidy  # 薪资总和
    # print('参数salary: {}'.format(salary))
    # print('参数bonus:{}'.format(bonus))
    # print('参数subsidy:{}'.format(subsidy))
    # print('参数args:{}'.format(args))
    # print('参数kwargs:{}'.format(kwargs))
    for i in args:
        sum1 += i
    # for j in kwargs:
    #     sum1 += kwargs[j]               # 1)通过dict[key]的方法取value值
    # for j in kwargs:
    #     sum1 += kwargs.get(j)           # 2)通过dict.get(key)的方法取value值
    for m in kwargs.values():
        sum1 += m                         # 3)通过dict.values()取到字典的所有value值，直接遍历相加
    # print(sum1)
    return sum1

# 函数调用
# good_job()

# 必备参数--函数调用
# good_job(8000,2000,100,1000,200,aa = 200,bb = 300)         # 传参-----实参

# 实际需求：想拿到这个薪资总和，再去判断是否是一个好工作

salary = good_job(8000,2000,100,1000,200,aa = 200,bb =3000)   # 定义一个变量，接收函数调用后的返回值
print(salary)

if salary > 10000:
    print('这工作不错，加油！')
else:
    print('骚年，赶紧跳槽吧')

# 补充  dict函数---内置函数，可以自动生成一个字典
# dict()

dict2 = dict(name = "小猪锅",age = 18,sex = '女')
print(dict2)