'''
@Author: your name
@Date: 2020-04-12 09:56:15
@LastEditTime: 2020-04-12 10:33:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\6.py
'''

a = 'ABCD'
x =y = 'YES'
for ele1 in f'{a[::2]}':
    x = 'NO' if ele1=='B' or ele1=='D' else x
print(x)
    #print('YES') if x==y=='YES' else print('NO')
    
for ele2 in f'{a[1::2]}':
    y = 'NO' if ele2=='A' or ele2=='C' else y
print(y)
    #print('YES') if x==y=='YES' else print('NO')
print('YES') if x==y=='YES' else print('NO')
'''
for ele in f'{a[::2]}':
    x = 0 if ele=='B' or ele=='D' else x
    
print(x)
'''
print(f'奇数位：{a[::2]}\n偶数位：{a[1::2]}')

'''
b=[]
b.append(input())
for i in range(int(b[0])):
    b.append(input())
x =y = 'YES'
for a in b[1:]:
    for ele1 in f'{a[::2]}':
        x = 'NO' if ele1=='B' or ele1=='D' else x       
    for ele2 in f'{a[1::2]}':
        y = 'NO' if ele2=='A' or ele2=='C' else y
    print('YES') if x==y=='YES' else print('NO')
'''