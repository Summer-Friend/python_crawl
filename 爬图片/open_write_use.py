'''
@Author: your name
@Date: 2020-02-01 21:05:24
@LastEditTime : 2020-02-01 23:03:43
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\爬图片\another.py
'''
import urllib
import urllib.request

import re#正则表达式
url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3"
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",#用户信息
	"referer":"https://image.baidu.com"#从百度图片网址跳转过来
	}#这里写爬虫的请求头，百度图片有反爬
req=urllib.request.Request(url,headers=headers)
body=urllib.request.urlopen(req).read().decode("utf-8")


key=r'thumbURL":"(.+?)"'
com=re.compile(key)
num=0
for string in re.findall(com,body):
	f_req=urllib.request.Request(string,headers=headers)
	f_body=urllib.request.urlopen(f_req).read()#读取图片的内容
	fs=open(str(num)+".jpg","wb+")#以二进制创建或打开一个jpg文件
	fs.write(f_body)#往文件里写入内容
	print ("正在下载："+string)
	fs.close()#关闭文件	
	print (string+"已下载成功")#做一下界面优化
	num+=1
