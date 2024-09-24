'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-24 18:50:10
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-24 22:39:48
FilePath: /Spider/4_大麦网演出爬虫/testDamai.py
Description: 
目标网站：https://search.damai.cn/
目标内容:第1页有10场演出信息，每一场演出信息包括演出名称、详情页网址、演出描述、演出时间、演出地点、票价。
保存结果：CSV
Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time
import os

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')

# 启动Chrome浏览器
service = Service('/usr/bin/chromedriver')  # 替换为chromedriver的实际路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开目标网页
url = 'https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.591b23e15dbtOt&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E5%8C%97%E4%BA%AC'
driver.get(url)
time.sleep(1)  # 等待页面加载

# 获取页面内容
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

# 关闭浏览器
driver.quit()

# 获取演出信息
item_block = soup.find('div',class_='item__box')
item_list = item_block.find_all('div',class_= 'items')

item_dict_list = []
for item in item_list:
    show_name = item.find('div',class_='items__txt__title').find('a').text
    show_list = item.find_all('div',class_='items__txt__time')
    if len(show_list) == 3:  
        show_player = show_list[0].text.strip()
        show_location = show_list[1].text.strip()
        show_time = show_list[2].text.strip()
    elif len(show_list) == 2:
        show_player = 'NULL'
        show_location = show_list[0].text.strip()
        show_time = show_list[1].text.strip()
    # print(show_player)
    item_dict = {
        'show_name': show_name,
        'show_player': show_player,
        'show_location': show_location,
        'show_time': show_time
    }
    item_dict_list.append(item_dict)

# print(item_dict_list)


# 写入csv文件
# 获取当前 Python 文件的绝对路径
current_file_path = os.path.abspath(__file__)


# 获取当前 Python 文件所在的目录
current_dir = os.path.dirname(current_file_path)

# 切换工作目录为当前 Python 文件所在的目录
os.chdir(current_dir)

with open('damai_show.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['show_name','show_player','show_location','show_time'])
    writer.writeheader()
    writer.writerows(item_dict_list)

