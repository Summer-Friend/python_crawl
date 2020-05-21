'''
@Author: your name
@Date: 2020-03-17 11:16:37
@LastEditTime: 2020-03-17 13:11:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\拉勾网\拉钩多线程.py
'''
import requests
import re
from requests.exceptions import  RequestException
from lxml import etree
from queue import Queue
import threading
import pandas as pd 
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
                
                for j in range(30):
                    url = 'https://www.lagou.com/zhaopin/{}/{}/'.format(page, j+1)
                    main(url, j)
                print(self.name, '完成任务：', page)


#拉勾网有反爬，cookies变化
#https://www.cnblogs.com/kuba8/p/10808023.html
def get_one_page(url):
        try:
            time.sleep(0.5)
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            
            #应对拉钩的反爬措施
            s = requests.Session() # 创建一个session对象
            s.get(url, headers=headers, timeout=3)  # 用session对象发出get请求，请求首页获取cookies
            cookie = s.cookies  # 为此次获取的cookies
            response = s.post(url, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
            
            #response = requests.get(url, headers = headers)
            #response.encoding = response.apparent_encoding
            if response.status_code==200:
                #print(response)
                return response.text
                #return response.content.decode("utf8", "ignore")
            return None
        except RequestException:
            return None

def parse_one_page(html):
    
    x = etree.HTML(html)
 
    #职位名称
    names = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3/text()')
    #//*[@id="s_position_list"]/ul/li[3]/div[1]/div[1]/div[1]/a/h3
    #print(names)
    
    #地点
    dire = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/span/em/text()')
    #print(dire)
    
    #薪资
    money = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[2]/div/span/text()')
    #print(len(money))
    
    #经验
    experience = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[2]/div/text()')
    #爬虫数据清洗 
    experience=[exp.strip() for exp in experience if exp.strip()!='']
    #print(experience)
    
    
    #公司条件
    condition = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[2]/div[2]/text()')
    condition=[exp.strip() for exp in condition if exp.strip()!='']
    
    #公司名称
    company = x.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[2]/div[1]/a/text()')
    
    #公司福利
    welfare = x.xpath('//*[@id="s_position_list"]/ul/li/div[2]/div[2]/text()')
    welfare=[exp.replace('“', '').replace('”', '') for exp in welfare if exp.strip()!='']
    #print(welfare)
    
    #利用字典存储多个内容，这样就可以避免使用for语句使元组隔开后分开读取了，是另外一种可行方法
    data = {'names':names, 'direction':dire, 'money':money, 'experience':experience, 'condition':condition,
            'company':company, 'welfare':welfare}
    basic_data = pd.DataFrame.from_dict(data = data)
    basic_data.to_csv(r'E:\vscode_code\多线程\拉勾网\拉勾网多线程.csv', index=False, mode='a', header=False)
    #print(basic_data)



def main(url, j):
    html = get_one_page(url)
    #print(html)
    #print('打印第',(j+1),'页')
    parse_one_page(html)


#写标题
with open(r'E:\vscode_code\多线程\拉勾网\拉勾网多线程.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['names', 'direction', 'money', 'experience', 'condition', 'company', 'welfare'])


#要爬取的队列标题
crawl_list = ['danpianji', 'dianlusheji', 'zidonghua', 'qianrushi', 'yingjian', 'Python'] 

#多线程开始
if __name__ == '__main__':
 
    # 任务开始事件
    start_time = time.time()
 
    # 创建队列任务
    page_queue = Queue()
    for page in crawl_list:
        page_queue.put(page)
 
    # 2 生成线程
    #这里过于丧心病狂写了9个线程
    craw1_name = ['c1', 'c2', 'c3']
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
    
    