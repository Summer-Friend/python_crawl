'''
@Author: your name
@Date: 2020-01-30 11:28:03
@LastEditTime : 2020-01-30 11:28:35
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\多进程\a.py
'''
from multiprocessing import Pool
import time
import os
 
 
def task(name):   
     print('a')

if __name__=='__main__':
    print ('Parent process %s'%os.getpid())
    p=Pool()
    for i in range(9):
        p.apply_async(task,args=(i,))
    print ('Waiting for all subprocess done ...')
    p.close()
    p.join()
    print ('All subprocess done')
