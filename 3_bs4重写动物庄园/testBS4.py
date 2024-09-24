'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-24 17:13:14
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-24 17:52:59
FilePath: /Spider/3_xpath重写动物庄园/testBS4.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from bs4 import BeautifulSoup
import re

html = '''
<html>
    <body>
        <div id="test-1">需要的内容1</div>
        <div id="test-2">需要的内容2</div>
        <div id="testfault">需要的内容3</div>
        <div id="useless">这是我不需要的内容</div>
    </body>
</html>
'''

# 解析html文件
soup = BeautifulSoup(html, 'html.parser')

#  获取div标签，id为test-1的div标签
#  .find 返回找到的第一个标签
#  .find_all 返回找到的所有标签作为列表
info = soup.find('div',id='test-1')
print(info.string)

content = soup.find_all(text=re.compile('需要的'))
# re.compile 的作用是
print(content)

pattern = re.compile(r'需要')