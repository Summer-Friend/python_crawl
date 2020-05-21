'''
@Author: your name
@Date: 2020-02-01 20:56:35
@LastEditTime : 2020-02-01 23:03:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\爬图片\pa图片.py
'''
#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.request.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8') #python3
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
     urllib.request.urlretrieve(imgurl,str(x)+".jpg")
     x += 1


html = getHtml("https://tieba.baidu.com/p/xxxxxxxx")
print(getImg(html))