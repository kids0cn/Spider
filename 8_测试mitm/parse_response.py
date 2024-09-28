'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 19:25:38
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-26 19:26:56
FilePath: /Spider/8_测试mitm/parse_response.py
Description: 

截取返回数据

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import json

def response(flow):
    resp = flow.response
    print(f'当前响应的URL为： {resp.url}')
    # print(f'当前响应的Cookies为： {resp.cookies}')
    # print(f'当前响应的body为： {resp.text}')

    # print(resp.headers)
    # print(resp.status_code)
    # print(resp.text)
    