# -*- coding: utf-8 -*- 
# @Time : 2020/12/24 21:40 
# @Author : GDR 
# @File : python1224.py


"""
接口测试：调用第三方库----别人写好的项目代码，可以直接拿来用的
Jmeter工具---接口测试  http协议
请求：请求行、请求头、请求体
响应：状态码、响应头、响应体
requests库除了url之外，其他参数一般使用字典

1、传请求正文的方法
1) json: 数据格式为json时
2) data

2、获取响应正文
1) text： 获取响应正文，文本，返回字符串格式
2) json: 获取响应正文是为json格式，返回字典


步骤：
1、安装requests库  pip  --在线下载并安装第三方库的工具/pycharm工具settings--project...
2、导入  import 库名   ---对当前这个文件生效
"""

import requests
import jsonpath


# 注册
url_reg = 'http://120.78.128.25:8766/futureloan/member/register'      # 请求地址
data_reg = {"mobile_phone": "18503468688","pwd": "lemon666","type":"1","reg_name":"zhutest"}     # 请求体
header_reg ={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}                   # 请求头

res_reg = requests.post(url = url_reg,json = data_reg,headers = header_reg )      # 调用post，用变量接收返回值

# print(res_reg.status_code)   # 获取http的状态码
# print(res_reg.headers)       # 获取响应头
# print(res_reg.text)
print(res_reg.json())          # 获取字典形式的响应数据

# 登录
url_login = 'http://120.78.128.25:8766/futureloan/member/login'      # 请求地址
data_login = {"mobile_phone": "18503468688","pwd": "lemon666"}       # 请求体
header_login ={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}

res_log = requests.post(url = url_login,json = data_login,headers = header_login).json()
print(res_log)


# # 充值
# 如何获取token值，id值
# 方式一： 字典嵌套取值
# token = res_log['data']['token_info']['token']                  # 字典嵌套获取token，赋值给变量token
# token1 = res_log.get('data').get('token_info').get('token')     # 另一种取字典的value值的方法，也可以取到token
# member_id = res_log['data']['id']                               # 获取id，赋值给变量member_id


# 方式二： jsonpath  --第三方的库  1) 先pip install jsonpath 安装  2) 导入  import
token = jsonpath.jsonpath(res_log,'$..token')       # 获取到的token是列表形式，引用时要加[0]
member_id = jsonpath.jsonpath(res_log,'$..id')      # 获取到的id是列表形式，引用时要加[0]

url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'      # 请求地址
data_recharge = {"member_id": member_id[0],"amount": "100.0"}                      # 请求体
header_recharge ={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer' + ' ' + token[0]}

res_rec = requests.post(url = url_recharge,json = data_recharge,headers = header_recharge).json()
print(res_rec)

# 把接口请求封装成函数
def api_fun(url,data):
    # url_login = 'http://120.78.128.25:8766/futureloan/member/login'  # 请求地址
    # data_login = {"mobile_phone": "18503468688", "pwd": "lemon666"}  # 请求体
    header_login = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'}

    res_log = requests.post(url=url, json=data, headers=header_login).json()
    return res_log

# 调用api_fun
result = api_fun(url_login,data_login)
print(result)
