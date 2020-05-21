'''
@Author: your name
@Date: 2020-01-19 09:26:30
@LastEditTime : 2020-02-02 21:12:37
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\猫眼\test.py
'''
import requests
from lxml import etree
#headers必须加，不然进不去返回不了源码
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url = 'https://movie.douban.com/subject/1292052/'
response = requests.get(url,headers=headers)
s = etree.HTML(response.text)
'''
data = requests.get(url).text
s=etree.HTML(data)
'''
#这个[0]使得你原本爬取的数据附带的中括号被消去了，原本看着挺不美观的
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]   #导演
actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')[0]
time=s.xpath('//*[@id="info"]/span[13]/text()')[0]
print("电影：",str(film)+'|'+"导演：",str(director)+'|'+"主演：",str(actor)+'|'+"时长：",str(time))
