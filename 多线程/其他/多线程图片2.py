'''
@Author: your name
@Date: 2020-03-13 23:44:02
@LastEditTime: 2020-03-14 10:40:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\多线程图片2.py
'''
import threading
from queue import Queue
import requests
import os
import time

CRAWL_EXIT = False
class ThreadCrawl(threading.Thread):

    def __init__(self, thread_name, page_queue):
        # threading.Thread.__init__(self)
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        self.threadName = thread_name
        self.page_queue = page_queue


    def run(self):
        print(self.threadName + ' 启动************')
        while not CRAWL_EXIT:
            try:
                #global tag, url, img_format  # 把全局的值拿过来
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', }

                # 队列为空 产生异常
                page = self.page_queue.get(block=False)  # 从里面获取值
                spider_url = 'https://tuchong.com/rest/tags/%E8%87%AA%E7%84%B6/posts?page={}&count=20&order=weekly'.format(page)
                print(spider_url)
            except:
                break

            timeout = 4  # 合格地方是尝试获取3次，3次都失败，就跳出
            while timeout > 0:
                timeout -= 1
                try:
                    with requests.Session() as s:
                        response = s.get(spider_url, headers=headers, timeout=3)
                        json_data = response.json()
                        if json_data is not None:
                            imgs = json_data["postList"]
                            for i in imgs:
                                imgs = i["images"]
                                for img in imgs:
                                    user_id = img["user_id"]
                                    img_id = img["img_id"]
                                    img_url = 'https://photo.tuchong.com/{}/f/{}.jpg'.format(user_id, img_id)
                                    #self.data_queue.put(img_url)  # 捕获到图片链接，之后，存入一个新的队列里面，等待下一步的操作
                                    title = 'download/' + str(img_id)
                                    #print(title)
                                    '''
                                    response = requests.get(img_url)

                                    # 保存图片名字有问题，不知道会不会重复
                                    with open(title + '.jpg', 'wb') as f:
                                        f.write(response.content)
                                        time.sleep(3)
                                    '''

                    break
                except Exception as e:
                    print(e)
            if timeout <= 0:
                print('time out!')

def main():
    # 声明一个队列，使用循环在里面存入100个页码
    page_queue  = Queue(100)
    for i in range(1,10):
        page_queue.put(i)
    # 采集结果(等待下载的图片地址)
    #data_queue = Queue()
    # 记录线程的列表
    thread_crawl = []
    # 每次开启4个线程
    craw_list = ['采集线程1号','采集线程2号','采集线程3号','采集线程4号']

    #if not os.path.exists('download'):
    #    os.mkdir('download')

    for thread_name in craw_list:
        c_thread = ThreadCrawl(thread_name, page_queue)
        c_thread.start()
        thread_crawl.append(c_thread)
    # 等待page_queue队列为空，也就是等待之前的操作执行完毕
    while not page_queue.empty():
        pass
    # 如果page_queue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True

if __name__ == '__main__':
    main()
