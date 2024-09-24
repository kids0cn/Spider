'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-24 19:03:44
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-24 19:04:00
FilePath: /Spider/1_贴吧帖子/testTieba.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
"""
任务描述：获取贴吧任一帖子所有回复的用户和评论内容
任务分解：
    - 浏览器中查看源代码
    - 使用python读取文本文件
    - 正则表达式读取需要信息
    - 写入csv文件


"""

import re
import csv
import os
import requests


filepath = 'source.txt'
filecwd = os.getcwd()

# 读取文件
try:
    with open(filepath,'r',encoding='utf-8') as f:
        source = f.read()
except FileNotFoundError:
    print(f'\n文件{filepath},在{filecwd}没有找到\n')

source_html = requests.get("https://tieba.baidu.com/p/9125129483").content.decode()



# 正则表达式处理
# 抓大放小原则，先把包含所需信息的每层楼的块找出来

pattern = 'l_post l_post_bright j_l_post clearfix (.*?)class="p_props_tail props_appraise_wrap'
pattern_username = 'fr=pb" target="_blank">(.*?)</a>'
pattern_content = '"d_post_content j_d_post_content " style="display:;">(.*?)<'
pattern_reply_time = 'class="tail-info">(2024.*?)<'

each_reply = re.findall(pattern,source_html,re.S)

# print(len(each_reply))
result_list = []
for each in each_reply:
    result = {}
    result["username"] = re.findall(pattern_username,each,re.S)[0]
    result["content"] = re.findall(pattern_content,each,re.S)[0].replace('                    ','')
    result["reply_time"] = re.findall(pattern_reply_time,each,re.S)[0]
    result_list.append(result)
    #print(result_list)

# 写入：
with open('result.csv','w',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=['username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)