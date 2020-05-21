'''
@Author: your name
@Date: 2020-03-01 16:22:44
@LastEditTime: 2020-03-01 16:28:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\疫情正则\职业.py
'''
#好啊吧，我承认这一天我太无聊了水着玩的
import requests
import re
from requests.exceptions import  RequestException
import csv


url = 'https://job.ncss.cn/student/jobs/index.html'

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
            }
        response = requests.get(url, headers = headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
    csv_file = open(r'E:\vscode_code\爬虫测试\json提取\疫情正则\zhiye.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    writer = csv.writer(csv_file)
    
    #针对于多条数据的正则表达式爬取，就是用多个括号       
    #pattern = re.compile(r'<div class="VirusTable_1-1-192_AcDK7v">(.*?)</div>.*?<td class="VirusTable_1-1-192_2bK5NN">(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',re.S)##正则
    #pattern = re.compile(r'<dd><a href=.*?>(.*?)</a></dd>',re.S)##正则
    pattern = re.compile(r' target="_blank">(.*?)</a>',re.S)

    #r'class="j_th_tit ">(.*?)</a><span class=.*? title="回复">(.*?)</span><span class=.*?title="主题作者:(.*?)" data-field=.*?><span class=.*? title="最后回复时间">(.*?)</span>'
    #这里爬到的是一个元组。所以需要给他隔开，不然csv读取后处理会有些麻烦
    items = re.findall(pattern,html) 
    #print(items)
    for item in items:
        #在这里给他分开读取
        #writer.writerow([item[0], item[1], item[2], item[3], item[4]])
        writer.writerow([item])
        print(item)
        #print(item)
    #print(items)
    csv_file.close()

def main():
    html = get_one_page(url)
    #print('打印第',(i+1),'页')
    parse_one_page(html)
    print('完成')

if __name__=='__main__':
    main()
