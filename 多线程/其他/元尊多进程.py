import threading
import requests
from bs4 import BeautifulSoup
import time
import sys
#多线程
class myThreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):

        getUrl(main())

def getUrl(page):
    i=1
    for nextpage in page:
        url = "http://book.zongheng.com/chapter/685640/{}.html".format(nextpage)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        response = requests.get(url,headers = headers)

        soup = BeautifulSoup(response.text,'html.parser')
        div = soup.findAll("div",class_ = "content")
        title = soup.findAll("div",class_ = "title_txtbox")
        #最终的标题
        souptitle = BeautifulSoup(str(title),'html.parser').text.strip("[]")
        #最终要写入文件的小说内容
        souptext = BeautifulSoup(str(div),'html.parser').text.strip("[]").replace("。","。\n")

        f = open(r"C:\Users\ThinkPad\Desktop\无人车\其他\Python\元尊\f.txt","a")
        f.write(str(souptitle)+'\r')
        f.write(str(souptext)+'\r')
        f.close()
        #打印进度条
        sys.stdout.write("\r已经完成：{}%".format(i/len(page)*100))
        sys.stdout.flush()
        time.sleep(0.1)
        i = i+1

def main():
    a = ['38883752']
    for i in range(90):
        url = "http://book.zongheng.com/chapter/685640/{}.html".format(a[i])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 小说内容在div标签里
        nextpage = soup.body['nextchapterid']
        a.append(nextpage)
    return a

if __name__ == '__main__':
    strattime = time.time()
    thread1 = myThreading()
    thread1.start()
    thread1.join()
    print("")
    print("爬取完成")
    endtime = time.time()
    print("耗时：{}s".format(endtime - strattime))
