'''
@Author: your name
@Date: 2020-03-13 23:44:02
@LastEditTime: 2020-03-14 10:31:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\多进程图片.py
'''
import urllib
import threading
from bs4 import BeautifulSoup
import requests
import os
import time
import lxml
 
# 页面链接的初始化列表
page_links_list=['http://www.netbian.com/']
# 图片链接列表
img_links_list = []
 
#获取爬取的页数和页面链接
def GetUrls(page_links_list):
    #pages = int(input('请输入你想爬取的页数：'))
    pages = 5
    if pages > 1:
        for page in range(2, pages + 1):
            url = 'http://www.netbian.com/index_' + str(page) + '.htm'
            page_links_list.append(url)
    else:
        page_links_list=page_links_list
 
#初始化锁,创建一把锁
gLock=threading.Lock()
 
#生产者，负责从每个页面中获取图片的链接
class Producer(threading.Thread):
    def run(self):
        print("%s is running"%threading.current_thread())
        while len(page_links_list)>0:
            #上锁
            gLock.acquire()
            #默认取出列表中的最后一个元素
            page_url=page_links_list.pop()
            #释放锁
            gLock.release()
 
            #获取img标签
            html = requests.get(page_url).content.decode('gbk')
            soup = BeautifulSoup(html, 'lxml')
            imgs = soup.select("div.list li a img")
 
            #加锁3
            gLock.acquire()
            for img in imgs:
                img_link = img['src']
                img_links_list.append(img_link)
            #释放锁
            gLock.release()
        #print(len(img_links_list))
 
#消费者，负责从获取的图片链接中下载图片
class Consumer(threading.Thread,):
    def run(self):
        print("%s is running"%threading.current_thread())
        while True:
            #print(len(img_links_list))
            #上锁
            gLock.acquire()
            if len(img_links_list)==0:
                #不管什么情况，都要释放锁
                gLock.release()
                continue
            else:
                img_url=img_links_list.pop()
                #print(img_links_list)
                gLock.release()
                filename=img_url.split('/')[-1]
                print('正在下载：', filename)
                #path = r'C:\Users\ThinkPad\Desktop\无人车\其他\Python\picture\\'+filename
                #urllib.request.urlretrieve(img_url, filename=path)
                if len(img_links_list)==0:
                    end=time.time()
                    print("消耗的时间为：", (end - start))
                    exit()
 
 
if __name__ == '__main__':
    GetUrls(page_links_list)
    #os.mkdir('./images')
    start=time.time()
    # 5个生产者线程，去从页面中爬取图片链接
    for x in range(5):
        Producer().start()
 
    # 10个消费者线程，去从中提取下载链接，然后下载
    for x in range(10):
        Consumer().start()
