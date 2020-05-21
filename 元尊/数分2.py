'''
@Author: your name
@Date: 2020-02-29 10:57:01
@LastEditTime: 2020-02-29 13:33:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\元尊\数分2.py
'''
import pandas as pd 
import numpy as np 
from pyecharts import WordCloud
from PIL import Image

data = pd.read_csv(r'E:\vscode_code\爬虫测试\元尊\yuanzun_2.csv')

def data_clean(data):
    if '章' in data:
        return 
    else:
        return 2
def data_clean_idea(data):
    a = [['嘲' ,'讽', '吕嫣', '陆玄音'],['水', '难看'],
     ['倒吸', '凉气', '此子', '一拳', '一脚', '一剑', '爆'],['恐怖如斯', '强', '厉害', '碾压'],
     ['亿', '万', '百', '千', '星辰', '源气'],['苏幼薇', '武瑶', '夭夭', '左丘青鱼', '绿萝'],
     ['周元', '元尊'], ['渡劫', '天阳', '元婴', '法域', '圣者', '养气', '太初', '开脉'], 
     ['菜', '鸡', '垃圾'], ['吞吞', '兽'], ['圣族', '圣元'], 
     ['章节', '网文','初次', '关照', '同人', '文'] ,['初期', '中期', '后期']]

    for element in a[0]:
        if element in data:
            return '嘲讽'
    for element in a[1]:
        if element in data:
            return '水尊'
    for element in a[2]:
        if element in data:
            return '恐怖如斯'
    for element in a[3]:
        if element in data:
            return '吹嘘'
    for element in a[4]:
        if element in data:
            return '源气'
    for element in a[5]:
        if element in data:
            return '女角'
    for element in a[6]:
        if element in data:
            return '元尊'
    for element in a[7]:
        if element in data:
            return '渡劫'
    for element in a[8]:
        if element in data:
            return '骂人'
    for element in a[8]:
        if element in data:
            return '吞吞'
    for element in a[9]:
        if element in data:
            return '圣族'
    for element in a[10]:
        if element in data:
            return '网文'
    for element in a[11]:
        if element in data:
            return '境界'
#清洗数据            
data['data_clean'] = data['元尊贴吧标题'].apply(data_clean)
data = data.dropna(subset = ['data_clean'])
data['data_clean'] = data['元尊贴吧标题'].apply(data_clean_idea)
data = data.dropna(subset = ['data_clean'])

#这里用astype不行了
#data_count = data.groupby('data_clean').count()
data['回复数'] = pd.to_numeric(data['回复数'], errors='coerce')
data.sort_values(by = '回复数', ascending=False, inplace=True)
data_clean = data.nlargest(500, '回复数')
#print(type(data.iloc[0, 0]))

data_clean.sort_values(by = '回复数', ascending=True, inplace=True)

#print(data_clean.head(10))
data_count = data_clean.groupby('data_clean')['data_clean'].count()
print(data_count)
