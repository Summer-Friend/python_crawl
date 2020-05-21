'''
@Author: your name
@Date: 2020-03-02 15:38:19
@LastEditTime: 2020-03-02 15:44:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\pandas提取\长江学者.py
'''
import pandas as pd
import csv

def get_one_page(num):
    url = 'http://news.sciencenet.cn/htmlnews/2018/1/399176.shtm'
    tb = pd.read_html(url, skiprows=[0])[num]  # 跳过前两行
    return tb # 去掉最后一行


with open(r'E:\vscode_code\爬虫测试\pandas提取\changjiang.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['推荐学校', '姓名', '岗位名称', '现任职单位'])

for i in range(3):  # 目前116页数据
    get_one_page(i).to_csv(r'E:\vscode_code\爬虫测试\pandas提取\changjiang.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    print('第'+str(i+1)+'张表格抓取完成')