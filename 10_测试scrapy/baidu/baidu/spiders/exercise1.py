'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-26 22:19:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-26 22:49:16
FilePath: /Spider/10_测试scrapy/baidu/baidu/spiders/exercise1.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import scrapy
from bs4 import BeautifulSoup

class Exercise1Spider(scrapy.Spider):
    name = "exercise1"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["http://exercise.kingname.info/exercise_xpath_2.html"]

    def parse(self, response):
        soup = BeautifulSoup(response.body.decode("utf-8"), "html.parser")
        lists = soup.find_all("ul", class_="item")
        items = []
        for li in lists:
            name_element = li.find('li', class_='name')
            price_element = li.find('li', class_='price')

            print("++++++++++++")
            print(price_element)
            item = {
                'name': name_element.text if name_element else 'NULL',
                'price': price_element.text if price_element else 'NULL',
                
            }
            items.append(item)
        
        for item in items:
            print(f"商品:{item['name']}, 价格:{item['price']}")




