'''
@Author: your name
@Date: 2020-04-10 16:49:34
@LastEditTime: 2020-04-12 09:56:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\编程测试\5.py
'''
a = [2, 99, 123]
num = input()
input_nums = input for i in range(num)
#input_num = 123
sum_num = 0

for input_num in a:
    while len(str(input_num)) != 1 :
        sum_num = 0
        for i  in range(len(str(input_num))):
            cut_num = str(input_num)[i:i + 1]
            # 重新给变量sum_num赋值为sum_num+截取到的数字的和
            sum_num = sum_num + int(cut_num)
        input_num = sum_num
    print(input_num)
'''
a=[]
a.append(input())
for i in range(int(a[0])):
    a.append(input())
sum_num = 0
for input_num in a[1:]:
    while len(str(input_num)) != 1 :
        sum_num = 0
        for i  in range(len(str(input_num))):
            cut_num = str(input_num)[i:i + 1]
            sum_num = sum_num + int(cut_num)
        input_num = sum_num
    print(input_num)
'''