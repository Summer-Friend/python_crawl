'''
@Author: your name
@Date: 2020-03-18 15:48:59
@LastEditTime: 2020-03-18 15:50:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\链家网\test.py
'''
from fake_useragent import UserAgent

headers = {
             "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
        }
print(headers)