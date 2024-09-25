'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-25 17:07:54
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-25 18:53:12
FilePath: /Spider/5_小说白夜行/testBaiyexing.py
Description: 
目标网站：https://baiyexing.chibaba.cn/。
目标内容：小说《白夜行》第一章到第十三章的正文内容。
任务要求：编写两个爬虫，
    爬虫1从https://baiyexing.chibaba.cn/获取小说《白夜行》第一章到第十三章的网址，
    并将网址添加到Redis里名为url_queue的列表中。
    爬虫2从Redis里名为url_queue的列表中读出网址，进入网址爬取每一章的具体内容，
    再将内容保存到MongoDB中。


Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options # 无头模式是指在后台运行，不显示浏览器窗口
import time
import redis
import pymongo
from multiprocessing import Pool

# 设置chromedriver
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

# 启动chromedriver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_option)


def get_toc_url(url,client_redis):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    url_list_block = soup.find('div',class_='booklist')
    url_list = url_list_block.find_all('a')
    #print(url_list)
    for url in url_list:
        client_redis.lpush('url_queue',url['href'])

    
def get_content(url):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    contetn = soup.find('div',{'class':'news_con','id':'TextContent'}).text
    title = soup.find('h1',{'class':'news_title'}).text
    return contetn,title


def init_redis():
    client_redis = redis.Redis()
    return client_redis


def init_mongo():
    client_mongo = pymongo.MongoClient()
    db = client_mongo['baiyexing']
    collection_beyexing = db['baiyexing']
    return collection_beyexing

def query_article(client_redis,collection_beyexing):
    while client_redis.llen('url_queue') > 0:
        url = client_redis.lpop('url_queue').decode('utf-8')
        content,title = get_content(url)
        collection_beyexing.insert_one({'title':title,'content':content})



if __name__ == '__main__':
    
    source = 'https://baiyexing.chibaba.cn/'
    client_redis = init_redis()
    collection_beyexing = init_mongo()

    get_toc_url(source,client_redis)
    
    query_article(client_redis,collection_beyexing)

    