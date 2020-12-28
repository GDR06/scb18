# -*- coding: utf-8 -*- 
# @Time : 2020/12/26 15:09 
# @Author : GDR 
# @File : run.py

from test.python122502 import read_case,api_fun,write_case


def execute_fun(filename,sheetname):
    case_list = read_case(filename,sheetname)    # 读数据，定义变量接收读取到的数据
    # eval()函数：运行被字符串包裹着的表达式
    for m in case_list:                                          # 遍历一个列表，每一个列表元素都是一条字典形式的数据
        case_id = m['case_id']                                   # 获取第几条用例
        response_dict = api_fun(url = m['url'],data = eval(m['data']))
        # real_code = response_dict['code']
        # expect_code = eval(m['expect'])['code']
        real_msg = response_dict['msg']
        expect_msg = eval(m['expect'])['msg']
        print("期望结果为：{}".format(expect_msg))
        print("实际结果为：{}".format(real_msg))
        if real_msg == expect_msg:
            print('第{}条用例执行通过！'.format(case_id))
            final_re = 'Passed'
        else:
            print('第{}条用例执行不通过！'.format(case_id))
            final_re = 'Failed'
        write_case(filename,sheetname,case_id + 1,8,final_re)
        print('*'*20)

execute_fun('C:\\Users\\郭丁榕\\.jenkins\\workspace\\scb18\\test_data\\test_case_api.xlsx', 'register')
execute_fun('C:\\Users\\郭丁榕\\.jenkins\\workspace\\scb18\\test_data\\test_case_api.xlsx', 'login')