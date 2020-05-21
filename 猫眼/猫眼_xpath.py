'''
@Author: your name
@Date: 2020-01-17 16:04:49
@LastEditTime: 2020-03-02 19:32:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\ceshi.py
'''
from lxml import etree
import requests
import time

url = 'http://maoyan.com/board/1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

response = requests.get(url,headers=headers)
html = response.text

movie_name_xpath = '//*[@id="app"]/div/div/div/dl/dd[1]/div/div/div[1]/p[1]/a/text()'
s = etree.HTML(html)
movie_name = s.xpath(movie_name_xpath)
print(movie_name)


def get_one_page(url):
    response = requests.get(url,headers=headers)
    selector = etree.HTML(response.text)
    #主节点配合子节点爬取
    film = selector.xpath('//*[@id="app"]/div/div/div/dl/dd')
    items = selector.xpath('//*[@id="app"]/div/div/div/dl/dd/div/div/div/p/a/text()')
    #print(items)
    for item in items:
        print(item)
    #print(a)
    '''
    #利用主节点配合子节点爬取主要就是因为元素太多储存在多个列表里面输出会有所困难，不然只能输出一个长列表了
    for div in film:
        Number = div.xpath('i/text()')[0]
        Title = div.xpath('div/div/div[1]/p[1]/a/text()')[0]
        Star = div.xpath('div/div/div[1]/p[2]/text()')[0]
        #这个不知道为啥报错list index out of range如果加了[0]
        Time = div.xpath('div/div/div[1]/p[3]/text()')
        #//*[@id="app"]/div/div/div[1]/dl/dd[5]/div/div/div[1]/p[3]
        print(" ",str(Number)," ",Title," ",Star," ",Time)
    '''

if __name__=='__main__':
    for i in range(3):
        url = 'https://maoyan.com/board/6?offset={}'.format(i*10)
        print('第{}页抓取完毕'.format(i+1))
        get_one_page(url)
        #t -- 推迟执行的秒数。
        time.sleep(0.5)
    
