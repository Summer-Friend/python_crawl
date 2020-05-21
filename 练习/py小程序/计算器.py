import math
import sys
#x = '1+2**(1/2)'
while True:
    x = input('请输入要计算的表达式')
    print('结果：', eval(x))
    y = input("请输入q键退出")
        if y == 'q':
                sys.exit()
