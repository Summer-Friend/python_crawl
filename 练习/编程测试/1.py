'''
@Author: your name
@Date: 2020-04-09 22:06:02
@LastEditTime: 2020-04-09 22:23:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\1.py
'''
a = [1,2,3,4]
count = 0
word = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            if (a[i]!=a[j]) and (a[j]!=a[k]) and (a[i]!=a[k]):
                word = a[i]*100+a[j]*10+a[k]
                count =count + 1
                print(word)
print(count)
