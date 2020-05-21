'''
@Author: your name
@Date: 2020-02-29 10:53:14
@LastEditTime: 2020-02-29 12:21:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\元尊\2.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv

#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\爬虫测试\元尊\yuanzun_3.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
#这个理论上应该用w模式打开，这里懒得改了
writer.writerow(['回复数', '元尊贴吧标题', '作者', '发帖时间'])
      
for i in range(2):
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
        csv_file = open(r'E:\vscode_code\爬虫测试\元尊\yuanzun_3.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
        writer = csv.writer(csv_file)
        #这个理论上应该用w模式打开，这里懒得改了
        #writer.writerow(['回复数', '元尊贴吧标题'])
        
        #针对于多条数据的正则表达式爬取，就是用多个括号       
        pattern = re.compile(r'class="j_th_tit ">(.*?)</a>',re.S)##正则
        #r'class="j_th_tit ">(.*?)</a><span class=.*? title="回复">(.*?)</span><span class=.*?title="主题作者:(.*?)" data-field=.*?><span class=.*? title="最后回复时间">(.*?)</span>'
        #这里爬到的是一个元组。所以需要给他隔开，不然csv读取后处理会有些麻烦
        items = re.findall(pattern,html) 
        for item in items:
            #在这里给他分开读取
            writer.writerow([item[0], item[1]])
            #
            #print(item)
        #print(items)
        csv_file.close()

    def main():
        html = get_one_page(url)
        print('打印第',(i+1),'页')
        parse_one_page(html)

    if __name__=='__main__':
        main()
