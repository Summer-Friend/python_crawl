'''
@Author: your name
@Date: 2020-03-06 11:27:23
@LastEditTime: 2020-05-07 09:29:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\美团\test.py
'''
import pandas as pd 
a = {'1':'2','0':'0'}
b = pd.DataFrame(a,index = [0])
print(b)

class_mapping = {'0':0, '1':1}
b = a.map(class_mapping)
print(b)
