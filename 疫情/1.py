'''
@Author: your name
@Date: 2020-03-01 20:01:39
@LastEditTime: 2020-03-01 20:27:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\疫情\1.py
'''
#https://blog.csdn.net/weixin_43130164/article/details/104113559?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import time 
import json
import requests
from datetime import datetime
import pandas as pd 
import numpy as np 

def catch_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    #返回数据字典
    data = json.loads(reponse['data'])
    return data

data = catch_data()

# 数据集包括["国内总量","国内新增","更新时间","数据明细","每日数据","每日新增"]
lastUpdateTime = data['lastUpdateTime']
chinaTotal = data['chinaTotal']
chinaAdd = data['chinaAdd']


# 数据明细，数据结构比较复杂，一步一步打印出来看，先明白数据结构
areaTree = data['areaTree']
# 国内数据
china_data = areaTree[0]['children']
china_list = []
for a in range(len(china_data)):
    province = china_data[a]['name']
    province_list = china_data[a]['children']
    for b in range(len(province_list)):
        city = province_list[b]['name']
        total = province_list[b]['total']
        today = province_list[b]['today']
        china_dict = {}
        china_dict['province'] = province
        china_dict['city'] = city
        china_dict['total'] = total
        china_dict['today'] = today
        china_list.append(china_dict)
        
china_data = pd.DataFrame(china_list)
#print(china_data['total'][1])
# 定义数据处理函数
def confirm(x):
    #eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    confirm = eval(str(x))['confirm']
    return confirm
def suspect(x):
    suspect = eval(str(x))['suspect']
    return suspect
def dead(x):
    dead = eval(str(x))['dead']
    return dead
def heal(x):
    heal =  eval(str(x))['heal']
    return heal


# 函数映射
#这里用apply和map都行，参照：https://www.cnblogs.com/cymwill/p/7577369.html

china_data['确认'] = china_data['total'].apply(confirm)
china_data['疑似'] = china_data['total'].map(suspect)
china_data['死亡'] = china_data['total'].map(dead)
china_data['治愈'] = china_data['total'].map(heal)

china_data = china_data[["province","city","确认","疑似","死亡","治愈"]]
china_data.to_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing_china.csv')

#国际数据处理
global_data = pd.DataFrame(data['areaTree'])
global_data['confirm'] = global_data['total'].map(confirm)
global_data['suspect'] = global_data['total'].map(suspect)
global_data['dead'] = global_data['total'].map(dead)
global_data['heal'] = global_data['total'].map(heal)
global_data = global_data[["name","confirm","suspect","dead","heal"]]
global_data.to_csv(r'E:\vscode_code\爬虫测试\疫情\yiqing_global.csv')



