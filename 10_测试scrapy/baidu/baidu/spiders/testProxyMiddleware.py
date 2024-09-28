'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-28 15:25:50
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-28 17:11:40
FilePath: /Spider/10_测试scrapy/baidu/baidu/spiders/testProxyMiddleware.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import scrapy


class TestproxymiddlewareSpider(scrapy.Spider):
    name = "testProxyMiddleware"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["http://exercise.kingname.info/exercise_middleware_ip",
                  'http://exercise.kingname.info/exercise_middleware_ip/2',
                  'http://exercise.kingname.info/exercise_middleware_ip/3']

    def parse(self, response):
        print(response.decode('utf-8'))
