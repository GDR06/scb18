# -*- coding: utf-8 -*- 
# @Time : 2020/12/23 16:27 
# @Author : GDR 
# @File : python1223.py

"""
python 常见的数据类型：字典dict、列表list、元组tuple、集合set

列表：list []  多个元素逗号隔开
1、列表中的元素  可以是任意数据类型
2、取值：根据索引取值，从0开始，参考字符串切片
3、len()  列表长度/元素个数
4、list元素可以改变：增、改、删
5、list元素可以重复  list是有序、可重复的
"""

list1 = []  # 空列表
print(type(list1))    # 打印list1的类型
list2 = [1, 520.0, True, 'Python', [1,2,3]]
print(list2)    # 输出列表中所有元素
print(list2[2])
print(list2[:len(list2):1])
print(len(list2))
print(list2[3][4])   # 列表中的嵌套取值 输出python中的o

# 列表元素的增
list2.append('小猪锅')    # 追加元素到列表末尾
list2.append('小猪锅')    # 重复添加相同的元素
print(list2)
list2.insert(1,'小锅包')  # 指定位置插入元素
print(list2)

# 列表元素的删
list2.pop()              # 默认删除最后一个元素
print(list2)
list2.pop(2)             # 指定索引的位置来进行删除
print(list2)
list2.remove('Python')      # 指定元素进行删除
# 若列表中有相同元素，指定元素删除时，删除元素中找到的第一个

# 列表元素的改
list2[0] = '鹿晗'         # 找到元素，重新赋值
print(list2)

# 元组 tuple  --了解
# 面试题：列表、元组、字典的区别？
"""
元组：tuple()
1、元组中元素：任意数据类型
2、取值：索引从0开始，参考字符串切片
3、元组中元素不能改变   
（除非强制类型转换，将元组转换成list，增加或删除元素后，再转换成元组）
（表面上看tuple的元素变了，但其实变的不是tuple的元素，而是list中的元素，tuple一开始指向的list并没有
改变成别的list，所以，tuple的不变说的是，tuple的每个元素，指向永远不变，即指向'a'，就不能改成指向'b'，
指向一个list，就不能改成指向其他对象，但指向的这个list本身是可以改变的）
"""

tuple1 = ()          # 空元组
tuple2 = (666, 'JAVA', 13.14, [6, 7, 8])
print(tuple1)
print(tuple2[1])
"""
思考：1)元组 --> list 2)list增删改 3)list-->元组
元组本身并未改变，一开始指向的list并没有改变成别的list
"""
list3 = list(tuple2)
list3.append('哈哈哈')
tuple3 = tuple(list3)

# 字典 dict {} key-value 一个键值对才是一个元素
"""
字典的应用场景：描述一个对象的基本信息
1、key: value
key ：只能取除列表和字典之外的不可变的数据类型
value ：任意数据类型
2、字典是没有顺序的
3、字典取值：取value值---通过key取
   2种取值方式
4、key是唯一的，不能重复，value可以改变---增删改

"""
dict1 = {"name":"小猪锅","age":3,"hobby":"喜欢钱"}
print(dict1)
print(dict1['name'])            # 通过key值取value值
print(dict1.get('name'))        # 字典的get方法取值

print(dict1.keys())             # 获取字典中的所有key值
print(dict1.values())           # 获取字典中的所有value值

# 字典value---增
dict1['city'] = '山西'          # 当key不存在时，新增一个键值对元素
print(dict1)

# 字典value---改
dict1['age'] = 2                # 当key存在时，直接覆盖掉原来的value值
print(dict1)

# 字典value---删
dict1.pop('city')               # 字典无顺序，所以必须指定key值进行删除
print(dict1)

# 集合set --->无序，不可重复
# 1、使用场景，给列表去重
# 2、相对dict，存储的是key
# 3、添加-->  add /  update-->把传入的元素拆分，作为个体传入到集合
# 4、删除 remove

"""
python  控制流：控制代码的走向，常用2种：判断、循环
（切记条件语句后面都要加冒号）
if判断：语法
if 条件a：  ----条件a为真，才会执行子语句
    子代码    ----缩进，默认4个空格  快捷键  Tab键
elif 条件b:     ----条件b为真，执行子代码，可以是多个条件，也可以没有
    子代码
...
else:
    没有满足任何条件，才会执行的语句

"""
#
# money = int(input('please enter your salary： '))
# # 此处注意：input函数输入的是一个字符串类型，如果想要和下面的整型数字
# # 比较，需要将输入的字符串类型强制转换类型，转换为int型，才能进行比较
# if money >= 30000:
#     print('有钱真好，想买啥买啥😊')
# elif money >= 20000:
#     print('工资还行，但是不能太放肆')
# elif money >=10000:
#     print('早日突破20000/(ㄒoㄒ)/~~')
# else:
#     print('加油吧打工人，你还差得远呐💪')


"""
for循环：遍历一个数据对象（字符串、列表、字典、元组）的每一个元素--从头到尾访问
语法：
for ... in 固定用法
什么时候结束循环？ ---遍历结束、循环也就结束
循环次数----元素个数

中断循环：
break   ---中断：for循环中后面的代码不再执行，跳出当前for整个循环
continue    ---中断：for循环中跳出本次循环，后面的循环会继续执行
"""

str1 = '小猪锅以后会很有很有钱的！大家也都会有的！！'
count = 0            #计数器
for x in str1:
    if x == '会':
        # break        # 中断：for循环中后面的代码不再执行，跳出当前for整个循环
        continue       # 中断：for循环中跳出本次循环，后面的循环会继续执行
    count += 1       # 每循环一次，count+1
    print(x)

print(count)     # 循环次数
print(len(str1))

# 内置函数：range()
# 生成一个整数序列，起始值默认是0
# 结合for循环使用

sum = 0
for num in range(101):     # range(101)-->生成1-100的整数
    sum +=num
print(sum)                 # 求1-100的和
