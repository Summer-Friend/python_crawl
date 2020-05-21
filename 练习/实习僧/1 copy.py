'''
@Author: your name
@Date: 2020-03-07 19:10:15
@LastEditTime: 2020-03-08 13:36:29
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
import chardet

mapping = {'&#xe028': 'k', '&#xe033': 'u', '&#xe063': '个', '&#xe077': 'n', '&#xe0f2': 'l', '&#xe11c': 'K', '&#xe1a2': 'p', '&#xe1c8': 'Q', '&#xe1f1': 'Z', '&#xe21c': '三', '&#xe24e': 'G', '&#xe2b9': 'g', '&#xe2d9': 'Y', '&#xe2e9': '软', '&#xe33e': 'P', '&#xe3c0': '天', '&#xe3f5': 'w', '&#xe430': 'o', '&#xe4f4': 'W', '&#xe4fe': 'U', '&#xe50e': '告', '&#xe51d': '广', '&#xe536': 'F', '&#xe5c6': '联', '&#xe5f3': 's', '&#xe62d': 'c', '&#xe63c': 'v', '&#xe64f': '0', '&#xe665': 'm', '&#xe6ce': 'i', '&#xe6e3': 'I', '&#xe749': '一', '&#xe795': '程', '&#xe7a8': 'q', '&#xe7be': '3', '&#xe7d6': 'E', '&#xe7f9': 't', '&#xe7fb': '4', '&#xe809': '端', '&#xe831': '银', '&#xe884': 'y', '&#xe893': '5', '&#xe8e6': '计', '&#xe95e': 'B', '&#xe96c': 'M', '&#xe975': '7', '&#xe976': 'b', '&#xe989': '二', '&#xe9be': '周', '&#xea2a': 'O', '&#xea94': '人', '&#xeabd': '财', '&#xeb61': '互', '&#xeb9c': 'X', '&#xebe2': '件', '&#xec15': '8', '&#xec2b': 'V', '&#xecaa': '工', '&#xed3c': 'h', '&#xed71': '行', '&#xed76': 'N', '&#xedf7': 'H', '&#xedfa': '场', '&#xee20': '年', '&#xee24': '市', '&#xee9e': '生', '&#xeed3': 'A', '&#xeee9': 'T', '&#xef13': 'z', '&#xef40': 'x', '&#xef43': 'S', '&#xef79': 'a', '&#xefcf': '网', '&#xf09c': '月', '&#xf154': '五', '&#xf221': '6', '&#xf242': '2', '&#xf3ff': 'r', '&#xf40a': '前', '&#xf434': '聘', '&#xf447': 'D', '&#xf475': '招', '&#xf485': '9', '&#xf48a': '政', '&#xf4a0': 'e', '&#xf58e': '师', '&#xf5e8': '四', '&#xf5f6': 'L', '&#xf6b4': 'f', '&#xf6d6': 'j', '&#xf6e5': '设', '&#xf718': '1', '&#xf71b': '会', '&#xf740': '作', '&#xf74d': 'd', '&#xf7c2': 'J', '&#xf7ef': 'R', '&#xf8b9': 'C'} # 映射字典，使用时需自行更新

def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


for i in range(1):
    url = 'https://www.shixiseng.com/interns?page={}&keyword=%E8%BD%AF%E4%BB%B6&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E6%9D%AD%E5%B7%9E&internExtend='.format(i)

    def get_one_page(url):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            response = requests.get(url, headers = headers)
            if response.status_code==200:
                response = requests.get(url=url, headers=headers).content  # 得到字节
                charset = chardet.detect(response).get('encoding')  # 得到编码格式
                response = response.decode(charset, "ignore")  # 解码得到字符串
                #print (decrypt_text(response.text))
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
        locate =s.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[2]/span[1]/text()')
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