'''
@Author: your name
@Date: 2020-01-19 09:26:30
@LastEditTime : 2020-02-02 21:47:35
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\猫眼\test.py
'''
import requests
from lxml import etree
#headers必须加，不然进不去返回不了源码
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
url = 'https://movie.douban.com/top250'
response = requests.get(url,headers=headers)
s = etree.HTML(response.text)
movies = s.xpath('//ol[@class="grid_view"]/li')
item = []
for movie in movies:
        '''
        time = movie.xpath('.//div[@class="pic"]/em/text()')[0]       
        film = movie.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]      
        director = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()')[0]  
        actor = movie.xpath('.//div[@class="star"]/span/text()')[0]        
        print("电影：",str(film)+'|'+"导演：",str(director)+'|'+"主演：",str(actor)+'|'+"时长：",str(time))
        '''
        item = movie.xpath('.//div[@class="pic"]/em/text()')[0]
        print(str(item))
        

                