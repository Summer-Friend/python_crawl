'''
@Author: your name
@Date: 2020-03-03 17:39:41
@LastEditTime: 2020-03-03 17:44:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\疫情\2.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv



#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\爬虫测试\疫情\2.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
#这个理论上应该用w模式打开，这里懒得改了
writer.writerow(['省','现有确诊人数'])
  

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        
        content=response.content.decode('utf-8')
        if response.status_code==200:
            #return response.text
            return content
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
    csv_file = open(r'E:\vscode_code\爬虫测试\疫情\2.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    writer = csv.writer(csv_file)
    
    pattern = re.compile(r'<span>(.*?)</span>',re.S)##正则

    #pattern = re.compile(r'<div class="num">(.*?)</div>.*?class="title">(.*?)</a>.*?<i class="b-icon play"></i>(.*?)</span>',re.S)##正则
    #这里爬到的是一个元组。所以需要给他隔开，不然csv读取后处理会有些麻烦
    items = re.findall(pattern,html) 
    print(items)
    '''
    for item in items:
        #在这里给他分开读取
        #writer.writerow([item])
        print(item)
    '''    
    #print(items)
    csv_file.close()

def main():
    html = get_one_page(url)
    #print('打印第',(i+1),'页')
    parse_one_page(html)
    print('ok')

if __name__=='__main__':
    main()
