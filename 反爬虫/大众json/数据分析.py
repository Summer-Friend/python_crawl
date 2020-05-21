'''
@Author: your name
@Date: 2020-03-06 09:20:12
@LastEditTime: 2020-03-06 09:21:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众json\数据分析.py
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Bar, Line, Overlap, WordCloud

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plt.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点

shop_data = pd.read_csv(r'E:\vscode_code\爬虫测试\反爬虫\大众json\大众_data.csv')
print(shop_data.info())