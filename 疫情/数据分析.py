'''
@Author: your name
@Date: 2020-03-01 20:27:30
@LastEditTime: 2020-03-02 22:20:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\疫情\数据分析.py
'''
import pandas as pd 
import numpy as np 
from pyecharts import Bar
import matplotlib.pyplot as plt 

data = pd.read_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing_global.csv')
data = data.set_index(['name'], drop = False)
data = data[data['name'] != '中国']

index = data['confirm'].nlargest(15).index
value = data['confirm'].nlargest(15).values
bar = Bar()
bar.add("", index, value, legend_text_size=18,xaxis_label_textsize=15,yaxis_label_textsize=18, xaxis_rotate=30)
bar.render(r'E:\vscode_code\爬虫测试\疫情\yiqing.html')
