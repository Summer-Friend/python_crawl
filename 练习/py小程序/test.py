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
