'''
@Author: your name
@Date: 2020-03-07 22:42:40
@LastEditTime: 2020-03-07 23:40:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\美团\携程.py
'''
import requests
import json
import pandas as pd
import csv
import time

#创建CSV文件，并写入表头信息，并设置编码格式为“utf-8-sig”防止中文乱码
fp = open(r'E:\vscode_code\爬虫测试\美团\数据.csv','a', newline='',encoding='utf-8-sig') #"./"表示当前文件夹，"a"表示添加
writer = csv.writer(fp) #方式为写入
writer.writerow(('用户名', '评论', '时间')) #表头

for i  in range(500):
    time.sleep(0.5)#睡0.5秒防止被发现
    #http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=13444&index=237&page=3&pageSize=10&tagType=0
    url = 'http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=13444&index={}&page={}&pageSize=10&tagType=0'.format(i,i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
        }

    # 使用request模块打开并获取网页内容
    response = requests.get(url, headers=headers)   # 禁止重定向
    content = response.text
    #print(content)
    #两种方法解析json都可以
    result = json.loads(content)
    #result2 = response.json()
    #print(result)
    data = result['data']['commentList']
    #print(data)
    """
    #pandas可以直接解析json，但是最好对相对规整的数据使用#########################################
    data_table = pd.read_json(content)
    data_table.to_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing1_data.csv')
    """
    
    for element in data:  
            author =  element['author']     
            content = element['content']  
            date = element['date']
            rep = (author, content, date)
            writer.writerow((rep))  
             
            #print(content)   
            #print("评论内容:{}".format(content))    
    print('爬取第{}页'.format(i+1))  

print('finished')