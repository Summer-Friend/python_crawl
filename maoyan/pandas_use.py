'''
@Author: your name
@Date: 2020-01-20 14:01:00
@LastEditTime : 2020-01-20 14:23:50
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\maoyan\pandas_use.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))#randn返回一个标准正态分布
print(df.describe().dataframe tbody tr th {
    vertical-align: top;
})

