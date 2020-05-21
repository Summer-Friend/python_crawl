'''
@Author: your name
@Date: 2020-04-10 09:28:06
@LastEditTime: 2020-04-10 16:46:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\4.py
'''

b=101.256745
print(b)  
print('They are %.3f kgs'%b) if b==100 else print('a') if b>100 else print('c')
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
a = '2020年4月4日'
print(a.split('年')[0], a.split('年')[1].split('月')[0], a.split('年')[1].split('月')[1].split('日')[0])
#计算是第几天
print(sum(months[0:int(a.split('年')[1].split('月')[0])+1])+1) if (int(a.split('年')[0]) % 400 == 0) or ((int(a.split('年')[0]) % 4 == 0) and (int(a.split('年')[0]) % 100 != 0)) else print(sum(months[0:int(a.split('年')[1].split('月')[0])+1]))

print(type((int(a.split('年')[0]))))
print(sum(months))
print(months[0:4])