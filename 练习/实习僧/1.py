'''
@Author: your name
@Date: 2020-03-07 19:10:15
@LastEditTime: 2020-03-07 20:34:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\实习僧\1.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv
from lxml import etree
import pandas as pd 

mapping = {'\uf242': '0', '\ue64f': '1', '&#xf19c': '2', '&#xe2d1': '3', '&#xe372': '4',
           '&#xeb5a': '5', '&#xf37c': '6', '&#xf8b6': '7', '&#xf252': '8', '&#xf3a0': '9'}  # 映射字典，使用时需自行更新


def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


for i in range(3):
    url = 'https://www.shixiseng.com/interns?page={}&keyword=%E8%BD%AF%E4%BB%B6&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E6%9D%AD%E5%B7%9E&internExtend='.format(i)

    def get_one_page(url):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            response = requests.get(url, headers = headers)
            if response.status_code==200:
                return decrypt_text(response.text)
            return None
        except RequestException:
            return None

    def parse_one_page(html):
        #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
        csv_file = open(r'E:\vscode_code\练习\实习僧\shixi_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
        writer = csv.writer(csv_file)
        writer.writerow(['名称', '类型', '主播', '热度'])
        
        s = etree.HTML(html)
        
        #网上代码剪贴过来的中英符号要注意，尤其是引号冒号这种不然会报错Invalid expression这种
        name=s.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[1]/a/text()')
        salary=s.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[1]/span/text()')
                     #//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[1]/a
        locate =s.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[2]/span[1]/text()')
                        #//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[2]/span[1]
        frequency=s.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[2]/span[3]/text()')
        print(name)
        print(salary)
        print(locate)
        print(frequency)
        
        ''' 
        data = {'names':names, 'nums':nums, 'people':file, 'num':file2}
        basic_data = pd.DataFrame.from_dict(data = data)
        '''
        #basic_data.to_csv(r'E:\vscode_code\爬虫测试\B站\Bzhan2.csv', index=False, header=False)
        #print(basic_data)
        csv_file.close()

    def main():
        html = get_one_page(url)
        print('打印第',(i+1),'页')
        parse_one_page(html)

    if __name__=='__main__':
        main()