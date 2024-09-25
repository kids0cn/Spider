'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-25 21:10:18
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-25 21:36:32
FilePath: /Spider/testZhihuLogin.py
Description: 
（1）初始化ChromeDriver。（2）打开知乎登录页面。
（3）找到用户名的输入框，输入用户名。（4）找到密码输入框，输入用户名。
（5）手动单击验证码。（6）按下Enter键。
Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # KEY类主要包含了模拟键盘输入的功能
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

# 设置无头模式
#chrome_option = Options()
# chrome_option.add_argument('--headless')
#chrome_option.add_argument('--disable-gpu')

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

url = 'https://www.zhihu.com/signin?next=%2F'
driver.get(url)

# 找到用户名输入框，输入用户名
driver.find_element(By.NAME,'username').send_keys('kids0cn@gmail.com')

# 找到密码输入框，输入密码
driver.find_element(By.NAME,'password').send_keys('fcts1230')

time.sleep(10)
print(driver.page_source)

driver.quit()