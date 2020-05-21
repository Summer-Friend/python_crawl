'''
@Author: your name
@Date: 2020-03-08 14:15:31
@LastEditTime: 2020-03-08 16:28:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\数据分析练习\大众\test.py
'''
a = ['12', '2']
def cope(items):
    i=0
    for item in items: 
        #print(len(item))
        if len(item) == 1:
            item = '0' + item
    items[i]=item
    i=i+1
for item in a:
    i=0
    #print(len(item))
    if len(item) == 1:
        item = '0' + item
    a[i]=item
    i=i+1
        
print(a)