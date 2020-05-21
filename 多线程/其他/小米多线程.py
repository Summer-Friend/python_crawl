import requests
import time
from multiprocessing import Queue
from threading import Thread
import json
import urllib.parse

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?'
        self.headers = {'User-Agent': 'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()

    # URL入队列
    def getUrl(self):
        # 生成10个URL地址,放到队列中
        for page in range(50):
            params = {
                'page': str(page),
                'categoryId' : '2',
                'pageSize' : '30'
            }
            params = urllib.parse.urlencode(params)
            # 把拼接的url放到url队列中
            fullurl = self.url + params
            self.urlQueue.put(fullurl)

    # 采集线程事件函数,发请求,把html给解析队列
    def getHtml(self):
        while True:
            # 如果队列不为空,则获取url
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                # 三步走
                res = requests.get(url,headers=self.headers)
                res.encoding = 'utf-8'
                html = res.text
                # 把html发到解析队列
                self.parseQueue.put(html)
            else:
                break

    # 解析线程事件函数,从解析队列get,提取并处理数据
    def parseHtml(self):
        while True:
            # 把html转换成json格式
            try:
                html = self.parseQueue.get(block=True,timeout=2)
                hList = json.loads(html)['data']
                # hList : [{应用信息1},{},{}]
                for h in hList:
                    # 应用名称
                    name = h['displayName']
                    # 应用链接
                    d = {
                        '应用名称' : name.strip(),
                        '应用链接' : 'http://app.mi.com/details?' + h['packageName']
                    }
                    with open(r'C:\Users\ThinkPad\Desktop\无人车\其他\Python\a\xiaomi.json','a') as f:
                        f.write(str(d) + '\n')
            except:
                break


    # 主函数
    def workOn(self):
        # url入队列
        self.getUrl()
        # 存放所有采集线程对象的列表
        tList = []
        # 存放所有解析线程对象的列表
        # 采集线程开始执行
        for i in range(5):
            t = Thread(target=self.getHtml)
            tList.append(t)
            t.start()
        # 解析线程开始执行
        for i in range(5):
            t = Thread(target=self.parseHtml)
            tList.append(t)
            t.start()
        # 统一回收解析线程
        for i in tList:
            i.join()

if __name__ == '__main__':
    begin = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print('执行时间:%.2f' % (end-begin))
