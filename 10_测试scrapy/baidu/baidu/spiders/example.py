'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 20:01:07
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-26 20:07:35
FilePath: /Spider/10_测试scrapy/baidu/baidu/spiders/example.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        print(response.body.decode("utf-8"))
