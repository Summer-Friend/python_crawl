'''
@Author: your name
@Date: 2020-03-14 21:30:37
@LastEditTime: 2020-03-14 21:41:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\双色球\多线程.py
'''
import random
import threading
import pandas as pd 
from queue import Queue
import time
import csv
 
# 第一步  写子类  需要继承父类THREAD 类  复写run方法
url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html' 
 
class Thread_crawl(threading.Thread):
 
    # 初始化
    def __init__(self, name, page_queue):
        threading.Thread.__init__(self)
        # 拿到任务队列
        self.page_queue = page_queue
        self.name = name
 
    def run(self):
        # # 任务开始事件
        # start_time = time.time()
        while True:
            if self.page_queue.empty():
                # # 任务结束时间
                # end_time = time.time()
                # # 需要时间
                # print(end_time - start_time)
                break
            else:
                print(self.name, '将要从队列中取任务')
                #这里就是利用了队列的特性，抽取之后就行了,get抽了之后对应的页码就消失了，不然就会重复抽取了
                page = self.page_queue.get()
                print(self.name, '取出的任务是：', page)
                url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (str(page))
                self.get_content(url=url)
                print(self.name, '完成任务：', page)
 
    def get_content(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6824.400 QQBrowser/10.3.3127.400'
        }
        tb = pd.read_html(url, skiprows=[0, 1])[0]  # 跳过前两行
        data = tb.drop([len(tb)-1])
        data.to_csv(r'E:\vscode_code\多线程\双色球\qiu2.csv', mode='a', encoding='utf_8_sig', header=0, index=0)


with open(r'E:\vscode_code\多线程\双色球\qiu2.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['开奖日期', '期号', '中奖号码', '销售额(元)', '中奖注数一等奖', '中奖注数二等奖', '详细'])
 
if __name__ == '__main__':
 
    # 任务开始事件
    start_time = time.time()
 
    # 创建队列任务
    page_queue = Queue()
    for page in range(1, 127):
        page_queue.put(page)
 
    # 2 生成线程
    #这里过于丧心病狂写了9个线程
    craw1_name = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
    craw1_tread = []
    # 为什么要创建一个空列表在集中join，如果直接使用c1 join的后果是，c1自己会干完多有的任务，才会结束
    # 因为join本身是一个阻塞线程，会使当前的线程结束后再执行第二个线程，需求是三个子线程执行操作后
    # 的总时间，而不是一个线程的时间，同时在前两个线程结束后，会形成阻塞，等待第三个完成，在三个子
    # 线程都完成的情况下，join阻塞线程才会结束，继续向下执行
    for name in craw1_name:
        crawl = Thread_crawl(name, page_queue)
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
