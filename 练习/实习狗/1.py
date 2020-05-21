'''
@Author: your name
@Date: 2020-03-08 18:10:25
@LastEditTime: 2020-03-08 20:07:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\实习狗\1.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv
from lxml import etree
import pandas as pd 


for i in range(1,6):
    url = 'https://search.51job.com/list/080200,000000,0000,32,9,99,%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
    def get_one_page(url):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            response = requests.get(url, headers = headers)
            response.encoding = response.apparent_encoding	#只要加上这行代码就可以完美解决这个问题。
            #content=response.content.decode('utf-8')
            if response.status_code==200:
                #print(response.text)
                return response.text
            return None
        except RequestException:
            return None

    def parse_one_page(html):
        #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
        s = etree.HTML(html)
        
        pattern1 = re.compile(r'<span>.*?<a target="_blank" title="(.*?)" href=.*?',re.S)##正则
        pattern2 = re.compile(r'<span class="t2"><a target="_blank" title="(.*?)" href=.*?</span>',re.S)##正则
        pattern3 = re.compile(r'<span class="t4">(.*?)</span>',re.S)##正则
        pattern4 = re.compile(r'<span class="DyListCover-hot">(.*)</span>',re.S)##正则
        
        names = re.findall(pattern1,html) 
        nums = re.findall(pattern2,html)
        salary = re.findall(pattern3, html)
        '''
        print((names))
        print((nums)) 
        print((salary[1:]))
        '''
        
        #利用字典存储多个内容，这样就可以避免使用for语句使元组隔开后分开读取了，是另外一种可行方法
        data = {'names':names, 'nums':nums, 'salary':salary[1:]}
        basic_data = pd.DataFrame.from_dict(data = data)
        basic_data.to_csv(r'E:\vscode_code\练习\实习狗\实习2.csv', mode = 'a', index=False, header=False)
        
 

    def main():
        html = get_one_page(url)
        print('打印第',(i),'页')
        parse_one_page(html)

    if __name__=='__main__':
        main()