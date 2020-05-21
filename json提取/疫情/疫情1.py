'''
@Author: your name
@Date: 2020-02-27 21:01:41
@LastEditTime: 2020-03-01 11:31:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\疫情\疫情1.py
'''
import requests
import json
import pandas as pd
import csv

url = 'https://huiyan.baidu.com/openapi/v1/migration/rank?type=move&ak=kgD2HiDnLdUhwzd3CLuG5AWNfX3fhLYe&adminType=country&name=%E5%85%A8%E5%9B%BD'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
    }

# 使用request模块打开并获取网页内容
response = requests.get(url, headers=headers)   # 禁止重定向
#content = response.content
content = response.text

#两种方法解析json都可以
result = json.loads(content)
result2 = response.json()
#print(result == result2)

"""
#pandas可以直接解析json，但是最好对相对规整的数据使用#########################################
data_table = pd.read_json(content)
data_table.to_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing1_data.csv')
"""
'''
result = result['result']['moveInList']

yq_list = []
for i in range(len(result)):
    yq = {}
    yq['city_name'] = result[i]['city_name']
    yq['province_name'] = result[i]['province_name']
    yq['value'] = result[i]['value']
    yq_list.append(yq)
    
# 准备好存储的csv文件
csv_file = open(r'E:\vscode_code\爬虫测试\疫情\yiqing2_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['市', '省', '价值'])
for data in yq_list:
    writer.writerow([data['city_name'], data['province_name'],data['value']])
csv_file.close()
'''