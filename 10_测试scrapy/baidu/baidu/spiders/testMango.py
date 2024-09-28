'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-28 12:31:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-28 12:51:42
FilePath: /Spider/10_测试scrapy/baidu/baidu/spiders/testMango.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import scrapy
from baidu.items import PersonInfoItem

class TestmangoSpider(scrapy.Spider):
    name = "testMango"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["http://exercise.kingname.info/exercise_xpath_3.html"]

    def parse(self, response):
        person_list = response.xpath("/html/body/div/table/tbody/tr")
        for person in person_list:
            item = PersonInfoItem()
            person_info  = person.xpath("./td/text()").extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item
