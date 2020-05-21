'''
@Author: your name
@Date: 2020-03-01 15:49:22
@LastEditTime: 2020-03-01 16:05:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\疫情正则\龙王传说.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from lxml import etree
from requests.exceptions import  RequestException
import csv


url = 'http://www.xinbqg.com/29/29199/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }
response = requests.get(url, headers = headers)
html = response.text
 
#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\爬虫测试\json提取\疫情正则\longwang.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)

pattern = re.compile(r'<a href =.*?>(.*?)</a>',re.S)


movie_name_xpath = '//*[@id="list"]/dl/dd/a/text()'
s = etree.HTML(html)
movie_name = s.xpath(movie_name_xpath)
for element in movie_name:
    writer.writerow([element])
    print(element)

'''
items = re.findall(pattern,html) 
#print(items)
for item in items:
    #在这里给他分开读取
    #writer.writerow([item[0], item[1], item[2], item[3], item[4]])
    writer.writerow([item])
    print(item)
#print(items)
csv_file.close()
'''
print('完成')

