'''
@Author: your name
@Date: 2020-03-14 16:02:39
@LastEditTime: 2020-03-14 22:39:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\笔趣阁\test.py
'''
import requests
import re
from requests.exceptions import  RequestException
from lxml import etree
from queue import Queue
import threading

url_test = 'https://www.biqiuge.com/book/1/'

def get_one_page(url):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            response = requests.get(url, headers = headers)
            response.encoding = response.apparent_encoding
            if response.status_code==200:
                return response.text
                #return response.content.decode("utf8", "ignore")
            return None
        except RequestException:
            return None

def parse_one_page(html):
    name = '龙符'
    pattern = re.compile(r'<dd><a href=(.*?)>.*?</a></dd>',re.S)##正则
    items = re.findall(pattern,html) 
    print(items)
    a = etree.HTML(html)
    lists = a.xpath("/html/div[6]/dl/dd[11]/text()")
    print(lists)
    
    '''
    for url in urls:
        url = 'https://www.biqiuge.com/book/1/' + url
        print(url)
    #将小说每一个章节的目录存放入队列
        page_queue.put(url)
    
    file = open(r'E:\vscode_code\多线程\笔趣阁\\' + name + ".txt", "a", encoding="utf8")
    file.write(title)
    file.write(novel)
    '''


def main():
    page_queue=Queue()
    html = get_one_page(url_test)
    #print('打印第',(i+1),'页')
    parse_one_page(html)
    while not page_queue.empty():
        print (page_queue.get())

if __name__=='__main__':
    main()