'''
@Author: your name
@Date: 2020-02-28 13:33:18
@LastEditTime: 2020-03-05 10:39:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\猫眼\元尊.py
'''

#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv


for i in range(100):
    url = 'https://tieba.baidu.com/f?kw=%E5%85%83%E5%B0%8A&ie=utf-8&pn={}'.format(i*50)

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
        csv_file = open(r'E:\vscode_code\爬虫测试\元尊\yuanzun_data.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
        writer = csv.writer(csv_file)
        writer.writerow(['元尊贴吧标题'])
       
        pattern = re.compile(r'class="j_th_tit ">(.*?)</a>',re.S)##正则
        items = re.findall(pattern,html) 
        for item in items:
            writer.writerow([item])
            #print(item)
        #print(items)
        csv_file.close()

    def main():
        html = get_one_page(url)
        print('打印第',(i+1),'页')
        parse_one_page(html)

    if __name__=='__main__':
        main()