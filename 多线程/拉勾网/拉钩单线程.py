'''
@Author: your name
@Date: 2020-03-17 11:16:30
@LastEditTime: 2020-03-17 12:55:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\拉勾网\拉钩单线程.py
'''
import requests
import re
from requests.exceptions import  RequestException
from lxml import etree
from queue import Queue
import threading
import pandas as pd 
import time

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
    basic_data.to_csv(r'E:\vscode_code\多线程\拉勾网\拉勾网单线程.csv', index=False, mode='a', header=False)
    #print(basic_data)



def main():
    page_queue=Queue()
    html = get_one_page(url)
    #print(html)
    print('打印第',(j+1),'页')
    parse_one_page(html)


i = 'dianlusheji'

for j in range(5):
    url = 'https://www.lagou.com/zhaopin/{}/{}/'.format(i, j+1)

    if __name__=='__main__':
        main()
