'''
@Author: your name
@Date: 2020-02-29 13:06:56
@LastEditTime: 2020-02-29 13:08:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\元尊\test.py
'''
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'state':['Ohio1','Ohio1','Ohio2','Nevada3','Nevada3'],
    'year':[2000,2001,2002,2001,2002],
    'pop':['1.5','1.7','3.6','2.4','2.9'],
    'salary':['1000K/MTH - 20000K/MTH', '7K/MTH - 8K/MTH',
       '10000K/MTH - 16000K/MTH', '3K/MTH - 5K/MTH', '7K/MTH - 12K/MTH',]
}
frame = pd.DataFrame(data)
print(type(frame.ilc[2, 0]))
