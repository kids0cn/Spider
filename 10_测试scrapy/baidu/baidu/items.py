'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 20:00:04
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-28 12:33:15
FilePath: /Spider/10_测试scrapy/baidu/baidu/items.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PersonInfoItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    salary = scrapy.Field()
    phone = scrapy.Field()

