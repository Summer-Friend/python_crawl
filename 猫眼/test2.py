'''
@Author: your name
@Date: 2020-02-29 10:01:12
@LastEditTime: 2020-02-29 10:38:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\猫眼\test2.py
'''
import pandas as pd 
import json
import csv 

#with open(r'爬虫测试\猫眼\maoyan_top100.json','r', encoding = 'utf-8') as f:
df = pd.DataFrame()
with open(r'爬虫测试\猫眼\maoyan_top100.json','r',encoding='utf-8')as f:
    for ff in f:
        data = json.loads(ff) 
        row = pd.DataFrame(data)
        df = df.append(row,ignore_index=True)
print(df.head())
