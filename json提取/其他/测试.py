'''
@Author: your name
@Date: 2020-02-06 13:03:33
@LastEditTime : 2020-02-06 13:36:43
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取.py\测试.py
'''
import requests
import json
import csv

first_level_url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=c40594997e50464590279fab1e3ce325&rt=064f85b27de94b278ae9bc757c681234&_v=0.87973111&userCode=1000019163&x-zp-page-request-id=112be33bbbed4d3bb626bddc85c5045c-1563247432055-34737&x-zp-client-id=0e3f91e5-379d-4cfd-a0cb-d034d314dc15'
headers={
'Referer': 'https://sou.zhaopin.com/?jl=653&sf=0&st=0&kw=python&kt=3',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
html_str=requests.get(url=first_level_url,headers=headers)
#data_json=html_str.json()
#data_json = json.loads(html_str.text)
print(html_str.text)

'''
#获取json中需要的字段
position_data_list=data_json['data']['results']
#用来存储键名
headers=[]
#存储键名信息到列表
for i in position_data_list:
    if headers:
        break
    else:
        for x in i.keys():
            headers.append(x)
print(headers)
#把文件存储到csv文件中
with open(r'E:\vscode_code\爬虫测试\json提取.py\测试信息.csv', 'w', newline='') as f:
	#先存储键名信息到csv文件中
    fieldnames = headers
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    # csv_file = open('csv/zhilian_python.csv', 'a+', newline='')
    # csv_writer = csv.writer(csv_file)
    #写入获取到的数据
    for j in position_data_list:
        print(j)
        writer.writerow(j)
'''

