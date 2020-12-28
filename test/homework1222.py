# -*- coding: utf-8 -*- 
# @Time : 2020/12/22 22:32 
# @Author : GDR 
# @File : test2.py

name = input('请输入姓名：')
age = input('请输入年龄：')
sex = input('请输入性别：')
# print('**************************')
# # print('姓名:',name)
# # print('性别:',sex)
# # print('年龄:',age)
# # print('**************************')

# ---格式化输出
print('''
************************************            
姓名：{}
性别：{}
年龄：{}
************************************
'''.format(name,sex,age))



# str1 = 'Python hello aaa 123123aabb'
# print(str1[:6])
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)
# str2 = str1.replace('Python','lemon')
# print(str2)
# print(str1.index('aaa'))