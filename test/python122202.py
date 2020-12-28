# -*- coding: utf-8 -*- 
# @Time : 2020/12/22 21:49 
# @Author : GDR 
# @File : python1222.py

# 内置函数  print()
# 内置函数  input()  从控制台输入
name = input('please enter your name:')
print(name)

'''
python常见8种数据类型：整型int、浮点型float-小数、布尔型bool-（True False）（注意python是大小写敏感的）、字符串str、字典dict、列表list、元组、集合
1、判断数据类型：
type():输出数据的类型
isinstance():参数为"数据本身，数据类型"  --两者作比较 ---> 返回 True或者False
'''

num = 6   # 定义一个变量，赋值6
fla = 66.66  # 浮点型
print(type(num))    # 打印num值的数据类型
print(type(fla))    # 打印fla值的数据类型

print(isinstance(num,bool))  # 判断num变量值是否是一个bool类型，若是返回True，若不是返回False

# 字符串：用成对的引号括起来的内容  可以是单引号、双引号、三引号
print('吃火锅吗')
print("吃烧烤吗")
print('''吃烤鱼吗''')

# 思考，为什么会有三种形式的字符串输出，比如输出：'小猪锅'要加油！
# 1）引号嵌套使用或用转义字符（两种方式均可）
print("'小猪锅'要加油！")
print('\'小猪锅\'要加油！')
# 2）三引号支持换行  --输入换行格式，输出也就是换行的格式，所见即所得
print('''---------------小猪锅同学的基本信息-------------
                        name：小猪锅
                        age：22
                        advantage：有钱
''')

# 字符串的切片：应用：取出某一个字符串中的部分内容
# 1、每一个字符串中的元素对应一个位置  --索引：0（从0开始）
# 2、字符串切片：[开始索引:结束索引:步长] 1）截取字符串为开始索引到结束索引-1内的字符串  2）索引头默认0，步长默认是1
# 3、len():内置函数  计算长度

# string = 'hello python!'
#           0123456789101112  从0位到12位
#                       -2-1  倒序 从-1位到-12位
string = 'hello python!'
print(string[6:10])  # 输出pyth
print(string[2:])    # 输出2-末尾的字符：llo python!
print(string[:5])    # 输出开始到4的字符串：hello
print(string[:])     # 输出整个字符串:hello python!
print(string[::3])   # 每隔两个字符取一个:hlph!
print(len(string))
print(string[:len(string):3])   # 从开始位置到该字符串的长度13位，每隔2个字符取一次：hlph!
print(string[::-1])     # 反着输出（倒序）

# 替换 replace()   python --->Java
str2 = string.replace('python','Java')
print(str2)

# 查找索引，获得字符串元素开始的位置  index()  find()
# find函数语法：str.find(str,beg = 0,end = len(str))
# str-->指定检索的字符串，beg-->开始索引，默认为0，end-->结束索引，默认为字符串的长度
# 若指定beg和end范围，则检查指定字符串是否包含在范围中，若是，则返回字符串开始的索引值，不包含则返回-1
# index函数，若存在指定检索字符串，则直接返回该字符串的开始索引
print(string.index('Java'))   #字符串不存在，报错
print(string.find('C++'))     #字符串不存在的时候，返回-1
print(string.index('thon'))   #输出：8

# 格式化输出 （2种方式）
# 1) .format()  -----占位符{}，,format()--变量的传入
# 指定顺序

name = '小猪锅'
age = 3
advantage = '有钱'
print('''---------------{}同学的基本信息-------------
                        name：{}
                        age：{}
                        advantage：{}     
'''.format(name,name,age,advantage))      #注意是print中引号中的内容调用.format()函数

# 如果format括号中是四个参数，也就是每个{}都有对应，那么{}中不需要写数字定位
# 如果format括号中是三个参数，没有一一对应{}，那么{}中就需要写数字（从0开始）定位

print('''---------------{0}同学的基本信息-------------
                        name：{0}
                        age：{1}
                        advantage：{2}
'''.format(name,age,advantage))      #注意是print中引号中的内容调用.format()函数

# 或者通过关键字定位输出
print('{name},{age},{advantage}'.format(name = '小猪锅',age = 18,advantage = '有钱'))

# 常见的运算符
# 1、算术运算符：+ - * / %  （/-->除法中得到的结果都是浮点数，不论被除数和除数是什么类型）
# //--->整除正好相反，得到的结果都是整数，若商为小数，取整数部分

amount = 1000
salary = 10000
print(amount + salary)
print(amount - salary)
print(amount * salary)
print(salary / amount)
print(salary % amount)

# 加法：除了数字相加，也可以字符串拼接
print('有翡' + '真好看！')
print('创造营' + str(2))    # str()  -- 强制转换数据类型为字符串  int()
# 乘法：字符串重复输出
print('鹿晗' * 100)

# 2、赋值运算符：= += -= *= /= %=
amount1 = 1000
# amount1 += 10 ----> amount1 = amount1 + 10
amount1 -= 10
# amount1 = amount1 - 10
print(amount1)

# 3、比较运算符：==、>、<、>=、<=、!=   结果：布尔值 True  False
salary1 = 11000
print(salary1 == 10000)   # False
print(salary1 > 10000)    # True
print(salary1 < 10000)    # False
print(salary1 != 10000)   # True

# 4、逻辑运算符：or 都假才为假  and 都真才为真  not 非
amount = 9000
salary = 10000
print(amount > 10000 or salary > 12000)     # False
print(not amount > 10000)                   # True

# 5、成员运算符：  in  not in  结果：布尔值
# 成员 in 集合    比较多在字典、列表中，字符串也可以
str1 = 'hello scb18!'
print('18' in str1)

str2 = '小猪锅会有钱的'
print('小猪锅' in str1)
