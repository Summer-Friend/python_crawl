'''
@Author: your name
@Date: 2020-03-11 22:33:46
@LastEditTime: 2020-03-12 11:45:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\ajax\马蜂窝ajax\首页修改.py
'''
import re
import time
import requests
from lxml import etree
import json

#评论内容所在的url，？后面是get请求需要的参数内容
comment_url='https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery1810017714238424474837_1583927717604&params=%7B"type"%3A"0"%7D&_=1583927717831'

requests_headers={
    'Referer': 'https://www.mafengwo.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}#请求头

params = {"type":0,"objid":0,"page":2,"ajax":1,"retina":1}
response =requests.get(url=comment_url,headers=requests_headers, params=params)
#response.encoding = response.apparent_encoding
#content=response.content.decode('utf-8')
#print(content)
#data = response.text
#data = response.content.decode('unicode-escape')

#如果是正则的话需要解码，但是xpath貌似不用，利用data = response.text和路径就直接出来了
data = response.content.decode('unicode-escape', 'ignore').encode('utf-8', 'ignore').decode('utf-8')#爬取页面并且解码
data = data.replace('\\/', '/')#将\/转换成/
#print(data)
#print(response.status_code)

#整体解码+正则
if 200==response.status_code:
    #data2= re.findall("jQuery1810017714238424474837_1583927717604\((.*?}})\);",data)[0]
    #print(data2)
    pattern = re.compile(r'<dt>.*?<a href="/i.*? target="_blank">(.*?)</a>',re.S)##正则
    x = re.findall(pattern, data)
    print(x)
    '''
    data3 = json.loads(data2)
    print(data3)
    #print('ok')
    #这个数据可能太不规整了根本不是json类型，还是正则好抓一点
    next_page =data3['data']['html']
    html = etree.HTML(next_page)
    infos = html.xpath('//div[@class="tn-image"]/a')
    for info in infos:
        link=info.xpath('@href')[0]
        print(link)
        #all_link.append('http://www.mafengwo.cn/'+link)
    '''
    
