'''
@Author: your name
@Date: 2020-03-06 13:27:34
@LastEditTime: 2020-03-06 13:45:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\美团\美团_json.py
'''
# https://www.meituan.com/meishi/193383554/ 商品链接

import requests, json, re, random, time, csv
from fake_useragent import UserAgent

starttime = time.time()#记录开始时间

#创建CSV文件，并写入表头信息，并设置编码格式为“utf-8-sig”防止中文乱码
fp = open(r'E:\vscode_code\爬虫测试\json提取\美团\another.csv','a', newline='',encoding='utf-8-sig') #"./"表示当前文件夹，"a"表示添加
writer = csv.writer(fp) #方式为写入
writer.writerow(('用户ID','用户名', '平均价','评论','回复')) #表头

for page in range(0, 371, 10):#0~100
    url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=9f45527e-2983-40c9-bc92-f58a8290c947&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F193383554%2F&riskLevel=1&optimusCode=10&id=193383554&userId=&offset={}&pageSize=10&sortType=1'.format(page)
    try:  
        #多个user伪装不知道为什么不行
        USER_AGENT_LIST = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]
        headers = {
        'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
        }
        headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        rep = requests.get(url=url, headers=headers1)
        print ("爬取条数：", page)
        for info in rep.json()['data']['comments']:
            userId = info['userId']
            userName = info['userName']
            avgPrice = info['avgPrice']
            comment = info['comment']
            merchantComment = info['merchantComment']
            data = (userId, userName, avgPrice, comment, merchantComment)
            writer.writerow((data))            
    except:
        print ("这里发生异常：", url)
        pass
fp.close() #关闭文件
endtime = time.time()#获取结束时间
sumTime = endtime - starttime #总的时间
print ("一共用的时间是%s秒"%sumTime)
