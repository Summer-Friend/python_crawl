'''
@Author: your name
@Date: 2020-03-07 11:19:08
@LastEditTime: 2020-03-07 12:03:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\斗鱼\crawl.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv
from lxml import etree
import pandas as pd 


for i in range(1):
    url = 'https://www.douyu.com/directory/all'

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
        csv_file = open(r'E:\vscode_code\练习\斗鱼\douyu_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
        writer = csv.writer(csv_file)
        writer.writerow(['名称', '类型', '主播', '热度'])
        
        pattern1 = re.compile(r'<h3 class="DyListCover-intro" title=(.*?)>',re.S)##正则
        pattern2 = re.compile(r'<span class="DyListCover-zone">(.*?)</span>',re.S)##正则
        pattern3 = re.compile(r'<class="DyListCover-hotIcon">(.*)</span>',re.S)##正则
        pattern4 = re.compile(r'<span class="DyListCover-hot">(.*)</span>',re.S)##正则
        
        names = re.findall(pattern1,html) 
        nums = re.findall(pattern2,html) 
        
        s = etree.HTML(html)
        #网上代码剪贴过来的中英符号要注意，尤其是引号冒号这种不然会报错Invalid expression这种
        file=s.xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div/a[1]/div[2]/div[2]/h2/text()')
        file2=s.xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div/a[1]/div[2]/div[2]/span/text()')
        
        ''' 
        data = {'names':names, 'nums':nums, 'people':file, 'num':file2}
        basic_data = pd.DataFrame.from_dict(data = data)
        '''
        basic_data.to_csv(r'E:\vscode_code\爬虫测试\B站\Bzhan2.csv', index=False, header=False)
        print(basic_data)
        csv_file.close()

    def main():
        html = get_one_page(url)
        print('打印第',(i+1),'页')
        parse_one_page(html)

    if __name__=='__main__':
        main()