'''
@Author: your name
@Date: 2020-01-30 11:09:15
@LastEditTime : 2020-01-30 13:37:30
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\天气网\duojincheng.py
'''
import re
import time
from multiprocessing import Pool
import requests
 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
 
def re_scraper(url):
    res = requests.get(url,headers=headers)
    names = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?</div',res.text,re.S)
    laughs = re.findall('<span class="stats-vote">.*?<i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    print('names:',comments)
    infos = []
    for name,content,laugh,comment in zip(names,contents,laughs,comments):
        info = {
            'name':name,
            'content':content,
            'laugh':laugh,
            'comment':comment,
        }
        infos.append(info)
        print('name:',info['name'])
        return  infos

 
if __name__ == "__main__":
    # re_scraper("https://www.qiushibaike.com/8hr/page/1/")
    urls = ["https://www.qiushibaike.com/8hr/page/{}/".format(str(i)) for i in range(1,35)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print('串行爬虫时间:',end_1-start_1)
    
'''
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(re_scraper,urls)
    end_2 = time.time()
    print('2进程爬虫耗时:',end_2-start_2)
 
 
    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper,urls)
    end_3 = time.time()
    print('2进程爬虫耗时:',end_3-start_3)
'''