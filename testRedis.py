'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-25 17:05:01
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-25 17:06:32
FilePath: /Spider/testRedis.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import redis


client = redis.StrictRedis()

client.lpush('test', '1','2','3','4','5')
print(client.lrange('test', 0, -1))