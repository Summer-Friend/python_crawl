'''
@Author: your name
@Date: 2020-03-11 20:29:31
@LastEditTime: 2020-05-06 13:07:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\ajax\微博\1.py
'''
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
 
base_url = 'https://m.weibo.cn/api/container/getIndex?' # 这里要换成对应Ajax请求中的链接
 
headers = {
    #'Host':'m.weibo.cn',
    #'Referer':'https://m.weibo.cn/u/2830678474',
    #'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}  #  不同于简单的requests,只需要传入客户端信息就好了
 
def get_page(page):
    params = {
        'type':'uid',
        'value':'2830678474',
        'containerid':'1076032830678474',
        'page':page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json() # 解析内容为json返回
    except requests.ConnectionError as e:
        print('Error',e.args) #输出异常信息
 
 
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text() # 这里面的文字内容又进行了一层解析,将正文里面的html标签去掉
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
 
if __name__ =='__main__': # 本脚本窗口下的程序名字就叫做main,且这样写在别的程序调用该脚本文件的函数时不会受到影响
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)