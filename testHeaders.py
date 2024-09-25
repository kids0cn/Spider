'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-25 20:12:14
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-25 20:14:38
FilePath: /Spider/testHeaders.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import requests
import json
url = 'http://exercise.kingname.info/exercise_headers_backend'

html= requests.get(url).content.decode()
html_json = json.loads(html)
print(html_json)