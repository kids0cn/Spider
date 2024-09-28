'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 19:29:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-26 19:30:48
FilePath: /Spider/8_测试mitm/testTartget.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
def response(flow):
    req = flow.request
    response = flow.response

    if 'baidu.com' in req.url:
        print("这是目标网站")
        print(f'请求头是:{req.headers}')
        print(f'响应体是:{response.text}')

