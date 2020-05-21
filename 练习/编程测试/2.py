'''
@Author: your name
@Date: 2020-04-09 22:34:42
@LastEditTime: 2020-04-09 22:45:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\2.py
'''


for i in range(10000):
    if (int(str((i+100)**(1/2)).split('.')[1]) == 0) and (int(str((i+268)**(1/2)).split('.')[1]) == 0):
        print(i)
print(289**0.5)