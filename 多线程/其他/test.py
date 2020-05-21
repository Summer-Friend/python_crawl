'''
@Author: your name
@Date: 2020-03-14 13:55:40
@LastEditTime: 2020-03-14 14:07:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\test.py
'''
import threading
import time

url = 'http://www.biqiuge.com/book/'   #多线程

exitFlag = False

class myThread(threading.Thread):
    def __init__(self,threadID,name,url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url
    def run(self):
        print('开始线程:' + self.name)
        time.sleep(1)
        print("退出线程:" + self.name)
# cmd = 'del /q /s *.txt'
# os.system(cmd)
start = 340
space = 350

craw1_tread = []

for i in range(start,space):
    url_tmp = url + str(i) + '/'
    #print(url_tmp)
    tmp = 'Thread-' + str(i)
    threadName = myThread(i,tmp, url_tmp)
    threadName.start()
    craw1_tread.append(threadName)
    #print(threadName)

'''    
for i in range(start,space):
    #threadName = myThread(i,tmp, url_tmp)
    threadName.join()
'''
#join确保所有分支线程执行完后再退出主线程
for thread in craw1_tread:
        thread.join()
   
     
print("exit")
