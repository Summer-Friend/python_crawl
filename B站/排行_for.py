'''
@Author: your name
@Date: 2020-03-02 12:20:52
@LastEditTime: 2020-03-02 13:12:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\B站\1.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv

'''
#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\爬虫测试\B站\Bzhan.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
#这个理论上应该用w模式打开，这里懒得改了
writer.writerow(['排名', '名称', '观看人数'])
'''     

url = 'https://www.bilibili.com/ranking/all/0/0/3'

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
    #csv_file = open(r'E:\vscode_code\爬虫测试\B站\Bzhan.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    #writer = csv.writer(csv_file)
    
    #针对于多条数据的正则表达式爬取，就是用多个括号       
    #针对匹配，一个尖括号结束之后最好用.*?过渡到另一个尖括号，不要什么都不加，可能抓不出来
    #pattern = re.compile(r'<div class="num">(.*?)</div>.*?class="title">(.*?)</a>',re.S)##正则
    pattern = re.compile(r'class="title">(.*?)</a>.*?<div class="num">(.*?)</div>',re.S)##正则

    #pattern = re.compile(r'<div class="num">(.*?)</div>.*?class="title">(.*?)</a>.*?<i class="b-icon play"></i>(.*?)</span>',re.S)##正则
    #r'class="j_th_tit ">(.*?)</a><span class=.*? title="回复">(.*?)</span><span class=.*?title="主题作者:(.*?)" data-field=.*?><span class=.*? title="最后回复时间">(.*?)</span>'
    #这里爬到的是一个元组。所以需要给他隔开，不然csv读取后处理会有些麻烦
    items = re.findall(pattern,html) 
    '''
    for item in items:
        #在这里给他分开读取
        writer.writerow([item[0], item[1], item[2]])
        #print(item)
    '''
    print(items)
    #csv_file.close()

def main():
    html = get_one_page(url)
    #print('打印第',(i+1),'页')
    parse_one_page(html)
    print('ok')

if __name__=='__main__':
    main()

