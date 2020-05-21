'''
@Author: your name
@Date: 2020-03-18 15:36:52
@LastEditTime: 2020-03-18 16:01:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\链家网\单线程.py
'''
import re 
import requests
from lxml import etree
import csv
import time
import json
from fake_useragent import UserAgent


#单线程抓取小区id前100页信息
def get_xiaoqu(x):
    head = {'Host': 'bj.lianjia.com',
            'Referer': 'https://bj.lianjia.com/chengjiao/',
            "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
            #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }
    n=x*20+1
    l=list(range(n,n+20))
    for i in l:
        url = 'https://bj.lianjia.com/xiaoqu/pg' + str(i)
        try:
            r = requests.get(url, headers=head, timeout=3)
            html = etree.HTML(r.text)
            datas=html.xpath('//li[@class="clear xiaoquListItem"]/@data-id')
            title=html.xpath('//li[@class="clear xiaoquListItem"]/div[@class="info"]/div[@class="title"]/a/text()')
            print('No:' + str(x), 'page:' + str(i), len(s), len(datas), len(title))
            #如果当前页没有返回数据，将当前页数加到列表l末尾，再次抓取
            if len(datas)==0:
                print(url)
                l.append(i)
            else:
                for data in datas:
                    s.add(data)
        # 如果当前页访问出现异常，将当前页数加到列表l末尾，再次抓取
        except Exception as e:
            l.append(i)
            print(e)
 
    print('      ****No:'+str(x)+' finish')
#本人购买的代理获取方式，需要根据你们自己的修改。函数功能获取n个ip，并以列表形式返回，每个元素为字典：{'https':'https://118.120.228.202:4286'}
def get_ip(n):
    url='XXXXXXXXXXXXXXXXXXXXXXXX'
    r=requests.get(url)
    html=json.loads(r.text)
    proxies=[]
    for i in range(n):
        a=html['data'][i]['ip']
        b=html['data'][i]['port']
        val='https://'+str(a)+':'+str(b)
        p={'https':val}
        proxies.append(p)
    return(proxies)

'''
#IP代理
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
'''
    
     
if __name__=='__main__':
    global s
    #将id保存在set中，达到排重效果
    s = set()
    #该页面网站会禁ip，所以每个ip只访问20页
    for x in range(2):
        now=time.time()
        #ls = get_ip(1)
        #p=ls[0]
        get_xiaoqu(x)
        print(time.time()-now)
    print('******************')
    print('抓取完成')
    #将抓取的id保存到本地csv
    with open(r'E:\vscode_code\多线程\链家网\xiaoqu_id.csv', 'a', newline='', encoding='gb18030')as f:
        write = csv.writer(f)
        for data in s:
            write.writerow([data])
        f.close()
