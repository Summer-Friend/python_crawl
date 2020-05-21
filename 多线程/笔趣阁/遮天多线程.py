'''
@Author: your name
@Date: 2020-03-15 08:45:37
@LastEditTime: 2020-03-15 09:48:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\笔趣阁\2.py
'''
import threading
import time
import requests
import re
from queue import Queue

#需要注意这里多线程并没有解决
headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "X-Requested-with": "XMLHttpRequest"
          }


class Thread_crawl(threading.Thread):
 
    # 初始化
    def __init__(self, name, chapter_queue):
        threading.Thread.__init__(self)
        # 拿到任务队列
        self.chapter_queue = chapter_queue
        self.name = name
 
    def run(self):
        # # 任务开始事件
        # start_time = time.time()
        while True:
            if self.chapter_queue.empty():
                # # 任务结束时间
                # end_time = time.time()
                # # 需要时间
                # print(end_time - start_time)
                break
            else:
                print(self.name, '将要从队列中取任务')
                #这里就是利用了队列的特性，抽取之后就行了,get抽了之后对应的页码就消失了，不然就会重复抽取了
                chapter = self.chapter_queue.get()
                print(self.name, '取出的任务是：', chapter)
                download(chapter)
                print(self.name, '完成任务：', chapter)
                
def get_urls(url):
    response = requests.get(url = url, headers = headers)
    datas = re.findall('<a href ="(.*?)">', response.text,re.S)   
    for data in datas:
        data = "https://www.sbiquge.com"+data
        chapter_queue.put(data)
    #return chapter_queue
    #download()       
        

path = r'E:\vscode_code\多线程\笔趣阁\遮天.txt'
             
def download(chapter):
    #print("start")   
    #for data in datas:
    text = requests.get(url = chapter,headers = headers).text
    try:
        contents = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',text,re.S)
        with open(path,'a+', encoding="utf-8") as file:
            for content in contents:
                file.write(content)
            file.write("\n")
            file.close()
    except Exception as e:
        print(e)

url = "https://www.sbiquge.com/0_466/"
           
if __name__ == '__main__':
 
    # 任务开始事件
    start_time = time.time()
 
    # 创建队列任务
    chapter_queue = Queue()
    #获取网址队列
    get_urls(url)
    '''
    for chapter in range(1, 127):
        chapter_queue.put(chapter)
    '''
 
    # 2 生成线程
    #这里过于丧心病狂写了9个线程
    craw1_name = ['c1', 'c2', 'c3', 'c4', 'c5']
    craw1_tread = []
    
    for name in craw1_name:
        crawl = Thread_crawl(name, chapter_queue)
        #start即调用run方法
        crawl.start()
        craw1_tread.append(crawl)
 
    ##join 阻塞线程，让子线程都完成任务后，主线程再往下进行
    for thread in craw1_tread:
        thread.join()
 
    # 任务结束时间
    end_time = time.time()
    # 需要时间
    print(end_time - start_time)

#download("https://www.sbiquge.com/0_466/")
