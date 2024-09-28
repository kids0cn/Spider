'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-28 16:02:02
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-28 17:19:22
FilePath: /Spider/10_测试scrapy/baidu/baidu/spiders/testUAmiddle.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import scrapy


class TestuamiddleSpider(scrapy.Spider):
    name = "testUAmiddle"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["http://exercise.kingname.info/exercise_middleware_ua",
                  "http://exercise.kingname.info/exercise_middleware_ua/1",
                  "http://exercise.kingname.info/exercise_middleware_ua/2",
                  "http://exercise.kingname.info/exercise_middleware_ua/3",
                  "http://exercise.kingname.info/exercise_middleware_ua/4",
                  "http://exercise.kingname.info/exercise_middleware_ua/5",
                  "http://exercise.kingname.info/exercise_middleware_ua/6",
                  "http://exercise.kingname.info/exercise_middleware_ua/7",
                  "http://exercise.kingname.info/exercise_middleware_ua/8",
                  "http://exercise.kingname.info/exercise_middleware_ua/9",
                  "http://exercise.kingname.info/exercise_middleware_ua/10",
            
                  ]

    def parse(self, response):
        user_agent = response.request.headers.get('User-Agent').decode('utf-8')
        print(f"User-Agent: {user_agent}")
