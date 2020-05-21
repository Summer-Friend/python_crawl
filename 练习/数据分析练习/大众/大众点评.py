'''
@Author: your name
@Date: 2020-03-08 13:54:24
@LastEditTime: 2020-03-08 16:29:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\数据分析练习\大众点评.py
'''
import pandas as pd
from pyecharts import Bar

data = pd.read_excel(r'E:\vscode_code\练习\数据分析练习\大众点评.xlsx')
data.to_csv(r'E:\vscode_code\练习\数据分析练习\大众\da1.csv',encoding='utf-8', index=False, header=True)
#这个时候一定要加'header=None', 这样读进来的列名就是系统默认的0，1，2... 序列号
data = pd.read_csv(r'E:\vscode_code\练习\数据分析练习\大众\da1.csv')
data['年'] = data["date"].str.split("年").str[0]
data['月'] = data["date"].str.split("月").str[0].str.split("年").str[1]
data['日'] = data["date"].str.split("月").str[1].str.split("日").str[0]

i=0
for item in data['月']:
    if len(item) == 1:
        item = '0' + item
    data['月'][i]=item
    i=i+1

j=0
for item in data['日']:
    if len(item) == 1:
        item = '0' + item
    data['日'][j]=item
    j=j+1
                   
data = data.drop(['desc'], axis=1)
print(data.head(10))

data['时间'] = data['时间'] = data['年'] + data['月'] + data['日']
data['时间'] = pd.to_numeric(data['时间'], errors='coerce')



cut_bins_2018 = [20180101, 20180201,20180301,20180401, 20180501, 20180601,20180701,20180801, 20180901, 20181001,20181101, 20181201, 20181230]
cut_bins_2019 = [20190101, 20190201,20190301,20190401, 20190501, 20190601,20190701,20190801, 20190901, 20191001,20191101, 20191201, 20191230]
cut_bins_2020 = [20200101, 20200201,20200301,20200401]
labels = ['1月', '2月', '3月','4月', '5月', '6月','7月', '8月', '9月','10月', '11月', '12月']
labels_2020 = ['1月', '2月', '3月']
data_cut = pd.cut(data['时间'], cut_bins_2020, labels=labels_2020)
data_count = (data_cut.value_counts())

print(data_count.values)


bar = Bar("2020年大众点评人数统计", "月份排序")
bar.add("", data_count.index, data_count.values, is_stack=True,
       xaxis_label_textsize=16, yaxis_label_textsize=16, is_label_show=True)
bar.render(r'E:\vscode_code\练习\数据分析练习\大众\2020年大众点评人数统计.html')
'''