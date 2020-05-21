'''
@Author: your name
@Date: 2020-02-27 17:14:08
@LastEditTime: 2020-02-27 18:56:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取.py\疫情.py
'''
import requests
import pandas as pd
import json
import csv

url = 'http://sa.sogou.com/new-weball/api/sgs/epidemin/protection/list?_=0.9284842481056663&type=all'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }

# 使用request模块打开并获取网页内容
response = requests.get(url, headers=headers)   # 禁止重定向
#content = response.content

content = response.text
result = json.loads(content)

'''
#pandas可以直接解析json#########################################
data_table = pd.read_json(content)
data_table.to_csv(r'E:\vscode_code\爬虫测试\json提取\yiqing2_data.csv')
'''

result = result['list']
#print(len(result))
#print(result[i]['title'] for i in range(5))
result_list = []

for i in range(10):
    res = {}
    res['title'] = result[i]['title']
    result_list.append(res)       # 列表存放字典
    #print(res)
#print(result_list)

csv_file = open(r'E:\vscode_code\爬虫测试\json提取\yiqing_data3.csv', 'w', newline='')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['评价'])
for data in result_list:
    print(data)
    #写一行,需要加中括号，不然会有逗号分割
    writer.writerow([data['title']])
csv_file.close()
