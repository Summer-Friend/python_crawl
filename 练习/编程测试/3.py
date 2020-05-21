'''
@Author: your name
@Date: 2020-04-09 22:51:39
@LastEditTime: 2020-04-10 09:34:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\3.py
'''
b = 1
x=1
y=2
'''
#if b>100:print(b) else (b==100):print('a') else:print('c')
print(b) if b>100 else ('a') if(b==100) else ('c')
c=b if b>100 else ('a') if(b==100) else ('c')
print(c)
'''
print(lambda c:x)

print (x, y) if x < y else (y, x)   
print(b) if b>100 else print('a') if b==100 else print(1)
#print(b) if b>100

b = 100
a = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
#奖金计算
salary = 10*a[0]+10*a[1]+20*a[2]+20*a[3]+40*a[4]+(b-100)*a[5] if b>100 else (10*a[0]+10*a[1]+20*a[2]+20*a[3]+(b-60)*a[4]) if b>60 else (10*a[0]+10*a[1]+20*a[2]+(b-40)*a[3]) if b>40 else (10*a[0]+10*a[1]+(b-20)*a[2]) if b>20 else (10*a[0]+(b-10)*a[1]) if b>10 else b*a[0]
print(salary)
print(10*a[0]+10*a[1]+20*a[2]+20*a[3]+40*a[4]+(b-100)*a[5]) if b>100 else print(10*a[0]+10*a[1]+20*a[2]+20*a[3]+(b-60)*a[4]) if b>60 else print(10*a[0]+10*a[1]+20*a[2]+(b-40)*a[3]) if b>40 else print(10*a[0]+10*a[1]+(b-20)*a[2]) if b>20 else print(10*a[0]+(b-10)*a[1]) if b>10 else print(b*a[0])

