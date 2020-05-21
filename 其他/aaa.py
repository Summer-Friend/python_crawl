'''
@Author: your name
@Date: 2020-01-29 19:53:18
@LastEditTime : 2020-01-29 19:57:49
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\其他\aaa.py
'''
import requests
from bs4 import BeautifulSoup


def request_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return ' '
    
    
def get_page_urls():

    for i in range(1,2):
        baseurl = 'https://www.mzitu.com/page/{}'.format(i)
        html = request_page(baseurl)
        soup = BeautifulSoup(html, 'lxml')
        list = soup.find(class_='postlist').find_all('li')
        urls=  []
        for item in list:
            url =item.find('span').find('a').get('href')
            urls.append(url)
    #print(url)
    return urls

if __name__ == '__main__':
    get_page_urls()
    
