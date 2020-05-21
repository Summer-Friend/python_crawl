'''
@Author: your name
@Date: 2020-03-02 17:28:40
@LastEditTime: 2020-03-04 09:21:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\B站\弹幕.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv


#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\爬虫测试\B站\danmu.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
#这个理论上应该用w模式打开，这里懒得改了
writer.writerow(['弹幕'])
  

url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=2238927'

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        
        #这里，，不知道为啥要这样，可能是网页的编码方式不同
        content=response.content.decode('utf-8')
        if response.status_code==200:
            #return response.text
            return content
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
    csv_file = open(r'E:\vscode_code\爬虫测试\B站\danmu.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    writer = csv.writer(csv_file)
    
    pattern = re.compile(r'<d.*?>(.*?)</d>',re.S)##正则
    items = re.findall(pattern,html) 

    for item in items:
        #在这里给他分开读取
        writer.writerow([item])
        #print(item)
    
    #print(items)
    csv_file.close()

def main():
    html = get_one_page(url)
    #print('打印第',(i+1),'页')
    parse_one_page(html)
    print('ok')

if __name__=='__main__':
    main()
