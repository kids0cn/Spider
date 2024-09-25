'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-24 23:10:05
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-25 15:44:50
FilePath: /Spider/testMongo.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['test'] 

collection = db['test']

collection.insert_one({'name': 'John', 'age': 30})

more_data = [
            {'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
            {'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
            {'id': 4, 'name': '王五', 'age': 40, 'salary': 1000},
            {'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'}]

collection.insert_many(more_data)

print(x for x in collection.find())

