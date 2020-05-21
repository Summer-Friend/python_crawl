'''
@Author: your name
@Date: 2020-03-07 21:42:19
@LastEditTime: 2020-03-07 21:44:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\美团\评论.py
'''
# https://www.meituan.com/meishi/193383554/ 商品链接

import requests, json, re, random, time, csv
from fake_useragent import UserAgent

starttime = time.time()#记录开始时间

ips = [] #装载有效 IP 
for i in range(1, 6):
    headers = {
    "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
    }
    ip_url = 'http://www.89ip.cn/index_{}.html'.format(i)
    html = requests.get(url=ip_url, headers=headers).text
    res_re = html.replace(" ", "").replace("\n", "").replace("\t", "")
    #使用正则表达式匹配出IP地址及端口
    r = re.compile('<tr><td>(.*?)</td><td>(.*?)</td><td>')
    result = re.findall(r, res_re)
    for i in range(len(result)):
        ip = "http://" + result[i][0] + ":" + result[i][1]
        # 设置为字典格式
        proxies = {"http": ip}
        #使用上面的IP代理请求百度，成功后状态码200
        baidu = requests.get("https://www.baidu.com/", proxies = proxies)
        if baidu.status_code == 200:        
            ips.append(proxies)
    print ("正在准备IP代理，请稍后。。。")

#创建CSV文件，并写入表头信息，并设置编码格式为“utf-8-sig”防止中文乱码
fp = open('./美团_大学城.csv','a', newline='',encoding='utf-8-sig') #"./"表示当前文件夹，"a"表示添加
writer = csv.writer(fp) #方式为写入
writer.writerow(('用户ID','用户名', '平均价','评论','回复')) #表头

for page in range(0, 371, 10):#0~100
    url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=dc2291347be6488383b2.1583588235.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F4804147%2F&riskLevel=1&optimusCode=10&id=4804147&userId=&offset={}0&pageSize=10&sortType=1'.format(page)
    try:  
        headers = {
             "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
        }
        rep = requests.get(url=url, headers=headers, proxies=ips[random.randint(0 , len(ips)-1)])
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
