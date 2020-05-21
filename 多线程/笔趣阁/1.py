'''
@Author: your name
@Date: 2020-03-14 15:42:40
@LastEditTime: 2020-03-14 16:13:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\笔趣阁\1.py
'''
import requests
from lxml import etree
from queue import Queue
import threading
q =False


#爬取改小说目录的所有章节url地址
def spider(url,page_queue):
    req = requests.get(url)
    #获取小说章节目录得地址
    html = etree.HTML(req.content.decode("utf8", "ignore"))
    lists = html.xpath("//div[@id ='list']/dl//dd")
    for list in lists:
       title_url = "".join(list.xpath("./a/@href"))
       #效果一样
       #title_url = (list.xpath("./a/@href"))[0]
      #将小说每一个章节的目录存放入队列
       page_queue.put(title_url)

#多线程下载小说章节
def download(page_queue,file,lock):
    while not q:
        try:
            url = page_queue.get(False)
            req = requests.get("http://www.xbiquge.la"+url)  # 获取响应
            html = etree.HTML(req.content.decode("utf8", "ignore"))
            title = html.xpath("//div[@class='bookname']/h1/text()")
            title = "".join(title)
            lists = html.xpath("//div[@id='content']/text()")
            novel = "\n".join(lists).replace("&nbsp", " ")
            print("章节"+title+"下载完毕")
            #设置锁 避免多线程对文件的读写出错
            '''
            with lock:
                file.write(title)
                file.write("\n")
                file.write(novel)
                file.write("\n")
            '''
        except:
            pass

def main():
    name = '伏天氏'
    url = 'http://www.xbiquge.la/0/951/'
    if url!="":
        page_queue=Queue()
        file = open(r'E:\vscode_code\多线程\笔趣阁\\' + name + ".txt", "a", encoding="utf8")
        spider(url,page_queue)
        lock=threading.Lock()
        threadlist=[]
        print("开始下载小说：  "+name)
        #开设8个线程一起运行下载的方法
        for i in range(1,28):
            t=threading.Thread(target=download,args=(page_queue,file,lock,))
            t.start()
            threadlist.append(t)
           #判断章节目录有无空，不为空一直运行
        while not page_queue.empty():
            pass
        global q
        q=True
        #另主线程阻塞等待，使创建的线程都执行完毕
        for thread in threadlist:
            thread.join()
        file.close()
        print("小说：  "+name+"    下载完毕")
if __name__ == '__main__':
    main()
