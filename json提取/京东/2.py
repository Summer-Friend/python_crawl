'''
@Author: your name
@Date: 2020-03-03 22:54:15
@LastEditTime: 2020-05-06 12:39:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\京东\2.py
'''
import requests
import urllib3
import json
import urllib
import urllib.request
from bs4 import BeautifulSoup
for i in range(100):    
    url1 = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4403&productId=3487485&score=3&sortType=5&page='    
    url2 = str(i)    
    uel3 = '&pageSize=10&isShadowSku=0&rid=0&fold=1'    
    finalurl = url1+url2+uel3    
    print(finalurl)
    xba = requests.get(finalurl)    
    content = xba.text[26:-2]
    #print(content)
    data=json.loads(xba.text[26:-2])
    '''    
    for i in data['comments']:        
        content = i['content']     
        #print(content)   
        print("评论内容:{}".format(content))     
    '''   
    
    for element in data['comments']:        
            content = element['content']  
            file=open(r"E:\vscode_code\爬虫测试\json提取\京东\comm2.txt", 'a')
            file.writelines(format(content))
             
            #print(content)   
            #print("评论内容:{}".format(content))    
    print('爬取第{}页'.format(i+1))  
print("finished")
