'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 20:00:04
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-28 13:05:44
FilePath: /Spider/10_测试scrapy/baidu/baidu/pipelines.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo



class BaiduPipeline:
    def process_item(self, item, spider):
        return item

class PersonInfoPipeline(object):

    def __init__(self,crawler):
        self.settings = crawler.settings
        host = self.settings.get('MONGODB_HOST')
        port = self.settings.get('MONGODB_PORT')
        dbname = self.settings.get('MONGODB_DBNAME')
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.post = db[self.settings.get('MONGODB_DOCNAME')]
        

    def process_item(self, item, spider):
        person_info = dict(item)
        self.post.insert_one(person_info)  # 将 insert 改为 insert_one
        return item

    @classmethod
    def from_crawler(cls, crawler): 
        return cls(crawler)