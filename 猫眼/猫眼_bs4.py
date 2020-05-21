'''
@Author: your name
@Date: 2020-01-19 08:44:19
@LastEditTime : 2020-01-19 09:09:54
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\猫眼_bs4.py
'''
import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

for i in range(5):
    url = 'http://maoyan.com/board/6?offset={}'.format(i*10)
    response = requests.get(url , headers = headers)
    content = response.text
    #这个parser只是对应方法，不加也可以
    soup = BeautifulSoup(content,'html.parser')
    dl = soup.find('dl',class_=re.compile("board-wrapper"))
    #可能报错'NoneType' object has no attribute 'text'，定位显示为actors那一行，可能是没有找到对应数据
    for div in dl.find_all('dd'):
        Number = div.find('i',class_=re.compile('index')).text
        Name = div.find('p',class_='name').find('a').text
        Actors =div.find('p',class_='star').text
        Time = div.find('p',class_='releasetime').text
        print(Number," ",Name," ",Actors," ",Time)
