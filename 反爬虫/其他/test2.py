'''
@Author: your name
@Date: 2020-03-05 17:08:33
@LastEditTime: 2020-03-05 17:19:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\其他\test2.py
'''
import requests,json,re


#这是加密的json网站
url='https://www.shixiseng.com/app/interns/search/v2?build_time=1569124722750&page=3&keyword=%E6%95%B0%E6%8D%AE%E5%BA%93&type=intern&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.shixiseng.com",
    "If-None-Match": 'W/"02d6c2c96e9590c77f0f8cb9a908f8b59a64e114"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
}
response=requests.get(url,headers=headers)
data=json.loads(response.text)["msg"]["data"]

'''
font_name = {}
for index,value in enumerate(texts):
        #把映射关系写成一个字典
        a = font_names[index].replace('uni', '&#x').lower() + ";"
        font_name[a] = value
'''       
for d in data:
    print(d)
    ms=''
    for  i in d["minsal"].split("&#"):
        print(i)