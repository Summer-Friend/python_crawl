'''
@Author: your name
@Date: 2020-03-18 15:50:46
@LastEditTime: 2020-03-18 15:51:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\链家网\IP代理.py
'''
import requests, json, re, random, time, csv
from fake_useragent import UserAgent

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
