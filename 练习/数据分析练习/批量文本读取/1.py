'''
@Author: your name
@Date: 2020-04-01 10:08:53
@LastEditTime: 2020-04-01 10:19:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\数据分析练习\批量文本读取\1.py
'''
import pandas as pd 
import numpy as np
import glob,os

path=r'E:\vscode_code\练习\数据分析练习'        #批量表格所在文件路径
files=glob.glob(os.path.join(path, "*.xlsx"))      #每一个表格相同名称部分
print(files)
for file in files:
    data = pd.read_excel(file)
    print(data.head())
    print(file)
#下面的数据是针对文件内容也基本一致的时候可以使用
'''    
dl= []
for f in file:
dl.append(pd.read_csv(f,index_col=None,encoding='ANSI'))     #读取每个表格
df=pd.concat(dl)     #合并
'''