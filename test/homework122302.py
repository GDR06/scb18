# -*- coding: utf-8 -*- 
# @Time : 2020/12/24 8:48 
# @Author : GDR 
# @File : homework122302.py


# 将字符串转换成列表
# 方式一：将字符串拆分存放到列表 -list()
def exchange(str):
    list1 = list(str)
    return list1

str1 = "走啊去吃火锅 hahaha"
list2 = exchange(str1)
print(list2)
# 方式二：
# 字符串的spilt()函数，以字符串之间的空格为间隔，不用拆分字符串，将字符串存放进列表
list_a = str1.split()
print(list_a)




# 整数序列求和
def sum1(num):
    sum1 = 0
    for i in range(num + 1):
        sum1 += i
    return sum1
# 求1-100的整数和
sum2 = sum1(100)
print('1-100的整数和是：',sum2)

# 判断对象的长度
def judge_len(subject):
    if type(subject) == list or type(subject) == dict or type(subject) == str:
        if len(subject) >= 5:
            return True
        else:
            return False
    else:
        print('该数据类型不能计算长度！')

# 定义一个列表
list3 = [1, 520.0, True, 'Python', [1,2,3]]
print(judge_len(list3))
# 定义一个字典
dict1 = {"name":"小猪锅","age":3,"hobby":"喜欢钱"}
print(judge_len(dict1))
# 定义一个字符串
str3 = 'hahahhahah加油吧'
print(judge_len(str3))

judge_len(12)
