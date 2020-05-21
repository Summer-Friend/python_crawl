'''
@Author: your name
@Date: 2020-01-19 09:50:38
@LastEditTime : 2020-01-19 10:26:21
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\豆瓣.py\bs4.py
'''
import requests
from lxml import etree
#headers必须加，不然进不去返回不了源码
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'}
url = 'https://book.douban.com/top250/'
response = requests.get(url,headers=headers)
s = etree.HTML(response.text)
#网上代码剪贴过来的中英符号要注意，尤其是引号冒号这种不然会报错Invalid expression这种
file=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/text()')
#file=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/text()')
print(file)
#,encoding='utf-8'才能保证存储的信息解码
with open('爬虫测试\豆瓣.py\豆瓣_bs4.txt','w',encoding='utf-8') as f:
    f.write(str(file))