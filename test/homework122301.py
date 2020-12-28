# -*- coding: utf-8 -*- 
# @Time : 2020/12/23 18:42 
# @Author : GDR 
# @File : homework122301.py


a = [1, 2, '6', 'summer']
if 'i' in a:
    print(True)
else:
    print(False)


dict_1 = {"class_id": 45, 'num': 20}
if dict_1['num'] > 5:
    print('班级的人数是：{}'.format(dict_1['num']))
else:
    print('该班级上课人数少于5人')


list1 = ['先森', '小米椒', 'lucia', 'K', '建文', '婷婷']
# 姓名、性别、年龄、城市
# 手动添加
dict1 = dict(name = '先森', sex = '女', age = 18, city = '山西')
dict2 = dict(name = '小米椒', sex = '男', age = 19, city = "湖北")
dict3 = dict(name = "lucia", sex = '女', age = 20, city = "湖南")
dict4 = dict(name = "K", sex = '男', age = 21, city = "四川")
dict5 = dict(name = "建文", sex = '女', age = 22, city = "重庆")
dict6 = dict(name = "婷婷", sex = '男', age = 23, city = "海南")

# 存放到列表中
# 方式一：
list2 = [dict1,dict2,dict3,dict4,dict5,dict6]
print(list2)
# 方二：
listnew =[]
listnew.append(dict1)
listnew.append(dict2)
listnew.append(dict3)
listnew.append(dict4)
listnew.append(dict5)
listnew.append(dict6)
print(listnew)

# 自动添加

