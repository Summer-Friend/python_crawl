'''
@Author: your name
@Date: 2020-03-14 21:23:30
@LastEditTime: 2020-03-14 21:32:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\双色球\单线程.py
'''
import pandas as pd
import csv
import time


def get_one_page(page):
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (str(page))
    tb = pd.read_html(url, skiprows=[0, 1])[0]  # 跳过前两行
    return tb.drop([len(tb)-1])  # 去掉最后一行


with open(r'E:\vscode_code\多线程\双色球\qiu1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['开奖日期', '期号', '中奖号码', '销售额(元)', '中奖注数一等奖', '中奖注数二等奖', '详细'])


start_time = time.time()

for i in range(1,127):  # 目前126页数据，取20页
    get_one_page(i).to_csv(r'E:\vscode_code\多线程\双色球\qiu1.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    print('第'+str(i)+'页抓取完成')
    
end_time = time.time()
print('耗时:', end_time-start_time, '秒')