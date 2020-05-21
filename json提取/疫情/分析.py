'''
@Author: your name
@Date: 2020-02-27 21:16:38
@LastEditTime: 2020-02-28 12:03:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\疫情\分析.py
'''
import pandas as pd 
from pyecharts import Bar

data = pd.read_csv(r'E:\vscode_code\爬虫测试\json提取\疫情\yiqing2_data.csv')
bar = Bar('value', '单位：忘记了')
bar.add('', data['市'], data['价值'])
bar.render(r'E:\vscode_code\爬虫测试\json提取\疫情\图标.html')