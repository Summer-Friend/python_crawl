'''
@Author: your name
@Date: 2020-01-17 21:53:46
@LastEditTime: 2020-02-29 10:43:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\douban_top_250_books.py
'''
import requests
import re
from requests.exceptions import  RequestException
import csv 

'''
#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理，但是标题不需要重复，所以是w
csv_file = open(r'E:\vscode_code\爬虫测试\猫眼\maoyan.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['top', 'image', 'title', 'actor', 'time', 'score'])
'''

import requests
import re
import json
import time
'''
爬取猫眼网TOP100，url：http://maoyan.com/board/4
使用requests爬取网页，正则表达式提取网页。
'''


def get_one_page(url):
    '''
    :param url:需要爬取的网页URL
    :return: 若response.status_code == 200 ,返回response.text
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_one_page(html):
    # 将正则字符串编译成正则表达式对象pattern
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>',
        re.S)
    items = re.findall(pattern, html)
    # 遍历提取结果并生成字典，形成结构数据化。
    for item in items:
        yield {
            'top': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open(r'E:\vscode_code\爬虫测试\猫眼\maoyan_top100.txt', 'a', encoding='UTF-8') as f:
        # print(type(json.dumps(content)))
        # json.dump()实现字典的序列化，并指定ensure_ascii=False，保证输出结果是中文形式而不是Unicode编码
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    '''
    调用get_one_page()的函数,并将返回的值传递给parse_one_page()进行数据提取。
    '''
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)