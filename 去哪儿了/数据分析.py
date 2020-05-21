'''
@Author: your name
@Date: 2020-03-07 23:12:23
@LastEditTime: 2020-03-08 11:06:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\美团\数据分析.py
'''
import pandas as pd 
import numpy as np 
from datetime import datetime
from dateutil.parser import parse
import time 
from pyecharts import Bar
import matplotlib.pyplot as plt

data = pd.read_csv(r'E:\vscode_code\爬虫测试\美团\数据.csv')
data['年'] = data["time"].str.split("-").str[0]
data['月'] = data["time"].str.split("-").str[1]
data['日'] = data["time"].str.split("-").str[2]
data['时间'] = data['年'] + data['月'] + data['日']
data_clean = data.drop(['评论', '年', '月', '日'], axis=1)
data_clean = data_clean.dropna(axis=0,how='any')

data_clean['时间'] = pd.to_numeric(data_clean['时间'], errors='coerce')
#data['时间'] = data['时间'].astype('int')
#print(type(data_clean['时间'][0]))
#print(data_clean['时间'].head(10))

cut_bins_2017 = [20170101, 20170201,20170301,20170401, 20170501, 20170601,20170701,20170801, 20170901, 20171001,20171101, 20171201, 20171230]
cut_bins_2018 = [20180101, 20180201,20180301,20180401, 20180501, 20180601,20180701,20180801, 20180901, 20181001,20181101, 20181201, 20181230]
cut_bins_2020 = [20200101, 20200201,20200301,20200401]
labels = ['1月', '2月', '3月','4月', '5月', '6月','7月', '8月', '9月','10月', '11月', '12月']
data_cut = pd.cut(data_clean['时间'], cut_bins_2017, labels=labels)
data_count = (data_cut.value_counts())
print(data_count.values)


bar = Bar("2017年大阪出行人数统计", "月份排序")
bar.add("", data_count.index, data_count.values, is_stack=True,
       xaxis_label_textsize=16, yaxis_label_textsize=16, is_label_show=True)
bar.render(r'E:\vscode_code\爬虫测试\美团\2017年大阪出行人数统计.html')

