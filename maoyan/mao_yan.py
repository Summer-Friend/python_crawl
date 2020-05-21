'''
@Author: your name
@Date: 2020-01-20 14:36:52
@LastEditTime: 2020-02-28 09:08:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\mao_yan.py
'''
import pandas as pd                         #导入pandas包
data = pd.read_csv('爬虫测试\maoyan\mao_yan.csv')             #读取csv文件
'''
print(data)                                #打印所有文件
print (data.head(5)) 
'''  
print(data.columns)                         #返回全部列名
print(data.shape)                           #f返回csv文件形状
print(data.loc[1:2])                        #打印第1到2行
print(data.loc[2:4, ['name', 'sex']])      #打印行中特定列
print(data.iloc[2:4, 2:3])      #打印行中特定列

