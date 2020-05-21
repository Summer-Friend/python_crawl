import sys
#电阻并联
def resis(n):
    r1=n[0]
    for i in range(1,len(n)):
        x = r1*n[i]/(r1+n[i])
        r1=x
    return x
#数字转换
def change_k(n):
    b = []
    for x in n:
        if 'k' in x :
            x = float(x.replace('k',''))*1000
            b.append(x)
        elif '千' in x:
            x = float(x.replace('千',''))*1000
            b.append(x)
        elif 'w' in x:
            x = float(x.replace('w',''))*10000
            b.append(x)
        elif '万' in x:
            x = float(x.replace('万',''))*10000
            b.append(x)
        elif 'm' in x:
            x = float(x.replace('m',''))*10**(-3)
        else:
            b.append(float(x))
    return b

#num=input('请输入希望并联的数组')
#输入操作
while True:
        arr = input("输入一个一维数组，每个数之间使空格隔开")    #输入一个一维数组，每个数之间使空格隔开
        num = [(n) for n in arr.split()]    #将输入每个数以空格键隔开做成数组
        #num=[1,2,3]
        num = change_k(num)
        #print(num)
        print('普通：', resis(num))
        #科学计数法保留六位小数
        print('科学计数法',  '%e' % resis(num))
        #退出程序
        x = input("请输入q键退出")
        if x == 'q':
                sys.exit()
        

