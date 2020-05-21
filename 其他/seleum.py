'''
@Author: your name
@Date: 2020-01-17 22:43:00
@LastEditTime : 2020-01-18 11:43:44
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\seleum.py
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("洛克王国")

button = driver.find_element_by_css_selector('#su')
button.click()

