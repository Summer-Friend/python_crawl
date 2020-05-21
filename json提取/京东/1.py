'''
@Author: your name
@Date: 2020-03-03 22:20:53
@LastEditTime: 2020-03-04 08:39:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\京东\1.py
'''
import requests
import json
import pandas as pd
import csv

for i  in range(100):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=52674737378&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
        }

    # 使用request模块打开并获取网页内容
    response = requests.get(url, headers=headers)   # 禁止重定向
    content = response.text[20:-2]
    #print(content)
    #两种方法解析json都可以
    result = json.loads(content)
    #result2 = response.json()
    print(result)
    data = result
    """
    #pandas可以直接解析json，但是最好对相对规整的数据使用#########################################
    data_table = pd.read_json(content)
    data_table.to_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing1_data.csv')
    """

    for element in data['comments']:        
            content = element['content']  
            file=open(r"E:\vscode_code\爬虫测试\json提取\京东\comm.txt", 'a')
            file.writelines(format(content))
             
            #print(content)   
            #print("评论内容:{}".format(content))    
    print('爬取第{}页'.format(i+1))  
print('finished')