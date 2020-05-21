'''
@Author: your name
@Date: 2020-03-11 19:27:05
@LastEditTime: 2020-03-12 11:49:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\马蜂窝ajax\首页.py
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

#print(content)
data = response.text

#json格式会自动解码，所以下面的解码语句可加可不加了
#response.encoding = response.apparent_encoding
#content=response.content.decode('utf-8')
#data = response.content.decode('unicode-escape')
#data = response.content.decode('unicode-escape', 'ignore').encode('utf-8', 'ignore').decode('utf-8')#爬取页面并且解码


#原先是<\/a>这种数据
#但是这个只对正则表达式有影响，xpath和bs4不受影响
data = data.replace('\\/', '/')#将\/转换成/
#print(data)

#确定网址正确访问
#print(response.status_code)

if 200==response.status_code:
    data2= re.findall("jQuery1810017714238424474837_1583927717604\((.*?}})\);",data)[0]
    '''
    data3 = json.loads(data2)
    #print(data3)
    #print('ok')
    #1.json+正则抓取
    #这个数据可能太不规整了根本不是json类型，还是正则好抓一点,其实还是挺规整的，利用json.loads和
    data2 =data3['data']['html']
    print(data2)
    pattern = re.compile(r'<dt>.*?<a href="/i.*? target="_blank">(.*?)</a>',re.S)##正则
    x = re.findall(pattern, data2)
    print(x)
    '''
    #2.xpath抓取
    data3 = json.loads(data2)
    #print(data3)
    #print('ok')
    #这个数据可能太不规整了根本不是json类型，还是正则好抓一点
    next_page =data3['data']['html']
    html = etree.HTML(next_page)
    #infos = html.xpath('//div[@class="tn-image"]/a')
    #infos = html.xpath('//*[@id="_j_tn_content"]/div[1]/div/div[2]/dl/dt/a/text()')
    infos = html.xpath('//*[@id="_j_tn_content"]/div[1]/div/div[2]/dl/dt/a')
    #//*[@id="_j_tn_content"]/div[1]/div[12]/div[2]/dl/dt/a
    #print(infos)
    for info in infos:
        #print(info)
        #如果要抓取网页网址的话，直接把text()改成@href就行了，针对于xpath
        name = info.xpath('text()')[0]
        link=info.xpath('@href')[0]
        print(name, '  ', link)
        #all_link.append('http://www.mafengwo.cn/'+link)
    
    
