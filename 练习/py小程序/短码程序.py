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
