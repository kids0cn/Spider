'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 19:20:37
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-26 22:43:24
FilePath: /Spider/8_测试mitm/parse_request.py
Description: 

截取发送数据

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
def request(flow):
      req = flow.request
      print(f'当前请求的URL为： {req.url}')
      #print(f'当前的请求方式为： {req.method}')
      #print(f'当前的Cookies为： {req.cookies}')
      #print(f'请求的body为： {req.text}')

    # print(flow.request.headers)
    # # print(flow.request.method)
    # # print(flow.request.headers)
    # # print(flow.request.cookies)
    # # print(flow.request.body)
    # # print(flow.request.urlencoded_form)
    # # print(flow.request.json)
    # # print(flow.request.text)
    