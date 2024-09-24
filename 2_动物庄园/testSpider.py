'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-14 22:05:50
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-23 21:32:52
FilePath: /Spider/testSpider.py
Description

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''



import requests
import re
import os
from multiprocessing.dummy import Pool
import time
import random
import chardet 


def save(title,article):
    '''
    description:
    @param title:章节名称
    @param article:章节内容
    return {*}
    '''    
    os.makedirs(file_dir,exist_ok=True) 
    file_path = os.path.join(file_dir,title+'.txt')
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(article)
    return 1
    

def get_article(url):
    '''
    description: 
    @param url : 文章的网页
    return {*}
        title : 文章标题
        article : 文章内容
    '''    
    time.sleep(random.uniform(0.5,3))
    import chardet

def get_article(url):
    response = requests.get(url)
    encoding = chardet.detect(response.content)['encoding']
    if encoding.lower() == 'gb2312':
        encoding = 'gbk'

    # print('+++++++++++')
    # print(url)
    # print(encoding)
    # print('+++++++++++')

    source = response.content.decode(encoding)
    title = re.findall('size="4"> (.*?)<',source,re.S)[0]
    article = re.search('<p>(.*?)</p>',source,re.S).group(1)
    article = article.replace('<br />','')
    article = article.replace('&nbsp;','')
    return title,article


def get_toc(html_toc):
    
    '''
    输入：url
    输出：文章目录
    '''
    url_list = []
    toc_block = re.findall('>正文<(.*?)>上一篇',html_toc,re.S)[0]
    toc_url = re.findall('<a href="(.*?)">',toc_block,re.S)
    for url in toc_url:
        url_list.append(source+url)
    return url_list
    


def query_article(toc):
    '''
    输入：目录列表
    输出： 直接保存当前目录的文章
    '''
    title,article = get_article(toc)
    save(title,article)

# def check_charset(url):
#     response = requests.get(url)
#     encoding = chardet.detect(response.content)['encoding']
#     if encoding.lower() == 'gb2312':
#         encoding = 'gbk'
#     print(encoding)
#     return encoding

if __name__ == '__main__':
    source = input("请输入网址: ")
    if not source:
        source = "https://www.kanunu8.com/book3/6879/"  # 如果用户没有输入网址，则默认使用
    print(f"使用的网址: {source}")

    response = requests.get(source)
    encoding = chardet.detect(response.content)['encoding']
    if encoding.lower() == 'gb2312':
        encoding = 'gbk'
    html_toc = response.content.decode(encoding)
    file_dir = re.findall('<title>([^\\s]*)',html_toc,re.S)[0]
    print(f"小说名字: {file_dir}")

    # 获取文章列表
    toc_list = get_toc(html_toc)
    print(toc_list)

    pool = Pool(10)
    pool.map(query_article,toc_list)
    pool.close()
    pool.join() # 确保子进程完成，
    

    


