'''
@Author: your name
@Date: 2020-04-01 10:13:47
@LastEditTime: 2020-04-01 10:18:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\数据分析练习\批量文本读取\test.py
'''
import pandas as pd 

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
result = pd.merge(left, right, how='outer')
#result = pd.concat([left, right], axis = 1)
print(result)
